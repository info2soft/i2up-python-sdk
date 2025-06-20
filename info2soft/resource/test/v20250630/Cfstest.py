
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Cfs
from info2soft.resource.v20250630.Cfs import Cfs
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


class CfsTestCase(unittest.TestCase):
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

    def testCreateCfs(self):
        a = Auth(username, pwd)
        body = {
            'cfs_name': '',
            'ip': '',
            'port': 1,
            'user': '',
            'pwd': '',
            'biz_grp_list': [],
            'maintenance': 1,
            'db_name': '',
        }
        
        
        cfs = Cfs(a)
        r = cfs.createCfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cfs', 'createCfs', body)

    def testModifyCfs(self):
        a = Auth(username, pwd)
        body = {
            'cfs_name': '',
            'ip': '',
            'port': 1,
            'user': '',
            'pwd': '',
            'biz_grp_list': [],
            'random_str': '',
            'maintenance': 1,
            'db_name': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cfs = Cfs(a)
        r = cfs.modifyCfs(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cfs', 'modifyCfs', body)

    def testDescribeCfs(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cfs = Cfs(a)
        r = cfs.describeCfs(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cfs', 'describeCfs', body)

    def testListCfs(self):
        a = Auth(username, pwd)
        body = {
            'limit': 15,
            'page': 1,
        }
        
        
        cfs = Cfs(a)
        r = cfs.listCfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cfs', 'listCfs', body)

    def testDeleteCfs(self):
        a = Auth(username, pwd)
        body = {
            'cfs_uuids': [],
            'force': 1,
        }
        
        
        cfs = Cfs(a)
        r = cfs.deleteCfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cfs', 'deleteCfs', body)

    def testListCfsStatus(self):
        a = Auth(username, pwd)
        body = {
            'cfs_uuids': [],
            'force_refresh': 1,
        }
        
        
        cfs = Cfs(a)
        r = cfs.listCfsStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cfs', 'listCfsStatus', body)

    def testMaintainCfs(self):
        a = Auth(username, pwd)
        body = {
            'cfs_uuids': [],
            'operate': '',
            'switch': 1,
        }
        
        
        cfs = Cfs(a)
        r = cfs.maintainCfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cfs', 'maintainCfs', body)

    def testTestConnect(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
            'port': 1,
            'user': '',
            'pwd': '',
            'db_name': '',
            'cfs_uuid': '',
        }
        
        
        cfs = Cfs(a)
        r = cfs.testConnect(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cfs', 'testConnect', body)

    def testListCfsZoneFs(self):
        a = Auth(username, pwd)
        body = {
            'cfs_uuid': '',
        }
        
        
        cfs = Cfs(a)
        r = cfs.listCfsZoneFs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cfs', 'listCfsZoneFs', body)


if __name__ == '__main__':
    unittest.main()
