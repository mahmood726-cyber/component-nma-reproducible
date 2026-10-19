source("r_session.R")
G<-function(x,n)x[[n,exact=TRUE]]
old<-jsonlite::fromJSON("wrapper-reference.json",simplifyVector=FALSE)
cases<-jsonlite::fromJSON("focused-corpus.json",simplifyVector=FALSE)
wanted<-paste0("focused::",c("built-in","tiny","saturated","disconnected-identifiable","no-literal-control-identifiable"))
out<-old[!vapply(old,function(x)G(x,"key")%in%wanted,logical(1))]
for(c in cases){
 if(!G(c,"key")%in%wanted)next
 d<-do.call(rbind,lapply(G(c,"rows"),as.data.frame,stringsAsFactors=FALSE));warns<-character()
 result<-tryCatch(withCallingHandlers({
  z<-netmeta::discomb(TE=d[["te"]],seTE=d[["se"]],treat1=d[["A"]],treat2=d[["B"]],studlab=seq_len(nrow(d)),sm="MD",inactive=if("control"%in%c(d[["A"]],d[["B"]]))"control" else NULL,common=TRUE,random=TRUE)
  effect<-function(prefix,nms){setNames(lapply(seq_along(nms),function(i)list(est=G(z,paste0(prefix,".random"))[i],se=G(z,paste0("se",prefix,".random"))[i],lo=G(z,paste0("lower.",prefix,".random"))[i],hi=G(z,paste0("upper.",prefix,".random"))[i])),nms)}
  list(key=G(c,"key"),status="ok",oracle="public discomb with automatic C and inactive control",tau2=G(z,"tau")^2,Q=G(z,"Q.additive"),df=G(z,"df.Q.additive"),components=effect("Comp",G(z,"comps")),combinations=effect("Comb",G(z,"trts")))
 },warning=function(w){warns<<-c(warns,conditionMessage(w));invokeRestart("muffleWarning")}),error=function(e)list(key=G(c,"key"),status="error",reason=conditionMessage(e)))
 result[["warnings"]]<-as.list(warns);out[[length(out)+1]]<-result
 cat(G(c,"key"),G(result,"status"),"\n")
}
write_json17(out,"wrapper-reference.json");cat("PUBLIC DISCOMB BRIDGE",length(out),"total retained wrapper cases\n")
