import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '#cbn!5h@=e03-$tp9v%fv(4p)hsanx-5ydu-cg!4@6=+yd&fx%'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True