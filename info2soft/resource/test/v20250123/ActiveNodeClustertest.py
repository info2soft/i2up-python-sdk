
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import ActiveNodeCluster
from info2soft.resource.v20250123.ActiveNodeCluster import ActiveNodeCluster
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


class ActiveNodeClusterTestCase(unittest.TestCase):

    def testListActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'limit': '',
            'page': '',
            'filter_by_biz_grp': '',
        }
        
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.listActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'listActiveNodeCluster', body)

    def testCreateActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': '',
            'node_uuids': [],
            'maintenance': 1,
            'comment': '',
            'biz_grp_list': [],
        }
        
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.createActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'createActiveNodeCluster', body)

    def testGetActiveNodeClusterInfo(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.getActiveNodeClusterInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'getActiveNodeClusterInfo', body)

    def testModifyActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': '',
            'node_uuids': [],
            'maintenance': 1,
            'comment': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.modifyActiveNodeCluster(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'modifyActiveNodeCluster', body)

    def testDeleteActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 1,
        }
        
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.deleteActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'deleteActiveNodeCluster', body)

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
        
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.listClusterActiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'listClusterActiveNode', body)

    def testAddNodeActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuid': '',
            'node_uuids': [],
        }
        
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.addNodeActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'addNodeActiveNodeCluster', body)

    def testRemoveNodeActiveNodeCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuid': '',
            'node_uuids': [],
        }
        
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.removeNodeActiveNodeCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'removeNodeActiveNodeCluster', body)

    def testListActiveNodeClusterStatus(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuids': '6c9F7985-9CeE-0e8c-38C5-cbcf01AFBD9B',
        }
        
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.listActiveNodeClusterStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'listActiveNodeClusterStatus', body)

    def testSwitchAdtiveNodeClusterMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': 0,
            'uuid': 'bBae9dCA-f6cc-BA66-bF59-8DFc395eD094',
        }
        
        
        activeNodeCluster = ActiveNodeCluster(a)
        r = activeNodeCluster.switchAdtiveNodeClusterMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveNodeCluster', 'switchAdtiveNodeClusterMaintenance', body)


if __name__ == '__main__':
    unittest.main()
