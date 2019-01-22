
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

    def testListTaskLog(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'F97B3FD5-4D5D-41EE-22A9-740A74E1E13C',
            'level': 1,
            'start': 1,
            'page': 1,
            'end': 1,
            'limit': 10,
        }
        logs = Logs(a)
        r = logs.listTaskLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Logs', 'listTaskLog', body)

    def testListHALog(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'end': 1,
            'level': 1,
            'start': 1,
            'node_uuid': '',
            'page': 1,
            'limit': 1,
        }
        logs = Logs(a)
        r = logs.listHALog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Logs', 'listHALog', body)

    def testListNodeLog(self):
        a = Auth(username, pwd)
        body = {
            'level': 1,
            'page': 1,
            'limit': 10,
            'start': 1,
            'uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'end': 1,
        }
        logs = Logs(a)
        r = logs.listNodeLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Logs', 'listNodeLog', body)

    def testListNpsvrLog(self):
        a = Auth(username, pwd)
        logs = Logs(a)
        r = logs.listNpsvrLog()
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Logs', 'listNpsvrLog', None)

    def testListTrafficLog(self):
        a = Auth(username, pwd)
        body = {
            'start_stamp': 1545637314,
            'type': 'month',
            'uuid': 'F97B3FD5-4D5D-41EE-22A9-740A74E1E13C',
        }
        logs = Logs(a)
        r = logs.listTrafficLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Logs', 'listTrafficLog', body)


if __name__ == '__main__':
    unittest.main()  
