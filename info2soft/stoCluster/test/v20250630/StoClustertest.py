
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import StoCluster
from info2soft.stoCluster.v20250630.StoCluster import StoCluster
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


class StoClusterTestCase(unittest.TestCase):
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

    def testCreateDedupeStorageCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': '',
            'type': 1,
            'data_warn': 1,
            'data_full': 1,
            'data_port': 1,
            'node_list': [{
            'node_name': '',
            'node_uuid': '',
            'dir': '',
            'addr': '',},],
        }
        
        
        stoCluster = StoCluster(a)
        r = stoCluster.createDedupeStorageCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoCluster', 'createDedupeStorageCluster', body)

    def testModifyDedupeStorageCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': '',
            'type': 1,
            'data_warn': 1,
            'data_full': 1,
            'data_port': 1,
            'node_list': [{
            'node_name': '',
            'node_uuid': '',
            'dir': '',
            'addr': '',},],
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        stoCluster = StoCluster(a)
        r = stoCluster.modifyDedupeStorageCluster(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoCluster', 'modifyDedupeStorageCluster', body)

    def testDescribeDedupeStorageCluster(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        stoCluster = StoCluster(a)
        r = stoCluster.describeDedupeStorageCluster(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoCluster', 'describeDedupeStorageCluster', body)

    def testListDedupeStorageCluster(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        
        stoCluster = StoCluster(a)
        r = stoCluster.listDedupeStorageCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoCluster', 'listDedupeStorageCluster', body)

    def testDeleteDedupeStorageCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuids': [],
            'force': '',
        }
        
        
        stoCluster = StoCluster(a)
        r = stoCluster.deleteDedupeStorageCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoCluster', 'deleteDedupeStorageCluster', body)

    def testListDedupeStorageClusterStatus(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuids': [],
            'force_refresh': 1,
        }
        
        
        stoCluster = StoCluster(a)
        r = stoCluster.listDedupeStorageClusterStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoCluster', 'listDedupeStorageClusterStatus', body)


if __name__ == '__main__':
    unittest.main()
