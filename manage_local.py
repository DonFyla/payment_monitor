#!/usr/bin/env python
"""Management script for local development (SQLite)"""
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chess_academy.settings_local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Did you install requirements?\n"
            "Run: pip install -r requirements.txt"
        ) from exc
    execute_from_command_line(sys.argv)
