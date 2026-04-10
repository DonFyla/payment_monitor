#!/usr/bin/env python
"""
Simple script to run the Django application locally without Docker.
This sets up SQLite database and runs migrations automatically.
"""
import os
import subprocess
import sys


def run_command(command, description):
    """Run a command and print status"""
    print(f"\n{'='*60}")
    print(f"{description}...")
    print('='*60)
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error: {description} failed!")
        sys.exit(1)
    print(f"✓ {description} completed!")


def main():
    # Set environment variables for local development
    os.environ.setdefault('DEBUG', '1')
    os.environ.setdefault('SECRET_KEY', 'local-dev-secret-key-not-for-production')
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║          Chess Academy Payment System - Local Setup          ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Run migrations
    run_command('python manage.py migrate', 'Running database migrations')
    
    # Create superuser if needed
    print("\n" + "="*60)
    print("Would you like to create an admin user? (y/n)")
    print("="*60)
    response = input().strip().lower()
    if response == 'y':
        run_command('python manage.py createsuperuser', 'Creating admin user')
    
    # Create sample data
    print("\n" + "="*60)
    print("Would you like to create sample data? (y/n)")
    print("="*60)
    response = input().strip().lower()
    if response == 'y':
        run_command('python manage.py create_sample_data', 'Creating sample data')
    
    # Run server
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    Starting Server...                        ║
║                                                              ║
║  Access the application at: http://127.0.0.1:8000           ║
║  Admin panel: http://127.0.0.1:8000/admin                   ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    subprocess.run('python manage.py runserver', shell=True)


if __name__ == '__main__':
    main()
