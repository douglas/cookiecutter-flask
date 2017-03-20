# coding: utf-8

"""
The app module, containing the app factory function.
"""

from flask import Flask
from flask_babel import Babel

from {{cookiecutter.app_name}} import commands
from {{cookiecutter.app_name}}.extensions import debug_toolbar
from {{cookiecutter.app_name}}.settings import Production
from {{cookiecutter.app_name}}.apps import public


def create_app(environment=Production):
    """
    The application factory
    """

    app = Flask(__name__.split(".")[0])
    app.babel = Babel(app)
    app.config.from_object(environment)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    """ Register Flask extensions. """

    debug_toolbar.init_app(app)


def register_blueprints(app):
    """ Register Flask blueprints. """

    app.register_blueprint(public.views.blueprint)


def register_commands(app):
    """ Register Click commands """

    app.cli.add_command(commands.test)
    app.cli.add_command(commands.clean)
