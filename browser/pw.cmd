@echo off
set R_LIBS_USER=<AUDIT_ROOT>/allmeta-offload/Rlib_dta
set R_LIBS=<AUDIT_ROOT>/allmeta-offload/Rlib_extra
set R_ENVIRON_USER=NUL
set RS="C:\Program Files\R\R-4.6.0\bin\Rscript.exe"
call :main > <AUDIT_ROOT>\jobs\pw.log 2>&1
echo %ERRORLEVEL% > <AUDIT_ROOT>\jobs\pw.done
exit /b
:main
cd /d <AUDIT_ROOT>\allmeta\hub\shared\tests
copy /y <AUDIT_ROOT>\jobs\component-nma-parity.spec.mjs component-nma-parity.spec.mjs
copy /y <AUDIT_ROOT>\jobs\pw.strict.config.mjs zz-p19-local.config.mjs
set PW_CHANNEL=msedge
call npx playwright test component-nma-parity.spec.mjs nma-bus-reader.spec.mjs chart-export.spec.mjs a11y-sweep.spec.mjs --config zz-p19-local.config.mjs --workers=1 --reporter=list
echo PW_EXIT=%ERRORLEVEL%
del zz-p19-local.config.mjs
rmdir /s /q test-results
exit /b %ERRORLEVEL%
