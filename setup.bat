@echo off
echo.
echo ===========================================
echo   Chess Academy - First Time Setup
echo ===========================================
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies (this may take a few minutes)...
pip install -r requirements.txt

REM Run migrations
echo Running database migrations...
python manage.py migrate --noinput

REM Create superuser
echo.
echo ===========================================
echo   Create Admin Account
echo ===========================================
python manage.py createsuperuser

REM Create sample data
echo.
set /p sample_data="Create sample parents? (y/n): "
if /i "%sample_data%"=="y" (
    python manage.py create_sample_data
)

echo.
echo ===========================================
echo   Setup Complete!
echo ===========================================
echo.
echo To start the server, run: start.bat
echo.
pause
