# 開発環境固有の設定ファイル

from .settings_common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#5t_28ka8lyfr_ls-5&o*^99l_5_qpcg4@$z%lnk1$-@5g$qwb'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




# ロギング設定
LOGGING = {
    'version': 1,   # 1固定
    'disable_existing_loggers': False,

    # ロガー設定
    'loggers': {
        # djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(pastime)s',
                '[%(level)s]',
                '%(pathname)s(Line:%(lineno)d',
                '%(message)s'
            ])
        },
    }
}

# メール配送先をコンソールに設定する
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
