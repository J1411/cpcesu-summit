from .shared import(
    BASE_DIR,
    PROJ_DIR,
    SECRET_KEY,
    DEBUG,
    ALLOWED_HOSTS,
    INSTALLED_APPS,
    MIDDLEWARE,
    ROOT_URLCONF,
    TEMPLATES,
    WSGI_APPLICATION,
    DATABASES,
    AUTH_PASSWORD_VALIDATORS,
    LANGUAGE_CODE,
    TIME_ZONE,
    USE_I18N,
    USE_L10N,
    USE_TZ,
    STATIC_URL,
    STATICFILES_DIRS,
    STATIC_ROOT,
    APPEND_SLASH,
    LOGIN_URL,
    LOGOUT_REDIRECT_URL,
)

__all__ = [
    'BASE_DIR',
    'PROJ_DIR',
    'SECRET_KEY',
    'DEBUG',
    'ALLOWED_HOSTS',
    'INSTALLED_APPS',
    'MIDDLEWARE',
    'ROOT_URLCONF',
    'TEMPLATES',
    'WSGI_APPLICATION',
    'DATABASES',
    'AUTH_PASSWORD_VALIDATORS',
    'LANGUAGE_CODE',
    'TIME_ZONE',
    'USE_I18N',
    'USE_L10N',
    'USE_TZ',
    'STATIC_URL',
    'STATICFILES_DIRS',
    'STATIC_ROOT',
    'APPEND_SLASH',
    'INTERNAL_IPS',
    'LOGIN_URL',
    'LOGOUT_REDIRECT_URL',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'summit_db',
    'USER': 'summit_db_user',
    'PASSWORD': '$umM1T_DB)',
    'HOST': '127.0.0.1',
    'PORT': '5432'
}
INTERNAL_IPS = ['127.0.0.1', 'localhost']
INSTALLED_APPS = ['whitenoise.runserver_nostatic', *INSTALLED_APPS, 'debug_toolbar']
