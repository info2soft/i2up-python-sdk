# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft import Auth, User, Node, Cluster

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
    def testToken(self):
        a = Auth(username, pwd)
        token = a.token()
        print(token)

    def testDescribePhoneCode(self):
        a = Auth(username, pwd)
        r = a.describePhoneCode()
        print(r)

    def testRegAccount(self):
        a = Auth(username, pwd)
        r = a.regAccount()
        print(r)

    def testResetPwd(self):
        a = Auth(username, pwd)
        r = a.resetPwd()
        print(r)

    def testCheckLoginStatus(self):
        a = Auth(username, pwd)
        r = a.checkLoginStatus()
        print(r)


class SystemTestCase(unittest.TestCase):
    def testGetUser(self):
        a = Auth(username, pwd)
        user = User(a)
        r = user.listUser(10, 10)
        print(r)


class UserTestCase(unittest.TestCase):
    def testUpgradeNode(self):
        a = Auth(username, pwd)
        node = Node(a)
        r = node.listNode({})
        print(r)

class ResTestCase(unittest.TestCase):
    def testGetCluster(self):
        a = Auth(username, pwd)
        cls = Cluster(a)
        r = cls.listCls({})
        print(r)


if __name__ == '__main__':
    unittest.main()
