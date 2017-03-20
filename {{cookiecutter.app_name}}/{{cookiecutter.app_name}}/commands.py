# coding: utf-8

"""
Custom Flask commands using Click.
"""

import os
import sys
import click
import shutil


@click.command()
def test():
    """ Run the tests """
    
    import pytest
    sys.exit(pytest.main(sys.argv[2:]))


@click.command()
def clean():
    """
    Remove *.pyc, *.pyo, __pycache__ files recursively starting at current directory.
    
    Borrowed from Flask-Script, converted to use Click.
    """
    
    for dirpath, dirnames, filenames in os.walk('.'):
        for dirname in dirnames:
            if dirname == "__pycache__":
                full_pathname = os.path.join(dirpath, dirname)
                click.echo('Removing {}'.format(full_pathname))
                shutil.rmtree(full_pathname)
        for filename in filenames:
            if filename.endswith('.pyc') or filename.endswith('.pyo'):
                full_pathname = os.path.join(dirpath, filename)
                click.echo('Removing {}'.format(full_pathname))
                os.remove(full_pathname)
