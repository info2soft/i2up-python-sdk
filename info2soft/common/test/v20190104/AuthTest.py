
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.Auth import Auth
from info2soft import Auth
from info2soft.fileWriter import write
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
        r = a.describePhoneCode()
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Auth', 'describePhoneCode', None)

    def testRegAccount(self):
        a = Auth(username, pwd)
        r = a.regAccount()
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Auth', 'regAccount', None)

    def testToken(self):
        a = Auth(username, pwd)
        body = {
            'pwd': 'Info1234',
            'username': 'admin',
        }
        r = a.token(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Auth', 'token', body)

    def testResetPwd(self):
        a = Auth(username, pwd)
        r = a.resetPwd()
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Auth', 'resetPwd', None)

    def testCheckLoginStatus(self):
        a = Auth(username, pwd)
        body = {
            'access_token': 'a10b45cd8b94ad53UEsc8H-gxjMU-jX76eFd2z4eoDh0vlVkPPDWaJyBWssjwWdYAtk4SdFaL8dQH48QQv29c3TRNX3FQo4Ub_V1qwehbRQ28KBEtYqTG6wy8sbAEWPVcBoE2uWXnmP_J5R9hXl8yHbeyaMwMjLpWe0onA',
        }
        r = a.checkLoginStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Auth', 'checkLoginStatus', body)


if __name__ == '__main__':
    unittest.main()  
