from pathlib import Path

import environ

env = environ.Env()
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = ROOT_DIR / "jorevi"

env.read_env(str(ROOT_DIR / ".env"))  # noqa F405


# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = "Asia/Shanghai"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres:///jorevi"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CACHE(Default is Redis)
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}
CACHE_TTL = 60 * 5
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"


# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.contenttypes",
    "grappelli.dashboard",
    "grappelli",
    "filebrowser",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.postgres",
    "django.forms",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_countries",
    "mptt",
    "tinymce",
    "reversion",
    "taggit",
    "sorl.thumbnail",
    "phonenumber_field",
    "import_export",
    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
]

LOCAL_APPS = [
    "jorevi.users.apps.UsersConfig",
    "jorevi.blog.apps.BlogConfig",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "jorevi.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.ScryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(APPS_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": True,
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "jorevi.utils.context_processors.settings_context",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = env.str("DJANGO_ADMIN_URL", default="admin")
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""xblzbjs""", "t710255295@gmail.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}


# Celery
# ------------------------------------------------------------------------------
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
CELERY_TIMEZONE = TIME_ZONE  # noqa F405
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_TRACK_STARTED = True
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-time-limit
CELERY_TASK_TIME_LIMIT = 30 * 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-soft-time-limit
CELERY_TASK_SOFT_TIME_LIMIT = 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-always-eager
CELERY_TASK_ALWAYS_EAGER = True
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = True


# django-allauth
# ------------------------------------------------------------------------------
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400  # 1 day in seconds
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login/"
ACCOUNT_ADAPTER = "jorevi.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
ACCOUNT_FORMS = {
    "signup": "jorevi.users.forms.UserSignupForm",
    "login": "jorevi.users.forms.UserLoginForm",
}


# django-compressor
# ------------------------------------------------------------------------------
# https://django-compressor.readthedocs.io/en/stable/settings.html
INSTALLED_APPS += ["compressor"]
STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]


# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"


# django-rest-framework
# -------------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    # API policy settings
    # https://www.django-rest-framework.org/api-guide/settings/#api-policy-settings
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_THROTTLE_CLASSES": ["rest_framework.throttling.UserRateThrottle"],
    "DEFAULT_THROTTLE_RATES": {"user": "1000/day"},
    "DEFAULT_CONTENT_NEGOTIATION_CLASS": "rest_framework.negotiation.DefaultContentNegotiation",
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.openapi.AutoSchema",
    # Generic view settings
    # https://www.django-rest-framework.org/api-guide/settings/#generic-view-settings
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "SEARCH_PARAM": "q",
    "ORDERING_PARAM": "sort_by",
    # Versioning settings
    # https://www.django-rest-framework.org/api-guide/settings/#versioning-settings
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.AcceptHeaderVersioning",
    "DEFAULT_VERSION": "1.0",
    "ALLOWED_VERSIONs": ["1.0"],
    "VERSION_PARAM": "version",
    # Authentication settings
    # https://www.django-rest-framework.org/api-guide/settings/#authentication-settings
    "UNAUTHENTICATED_USER": "django.contrib.auth.models.AnonymousUser",
    "UNAUTHENTICATED_TOKEN": None,
    # Test settings
    # https://www.django-rest-framework.org/api-guide/settings/#test-settings
    "TEST_REQUEST_DEFAULT_FORMAT": "multipart",
    "TEST_REQUEST_RENDERER_CLASSES": (
        "rest_framework.renderers.MultiPartRenderer",
        "rest_framework.renderers.JSONRenderer",
    ),
    # Schema generation controls
    # https://www.django-rest-framework.org/api-guide/settings/#schema-generation-controls
    "SCHEMA_COERCE_PATH_PK": True,
    "SCHEMA_COERCE_METHOD_NAMES": {"retrieve": "read", "destroy": "delete"},
    # Content type controls
    # https://www.django-rest-framework.org/api-guide/settings/#content-type-controls
    "URL_FORMAT_OVERRIDE": "format",
    "FORMAT_SUFFIX_KWARG": "format",
    # Date and time formatting
    # https://www.django-rest-framework.org/api-guide/settings/#date-and-time-formatting
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
    "DATETIME_INPUT_FORMATS": ["%Y-%m-%dT%H:%M:%S%z", "iso-8601"],
    "DATE_FORMAT": "iso-8601",
    "DATE_INPUT_FORMATS": ["iso-8601"],
    "TIME_FORMAT": "iso-8601",
    "TIME_INPUT_FORMATS": ["iso-8601"],
    # Encodings
    # https://www.django-rest-framework.org/api-guide/settings/#encodings
    "UNICODE_JSON": True,
    "COMPACT_JSON": True,
    "STRICT_JSON": True,
    "COERCE_DECIMAL_TO_STRING": True,
    # View names and descriptions
    # https://www.django-rest-framework.org/api-guide/settings/#view-names-and-descriptions
    "VIEW_NAME_FUNCTION": "rest_framework.views.get_view_name",
    "VIEW_DESCRIPTION_FUNCTION": "rest_framework.views.get_view_description",
    # HTML Select Field cutoffs
    # https://www.django-rest-framework.org/api-guide/settings/#html-select-field-cutoffs
    "HTML_SELECT_CUTOFF": 1000,
    "HTML_SELECT_CUTOFF_TEXT": "More than {count} items...",
    # Miscellaneous settings
    # https://www.django-rest-framework.org/api-guide/settings/#miscellaneous-settings
    "EXCEPTION_HANDLER": "jorevi.core.exceptions.custom_exception_handler",
    "NON_FIELD_ERRORS_KEY": "non_field_errors",
    "URL_FIELD_NAME": "url",
    "NUM_PROXIES": None,
}


# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"


# django-tinymce https://django-tinymce.readthedocs.io/en/latest/installation.html#configuration
TINYMCE_DEFAULT_CONFIG = {
    "mode": "textarea",
    "theme": "silver",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
}
TINYMCE_SPELLCHECKER = True


# django-grappelli  https://django-grappelli.readthedocs.io/en/latest/customization.html#available-settings
# ------------------------------------------------------------------------------
GRAPPELLI_ADMIN_TITLE = "jorevi"
GRAPPELLI_AUTOCOMPLETE_LIMIT = 30
# GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS
GRAPPELLI_SWITCH_USER = True
# GRAPPELLI_SWITCH_USER_ORIGINAL
# GRAPPELLI_SWITCH_USER_TARGET
# GRAPPELLI_CLEAN_INPUT_TYPES
GRAPPELLI_INDEX_DASHBOARD = "config.dashboard.CustomIndexDashboard"


# django-filebrowser https://django-filebrowser.readthedocs.io/en/latest/settings.html#settings
# ------------------------------------------------------------------------------
FILEBROWSER_DIRECTORY = "uploads/"


# django-import-export https://django-import-export.readthedocs.io/en/latest/installation.html
# ------------------------------------------------------------------------------
IMPORT_EXPORT_USE_TRANSACTIONS = True
IMPORT_EXPORT_SKIP_ADMIN_LOG = True
IMPORT_EXPORT_TMP_STORAGE_CLASS = "import_export.tmp_storages.TempFolderStorage"
IMPORT_EXPORT_IMPORT_PERMISSION_CODE = "import"
IMPORT_EXPORT_EXPORT_PERMISSION_CODE = "export"
IMPORT_EXPORT_CHUNK_SIZE = 100


# django-phonenumber-field
# ------------------------------------------------------------------------------
PHONENUMBER_DB_FORMAT = "E164"  # default
PHONENUMBER_DEFAULT_REGION = None  # default
PHONENUMBER_DEFAULT_FORMAT = "E164"  # default
