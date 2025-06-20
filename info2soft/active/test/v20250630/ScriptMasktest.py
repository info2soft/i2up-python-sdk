
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import ScriptMask
from info2soft.active.v20250630.ScriptMask import ScriptMask
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


class ScriptMaskTestCase(unittest.TestCase):
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

    def testCreateScript(self):
        a = Auth(username, pwd)
        body = {
            'script_name': '',
            'config': {
            'desc': '',
            'script': '',},
            'script_type': 1,
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.createScript(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'createScript', body)

    def testModifyScript(self):
        a = Auth(username, pwd)
        body = {
            'script_name': '',
            'config': {
            'desc': '',
            'script': '',},
            'script_type': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        scriptMask = ScriptMask(a)
        r = scriptMask.modifyScript(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'modifyScript', body)

    def testDeleteScript(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.deleteScript(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'deleteScript', body)

    def testListScript(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'like_args': [{
            'mask_node_name': '',
            'rule_name': '',
            'search_script_name': '',},],
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.listScript(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'listScript', body)

    def testDownloadScript(self):
        a = Auth(username, pwd)
        body = {
            'version_id': '',
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.downloadScript(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'downloadScript', body)

    def testDescriptScript(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        id = 123456
        scriptMask = ScriptMask(a)
        r = scriptMask.descriptScript(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'descriptScript', body)

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
            'script_type': 0,},
            'src_db_uuid': '',
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.createRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'createRule', body)

    def testModifyScriptRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'node_uuid': '',
            'config': {
            'script': [],
            'src_type': '',
            'dyn_thd': 1,
            'lderrset': 'continue',
            'script_type': 0,},
            'src_db_uuid': '',
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.modifyScriptRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'modifyScriptRule', body)

    def testDeleteRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
            'force': True,
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.deleteRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'deleteRule', body)

    def testListRules(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'search_field': 'rule_name',
            'search_value': '',
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.listRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'listRules', body)

    def testDescriptRule(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        id = 123456
        scriptMask = ScriptMask(a)
        r = scriptMask.descriptRule(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'descriptRule', body)

    def testGetScriptRuleResultDetail(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        scriptMask = ScriptMask(a)
        r = scriptMask.getScriptRuleResultDetail(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'getScriptRuleResultDetail', body)

    def testListRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.listRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'listRuleStatus', body)

    def testStartRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'uuids': [],
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.startRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'startRule', body)

    def testStopRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'uuids': [],
        }
        
        
        scriptMask = ScriptMask(a)
        r = scriptMask.stopRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ScriptMask', 'stopRule', body)


if __name__ == '__main__':
    unittest.main()
