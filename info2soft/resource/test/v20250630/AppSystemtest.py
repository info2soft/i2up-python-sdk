
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import AppSystem
from info2soft.resource.v20250630.AppSystem import AppSystem
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


class AppSystemTestCase(unittest.TestCase):
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

    def testSecDirList(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.secDirList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'secDirList', body)

    def testCreateSecDir(self):
        a = Auth(username, pwd)
        body = {
            'dir_name': '',
            'pid': 1,
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.createSecDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createSecDir', body)

    def testModifySecDir(self):
        a = Auth(username, pwd)
        body = {
            'dir_name': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appSystem = AppSystem(a)
        r = appSystem.modifySecDir(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifySecDir', body)

    def testDeleteSecDir(self):
        a = Auth(username, pwd)
        body = {
            'dir_uuids': [],
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.deleteSecDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteSecDir', body)

    def testAppSystemList(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'limit': 1,
            'page': 1,
            'search_field': '',
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.appSystemList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'appSystemList', body)

    def testAppSystemMembersList(self):
        a = Auth(username, pwd)
        body = {
            'rule_type': 1,
            'name': '',
            'os_type': 1,
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.appSystemMembersList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'appSystemMembersList', body)

    def testDescribeAppSystem(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appSystem = AppSystem(a)
        r = appSystem.describeAppSystem(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeAppSystem', body)

    def testCreateAppSystem(self):
        a = Auth(username, pwd)
        body = {
            'dir_uuid': '73412DAD-A7A6-4605-A9FF-081495C8800B',
            'sys_name': '应用系统name',
            'level_cfg': [{
            'day': [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',],
            'periods': [{
            'level': 0,
            'start_time': '10:10',
            'end_time': '12:20',},],},],
            'node_uuids': [
            'EA52A961-9883-66FE-188B-D7266AD9594B',
            '09EEA553-C3B8-0D7A-4797-F7A7E2D4FAE1',],
            'vm_uuids': [],
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.createAppSystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createAppSystem', body)

    def testModifyAppSystem(self):
        a = Auth(username, pwd)
        body = {
            'dir_uuid': '',
            'sys_name': '',
            'level_cfg': [{
            'day': [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',],
            'periods': [{
            'level': 1,
            'start_time': '10:10',
            'end_time': '12:20',},],},],
            'random_str': '',
            'node_uuids': [
            'EF4825D6-7FB3-7961-6271-5E5B2603414D',],
            'vm_uuids': [
            'EF4825D6-7FB3-7961-6271-5E5B2603414D',],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appSystem = AppSystem(a)
        r = appSystem.modifyAppSystem(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifyAppSystem', body)

    def testDeleteAppSystem(self):
        a = Auth(username, pwd)
        body = {
            'sys_uuids': [],
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.deleteAppSystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteAppSystem', body)

    def testGetVmList(self):
        a = Auth(username, pwd)
        body = {
            'search_field': 'vm_name',
            'search_value': 'vm_name',
            'where_args': {
            'vp_uuid': '',},
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.getVmList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'getVmList', body)

    def testGetMembersList(self):
        a = Auth(username, pwd)
        body = {
            'sys_uuid': '',
            'page': 1,
            'limit': 1,
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.getMembersList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'getMembersList', body)

    def testAutoRegisterNode(self):
        a = Auth(username, pwd)
        body = {
            'node_name': '',
            'os_type': 1,
            'os_user': '',
            'os_pwd': '',
            'cc_ip': '',
            'config_addr': '',
            'root': '',
            'disk_limit': 1,
            'mem_limit': 1,
            'disk_free_space_limit': 1,
            'uuid': '',
            'vm_uuid': '',
            'config_port': 1,
            'vp_uuid': '',
            'cache_path': '',
            'log_path': '',
        }
        
        
        appSystem = AppSystem(a)
        r = appSystem.autoRegisterNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'autoRegisterNode', body)


if __name__ == '__main__':
    unittest.main()
