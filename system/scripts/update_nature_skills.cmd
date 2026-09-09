@echo off
setlocal
set "SCRIPT_DIR=%~dp0"

echo Nature Skills updater
echo =====================
echo.

python "%SCRIPT_DIR%update_nature_skills.py" %*
set "EXIT_CODE=%ERRORLEVEL%"

echo.
if "%EXIT_CODE%"=="0" (
    echo Finished successfully.
) else (
    echo The updater stopped with exit code %EXIT_CODE%.
    echo Send the message above to Codex if you need help.
)
echo.
pause
exit /b %EXIT_CODE%
