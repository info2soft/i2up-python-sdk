
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import GuardData
from info2soft.guardData.v20250123.GuardData import GuardData
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
pwd = 'Info@123'


class GuardDataTestCase(unittest.TestCase):

    def testNodeGuardDataEnabled(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '',
            'config_port': 1,
        }
        
        
        guardData = GuardData(a)
        r = guardData.nodeGuardDataEnabled(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GuardData', 'nodeGuardDataEnabled', body)

    def testListGuardData(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        guardData = GuardData(a)
        r = guardData.listGuardData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GuardData', 'listGuardData', body)

    def testCreateGuardData(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'policy_name': '',
            'subject': '',
            'object': '',
            'operate': 1,
            'decision': 1,
            'policy_type': 0,
        }
        
        
        guardData = GuardData(a)
        r = guardData.createGuardData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GuardData', 'createGuardData', body)

    def testModifyGuardData(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'policy_name': '',
            'subject': '',
            'object': '',
            'operate': 1,
            'decision': 1,
            'policy_type': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        guardData = GuardData(a)
        r = guardData.modifyGuardData(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GuardData', 'modifyGuardData', body)

    def testDeleteGuardData(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuids': [],
        }
        
        
        guardData = GuardData(a)
        r = guardData.deleteGuardData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GuardData', 'deleteGuardData', body)

    def testListNodeStatus(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
        }
        
        
        guardData = GuardData(a)
        r = guardData.listNodeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GuardData', 'listNodeStatus', body)

    def testListGuardDataLogs(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'page': 1,
            'limit': 1,
            'start': 0,
            'end': 0,
        }
        
        
        guardData = GuardData(a)
        r = guardData.listGuardDataLogs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GuardData', 'listGuardDataLogs', body)

    def testThreatPerception(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'start': 1,
            'end': 1,
        }
        
        
        guardData = GuardData(a)
        r = guardData.threatPerception(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GuardData', 'threatPerception', body)


if __name__ == '__main__':
    unittest.main()
