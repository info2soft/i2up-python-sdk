
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Dashboard
from info2soft.dashboard.v20250630.Dashboard import Dashboard
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
    3
if is_py3:
    import io
    import urllib

    StringIO = io.StringIO
    urlopen = urllib.request.urlopen

username = 'admin'
pwd = 'Info@123'


class DashboardTestCase(unittest.TestCase):
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

    def testResourceView(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        dashboard = Dashboard(a)
        r = dashboard.resourceView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dashboard', 'resourceView', body)

    def testListBackupCenter(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        dashboard = Dashboard(a)
        r = dashboard.listBackupCenter(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dashboard', 'listBackupCenter', body)

    def testGetBackupCenterInfo(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }
        
        
        dashboard = Dashboard(a)
        r = dashboard.getBackupCenterInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dashboard', 'getBackupCenterInfo', body)

    def testListHosts(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        dashboard = Dashboard(a)
        r = dashboard.listHosts(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dashboard', 'listHosts', body)

    def testResourceProtectionCoverage(self):
        a = Auth(username, pwd)
        body = {
            'level_a': 1,
            'level_b': 1,
            'level_c': 1,
            'vp_uuid': '',
        }
        
        
        dashboard = Dashboard(a)
        r = dashboard.resourceProtectionCoverage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dashboard', 'resourceProtectionCoverage', body)

    def testTaskView(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        dashboard = Dashboard(a)
        r = dashboard.taskView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dashboard', 'taskView', body)

    def testRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'type': 0,
            'page': 1,
        }
        
        
        dashboard = Dashboard(a)
        r = dashboard.repBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dashboard', 'repBackup', body)

    def testHa(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        dashboard = Dashboard(a)
        r = dashboard.ha(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dashboard', 'ha', body)

    def testNode(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
            'type': 1,
        }
        
        
        dashboard = Dashboard(a)
        r = dashboard.node(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dashboard', 'node', body)


if __name__ == '__main__':
    unittest.main()
