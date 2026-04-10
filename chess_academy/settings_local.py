"""
Local development settings for chess_academy project.
Uses SQLite database - no Docker required!
"""

from .settings import *

# Use SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Disable browser reload in local mode (optional)
# INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'django_browser_reload']
# MIDDLEWARE = [m for m in MIDDLEWARE if 'django_browser_reload' not in m]

# Console email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug settings
DEBUG = True
SECRET_KEY = 'local-dev-secret-key-not-for-production-use-only'

print("=" * 60)
print("Running in LOCAL DEVELOPMENT mode with SQLite")
print("=" * 60)
