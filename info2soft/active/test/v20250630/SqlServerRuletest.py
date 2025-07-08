
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import SqlServerRule
from info2soft.active.v20250630.SqlServerRule import SqlServerRule
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
    def setUp(self):
        """在每个测试方法运行前执行"""
        self.original_cwd = os.getcwd()
        # 获取当前测试文件的目录
        test_dir = os.path.dirname(os.path.abspath(__file__))
        # 切换工作目录到测试文件所在的目录
        os.chdir(test_dir)

    def tearDown(self):
        """在每个测试方法运行后执行"""
        # 恢复原始工作目录，避免影响其他测试
        os.chdir(self.original_cwd)

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
            'rule_uuid': 'ACdCCA2e-33bC-DEFc-Ce8f-B3b5dB98d2E1',
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
            'uuids': 'dFb15860-FEd2-e26b-Ae43-Bd01226CfDAc',
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.deleteBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'deleteBkTakeover', body)

    def testDescribeBkTakeoverResult(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuid': '0D0c72E5-c3A3-E126-bb77-40fF9ca2C9dd',
        }
        
        
        sqlServerRule = SqlServerRule(a)
        r = sqlServerRule.describeBkTakeoverResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SqlServerRule', 'describeBkTakeoverResult', body)

    def testStopBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuids': 'A32C7fDa-4A6c-831f-9AcF-610fA4ff4e22',
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
            'bk_takeover_uuids': '76cFEffF-EBdC-49c0-abdD-981Fb149dbaE',
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
