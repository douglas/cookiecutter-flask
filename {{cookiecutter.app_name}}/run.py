# coding: utf-8

"""
Create an application instance.
"""

from flask import request

from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import CONFIG

app = create_app(CONFIG)


@app.babel.localeselector
def get_locale():
    languages = CONFIG.LANGUAGES.keys()
    return request.accept_languages.best_match(languages)


if __name__ == "__main__":
    app.run()
