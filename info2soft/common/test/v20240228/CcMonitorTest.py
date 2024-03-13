
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.common.v20240228.CcMonitor import CcMonitor
# from info2soft.common.v20200722.CcMonitor import CcMonitor
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


class CcMonitorTestCase(unittest.TestCase):

    def testListCcMonitor(self):
        a = Auth(username, pwd)
        body = {
        }
        
        ccMonitor = CcMonitor(a)
        r = ccMonitor.listCcMonitor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CcMonitor', 'listCcMonitor', body)

    def testListNodeStatus(self):
        a = Auth(username, pwd)
        body = {
            'node_ip': '',
            'start_time': 1,
            'last_time': 1,
        }
        
        ccMonitor = CcMonitor(a)
        r = ccMonitor.listNodeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CcMonitor', 'listNodeStatus', body)

    def testListCronTask(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 15,
        }

        ccMonitor = CcMonitor(a)
        r = ccMonitor.listCronTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CcMonitor', 'listCronTask', body)

    def testResetCronTask(self):
        a = Auth(username, pwd)
        body = {
            'id': 4,
            '_': 'f7d34d2ebc8e6',
        }

        ccMonitor = CcMonitor(a)
        r = ccMonitor.resetCronTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CcMonitor', 'resetCronTask', body)

    def testModifyCronTask(self):
        a = Auth(username, pwd)
        body = {
            'id': '',
            'interval': 1,
        }

        ccMonitor = CcMonitor(a)
        r = ccMonitor.modifyCronTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CcMonitor', 'modifyCronTask', body)

    def testDescribeCcGeneralInfo(self):
        a = Auth(username, pwd)
        body = {
            'type': 'all',
            'process_sort_by': 'cpu',
            'process_filter_name': '',
            'process_limit': 1,
        }

        ccMonitor = CcMonitor(a)
        r = ccMonitor.describeCcGeneralInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CcMonitor', 'describeCcGeneralInfo', body)

    def teststartCcService(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'service_name': ''
        }

        ccMonitor = CcMonitor(a)
        r = ccMonitor.startCcService(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'startCcService', body)

    def testreloadCcService(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'service_name': ''
        }

        ccMonitor = CcMonitor(a)
        r = ccMonitor.reloadCcService(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'reloadCcService', body)

    def teststopCcService(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'service_name': ''
        }

        ccMonitor = CcMonitor(a)
        r = ccMonitor.stopCcService(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'stopCcService', body)

    def testkillCcProcess(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'pid': ''
        }

        ccMonitor = CcMonitor(a)
        r = ccMonitor.killCcProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'killCcProcess', body)


if __name__ == '__main__':
    unittest.main()
