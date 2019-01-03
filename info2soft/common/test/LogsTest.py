
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.v20181227.Logs import Logs
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
    
                
class LogsTestCase(unittest.TestCase):

    def testListTaskLog(self):
        a = Auth(username, pwd)
        logs = Logs(a)
        body = {}
        r = logs.listTaskLog(body)
        print(r[0])

    def testListHALog(self):
        a = Auth(username, pwd)
        logs = Logs(a)
        body = {}
        r = logs.listHALog(body)
        print(r[0])

    def testListNodeLog(self):
        a = Auth(username, pwd)
        logs = Logs(a)
        body = {}
        r = logs.listNodeLog(body)
        print(r[0])

    def testListNpsvrLog(self):
        a = Auth(username, pwd)
        logs = Logs(a)
        body = {}
        r = logs.listNpsvrLog(body)
        print(r[0])

    def testListTrafficLog(self):
        a = Auth(username, pwd)
        logs = Logs(a)
        body = {}
        r = logs.listTrafficLog(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
