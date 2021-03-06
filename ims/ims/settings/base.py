"""
Django settings for ims project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from pathlib import Path

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = 'm_7p0j9frtym$ybb$b%^f231+a)q3bji)yr4e1%3a%h-t0eii$'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventory.apps.InventoryConfig',
    'admin_reorder',
    'adminsortable',
    'import_export',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'ims.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django_settings_export.settings_export',
                # 'ims_context_processors.ims_context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'ims.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ims23',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'gay@tri12345',
    }
} 

LOGIN_URL = '/login'

LOG_LOCATION = [os.path.join(BASE_DIR, 'Logs')]

LOGGING = {
    'version':1,
    'disable_existing_loggers': True,
    'formatters':{
        'log_formatter':{
                        'format': '%(asctime)s, File: %(module)s.py, Function: %(funcName)s, Message: %(message)s'
                    }

                },
    'handlers':{
        'file': {
                    'level': 'DEBUG',
                    'class': 'logging.FileHandler',
                    'filename': 'Logs/debug.log',
                    'formatter': 'log_formatter',
                },
        'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'log_formatter',
                },
               },
    'loggers': {

            'logs': {
                        'handlers': ['file'],
                        'level': 'DEBUG',
                        'propagate': True,
                      },
            'django': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': False,
        },
                }
            }
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

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

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'ims\static')]
STAT_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(STAT_PATH, 'static_root')

# admin models reoredering
ADMIN_REORDER = (
    {'app': 'inventory', 'label': 'Master Data', 'models': (
        'inventory.SubsidiaryMaster', 'inventory.ProjectMaster', 'inventory.EmployeeMaster'
    )},
    {'app': 'auth', 'label': 'Users and Groups', 'models': ('auth.User', 'auth.Group')},
    {'app': 'inventory', 'label': 'Inventory', 'models': (
        'inventory.Device', 'inventory.Allocation', 'inventory.Service', 'inventory.Report',
        'inventory.Item_type', 'inventory.Manufacturer', 'inventory.Location','inventory.ItemName',
        'inventory.CPUTYPE','inventory.RAMS','inventory.OSS','inventory.ManufacturerPart', 'inventory.poYear', 'inventory.poIni'

    )},

)
# ************ IFM LDAP SERVER***************

IFM_LDAP_SERVER = 'inpu12w006.intra.ifm'

# ******** END ***********

# IFM_LDAP_SERVER = 'SANJAY DIST'

InventoryManagementSystem_version = 'version 1.0'

TEMPLATE_CONTEXT_PROCESSORS = (

    'ims_context_processors.ims_context_processor',
)
