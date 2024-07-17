from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','3.129.209.56', 'kangaroocook-frontend.s3-website.us-east-2.amazonaws.com', 'd11fdf7a041hyl.cloudfront.net'] # Adjust as per your deployment environment

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'recipe_application',
    'corsheaders',
    'storages',  # Add this for AWS S3
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Keep this at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kanga_backend.urls'

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

WSGI_APPLICATION = 'kanga_backend.wsgi.application'

# CORS Settings
CORS_ALLOW_ALL_ORIGINS = True  # This allows all origins, change in production

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kangacook',
        'USER': 'postgres',
        'PASSWORD': 'Sachin@10000',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# AWS S3 and CloudFront Settings
AWS_ACCESS_KEY_ID =os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'kangaroocook'
AWS_S3_CUSTOM_DOMAIN = 'd11fdf7a041hyl.cloudfront.net'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = None

# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

# Media files (Uploaded files)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password validation, internationalization settings remain unchanged