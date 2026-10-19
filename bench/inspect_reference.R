source("r_session.R")
for(f in c("nma_additive","createC","prepare")) writeLines(capture.output(print(get(f,asNamespace("netmeta")))),paste0("documentation/",f,"-source.txt"))
z<-discomb(TE=c(-.4,-.3,-.65,-.55,-.2,-.45,-.8),seTE=c(.12,.15,.13,.16,.18,.14,.20),treat1=c("a","b","a+b","a+c","c","b+c","a+b+c"),treat2=rep("control",7),studlab=1:7,inactive="control",sm="MD")
print(z)
for(n in c("comps","trts","Comp.random","Comb.random","Cov.random","C.matrix","X.matrix","Q.additive","df.Q.additive","tau")) {cat(n,"\n");print(z[[n,exact=TRUE]])}
