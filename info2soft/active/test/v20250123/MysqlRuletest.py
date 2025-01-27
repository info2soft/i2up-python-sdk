
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import MysqlRule
from info2soft.active.v20250123.MysqlRule import MysqlRule
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


class MysqlRuleTestCase(unittest.TestCase):

    def testListBkTakeoveNetworkCard(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        mysqlRule = MysqlRule(a)
        r = mysqlRule.listBkTakeoveNetworkCard(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MysqlRule', 'listBkTakeoveNetworkCard', body)

    def testCreateBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '6aEF6382-53Bb-8B87-D2eB-aa239deA84cb',
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
        
        
        mysqlRule = MysqlRule(a)
        r = mysqlRule.createBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MysqlRule', 'createBkTakeover', body)

    def testDescribeBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mysqlRule = MysqlRule(a)
        r = mysqlRule.describeBkTakeover(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MysqlRule', 'describeBkTakeover', body)

    def testDeleteBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'force': False,
            'uuids': '9DE3DAC1-AC53-D88C-5c4B-Ba07ffba91f6',
        }
        
        
        mysqlRule = MysqlRule(a)
        r = mysqlRule.deleteBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MysqlRule', 'deleteBkTakeover', body)

    def testDescribeBkTakeoverResult(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuid': 'cFE8B23d-2D8A-cA8e-d9A6-6dD5B8fD773A',
        }
        
        
        mysqlRule = MysqlRule(a)
        r = mysqlRule.describeBkTakeoverResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MysqlRule', 'describeBkTakeoverResult', body)

    def testStopBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuids': '4Ac9De11-Af75-031B-c879-b51fCE8dE698',
            'operate': '',
        }
        
        
        mysqlRule = MysqlRule(a)
        r = mysqlRule.stopBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MysqlRule', 'stopBkTakeover', body)

    def testRestartBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuids': '942bff8D-02d3-eCcE-C6CB-55d3e07bB2d6',
            'operate': '',
        }
        
        
        mysqlRule = MysqlRule(a)
        r = mysqlRule.restartBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MysqlRule', 'restartBkTakeover', body)

    def testListBkTakeoverStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        mysqlRule = MysqlRule(a)
        r = mysqlRule.listBkTakeoverStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MysqlRule', 'listBkTakeoverStatus', body)

    def testListBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        mysqlRule = MysqlRule(a)
        r = mysqlRule.listBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MysqlRule', 'listBkTakeover', body)


if __name__ == '__main__':
    unittest.main()
