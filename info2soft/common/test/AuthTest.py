
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.v20181227.Auth import Auth
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

    def testDescribePhoneCode(self):
        a = Auth(username, pwd)
        auth = Auth(a)
        body = {}
        r = auth.describePhoneCode(body)
        print(r[0])

    def testRegAccount(self):
        a = Auth(username, pwd)
        auth = Auth(a)
        body = {}
        r = auth.regAccount(body)
        print(r[0])

    def testToken(self):
        a = Auth(username, pwd)
        auth = Auth(a)
        body = {}
        r = auth.token(body)
        print(r[0])

    def testResetPwd(self):
        a = Auth(username, pwd)
        auth = Auth(a)
        body = {}
        r = auth.resetPwd(body)
        print(r[0])

    def testCheckLoginStatus(self):
        a = Auth(username, pwd)
        auth = Auth(a)
        body = {}
        r = auth.checkLoginStatus(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
