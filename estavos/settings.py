# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

from decouple import Csv, config
from dj_database_url import parse as dburl
from django import VERSION as DJANGO_VERSION
from django.utils.translation import ugettext_lazy as _

######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for conveniently
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
ADMIN_MENU_ORDER = (
    ("Content", ("pages.Page", "blog.BlogPost",
       "generic.ThreadedComment", (_("Media Library"), "fb_browse"),)),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
    ("Users", ("auth.User", "auth.Group",)),
    ("Cursos", ("estavos.courses.Inscription"))
)

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

PAGE_MENU_TEMPLATES = (
    (1, _("Top navigation bar"), "pages/menus/dropdown.html"),
    (2, _("Left-hand tree"), "pages/menus/tree.html"),
    (3, _("Footer"), "pages/menus/footer.html"),
    (4, _("Bottom Footer"), "pages/menus/footer-list.html"),
)

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
# EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         (_("Image"),),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         (_("Another name"),),
#         {"blank": True, "default": 1},
#     ),
# )

# Setting to turn on featured images for blog posts. Defaults to False.

BLOG_USE_FEATURED_IMAGE = True

# If True, the django-modeltranslation will be added to the
# INSTALLED_APPS setting.
USE_MODELTRANSLATION = False


########################
# MAIN DJANGO SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=".estavos.com, .estavos.com.br", cast=Csv())

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

USE_L10N = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "pt-BR"

# Supported languages
LANGUAGES = (
    ('pt_BR', _('Brazilian Portuguese')),
)

# secret_key
SECRET_KEY = config('SECRET_KEY')
NEVERCACHE_KEY = config('NEVERCACHE_KEY')

# A boolean that turns on/off debug mode. When set to ``True``, stack traces
# are displayed for error pages. Should always be set to ``False`` in
# production. Best set to ``True`` in local_settings.py
DEBUG = config('DEBUG', default=False, cast=bool)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

DATE_INPUT_FORMATS = (
    "%d/%m/%Y", "%d/%m/%y"
)

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644


#########
# PATHS #
#########

# Full filesystem path to the project.
PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)


#############
# DATABASES #
#############

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.db')
DATABASES = {
    "default": config('DATABASE_URL', default=default_dburl, cast=dburl),
}

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
static_root_default = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))
STATIC_ROOT = config('STATIC_ROOT', default=static_root_default)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
media_root_default = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))
MEDIA_ROOT = config('MEDIA_ROOT', default=media_root_default)

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = "%s.urls" % PROJECT_APP

################
# APPLICATIONS #
################

INSTALLED_APPS = (
    'estavos.theme',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.galleries",
    "mezzanine.accounts",
    # "mezzanine.twitter",
    'djangosecure',
    'sslserver',
    'django_extensions',
    'test_without_migrations',
    'pagseguro',
    'import_export',
    # "mezzanine.mobile",
    'estavos.courses.apps.CoursesAppConfig',
    'estavos.categorylink',
    'estavos.subscriptions',
    'estavos.tournaments',
    'estavos.clubs',
)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    "mezzanine.core.middleware.UpdateCacheMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment if using internationalisation or localisation
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    # Uncomment the following if using any of the SSL settings:
    "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

# Security directives
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', cast=bool, default=False)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', cast=bool, default=False)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', cast=bool, default=False)
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', cast=int, default=0)

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_ROOT, "templates")
        ],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
            ],
            "builtins": [
                "mezzanine.template.loader_tags",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ]
        },
    },
]

if DJANGO_VERSION < (1, 9):
    del TEMPLATES[0]["OPTIONS"]["builtins"]

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

######################
#   CACHE SETTINGS   #
######################

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "TIMEOUT": config("CACHE_TIMEOUT", default=300, cast=int),
    }
}

CACHE_ANONYMOUS_ONLY = True

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

######################
# DISQUS INTEGRATION #
######################

COMMENTS_DISQUS_SHORTNAME = 'estavos'

#######################
# Email configuration #
#######################

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

######################
# Pagseguro settings #
######################

PAGSEGURO_EMAIL = config('PAGSEGURO_EMAIL')
PAGSEGURO_TOKEN = config('PAGSEGURO_TOKEN')
PAGSEGURO_SANDBOX = config('PAGSEGURO_SANDBOX', cast=bool)
PAGSEGURO_LOG_IN_MODEL = config('PAGSEGURO_LOG_IN_MODEL', cast=bool) # se o valor for True, os checkouts e transações vão ser logadas no database.


####################
# GOOGLE ANALYTICS #
####################

GOOGLE_ANALYTICS_ID = config('GOOGLE_ANALYTICS_ID', default='')

#####################
#    GOOGLE API     #
#####################

SERVICE_ACCOUNT_FILE = config('GAPI_SERVICE_ACCOUNT_FILE')


#####################
# ACCOUNTS SETTINGS #
#####################

ACCOUNTS_VERIFICATION_REQUIRED = True
ACCOUNTS_APPROVAL_REQUIRED = True


##########
# ADMINS #
##########
ADMINS = (('Bruno Barbosa', 'bruno@estavos.com'), )


##########
# FABRIC #
##########
FABRIC = {
    "DEPLOY_TOOL": "git",  # Deploy with "git", "hg", or "rsync"
    "SSH_USER": config("SSH_USER"),  # VPS SSH username
    "HOSTS": ["45.55.197.249"],  # The IP address of your VPS
    "DOMAINS": ["estavos.com", "estavos.com.br", "www.estavos.com", "www.estavos.com.br"],
    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
    "GUNICORN_PORT": 8000,
    "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
    "DB_PASS": config("DB_PASS"),  # Live database password
    "ADMIN_PASS": config("ADMIN_PASS"),  # Live admin user password
    "SECRET_KEY": SECRET_KEY,
    "NEVERCACHE_KEY": NEVERCACHE_KEY,
}

####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
