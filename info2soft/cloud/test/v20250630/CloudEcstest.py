
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import CloudEcs
from info2soft.cloud.v20250630.CloudEcs import CloudEcs
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


class CloudEcsTestCase(unittest.TestCase):
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

    def testCreateEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'ecs_name': '',
            'flavorid': '',
            'volume_sys_id': '',
            'server_zone': '',
            'volume_data_ids': [],
            'wk_uuid': '',
            'rc_point': {
            'time': '',
            'disk_num': 1,
            'total_size': '',
            'list': [{
            'id': '',
            'size': '',
            'boot_index': 1,},],},
            'from_backup': 0,
            'bind_public_ip': 1,
            'cloud_backup_uuid': '',
            'ecs_type': 1,
            'config': {
            'vpc': {
            'id': '',
            'name': '',},
            'subnet': [{
            'id': '',
            'name': '',
            'network_id': 'b1e0f8fc-3be7-4539-b68e-ab7b7b69852c',
            'ip': '',},],
            'security_group': {
            'group_id': '',
            'group_name': '',
            'ingress': '',
            'egress': '',},
            'subnet_type': 1,
            'band_width': 1,
            'cpu': '',
            'ram': '',},
            'disk_billing_type': 1,
            'order_cycle_unit': 1,
            'order_cycle': 1,
            'bk_uuid': '',
            'priority': 1,
            'host_name': '',
            'vpc_settings': [{
            'vpc_id': '',
            'network_id': '',
            'security_group_id': '',
            'ipaddress': '',
            'port_id': '',
            'primary': False,},],
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.createEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'createEcs', body)

    def testListVncConsole(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.listVncConsole(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'listVncConsole', body)

    def testListEcsStatus(self):
        a = Auth(username, pwd)
        body = {
            'ecs_ids': [],
            'force_refresh': 1,
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.listEcsStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'listEcsStatus', body)

    def testListEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'page': 1,
            'limit': 1,
            'type': 1,
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.listEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'listEcs', body)

    def testDeleteEcs(self):
        a = Auth(username, pwd)
        body = {
            'ecs_ids': [],
            'complete_delete': 1,
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.deleteEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'deleteEcs', body)

    def testStartECS(self):
        a = Auth(username, pwd)
        body = {
            'ecs_ids': [],
            'operate': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.startECS(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'startECS', body)

    def testStopECS(self):
        a = Auth(username, pwd)
        body = {
            'ecs_ids': [],
            'operate': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.stopECS(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'stopECS', body)

    def testGetTakeoverECSInfo(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.getTakeoverECSInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'getTakeoverECSInfo', body)

    def testGetTakeoverVPCInfo(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'ecs_id': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.getTakeoverVPCInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'getTakeoverVPCInfo', body)

    def testAttachPoint(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.attachPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'attachPoint', body)

    def testBindNode(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
            'node_uuid': '',
            'operate': '',
            'node_name': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.bindNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'bindNode', body)

    def testUntieNode(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
            'node_uuid': '',
            'operate': '',
            'node_name': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.untieNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'untieNode', body)

    def testConfigRehearse(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup_uuid': '',
            'source': {
            'node_name': '8.180',
            'host_name': 'Windows Ftp Server',
            'host_ip': '192.168.8.180',
            'node_os': 'Windows Server 2012 R2 64bits',
            'vcpus': '8',
            'memory': '40957',
            'disk_num': '2',
            'disk_size': '64420392960',
            'ecs_id': '',},
            'zone': {
            'zone_name': '华北-北京一',
            'availability_zone': 'cn-east-2c',},
            'rc_point': {
            'time': '2019-08-13 17:13:28',
            'id': '7a268c3f-4d73-4e6c-b4fd-c3be235f33dd',
            'disk_num': 2,
            'total_size': '8000',
            'list': [{
            'id': '7a268c3f-4d73-4e6c-b4fd-c3be235f41dd',
            'size': '4000',
            'boot_index': 0,},],},
            'ecs_name': 'Rehearse lij-test',
            'flavor': {
            'id': 'ai1.2xlarge.4',
            'name': 'ai1.2xlarge.4',
            'vcpus': '8',
            'ram': 32768,
            'disk': '0',
            'disabled': False,
            'is_public': True,},
            'vpc': {
            'id': '356c3295-afd0-4a09-8e6f-03620ef70854',
            'name': 'vpc-49a5,192.168.0.0/16',},
            'subnet': {
            'id': '3509d824-1a5b-41e5-9570-4cf51440078f',
            'name': 'subnet-1df4,192.168.64.0/24',},
            'ip_address': '192.168.192.101',
            'security_group': [{
            'group_id': '3509d824-1a5b-41e5-9570-4cf51440078f',
            'group_name': 'i2',
            'ingress': 'ICMP,TCP/22,80,443,26821-26868,55443',
            'egress': 'ICMP',},],
            'network_switch': 1,
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.configRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'configRehearse', body)

    def testListRehearseGroup(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
            'cloud_uuid': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.listRehearseGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'listRehearseGroup', body)

    def testCreateRehearseGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'group_name': '',
            'ecs_ids': [
            '396c8bde-2d3a-4cad-87ea-8d1f81e2451c',
            'f3ca421d-9b6e-42b9-b911-36ebbeabb485',],
            'group_content': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.createRehearseGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'createRehearseGroup', body)

    def testDeleteRehearseGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuids': [
            'A14875A3-738E-3E5B-65D3-483CADE35E5D',
            'A14875A3-738E-3E5B-65D3-483CADE35E5D',],
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.deleteRehearseGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'deleteRehearseGroup', body)

    def testDescribeRehearseGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.describeRehearseGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'describeRehearseGroup', body)

    def testDescribeEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup_uuid': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.describeEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'describeEcs', body)

    def testBatchCreateEcs(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'ecs_name': '',
            'flavorid': '',
            'volume_sys_id': '',
            'server_zone': '',
            'volume_data_ids': [],
            'wk_uuid': '',
            'rc_point': {
            'time': '',
            'disk_num': 1,
            'total_size': '',
            'list': [{
            'id': '',
            'size': '',
            'boot_index': 1,},],},
            'bind_public_ip': 1,
            'cloud_backup_uuid': '',
            'config': {
            'vpc': {
            'id': '',
            'name': '',},
            'subnet': [{
            'id': '',
            'name': '',
            'network_id': 'b1e0f8fc-3be7-4539-b68e-ab7b7b69852c',
            'ip': '',},],
            'security_group': {
            'group_id': '',
            'group_name': '',
            'ingress': '',
            'egress': '',},
            'subnet_type': 1,
            'band_width': 1,
            'cpu': '',
            'ram': '',},
            'disk_billing_type': 1,
            'order_cycle_unit': 1,
            'order_cycle': 1,
            'bk_uuid': '',
            'priority': 1,
            'cloud_uuid': '',
            'host_name': '',},],
            'prefix': '',
            'ecs_type': '',
        }
        
        
        cloudEcs = CloudEcs(a)
        r = cloudEcs.batchCreateEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudEcs', 'batchCreateEcs', body)


if __name__ == '__main__':
    unittest.main()
