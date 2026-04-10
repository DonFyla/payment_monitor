"""
ASGI config for chess_academy project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chess_academy.settings')

application = get_asgi_application()
