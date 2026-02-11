@echo off
REM Job Application Sender - Quick Start Script (Windows)

echo ================================================
echo   Job Application Sender - Quick Start
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed!
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo X Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [OK] Dependencies installed successfully
echo.

REM Create uploads folder
if not exist "uploads" mkdir uploads

echo ================================================
echo   Starting the application...
echo ================================================
echo.
echo Backend will run on: http://localhost:5000
echo Frontend: Open http://localhost:5000 in your browser
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the Flask app
python app.py
