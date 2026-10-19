source("r_session.R")
G<-function(x,n)x[[n,exact=TRUE]]
corpus<-jsonlite::fromJSON("corpus.json",simplifyVector=FALSE)
corpus<-head(corpus,40)
output<-list(); cache<-new.env(parent=emptyenv())
canon<-function(s) if(tolower(trimws(s))=="control") "control" else paste(sort(tolower(strsplit(trimws(s),"\\s*\\+\\s*",perl=TRUE)[[1]])),collapse="+")
pack<-function(z){
  effect<-function(prefix,names){
   out<-lapply(seq_along(names),function(i)list(est=G(z,paste0(prefix,".random"))[i],se=G(z,paste0("se",prefix,".random"))[i],lo=G(z,paste0("lower.",prefix,".random"))[i],hi=G(z,paste0("upper.",prefix,".random"))[i]))
   setNames(out,names)
  }
  list(tau2=G(z,"tau")^2,Q=G(z,"Q.additive"),df=G(z,"df.Q.additive"),components=effect("Comp",G(z,"comps")),combinations=effect("Comb",G(z,"trts")),C=unname(split(G(z,"C.matrix"),row(G(z,"C.matrix")))),C_rows=as.list(rownames(G(z,"C.matrix"))),C_cols=as.list(colnames(G(z,"C.matrix"))),n_subnets=G(z,"n.subnets"))
}
for(ci in seq_along(corpus)) {
 c<-corpus[[ci]];key<-G(c,"key"); warnings<-character()
 writeLines(paste(ci,key),"reference-current.txt")
 if(!is.null(G(c,"expected_refusal"))){output[[ci]]<-list(key=key,status="refused",reason=G(c,"expected_refusal"));next}
 d<-do.call(rbind,lapply(G(c,"rows"),function(r)data.frame(A=canon(G(r,"A")),B=canon(G(r,"B")),te=G(r,"te"),se=G(r,"se"),study=G(r,"study"))))
 hash<-paste(G(c,"input_sha256"),paste(d[["study"]],collapse="|"),sep="::")
 if(exists(hash,cache,inherits=FALSE)){ans<-get(hash,cache);ans[["key"]]<-key;output[[ci]]<-ans;next}
 ans<-tryCatch(withCallingHandlers({
  if(nrow(d)<2)stop("At least 2 valid contrasts are required.")
  trts<-sort(unique(c(d[["A"]],d[["B"]])))
  tokens<-lapply(trts,function(s)if(s=="control")character() else strsplit(s,"+",fixed=TRUE)[[1]])
  comps<-sort(unique(unlist(tokens)))
  C<-matrix(0,length(trts),length(comps),dimnames=list(trts,comps))
  for(i in seq_along(tokens))for(a in tokens[[i]])C[i,a]<-C[i,a]+1
  X<-C[d[["A"]],,drop=FALSE]-C[d[["B"]],,drop=FALSE]
  if(!length(comps)||qr(X)$rank<length(comps)) stop("Components are not identifiable from the contrasts.")
  # The page has no study field: this oracle explicitly validates its declared
  # independent-row model. Native-study results are retained separately below.
  args<-list(TE=d[["te"]],seTE=d[["se"]],treat1=d[["A"]],treat2=d[["B"]],studlab=seq_len(nrow(d)),sm="MD",common=TRUE,random=TRUE)
  nc<-do.call(netmeta::netconnection,args[c("treat1","treat2","studlab")])
  connected<-G(nc,"n.subnets")==1
  fit<-function(ids){
   aa<-args;aa[["studlab"]]<-ids
   if(connected){nn<-do.call(netmeta::netmeta,c(aa,list(method.tau="DL")));netmeta::netcomb(nn,C.matrix=C,common=TRUE,random=TRUE)}
   else do.call(netmeta::discomb,c(aa,list(C.matrix=C)))
  }
  z<-fit(seq_len(nrow(d))); vals<-pack(z)
  native<-NULL
  if(anyDuplicated(d[["study"]])) native<-tryCatch(pack(fit(d[["study"]])),error=function(e)list(error=conditionMessage(e)))
  c(list(key=key,status="ok",oracle=if(connected)"netcomb(netmeta(method.tau=DL), C.matrix)" else "discomb(C.matrix)",connected=connected,k=nrow(d),studies=length(unique(d[["study"]])),comps=as.list(comps),combination_names=as.list(setdiff(trts,"control")),native=native,design=unname(split(X,row(X)))),vals)
 },warning=function(w){warnings<<-c(warnings,conditionMessage(w));invokeRestart("muffleWarning")}),error=function(e)list(key=key,status=if(conditionMessage(e)%in%c("At least 2 valid contrasts are required.","Components are not identifiable from the contrasts."))"refused" else "error",reason=conditionMessage(e)))
 ans[["warnings"]]<-as.list(unique(warnings));assign(hash,ans,cache);output[[ci]]<-ans
 if(ci%%20==0){write_json17(output,"wrapper-partial.json");cat(ci,"/",length(corpus),"completed\n");flush.console();gc()}
}
write_json17(output,"wrapper-reference.json")
cat("REFERENCE",length(output),"configurations;",sum(vapply(output,function(z)G(z,"status")=="ok",logical(1))),"numerical fits;",sum(vapply(output,function(z)G(z,"status")=="refused",logical(1))),"support refusals;",sum(vapply(output,function(z)G(z,"status")=="error",logical(1))),"errors\n")
