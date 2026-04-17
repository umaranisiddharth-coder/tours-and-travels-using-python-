"""
Add top 20 Indian cities with real hotel names, images, descriptions.
Run: py reset_hotels.py
"""
from app import create_app, db
from app.models import Hotel

app = create_app()

HOTELS = [
