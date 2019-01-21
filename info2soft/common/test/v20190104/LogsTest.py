
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.Logs import Logs
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
    
                
class LogsSDKTestCase(unittest.TestCase):

    def testListOpLog(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'end_time': 1,
            'limit': 10,
            'start_time': 1,
        }
        logs = Logs(a)
        r = logs.listOpLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Logs', 'listOpLog', body)

    def testTempFuncName(self):
        a = Auth(username, pwd)
        body = {
            'start_time': 1508833766,
            'end_time': 1508833953,
        }
        logs = Logs(a)
        r = logs.tempFuncName(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Logs', 'tempFuncName', body)

    def testTempFuncName(self):
        a = Auth(username, pwd)
        body = {
            'end_time': 1,
            'start_time': 1,
        }
        logs = Logs(a)
        r = logs.tempFuncName(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Logs', 'tempFuncName', body)


if __name__ == '__main__':
    unittest.main()  
