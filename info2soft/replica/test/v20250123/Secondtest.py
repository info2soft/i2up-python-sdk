
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Second
from info2soft.replica.v20250123.Second import Second
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


class SecondTestCase(unittest.TestCase):

    def testCreateSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'fsp_type': 22,
            'wk_uuid': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            'timeout': 0,
            'wk_path': [],
            'bk_path': [],
            'resource_settings': {
            'tgt_uuid': '',
            'new_dc': '',
            'new_host': '',
            'new_ds': '',
            'new_dc_mor': '',
            'vm_list': [{
            'disk_list': [{
            'boot_index': '',
            'file_name': '',
            'new_ds': '',
            'size': '',
            'is_ignored': '',
            'disk_name': '',
            'disk_path': '',
            'id': '',
            'disk_provision_type': 1,},],
            'vm_name': '',
            'new_vm_name': '',
            'custom_config': 1,
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'dynamic_mem': '0',
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'auto_ip': False,
            'ip': '',
            'security_group_name': '',
            'gateway': '',
            'is_defroute': False,},],
            'new_vm_hostname': '',},],
            'create_vm_type': 1,},
            'fsp_name': '',
            'bk_data_type': 21,
            'wk_data_type': 0,
            'auto_register': 0,
            'node_name': '',
            'node_lic_list': [],},
        }
        
        
        second = Second(a)
        r = second.createSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'createSecondReplica', body)

    def testListSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        
        second = Second(a)
        r = second.listSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'listSecondReplica', body)

    def testDescribeSecondReplica(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        second = Second(a)
        r = second.describeSecondReplica(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'describeSecondReplica', body)

    def testModifySecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'fsp_type': 22,
            'wk_uuid': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            'timeout': 0,
            'wk_path': [],
            'bk_path': [],
            'resource_settings': {
            'tgt_uuid': '',
            'new_dc': '',
            'new_host': '',
            'new_ds': '',
            'new_dc_mor': '',
            'vm_list': [{
            'disk_list': [{
            'boot_index': '',
            'file_name': '',
            'new_ds': '',
            'size': '',
            'is_ignored': '',
            'disk_name': '',
            'disk_path': '',
            'id': '',
            'disk_provision_type': 1,},],
            'vm_name': '',
            'new_vm_name': '',
            'custom_config': 1,
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'dynamic_mem': '0',
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'auto_ip': False,
            'ip': '',
            'security_group_name': '',
            'gateway': '',
            'is_defroute': False,},],},],},
            'fsp_name': '',
            'bk_data_type': 21,
            'wk_data_type': 0,
            'auto_register': 0,
            'node_name': '',
            'node_lic_list': [],},
        }
        
        
        second = Second(a)
        r = second.modifySecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'modifySecondReplica', body)

    def testStartSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'fsp_uuids': [],
        }
        
        
        second = Second(a)
        r = second.startSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'startSecondReplica', body)

    def testStopSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'fsp_uuids': [],
        }
        
        
        second = Second(a)
        r = second.stopSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'stopSecondReplica', body)

    def testStartVmSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'fsp_uuids': [],
        }
        
        
        second = Second(a)
        r = second.startVmSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'startVmSecondReplica', body)

    def testStopVmSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'fsp_uuids': [],
        }
        
        
        second = Second(a)
        r = second.stopVmSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'stopVmSecondReplica', body)

    def testDeleteSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'del_policy': 1,
            'force': 1,
        }
        
        
        second = Second(a)
        r = second.deleteSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'deleteSecondReplica', body)

    def testListSecondReplicaStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'force_refresh': 1,
        }
        
        
        second = Second(a)
        r = second.listSecondReplicaStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Second', 'listSecondReplicaStatus', body)


if __name__ == '__main__':
    unittest.main()
