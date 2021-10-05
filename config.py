import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = b'o\xa4\xcd\xd4A\xafWAG\xb8g\xc6\x93\x921c\xafZ\x1a#\xe0p\x19\x11\x1b\xd8\x84\x82/\x7fA\xef\x13\x15'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

HOST = os.getenv('HOST', '127.0.0.1')
PORT = os.getenv('PORT', 12345)
