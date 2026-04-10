import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
=======

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
>>>>>>> e6072b2243bbfe2f022f0de6a5997cee871c48ad
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-xwqkcuj8wv9f6nwm7()+cew-oblp0y&0%fl_*er+^0$(+et%%2'
)

<<<<<<< HEAD
=======
# SECURITY WARNING: don't run with debug turned on in production!
>>>>>>> e6072b2243bbfe2f022f0de6a5997cee871c48ad
DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        'DJANGO_ALLOWED_HOSTS',
<<<<<<< HEAD
        'localhost,127.0.0.1'
=======
        'nolwazis-blog.vercel.app,.vercel.app'
>>>>>>> e6072b2243bbfe2f022f0de6a5997cee871c48ad
    ).split(',')
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    'https://nolwazis-blog.vercel.app',
    'https://*.vercel.app',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recipes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nolwazi_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nolwazi_blog.wsgi.application'

<<<<<<< HEAD
# Database — reads DATABASE_URL env var in production, falls back to SQLite locally
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR}/db.sqlite3',
        conn_max_age=600,
=======

# Database
# Use DATABASE_URL from Vercel / Neon
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
>>>>>>> e6072b2243bbfe2f022f0de6a5997cee871c48ad
    )
}


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

<<<<<<< HEAD
=======

# Password validation
>>>>>>> e6072b2243bbfe2f022f0de6a5997cee871c48ad
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

<<<<<<< HEAD
=======

# Internationalization
>>>>>>> e6072b2243bbfe2f022f0de6a5997cee871c48ad
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

<<<<<<< HEAD
# Static files
STATIC_URL = '/static/'
=======

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
>>>>>>> e6072b2243bbfe2f022f0de6a5997cee871c48ad
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

<<<<<<< HEAD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security — Vercel terminates SSL and forwards X-Forwarded-Proto: https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
=======

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
>>>>>>> e6072b2243bbfe2f022f0de6a5997cee871c48ad
