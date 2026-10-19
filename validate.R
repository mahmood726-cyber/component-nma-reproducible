# One-command validation: Rscript validate.R (run from the archive root).
# Checks R/package versions, verifies every archived input against SOURCE_SHA256.json, refits all
# 595 configurations afresh with netmeta, compares both archived page captures with that fresh
# reference, and exits non-zero on any mismatch with expected/paper_values.json.
lib <- c(Sys.getenv('R_LIBS_USER'), strsplit(Sys.getenv('R_LIBS'), .Platform$path.sep)[[1]])
.libPaths(c(lib[nzchar(lib)], .libPaths()))
print(.libPaths())
pkgs <- c('netmeta', 'meta', 'metadat', 'metafor', 'jsonlite')
actual <- c(R = as.character(getRversion()), vapply(pkgs, function(p) as.character(packageVersion(p)), character(1)))
print(actual)
expected <- c(R = '4.6.0', netmeta = '3.7.0', meta = '8.5.0', metadat = '1.6.0', metafor = '5.2.1', jsonlite = '2.0.0')
if (!identical(actual, expected)) stop('Wrong R or package versions (expected ', paste(names(expected), expected, collapse = ', '), ')')
python <- Sys.getenv('PYTHON', unset = 'python')
if (system2(python, c('analysis/verify_archive.py')) != 0) stop('Archive integrity check failed')
rs <- file.path(R.home('bin'), if (.Platform$OS.type == 'windows') 'Rscript.exe' else 'Rscript')
t0 <- Sys.time()
status <- system2(python, c('analysis/run_validation.py', shQuote(rs)))
if (status != 0) stop('Full R validation failed')
cat(sprintf('VALIDATE PASS in %.1f minutes\n', as.numeric(difftime(Sys.time(), t0, units = 'mins'))))
