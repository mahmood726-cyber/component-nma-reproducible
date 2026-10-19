source("r_session.R")
G<-function(x,n)x[[n,exact=TRUE]]
corpus<-jsonlite::fromJSON("corpus.json",simplifyVector=FALSE)
if(file.exists("focused-corpus.json"))corpus<-c(corpus,jsonlite::fromJSON("focused-corpus.json",simplifyVector=FALSE))
output<-list(); cache<-new.env(parent=emptyenv())
previous<-if(file.exists("reference.json"))jsonlite::fromJSON("reference.json",simplifyVector=FALSE) else list()
previous<-setNames(previous,vapply(previous,function(x)G(x,"key"),character(1)))
refresh_native<-"native" %in% commandArgs(TRUE)
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
 if(key %in% names(previous) && !(refresh_native && !is.null(G(previous[[key,exact=TRUE]],"native")))){output[[ci]]<-previous[[key,exact=TRUE]];next}
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
   # Call the installed implementation used verbatim by netcomb/discomb.
   # This bypasses only the unrelated standard-NMA design decomposition.
   # netmeta normalizes contrast direction before prepare; covar_study assumes
   # lexically ordered pairs within each multi-arm study. Preserve the original
   # page design separately, but apply that package preprocessing here.
   dd<-d;flip<-match(dd[["A"]],trts)>match(dd[["B"]],trts)
   oldA<-dd[["A"]];dd[["A"]][flip]<-dd[["B"]][flip];dd[["B"]][flip]<-oldA[flip];dd[["te"]][flip]<--dd[["te"]][flip]
   B<-matrix(0,nrow(dd),length(trts),dimnames=list(NULL,trts))
   for(i in seq_len(nrow(dd))){B[i,dd[["A"]][i]]<-1;B[i,dd[["B"]][i]]<--1}
   XF<-B%*%C
   if(anyDuplicated(ids))get("chkmultiarm",asNamespace("netmeta"))(dd[["te"]],dd[["se"]],dd[["A"]],dd[["B"]],ids,correlated=rep(FALSE,nrow(dd)))
   prepare<-get("prepare",asNamespace("netmeta"));engine<-get("nma_additive",asNamespace("netmeta"));inverse<-get("invmat",asNamespace("netmeta"))
   prepared<-function(tau)prepare(dd[["te"]],dd[["se"]],dd[["A"]],dd[["B"]],ids,tau=tau,func.inverse=inverse)
   p0<-prepared(0);dat0<-G(p0,"data")
   narms<-G(dat0,"narms")[!duplicated(G(dat0,"studlab"))]
   df<-sum(narms)-length(unique(ids))-ncol(X)
   calc<-function(pp){dat<-G(pp,"data");oo<-G(dat,"order");engine(G(dat,"TE"),G(pp,"W"),G(dat,"treat1"),G(dat,"treat2"),G(dat,"studlab"),.95,XF[oo,,drop=FALSE],C,B[oo,,drop=FALSE],df,length(trts),":")}
   fe<-calc(p0);re<-calc(prepared(G(fe,"tau")))
   effect<-function(which,nms){zz<-G(re,which);setNames(lapply(seq_along(nms),function(i)list(est=as.numeric(G(zz,"TE")[i]),se=as.numeric(G(zz,"seTE")[i]),lo=as.numeric(G(zz,"lower")[i]),hi=as.numeric(G(zz,"upper")[i]))),nms)}
   list(tau2=G(fe,"tau")^2,Q=G(fe,"Q.additive"),df=G(fe,"df.Q.additive"),components=effect("components",comps),combinations=effect("combinations",trts),C=unname(split(C,row(C))),C_rows=as.list(trts),C_cols=as.list(comps))
  }
  vals<-fit(seq_len(nrow(d)))
  native<-NULL
  if(anyDuplicated(d[["study"]])) native<-tryCatch(fit(d[["study"]]),error=function(e)list(error=conditionMessage(e)))
  c(list(key=key,status="ok",oracle="netmeta:::nma_additive + prepare (unmodified netcomb/discomb implementation)",connected=connected,k=nrow(d),studies=length(unique(d[["study"]])),comps=as.list(comps),combination_names=as.list(setdiff(trts,"control")),native=native,design=unname(split(X,row(X)))),vals)
 },warning=function(w){warnings<<-c(warnings,conditionMessage(w));invokeRestart("muffleWarning")}),error=function(e)list(key=key,status=if(conditionMessage(e)%in%c("At least 2 valid contrasts are required.","Components are not identifiable from the contrasts."))"refused" else "error",reason=conditionMessage(e)))
 ans[["warnings"]]<-as.list(unique(warnings));assign(hash,ans,cache);output[[ci]]<-ans
 if(ci%%20==0){write_json17(output,"reference-partial.json");cat(ci,"/",length(corpus),"completed\n");flush.console();gc()}
}
# Preserve matrix dimensions in JSON even for a one-component design.
for(i in seq_along(output)) {
 for(n in c("design","C")) if(!is.null(G(output[[i]],n))) output[[i]][[n]]<-lapply(G(output[[i]],n),as.list)
}
write_json17(output,"reference.json")
cat("REFERENCE",length(output),"configurations;",sum(vapply(output,function(z)G(z,"status")=="ok",logical(1))),"numerical fits;",sum(vapply(output,function(z)G(z,"status")=="refused",logical(1))),"support refusals;",sum(vapply(output,function(z)G(z,"status")=="error",logical(1))),"errors\n")
