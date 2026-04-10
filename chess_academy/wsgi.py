"""
WSGI config for chess_academy project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chess_academy.settings')

application = get_wsgi_application()
