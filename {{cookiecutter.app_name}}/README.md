===============================
{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Quickstart
----------

Before running shell commands, set the ``SECRET``, ``FLASK_APP`` and ``FLASK_DEBUG``
environment variables ::

.. code-block:: bash

    export SECRET="something-really-secret"
    export FLASK_APP=run.py
    export FLASK_DEBUG=1

Then run the following commands to bootstrap your environment ::

.. code-block:: bash

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
    cd {{cookiecutter.app_name}}
    pipenv --three
    pipenv install --dev
    flask run

You will see a pretty welcome screen.


Deployment
----------

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``Production`` configuration
is used.


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
-------------

To run all tests, run ::

    flask test
