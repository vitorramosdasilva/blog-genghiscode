import os
import dj_database_url
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# #### Removido SECURITY KEY
# SECURITY WARNING: keep the secret key used in production secret!


SECRET_KEY = os.environ.get('SECRET_KEY')

# EMAIL_HOST_USER = os.environ.get ('EMAIL_HOST_USER') 
# EMAIL_HOST_PASSWORD = os.environ.get ('EMAIL_HOST_PASSWORD')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = os.environ.get('DEBUG') == True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'https://xxxxx.pythonanywhere.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps ..
    'blog',
    'categoria',
    # Libs
    'ckeditor',
    'cloudinary',
    'crispy_forms',
    'accounts',
    # 'ckeditor_uploader',
    # 'widget_tweaks',
    # 'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # em produção ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_project.urls'
# 'DIRS': [os.path.join(BASE_DIR, 'templates')],

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # apps
                'blog.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# #### Removida Configuracoes do Banco de Dados Posgres...

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Python Whenere ..
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Produção ....
# DATABASES = {
#     'default': dj_database_url.config()
# }
# django_heroku.settings(locals())

# Em Dev ....
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'blog',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Prod PythonAnyWhere
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
ADMIN_MEDIA_PREFIX = '/static/admin/'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = 'media'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_RESTRICT_BY_USER = True
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_DIRS = [
#     'statics'
# ]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/accounts/login'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CLOUDINARY = {
    'cloud_name': os.environ.get('cloud_name'),
    'api_key': os.environ.get('api_key'),
    'api_secret': os.environ.get('api_secret')
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Em Dev .....
# STATIC_URL = '/static/'
# MEDIA_URL = '/mediSa/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_RESTRICT_BY_USER = True

# if ON_HEROKU:
#     DATABASE_URL = 'postgresql://<postgresql>'
# else:
#     DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

# DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

try:
    from .local_settings import *
except ImportError:
    pass

