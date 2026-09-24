@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
python "%SCRIPT_DIR%git20260905.py" %*
set "EXIT_CODE=%ERRORLEVEL%"
echo.
echo git20260905 finished with exit code %EXIT_CODE%.
pause
exit /b %EXIT_CODE%
