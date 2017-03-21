cookiecutter-flask
==================

A(nother) Flask template for cookiecutter.

.. image:: https://travis-ci.org/douglas/cookiecutter-flask.svg?branch=master
    :target: https://travis-ci.org/douglas/cookiecutter-flask

Use it now
----------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/douglas/cookiecutter-flask.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Features
--------

- Bootstrap 3 and Font Awesome 4 with starter templates
- Procfile for deploying to a PaaS (e.g. Heroku)
- pytest and Factory-Boy for testing (example tests included)
- Flask's Click CLI configured with simple commands
- Optional bower support for frontend package management
- Useful debug toolbar
- i18n
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns

Inspiration
-----------

- `Sloria cookiecutter-flask <https://github.com/sloria/cookiecutter-flask>`
- `Building Websites in Python with Flask <http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/>`_
- `Getting Bigger with Flask <http://maximebf.com/blog/2012/11/getting-bigger-with-flask/>`_
- `Structuring Flask Apps <http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/>`_
- `Flask-Foundation <https://github.com/JackStouffer/Flask-Foundation>`_ by `@JackStouffer <https://github.com/JackStouffer>`_
- `flask-bones <https://github.com/cburmeister/flask-bones>`_ by `@cburmeister <https://github.com/cburmeister>`_
- `flask-basic-registration <https://github.com/mjhea0/flask-basic-registration>`_ by `@mjhea0 <https://github.com/mjhea0>`_
- `Flask Official Documentation <http://flask.pocoo.org/docs/>`_


License
-------

BSD License.

Changelog
---------

0.0.1 (20/03/2017)
******************

- Add several improvements
- Derivating from `Sloria <https://github.com/sloria/cookiecutter-flask>`
