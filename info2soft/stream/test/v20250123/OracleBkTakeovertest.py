
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import OracleBkTakeover
from info2soft.stream.v20250123.OracleBkTakeover import OracleBkTakeover
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
            'rule_uuid': 'f09444AA-D9d0-6a8F-6D22-Addf7a2F7aA6',
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

    def testDescribeBkTakeoverResult(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuid': '5fECbBF2-4FA4-3AdD-C6D5-C7700E5cDd30',
        }
        
        
        oracleBkTakeover = OracleBkTakeover(a)
        r = oracleBkTakeover.describeBkTakeoverResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleBkTakeover', 'describeBkTakeoverResult', body)


if __name__ == '__main__':
    unittest.main()
