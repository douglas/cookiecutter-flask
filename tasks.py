# coding: utf-8

"""
Invoke tasks
"""

import os
import json
import shutil

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'cookiecutter.json'), 'r') as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)

COOKIEAPP_DIR = os.path.join(HERE, COOKIECUTTER_SETTINGS['app_name'])
APP = os.path.join(COOKIEAPP_DIR, 'run.py')


@task
def build(ctx):
    """ Build the cookiecutter """
    ctx.run('cookiecutter {0} --no-input'.format(HERE))


@task
def clean(ctx):
    """ Clean out generated cookiecutter. """
    
    if os.path.exists(COOKIEAPP_DIR):
        shutil.rmtree(COOKIEAPP_DIR)
        print('Removed {0}'.format(COOKIEAPP_DIR))
    else:
        print('App directory does not exist. Skipping.')


def _run_flask_command(ctx, command):
    ctx.run('FLASK_APP={0} flask {1}'.format(APP, command), echo=True)


@task(pre=[clean, build])
def test(ctx):
    """ Run the tests """
    
    os.chdir(COOKIEAPP_DIR)
    _run_flask_command(ctx, 'test')
