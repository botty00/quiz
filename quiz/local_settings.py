import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '+&*!k5f2z#952s(x(h^7-+8xvc6lzr&5odn+)se3hwq*k#aboi'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True