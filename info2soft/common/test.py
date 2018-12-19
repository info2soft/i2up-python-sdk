# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft import Auth

from info2soft.compat import is_py2, is_py3

if is_py2:
    import sys
    import StringIO
    import urllib

    # reload(sys)
    sys.setdefaultencoding('utf-8')
    StringIO = StringIO.StringIO
    urlopen = urllib.urlopen
if is_py3:
    import io
    import urllib

    StringIO = io.StringIO
    urlopen = urllib.request.urlopen


username = 'admin'
pwd = 'Info1234'


class AuthTestCase(unittest.TestCase):
    def test_token(self):
        a = Auth(username, pwd)
        token = a.token()
        print(token)


if __name__ == '__main__':
    unittest.main()
