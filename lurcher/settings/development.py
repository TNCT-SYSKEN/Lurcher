from .base import *

# この設定でMySQLの構成お願いします
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lurcher',
        'USER': 'lurcher',
        'PASSWORD': 'lurcher',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}