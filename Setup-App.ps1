# Chess Academy Payment System - First Time Setup Script

Write-Host "`n===========================================" -ForegroundColor Cyan
Write-Host "   Chess Academy - First Time Setup" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing dependencies (this may take a few minutes)..." -ForegroundColor Yellow
pip install -r requirements.txt

# Run migrations
Write-Host "Running database migrations..." -ForegroundColor Yellow
python manage.py migrate --noinput

# Create superuser
Write-Host "`n===========================================" -ForegroundColor Green
Write-Host "   Create Admin Account" -ForegroundColor Green
Write-Host "===========================================" -ForegroundColor Green
python manage.py createsuperuser

# Ask about sample data
Write-Host "`n"
$sampleData = Read-Host "Create sample parents? (y/n)"
if ($sampleData -eq 'y' -or $sampleData -eq 'Y') {
    python manage.py create_sample_data
}

Write-Host "`n===========================================" -ForegroundColor Green
Write-Host "   Setup Complete!" -ForegroundColor Green
Write-Host "===========================================" -ForegroundColor Green
Write-Host ""
Write-Host "To start the server, run: " -NoNewline
Write-Host ".\Start-App.ps1" -ForegroundColor Cyan
Write-Host "or" -ForegroundColor Gray
Write-Host "Start the app by double-clicking: " -NoNewline
Write-Host "start.bat" -ForegroundColor Cyan
Write-Host ""

Read-Host "Press Enter to exit"
