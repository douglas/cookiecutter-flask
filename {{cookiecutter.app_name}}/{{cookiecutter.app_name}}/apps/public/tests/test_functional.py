# coding: utf-8

"""
Functional tests for the public app
"""


class TestPublicViews:
    """ Test the public app views """

    def test_index_returns_200(self, testapp):
        """ Index page """

        client = testapp.get('/')
        assert client.status_code == 200
