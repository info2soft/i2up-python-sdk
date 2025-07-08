
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Cluster
from info2soft.ha.v20250630.Cluster import Cluster
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


class ClusterTestCase(unittest.TestCase):
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

    def testCreateHaCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': 'cluster',
            'center_vir_ip': '2.2.2.1',
            'node_list': [{
            'node_uuid': 'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'node_ip': '2.2.2.1',
            'label_list': [
            'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',],
            'ha_conf': {
            'ha_vir_ip_adapter': 'eth0',
            'ha_heartbeat_adapter': 'eth0',
            'ha_heartbeat_ip': '2.2.21',
            'ha_heartbeat_netif': '{DEFF6069-58A0-4723-BD1E-E63CF9E5499D}',},
            'total_service_limit': '1',
            'total_monitor_limit': '10',
            'center_vir_ip_adapter': 'eth0',},],
            'cluster_uuid': 'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'center_vir_mask': '255.255.255.0',
        }
        
        
        cluster = Cluster(a)
        r = cluster.createHaCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'createHaCluster', body)

    def testModifyHaCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': 'cluster',
            'center_vir_ip': '2.2.2.1',
            'node_list': [{
            'node_uuid': 'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'node_ip': '2.2.2.1',
            'label_list': [
            'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',],
            'ha_conf': {
            'ha_vir_ip_adapter': 'eth0',
            'ha_heartbeat_adapter': 'eth0',
            'ha_heartbeat_ip': '2.2.21',},
            'total_service_limit': '1',
            'total_monitor_limit': '10',
            'center_vir_ip_adapter': 'eth0',},],
            'cluster_uuid': 'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'random_str': 'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cluster = Cluster(a)
        r = cluster.modifyHaCluster(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'modifyHaCluster', body)

    def testDeleteHaClusterHost(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuid': '',
            'node_uuid': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.deleteHaClusterHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'deleteHaClusterHost', body)

    def testDeleteHaCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuids': [],
            'force': 1,
        }
        
        
        cluster = Cluster(a)
        r = cluster.deleteHaCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'deleteHaCluster', body)

    def testListHaCluster(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }
        
        
        cluster = Cluster(a)
        r = cluster.listHaCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listHaCluster', body)

    def testRegisterHaCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': 'cluster',
            'center_vir_ip': '2.2.2.1',
            'node_list': [{
            'node_uuid': 'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'node_ip': '2.2.2.1',
            'label_list': [
            'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',],
            'ha_conf': {
            'ha_vir_ip_adapter': 'eth0',
            'ha_heartbeat_adapter': 'eth0',
            'ha_heartbeat_ip': '2.2.21',},
            'total_service_limit': '1',
            'total_monitor_limit': '10',
            'center_vir_ip_adapter': 'eth0',},],
            'node_uuid': 'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'cluster_uuid': 'AEC19FB5-8DC6-27E7-7E6A-7A60ADFA7187',
            'center_vir_mask': '255.255.255.0',
        }
        
        
        cluster = Cluster(a)
        r = cluster.registerHaCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'registerHaCluster', body)

    def testStartHaCluster(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'cluster_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        
        cluster = Cluster(a)
        r = cluster.startHaCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'startHaCluster', body)

    def testStopHaCluster(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'cluster_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        
        cluster = Cluster(a)
        r = cluster.stopHaCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'stopHaCluster', body)

    def testDescribeHaCluster(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cluster = Cluster(a)
        r = cluster.describeHaCluster(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'describeHaCluster', body)

    def testCheckDupName(self):
        a = Auth(username, pwd)
        body = {
            'cluster_name': 'A',
            'cluster_uuid': '7432C18E-4FF6-D06B-8081-ACA41F673ADD',
        }
        
        
        cluster = Cluster(a)
        r = cluster.checkDupName(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'checkDupName', body)

    def testListHaClusterIpDuplicate(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuid': '',
            'center_vir_ip': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.listHaClusterIpDuplicate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listHaClusterIpDuplicate', body)

    def testListHaClusterID(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        cluster = Cluster(a)
        r = cluster.listHaClusterID(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listHaClusterID', body)

    def testListHaClusterMonitor(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuid': '',
            'label_uuids': [],
        }
        
        
        cluster = Cluster(a)
        r = cluster.listHaClusterMonitor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listHaClusterMonitor', body)

    def testListHaClusterStatus(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuids': [],
        }
        
        
        cluster = Cluster(a)
        r = cluster.listHaClusterStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listHaClusterStatus', body)


if __name__ == '__main__':
    unittest.main()
