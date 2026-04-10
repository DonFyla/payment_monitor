# Chess Academy Payment System - PowerShell Startup Script

Write-Host "`n===========================================" -ForegroundColor Cyan
Write-Host "   Chess Academy Payment System - Startup" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -q -r requirements.txt

# Run migrations
Write-Host "Running database migrations..." -ForegroundColor Yellow
python manage.py migrate --noinput

# Check if we should create sample data
$dbExists = Test-Path "db.sqlite3"
if (-not $dbExists) {
    Write-Host "`nDatabase created!" -ForegroundColor Green
}

Write-Host "`n===========================================" -ForegroundColor Green
Write-Host "   Starting Development Server" -ForegroundColor Green
Write-Host "===========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Access the app at: " -NoNewline
Write-Host "http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "Admin panel at: " -NoNewline
Write-Host "http://127.0.0.1:8000/admin" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press CTRL+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python manage.py runserver
