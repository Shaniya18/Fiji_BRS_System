import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from a .env file (only for local dev)
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. SECURITY SETTINGS
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-fallback-key-123')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# On Render, we need to allow our specific domain
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'fiji-brs-system.onrender.com,localhost,127.0.0.1').split(',')

# 2. INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'flights',
    'baggage_app',
]

# 3. MIDDLEWARE (WhiteNoise is correctly placed here)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Essential for static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'airport_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'airport_main.wsgi.application'

# 4. DATABASE CONFIGURATION
# This uses your Aiven MySQL details securely via Render's Environment Variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('AIVEN_DB_NAME', 'defaultdb'),
        'USER': os.environ.get('AIVEN_DB_USER', 'avnadmin'),
        'PASSWORD': os.environ.get('AIVEN_DB_PASSWORD'), 
        'HOST': os.environ.get('AIVEN_DB_HOST', 'brs-db-fiji-brs-2026.e.aivencloud.com'),
        'PORT': os.environ.get('AIVEN_DB_PORT', '23182'),
        'OPTIONS': {
            'ssl': {'ca': os.path.join(BASE_DIR, 'ca.pem')},
        }
    }
}

# 5. PASSWORD VALIDATORS
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 6. INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 7. STATIC FILES & CORS
CORS_ALLOW_ALL_ORIGINS = True # Essential for your C# dashboard to talk to the API

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# WhiteNoise helps serve static files without a separate web server
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 8. LOGGING (Crucial for debugging Render builds)
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