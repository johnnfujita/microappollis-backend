"""
Django settings for microbackend project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import csv
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd64)w&pu77wd37#e4sziun*ghph+ezq5&u@_7v4mw+(l%2(f0q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["microappollis.com", "*", 'localhost:3000']


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    

    
]

LOCAL_APPS = [
    'ggg_art.apps.GggArtConfig',
    'user_profiles.apps.UserProfilesConfig',
    'generic_vendor_profiles.apps.GenericVendorProfilesConfig',
    'product_generic_catalog.apps.ProductGenericCatalogConfig',
    'orders.apps.OrdersConfig',
    'microaccounts.apps.MicroaccountsConfig'
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    'djoser',
    'storages'
]


INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

AUTH_USER_MODEL = 'microaccounts.Account'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'microbackend.custompagination.LimitOffsetPaginationWithUpperBound',
    'PAGE_SIZE': 4,
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    "DEFAUL_PERMISSION_CLASSES": (
        "rest_frameword.permissions.IsAuthenticated",
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "rest_framework.authentication.TokenAuthentication",
    ),
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ),
    # 'DEFAULT_THROTTLE_RATES': {
    #     # 'anon': '300/hour',
    #     # 'user': '10/hour',
    #     # 'artworks': '20/hour',
    #     # 'locations': '15/hour'
    # }
    
}



DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {
        "user_create_password_retype": "microaccounts.serializers.UserCreateSerializerNew",
        "user": "microaccounts.serializers.UserCreateSerializerNew",
        "user_delete": "djoser.serializers.UserDeleteSerializer"
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'microbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'microbackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'microshop_2',
        'HOST': '127.0.0.1',
        'PORT': 5432,
        'PASSWORD': 'socratesdaimones666',
        'USER': 'microdaemon'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


EMAIL_BACKEND = "django_ses.SESBackend"
EMAIL_HOST_USER = "nao-responda@microappollis.com"
DEFAULT_FROM_EMAIL = "nao-responda@microappollis.com"

with open('../../private_config.csv', 'r') as csv_file:
        secrets = csv.reader(csv_file, delimiter=",")
        for row in secrets:
            AWS_ACCESS_KEY_ID = row[0]
            AWS_SECRET_ACCESS_KEY = row[1]
            AWS_STORAGE_BUCKET_NAME = row[2]
            
            AWS_S3_FILE_OVERWRITE = False
            AWS_DEFAULT_ACL = None
            DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'