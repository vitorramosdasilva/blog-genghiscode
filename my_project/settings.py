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


SECRET_KEY = os.environ.get ('SECRET_KEY') 
# SECRET_KEY = '&q_u05&=5+k36)*#n85*3-m)yi%94w#=9wx^v@a+dtb^n9r+i&'
# EMAIL_HOST_USER = os.environ.get ('EMAIL_HOST_USER') 
# EMAIL_HOST_PASSWORD = os.environ.get ('EMAIL_HOST_PASSWORD')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# ALLOWED_HOSTS = ['*']

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'blog-genghiscode.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps ..
    'my_app',
    # Libs
    'ckeditor',
    'ckeditor_uploader',
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
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # apps
                'my_app.context_processors.categories',
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

# Produção ....
DATABASES = { 
    'default': dj_database_url.config()
}
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
# DATABASES = { 'default': dj_database_url.config(conn_max_age=500) }
# DATABASES['default'] = dj_database_url.parse('postgres://lyxyddsxzirukw:626edb6da9450520320c7bf8caf26e3e47e7998dd0cc44b3594c838378abd436@ec2-18-235-109-97.compute-1.amazonaws.com:5432/d2j8pckd7ip2vr', conn_max_age=600)

# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)
# DATABASES = { 'default': dj_database_url.config() }

# Em Produção ....
# DATABASES = {
#     'default': dj_database_url.config()
# }

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

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Em Dev .....
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Em produção ....
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_URL = '/media/'
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR,'static')
# STATICFILES_DIRS = [os.path.join(BASE_DIR,'my_project/staticfiles')]
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ADMIN_MEDIA_PREFIX = '/static/admin/'
CKEDITOR_UPLOAD_PATH = "uploads/"
django_heroku.settings(locals())


