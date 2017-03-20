# coding: utf-8

"""
Test applicatin configs and settings
"""

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import Development, Production


def test_production_config():
    """ Test the Production configurations """

    app = create_app(Production)
    assert app.config['DEBUG'] is False
    assert app.config['DEBUG_TB_ENABLED'] is False


def test_dev_config():
    """ Test the Development configurations """

    app = create_app(Development)
    assert app.config['DEBUG'] is True
