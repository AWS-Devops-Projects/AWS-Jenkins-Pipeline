# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from web import myapp
import unittest

# python -m unittest test_app


class TestMyApp(unittest.TestCase):

    def setUp(self):
        self.app = myapp.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        assert b'Congratulations' in rv.data
        #assert False

    def test_404(self):
        rv = self.app.get('/other')
        self.assertEqual(rv.status, '404 NOT FOUND')


if __name__ == '__main__':
    unittest.main()
