import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_URL = 'http://localhost:7777/v1/'
BACKEND_URL = 'http://localhost:7777'
CENT_URL='http://localhost:9999/api'
CENT_KEY='e904b803-f695-4286-8af1-063b346a3955'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='769722....rcontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='...-YooaN'


'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pressa',                                   # Or path to database file if using sqlite3.
        'USER': 'root',                                   # Not used with sqlite3.
        'PASSWORD': '1q2w3e',                             # Not used with sqlite3.
        'HOST': 'localhost',                              # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                                         # Set to empty string for default. Not used with sqlite3.
    }
}




'''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
