# coding: utf-8

import os
from envparse import env

# Try to read an env file with the development
# configs
env.read_envfile()


class Production(object):
    """ Production configuration """

    SECRET_KEY = env("SECRET")
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG = False
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    LANGUAGES = {
        "en": "English",
        "pt_br": "Brazilian Portuguese"
    }


class Development(Production):
    """ Development configuration """

    DEBUG = True
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True


class Test(Production):
    """ Test configuration. """

    TESTING = True
    DEBUG = True

CONFIG = Development if env("FLASK_DEBUG") == "1" else Production
