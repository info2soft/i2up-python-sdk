
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import SqlServerRule
from info2soft.active.v20250123.SqlServerRule import SqlServerRule
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


class SqlServerRuleTestCase(unittest.TestCase):

    def testListBkTakeoveNetworkCard(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.listBkTakeoveNetworkCard(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'listBkTakeoveNetworkCard', body)

    def testCreateBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'script_content': '',
            'rule_uuid': 'd57F7Cbe-183D-37b4-f8Ec-A232e1c9493f',
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
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.createBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'createBkTakeover', body)

    def testDescribeBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.describeBkTakeover(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'describeBkTakeover', body)

    def testDeleteBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'force': False,
            'uuids': 'DcB2B150-85AF-480c-21d8-C2cEdBf99e9D',
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.deleteBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'deleteBkTakeover', body)

    def testDescribeBkTakeoverResult(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuid': 'aBEeb6d6-280D-Be8F-010a-06DcdBBfe52A',
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.describeBkTakeoverResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'describeBkTakeoverResult', body)

    def testStopBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuids': 'Bb6fEffb-Bf15-e741-1A3A-fFBe0D1546cf',
            'operate': '',
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.stopBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'stopBkTakeover', body)

    def testRestartBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuids': 'eEAF5129-86c5-96dC-aB9E-FcDcAFB5E4Dd',
            'operate': '',
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.restartBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'restartBkTakeover', body)

    def testListBkTakeoverStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.listBkTakeoverStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'listBkTakeoverStatus', body)

    def testListBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.listBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'listBkTakeover', body)


if __name__ == '__main__':
    unittest.main()
