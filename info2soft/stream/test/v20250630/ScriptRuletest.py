
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import ScriptRule
from info2soft.stream.v20250630.ScriptRule import ScriptRule
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


class ScriptRuleTestCase(unittest.TestCase):
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

    def testCreateRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'node_uuid': '',
            'config': {
            'script': [],
            'src_type': '',
            'dyn_thd': 1,
            'lderrset': 'continue',
            'script_type': 1,},
            'src_db_uuid': '',
        }
        
        
        scriptRule = ScriptRule(a)
        r = scriptRule.createRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptRule', 'createRule', body)

    def testDeleteRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
            'force': True,
        }
        
        
        scriptRule = ScriptRule(a)
        r = scriptRule.deleteRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptRule', 'deleteRule', body)

    def testListRules(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'search_field': 'rule_name',
            'search_value': '',
        }
        
        
        scriptRule = ScriptRule(a)
        r = scriptRule.listRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptRule', 'listRules', body)

    def testDescriptRule(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        scriptRule = ScriptRule(a)
        r = scriptRule.descriptRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptRule', 'descriptRule', body)

    def testGetScriptRuleResultDetail(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        scriptRule = ScriptRule(a)
        r = scriptRule.getScriptRuleResultDetail(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptRule', 'getScriptRuleResultDetail', body)

    def testListRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        scriptRule = ScriptRule(a)
        r = scriptRule.listRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptRule', 'listRuleStatus', body)

    def testStartRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'uuids': [],
        }
        
        
        scriptRule = ScriptRule(a)
        r = scriptRule.startRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptRule', 'startRule', body)

    def testStopRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'uuids': [],
        }
        
        
        scriptRule = ScriptRule(a)
        r = scriptRule.stopRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptRule', 'stopRule', body)


if __name__ == '__main__':
    unittest.main()
