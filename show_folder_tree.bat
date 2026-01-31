@echo off
echo Bismillahirrahmanirrahim
echo.
echo Generating folder tree...
echo.

REM Get the directory where this batch file is located
set "CURRENT_DIR=%~dp0"
set "CURRENT_DIR=%CURRENT_DIR:~0,-1%"

REM Python script should be in the same folder
set "PY_SCRIPT=%CURRENT_DIR%\folder_tree.py"

REM Check if Python script exists
if not exist "%PY_SCRIPT%" (
    echo ERROR: folder_tree.py not found!
    echo Make sure both files are in the same folder.
    pause
    exit /b 1
)

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    pause
    exit /b 1
)

REM Run the Python script
set "OUTPUT_FILE=%CURRENT_DIR%\folder_tree_output.txt"
chcp 65001 >nul
python "%PY_SCRIPT%" "%CURRENT_DIR%" > "%OUTPUT_FILE%" 2>&1
chcp 1252 >nul

if errorlevel 1 (
    echo ERROR: Python script failed!
) else (
    echo SUCCESS!
)

echo.
echo Elhamdulillah Done!
echo Tree saved to: folder_tree_output.txt
echo.

REM Open the output file
if exist "%OUTPUT_FILE%" (
    start notepad "%OUTPUT_FILE%"
)

pause
