import dj_database_url
from django.contrib import messages
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv
import os
from pathlib import Path
import sys

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# If SECRET_KEY is not set as environment variable, use a default value (optional)
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is not set!")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# Application definition
INSTALLED_APPS = [
    "stabby_web.apps.StabbyWebConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_resized",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "stabby.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "stabby_web.context_processors.collectors_group",
            ],
        },
    },
]

WSGI_APPLICATION = "stabby.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# SQLite
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "stabby.sqlite3",
#     }
# }
# python manage.py dumpdata --exclude stabby_web.ViewBladeGrid --exclude stabby_web.ViewKnifeGrid --exclude stabby_web.ViewSharpenerGrid --exclude=contenttypes.ContentType >  db.json

if DEVELOPMENT_MODE is True:
    # postgres
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": "localhost",  # Set to empty string for localhost.
            "PORT": "5432",  # Default port for PostgreSQL.
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != "collectstatic":
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "US/Central"

USE_I18N = True

USE_TZ = True

USE_DEPRECATED_PYTZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# STATICFILES_DIRS = [BASE_DIR / "stabby_web" / "static"]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "stabby_web/static"),
]

AWS_ACCESS_KEY_ID = os.getenv("SPACES_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("SPACES_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("SPACES_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.getenv("SPACES_URL")
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_QUERYSTRING_AUTH = True
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}

if not DEVELOPMENT_MODE:
    DEFAULT_FILE_STORAGE = "stabby_web.storage_backends.MediaStorage"

STORAGES = {
    "default": {
        "BACKEND": "stabby_web.media_storage.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

if DEVELOPMENT_MODE:
    MEDIA_URL = "/media/"
else:
    MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{os.getenv('SPACES_LOCATION', 'images')}/"


MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Directory to export staticfiles for production
# All files from all STATICFILES_DIRS will be copied by
# manage.py collectstatic to this directory.
# /!\ It will not be served by django, you have to setup
# your webserver (or use a third party module)
# to serve assets from there.
STATIC_ROOT = BASE_DIR / "production_assets"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "/"

MESSAGE_TAGS = {
    messages.DEBUG: "Info",
    messages.INFO: "Info",
    messages.SUCCESS: "Success",
    messages.WARNING: "Warning",
    messages.ERROR: "Error",
}
