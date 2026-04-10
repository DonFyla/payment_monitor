@echo off
echo.
echo ===========================================
echo   Chess Academy Payment System - Startup
echo ===========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -q -r requirements.txt

REM Run migrations
echo Running database migrations...
python manage.py migrate --noinput

REM Check if superuser exists (optional)
echo.
echo ===========================================
echo   Starting Development Server
echo ===========================================
echo.
echo Access the app at: http://127.0.0.1:8000
echo Admin panel at: http://127.0.0.1:8000/admin
echo.
echo Press CTRL+C to stop the server
echo.

python manage.py runserver

pause
