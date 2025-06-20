
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import ActiveNodeClusterV3
from info2soft.resource.v20250630.ActiveNodeClusterV3 import ActiveNodeClusterV3
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


class ActiveNodeClusterV3TestCase(unittest.TestCase):
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

    def testListActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'limit': '',
            'page': '',
            'filter_by_biz_grp': '',
        }
        
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.listActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'listActiveNodeCluster', body)

    def testCreateActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': '',
            'node_uuids': [],
            'maintenance': 1,
            'comment': '',
            'biz_grp_list': [],
        }
        
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.createActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'createActiveNodeCluster', body)

    def testGetActiveNodeClusterInfo(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.getActiveNodeClusterInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'getActiveNodeClusterInfo', body)

    def testModifyActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': '',
            'node_uuids': [],
            'maintenance': 1,
            'comment': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.modifyActiveNodeCluster(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'modifyActiveNodeCluster', body)

    def testDeleteActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 1,
        }
        
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.deleteActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'deleteActiveNodeCluster', body)

    def testListClusterActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'order_by': '',
            'page': 1,
            'limit': 10,
            'search_value': '',
            'cluster_uuid': '',
        }
        
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.listClusterActiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'listClusterActiveNode', body)

    def testAddNodeActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuid': '',
            'node_uuids': [],
        }
        
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.addNodeActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'addNodeActiveNodeCluster', body)

    def testRemoveNodeActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuid': '',
            'node_uuids': [],
        }
        
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.removeNodeActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'removeNodeActiveNodeCluster', body)

    def testListActiveNodeClusterStatus(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuids': 'ac9FBFAC-cC64-ecA0-C6FF-D4EC6eBdc6dB',
        }
        
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.listActiveNodeClusterStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'listActiveNodeClusterStatus', body)

    def testSwitchAdtiveNodeClusterMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': 0,
            'uuid': 'bBae9dCA-f6cc-BA66-bF59-8DFc395eD094',
        }
        
        
        activeNodeClusterV3 = ActiveNodeClusterV3(a)
        r = activeNodeClusterV3.switchAdtiveNodeClusterMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeClusterV3', 'switchAdtiveNodeClusterMaintenance', body)


if __name__ == '__main__':
    unittest.main()
