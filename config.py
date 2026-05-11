import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'

    # Database
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASS = os.getenv('DB_PASS', '')
    DB_NAME = os.getenv('DB_NAME', 'srtravels')
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Site
    SITE_NAME = os.getenv('SITE_NAME', 'SR Travels')
    SITE_URL = os.getenv('SITE_URL', 'http://localhost:5000')
    SITE_EMAIL = os.getenv('SITE_EMAIL', 'info@srtravels.com')
    SITE_PHONE = os.getenv('SITE_PHONE', '+91-9356437871')

    # Payment
    PAYMENT_TEST_MODE = os.getenv('PAYMENT_TEST_MODE', 'false') == 'true'
    RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID', '')
    RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET', '')
    PAYTM_MID = os.getenv('PAYTM_MID', '')
    PAYTM_KEY = os.getenv('PAYTM_KEY', '')
    PHONEPE_MERCHANT_ID = os.getenv('PHONEPE_MERCHANT_ID', '')
    PHONEPE_SALT_KEY = os.getenv('PHONEPE_SALT_KEY', '')

    # Email
    MAIL_SERVER = os.getenv('SMTP_HOST', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('SMTP_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('SMTP_USERNAME', '')
    MAIL_PASSWORD = os.getenv('SMTP_PASSWORD', '')
    MAIL_DEFAULT_SENDER = os.getenv('SITE_EMAIL', 'info@srtravels.com')

    # Google Maps
    GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY', '')
    WHATSAPP_ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN', '')
    WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID', '')

    # Booking
    BOOKING_TIMEOUT = 900       # 15 minutes
    ADVANCE_BOOKING_DAYS = 90
    CANCELLATION_HOURS = 6
