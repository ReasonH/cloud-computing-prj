"""
Django settings for Bloud project.
Generated by 'django-admin startproject' using Django 2.2.1.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from Bloud import awsconf
import os
import json
from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i86&&&+=xisnp&-lv(m0*y=@v5iao0ukbprh-4yh-)%6i%go_$'
SOCIAL_AUTH_GOOGLE_PLUS_KEY = "771200825076-t9048l4trbksh202c2ipce299vibvdge.apps.googleusercontent.com" #클라이언트 ID를 사이에 입력
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = "sIpUzJsMQxmrYv9OzFchasjW" #보안 비밀을 사이에 입력

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'web.apps.WebConfig',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Bloud.urls'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',  #구글 로그인 처리를 위한 파이썬 클래스
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    'django.contrib.auth.backends.ModelBackend', # Django 기본 유저모델
]

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
                'social_django.context_processors.backends',  # social 로그인 관련 template 추가부분
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Bloud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/tempfile/'
MEDIA_ROOT = os.path.join(BASE_DIR, "tempfile")

# Login redirect

LOGIN_REDIRECT_URL = '/login_check/'
LOGOUT_REDIRECT_URL = 'home'

# AWS

# If these are not defined, the EC2 instance profile and IAM role are used.
# This requires you to add boto3 (or botocore, which is a dependency of boto3)
# to your project dependencies.
AWS_ACCESS_KEY_ID = awsconf.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = awsconf.AWS_SECRET_ACCESS_KEY
