@echo off

REM Check if Python 3.11 is installed
python3.11 --version 2>nul | findstr /r /c:"3\.11" >nul
if errorlevel 1 (
    echo Python 3.11 is not installed. Please install Python 3.11 and try again.
    exit /b 1
)

REM Create virtual environment with Python 3.11
python3.11 -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

echo Virtual environment setup complete.
