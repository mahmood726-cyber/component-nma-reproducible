source("r_session.R")
G<-function(x,n)x[[n,exact=TRUE]]
out<-list()
for(c in jsonlite::fromJSON("bus-corpus.json",simplifyVector=FALSE)){
 if(!is.null(G(c,"expected_refusal"))){out[[length(out)+1]]<-list(key=G(c,"key"),reason=G(c,"expected_refusal"));next}
 env<-G(c,"env");sm<-G(env,"effectMeasure");rows<-list()
 for(s in G(env,"studies")){
  a<-G(s,"arms")[[1]];b<-G(s,"arms")[[2]]
  if(sm%in%c("OR","RR"))z<-metafor::escalc(measure=sm,ai=G(a,"events"),n1i=G(a,"n"),ci=G(b,"events"),n2i=G(b,"n"),add=.5,to="only0",drop00=FALSE)
  else z<-metafor::escalc(measure=sm,m1i=G(a,"mean"),sd1i=G(a,"sd"),n1i=G(a,"n"),m2i=G(b,"mean"),sd2i=G(b,"sd"),n2i=G(b,"n"))
  rows[[length(rows)+1]]<-list(te=as.numeric(G(z,"yi")),se=sqrt(as.numeric(G(z,"vi"))))
 }
 out[[length(out)+1]]<-list(key=G(c,"key"),rows=rows)
}
write_json17(out,"bus-reference.json");cat("BUS REFERENCE",length(out),"cases\n")
