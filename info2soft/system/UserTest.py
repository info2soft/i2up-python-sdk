
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.system.v20181227.User import User
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
    
                
class UserTestCase(unittest.TestCase):

    def testCreateUser(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.createUser(body)
        print(r[0])

    def testListUser(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.listUser(body)
        print(r[0])

    def testDescribeUser(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.describeUser(body)
        print(r[0])

    def testDeleteUser(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.deleteUser(body)
        print(r[0])

    def testModifyUser(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.modifyUser(body)
        print(r[0])

    def testModifyUserPwd(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.modifyUserPwd(body)
        print(r[0])

    def testListProfile(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.listProfile(body)
        print(r[0])

    def testModifyProfile(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.modifyProfile(body)
        print(r[0])

    def testLogout(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.logout(body)
        print(r[0])

    def testUpdateSetting(self):
        a = Auth(username, pwd)
        user = User(a)
        body = {}
        r = user.updateSetting(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
