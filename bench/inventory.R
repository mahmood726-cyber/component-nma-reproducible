source("r_session.R")
dir.create("documentation",showWarnings=FALSE)
inventory <- list()
catalogue <- as.data.frame(data(package=.packages(all.available=TRUE))[["results",exact=TRUE]],stringsAsFactors=FALSE)
catalogue[["LibPath"]] <- NULL
write.csv(catalogue,"installed-data-catalogue.csv",row.names=FALSE)
for (pkg in c("netmeta","metadat","meta","metafor","metabook","mixmeta","mvmeta")) {
 d <- as.data.frame(data(package=pkg)[["results",exact=TRUE]],stringsAsFactors=FALSE)
 rd <- tools::Rd_db(pkg)
 for (i in seq_len(nrow(d))) {
  nm <- d[["Item",exact=TRUE]][i]
  e <- new.env(); data(list=nm,package=pkg,envir=e)
  x <- get(nm,envir=e)
  doc <- rd[[paste0(nm,".Rd"),exact=TRUE]]
  txt <- if(!is.null(doc)) capture.output(tools::Rd2txt(doc)) else "No matching Rd"
  writeLines(txt,file.path("documentation",paste0(pkg,"-",nm,".txt")))
  inventory[[length(inventory)+1]] <- list(package=pkg,dataset=nm,title=d[["Title",exact=TRUE]][i],class=class(x),nrow=nrow(x),columns=names(x),structure=capture.output(str(x)),head=capture.output(print(head(x))))
 }
}
write_json17(inventory,"inventory.json")
for (f in c("netmeta","netcomb","discomb")) {
 writeLines(capture.output(print(get(f,asNamespace("netmeta")))),paste0("documentation/",f,"-source.txt"))
 writeLines(capture.output(tools::Rd2txt(tools::Rd_db("netmeta")[[paste0(f,".Rd"),exact=TRUE]])),paste0("documentation/",f,"-help.txt"))
}
cat(length(inventory),"datasets inventoried\n")
