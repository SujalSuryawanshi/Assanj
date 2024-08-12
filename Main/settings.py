import os
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-#ui%=r7zuufjfwktbv(#-1)%zgryp!2h*^^u&-q0x9pjpz(jyw'

DEBUG = False

ALLOWED_HOSTS = ['assanj.in','www.assanj.in','16.171.226.0']
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',   
    'allauth.account',  
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', 
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'embed_video',
    'core.templatetags',
    'crispy_forms',
    'crispy_bootstrap5',
    'core.apps.CoreConfig',
    'users.apps.UsersConfig',
]
AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 )
SITE_ID = 11

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL='/'
CRISPY_TEMPLATE_PACK = 'bootstrap5'



SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH2_CLIENT_ID': '911869189913-edsvf14np1nb8nqor7sp7tqdkgpobgkn.apps.googleusercontent.com',
        'OAUTH2_CLIENT_SECRET': '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',
        'OAUTH2_AUTHORIZE_URL': 'https://accounts.google.com/o/oauth2/auth',
        'OAUTH2_TOKEN_URL': 'https://accounts.google.com/o/oauth2/token',
    }
}


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '911869189913-edsvf14np1nb8nqor7sp7tqdkgpobgkn.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'core.middleware.SingleDeviceLoginMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
AUTH_USER_MODEL = 'users.CustomUser'

ROOT_URLCONF = 'Main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,('templates/'))],
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
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
WSGI_APPLICATION = 'Main.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'Anotheros',
         'USER': 'Thomas',
         'PASSWORD': 'noHackerhere#wwe14',
         'HOST': 'database-1.cda6weukikb8.eu-north-1.rds.amazonaws.com',
         'PORT': '5432',
    }
}
# Password validation
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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#STATICS
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticar')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#MAP
GOOGLE_MAPS_API_KEY = 'your_api_key'



# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CSRF_TRUSTED_ORIGINS = [
    'https://assanj.in',
    'https://www.assanj.in',
]



AWS_ACCESS_KEY_ID = 'AKIA42PHHYCVEFACWFIT '
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'anotheros'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'eu-north-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
