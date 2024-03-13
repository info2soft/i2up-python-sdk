
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import OracleBkTakeover
from info2soft.stream.v20240228.OracleBkTakeover import OracleBkTakeover
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


class OracleBkTakeoverTestCase(unittest.TestCase):

    def testListBkTakeoveNetworkCard(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.listBkTakeoveNetworkCard(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'listBkTakeoveNetworkCard', body)

    def testCreateBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '2c12DEf2-59Ab-E73E-a22e-45CD4d6e5085',
            'type': 1,
            'enable_trgjob': 1,
            'enable_alter_seq': 1,
            'start_val': 10,
            'execute_script': 1,
            'enable_attachip': 0,
            'net_adapter': '',
            'ip': '',
            'disable_trgjob': 1,
            'dettach_ip': 1,
            'script_content': '',
        }
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.createBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'createBkTakeover', body)

    def testDescribeBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.describeBkTakeover(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'describeBkTakeover', body)

    def testDescribeBkTakeoverResult(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuid': '87763FDc-BBf2-7e0e-ddFD-fe7B8defC197',
        }
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.describeBkTakeoverResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'describeBkTakeoverResult', body)

    def testStopBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuids': '1A9EbB73-fe15-8AE6-Ad25-9B2eFFdeb11c',
            'operate': '',
        }
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.stopBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'stopBkTakeover', body)


if __name__ == '__main__':
    unittest.main()
