
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.resource.v20230227.Cluster import Cluster
# from info2soft.resource.v20200722.Cluster import Cluster
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
pwd = 'Info1234'


class ClusterTestCase(unittest.TestCase):

    def testAuthCls(self):
        a = Auth(username, pwd)
        body = {
            'cls_is_local': 1,
            'os_pwd': 'info2soft_125',
            'os_user': 'i2test2018.com/administrator',
            'config_addr': '192.168.87.14',
            'config_port': 26821,
            'node_type': 3,
        }
        
        cluster = Cluster(a)
        r = cluster.authCls(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'authCls', body)

    def testVerifyClsNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': 'BD7D3EF7-2F75-E2BB-A2CB-CFE936CF1F6C',
            'cls_name': 'cluster-2018',
            'cls_node_name': 'cluster-node1',
            'node_type': 1,
        }
        
        cluster = Cluster(a)
        r = cluster.verifyClsNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'verifyClsNode', body)

    def testClsNodeInfo(self):
        a = Auth(username, pwd)
        body = {
            'cls_ip': '',
        }
        
        cluster = Cluster(a)
        r = cluster.clsNodeInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'clsNodeInfo', body)

    def testCreateCls(self):
        a = Auth(username, pwd)
        body = {
            'cls': {
            'comment': '',
            'cls_disk': [
            'E:/',],
            'config_port': '26821',
            'cls_node': 'GAUSS集群为带key值的数组；其余类型集群为节点uuid数组(["BD7D3EF7-2F75-E2BB-A2CB-CFE936CF1F6C"])',
            'node_type': 1,
            'cls_is_local': 1,
            'os_user': 'i2test2018.com/administrator',
            'config_addr': '192.168.74.25',
            'node_name': 'cls',
            'other_params': {
            'ora_home': '',
            'grid_home': '',
            'user': '',},
            'maintenance': 0,},
        }
        
        cluster = Cluster(a)
        r = cluster.createCls(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'createCls', body)

    def testDescribeCls(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cluster = Cluster(a)
        r = cluster.describeCls(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'describeCls', body)

    def testModifyCls(self):
        a = Auth(username, pwd)
        body = {
            'cls': {
            'comment': '',
            'cls_disk': [
            'E:/',],
            'config_port': '26821',
            'cls_node': [
            'BD7D3EF7-2F75-E2BB-A2CB-CFE936CF1F6C',],
            'node_type': 1,
            'cls_is_local': 1,
            'os_user': 'i2test2018.com/administrator',
            'config_addr': '192.168.74.25',
            'node_name': 'cls',
            'random_str': '11111111-1111-1111-1111-111111111111',
            'maintenance': 0,
            'other_params': {
            'ora_home': '',
            'grid_home': '',
            'user': '',},},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cluster = Cluster(a)
        r = cluster.modifyCls(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'modifyCls', body)

    def testListCls(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'search_value': '',
            'search_field': '',
            'page': 1,
            'where_args[node_type]': 1,
        }
        
        cluster = Cluster(a)
        r = cluster.listCls(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listCls', body)

    def testClsDetail(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'detail',
            'node_uuid': '11111111-1111-1111-1111-111111111111',
        }
        
        cluster = Cluster(a)
        r = cluster.clsDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'clsDetail', body)

    def testListClsStatus(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        cluster = Cluster(a)
        r = cluster.listClsStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listClsStatus', body)

    def testDeleteCls(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force': 1,
        }
        
        cluster = Cluster(a)
        r = cluster.deleteCls(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'deleteCls', body)

    def testListRacStatus(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
            'force_refresh': 1,
        }
        
        cluster = Cluster(a)
        r = cluster.listRacStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listRacStatus', body)

    def testSwitchMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'switch': 0,
        }
        
        cluster = Cluster(a)
        r = cluster.switchMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'switchMaintenance', body)

    def testGetGaussInfo(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '',
            'user': '',
            'config_port': '',
        }
        
        cluster = Cluster(a)
        r = cluster.getGaussInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'getGaussInfo', body)


if __name__ == '__main__':
    unittest.main()
