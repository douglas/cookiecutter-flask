# coding: utf-8

"""
Defines pytest fixtures that will be used in other tests.
"""

import pytest
from webtest import TestApp

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import Test


@pytest.fixture
def app():
    """An application for the tests."""
    _app = create_app(Test)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture
def testapp(app):
    """A Webtest app."""
    return TestApp(app)
