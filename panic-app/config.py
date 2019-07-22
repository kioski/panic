import os
from umongo import MotorAsyncIOInstance

def to_bool(value):
    return str(value).strip().lower() in ['1', 'true', 'yes']

def to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


SECRET_KEY = os.environ.get('APP_SECRET_KEY', 'some-secret-key')

MONGODB_USERNAME = os.environ.get("MONGODB_USERNAME", "user")
MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD", "password")
MONGODB_HOST = os.environ.get("MONGODB_HOST", "mongodb")
MONGODB_PORT = to_int(os.environ.get("MONGODB_PORT", 27017))
MONGODB_DATABASE = os.environ.get("MONGODB_DATABASE", None)
MONGODB_URI = 'mongodb://{}:{}@{}:{}/{}'.format(
    MONGODB_USERNAME,
    MONGODB_PASSWORD,
    MONGODB_HOST,
    MONGODB_PORT,
    MONGODB_DATABASE
)
LAZY_UMONGO = MotorAsyncIOInstance()