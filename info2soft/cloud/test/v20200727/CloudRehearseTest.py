
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import CloudRehearse
# from info2soft.cloud.v20200722.CloudRehearse import CloudRehearse
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
    
                
class CloudRehearseTestCase(unittest.TestCase):

    def testDescribeEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup_uuid': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.describeEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'describeEcs', body)

    def testListHost(self):
        a = Auth(username, pwd)
        body = {
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listHost', body)

    def testListEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'page': 1,
            'limit': 1,
            'group_uuid': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listEcs', body)

    def testListRecoveryPoint(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup_uuid': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listRecoveryPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listRecoveryPoint', body)

    def testListAvailabilityZone(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listAvailabilityZone(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listAvailabilityZone', body)

    def testListFlavor(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listFlavor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listFlavor', body)

    def testListVpc(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listVpc(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listVpc', body)

    def testListSubnet(self):
        a = Auth(username, pwd)
        body = {
            'vpc_id': '356c3295-afd0-4a09-8e6f-03620ef70854',
            'cloud_uuid': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listSubnet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listSubnet', body)

    def testListSecureGroup(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'ecs_id': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listSecureGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listSecureGroup', body)

    def testCreateRehearse(self):
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
            'disabled': 'false',
            'is_public': 1,},
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
            'egress ': 'ICMP',},],
            'network_switch': 1,
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.createRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'createRehearse', body)

    def testCreateBatchRehearse(self):
        a = Auth(username, pwd)
        body = {
            'rehearse_list': [{
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
            'disabled': 'false',
            'is_public': 1,},
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
            'egress ': 'ICMP',},],
            'network_switch': 1,},],
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.createBatchRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'createBatchRehearse', body)

    def testListRehearse(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listRehearse', body)

    def testListRehearseStatus(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [
            'f1312ce5-7cb0-4e0c-a687-4ba4e5475e4c',],
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listRehearseStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listRehearseStatus', body)

    def testListVncConsole(self):
        a = Auth(username, pwd)
        body = {
            'job_id': '',
            'ecs_id': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listVncConsole(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listVncConsole', body)

    def testEvacuateRehearse(self):
        a = Auth(username, pwd)
        body = {
            'job_id': '',
            'is_group': 1,
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.evacuateRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'evacuateRehearse', body)

    def testEvacuateBatchRehearse(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
            'is_group': 1,
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.evacuateBatchRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'evacuateBatchRehearse', body)

    def testListRehearseDetail(self):
        a = Auth(username, pwd)
        body = {
            'job_id': '',
            'type': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listRehearseDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listRehearseDetail', body)

    def testDescribeRehearse(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.describeRehearse(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'describeRehearse', body)

    def testDeleteRehearse(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.deleteRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'deleteRehearse', body)

    def testListEvacuatedRehearse(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listEvacuatedRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listEvacuatedRehearse', body)

    def testListNpsvrRehearseStatus(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listNpsvrRehearseStatus(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listNpsvrRehearseStatus', body)

    def testListNpsvrRehearseProgress(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listNpsvrRehearseProgress(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listNpsvrRehearseProgress', body)

    def testListNetwork(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '8E6FB8D2-F830-D67B-DA35-8E16F175053B',
            'network_conf': [{
            'vpc': {
            'id': '356c3295-afd0-4a09-8e6f-03620ef70854',
            'name': 'vpc-49a5,192.168.0.0/16',},
            'subnet': {
            'id': '3509d824-1a5b-41e5-9570-4cf51440078f',
            'name': 'subnet-1df4,192.168.64.0/24',},},],
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listNetwork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listNetwork', body)

    def testCreateNetwork(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.createNetwork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'createNetwork', body)

    def testListSubnetUsedIp(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'subnet_id': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listSubnetUsedIp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listSubnetUsedIp', body)

    def testCreateGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'group_config': [],
            'rehearse_name': '',
            'cloud_uuid': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.createGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'createGroup', body)

    def testListGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listGroup', body)

    def testDescribeGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.describeGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'describeGroup', body)

    def testDeleteGroup(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.deleteGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'deleteGroup', body)

    def testCreateEvacuateGroup(self):
        a = Auth(username, pwd)
        body = {
            'job_id': '',
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.createEvacuateGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'createEvacuateGroup', body)

    def testListGroupStatus(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listGroupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listGroupStatus', body)

    def testListEvacuatedGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listEvacuatedGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listEvacuatedGroup', body)

    def testListBatchRehearse(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
        }
        
        cloudRehearse = CloudRehearse(a)
        r = cloudRehearse.listBatchRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudRehearse', 'listBatchRehearse', body)


if __name__ == '__main__':
    unittest.main()
