
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import First
from info2soft.replica.v20240819.First import First
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


class FirstTestCase(unittest.TestCase):

    def testCreateFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 0,
            'vp_uuid': '',
            'auto': 0,
            'vm_list': [{
            'new_vm_name': '',
            'vm_ref': '',
            'cpu': 1,
            'ver_sig': '',
            'core_per_sock': 1,
            'mem_mb': 1024,
            'scripts': '',
            'bk_uuid': '',
            'bk_path': '',
            'time': '',
            'original_rule_uuid': '',
            'scripts_type': 0,
            'os_type': 1,
            'wk_uuid': '',
            'src_uuid': '',
            'data_ip_uuid': '',
            'bk_type': 0,
            'bucket_': '',
            'sto_uuid': '',
            'bucket_path': '',
            'disk_list': [{
            'datastore': '',
            'new_ds': '',
            'is_ignored': 1,
            'size': '',
            'boot_index': 1,
            'disk_dir': '',
            'disk_name': '',
            'id': '',},],
            'networks': [{
            'source_network_name': '',
            'source_network_id': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'ip_address': '',
            'subnet_name': '',
            'auto_ip': True,
            'ip': '',
            'security_group_name': '',
            'gateway': '',
            'is_defroute': False,},],
            'new_flavor_id': '',
            'vm_name': '',
            'new_vm_hostname': '',},],
            'quick_back': 1,
            'backup_type': 'i',
            'lan_free': 23,
            'del_bkup_data': 0,
            'automate': 0,
            'auto_shutdown': 1,
            'bkup_policy': 1,
            'bkup_schedule': {
            'sched_time_start': '0',
            'limit': 0,
            'sched_day': 6,
            'sched_every': 0,
            'sched_time': [],
            'sched_gap_min': 0,},
            'new_network_id': '',
            'new_network_name': '',
            'datastore': '',
            'hostname': '',
            'datacenter': '',
            'create_vm_type': 1,
        }
        
        
        first = First(a)
        r = first.createFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'First', 'createFirstReplica', body)

    def testListFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        
        first = First(a)
        r = first.listFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'First', 'listFirstReplica', body)

    def testDescribeFirstReplica(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        first = First(a)
        r = first.describeFirstReplica(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'First', 'describeFirstReplica', body)

    def testModifyFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 0,
            'vp_uuid': '',
            'auto': 0,
            'vm_list': [{
            'new_vm_name': '',
            'vm_ref': '',
            'cpu': 1,
            'ver_sig': '',
            'core_per_sock': 1,
            'mem_mb': 1024,
            'scripts': '',
            'bk_uuid': '',
            'bk_path': '',
            'time': '',
            'original_rule_uuid': '',
            'scripts_type': 0,
            'os_type': 1,
            'wk_uuid': '',
            'src_uuid': '',
            'data_ip_uuid': '',
            'bk_type': 0,
            'bucket_': '',
            'sto_uuid': '',
            'bucket_path': '',
            'disk_list': [{
            'datastore': '',
            'new_ds': '',
            'is_ignored': 1,
            'size': '',
            'boot_index': 1,
            'disk_dir': '',
            'disk_name': '',
            'id': '',},],
            'networks': [{
            'source_network_name': '',
            'source_network_id': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'ip_address': '',
            'subnet_name': '',
            'auto_ip': True,
            'ip': '',
            'security_group_name': '',
            'gateway': '',
            'is_defroute': False,},],
            'new_flavor_id': '',
            'vm_name': '',},],
            'quick_back': 1,
            'backup_type': 'i',
            'lan_free': 23,
            'del_bkup_data': 0,
            'automate': 0,
            'auto_shutdown': 1,
            'bkup_policy': 1,
            'bkup_schedule': {
            'sched_time_start': '0',
            'limit': 0,
            'sched_day': 6,
            'sched_every': 0,
            'sched_time': [],
            'sched_gap_min': 0,},
            'new_network_id': '',
            'new_network_name': '',
            'datastore': '',
            'hostname': '',
            'datacenter': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        first = First(a)
        r = first.modifyFirstReplica(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'First', 'modifyFirstReplica', body)

    def testListFirstReplicaStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': 1,
            'force_refresh': 1,
        }
        
        
        first = First(a)
        r = first.listFirstReplicaStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'First', 'listFirstReplicaStatus', body)

    def testStartVmFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
        }
        
        
        first = First(a)
        r = first.startVmFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'First', 'startVmFirstReplica', body)

    def testStopVmFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
        }
        
        
        first = First(a)
        r = first.stopVmFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'First', 'stopVmFirstReplica', body)

    def testDeleteFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': '',
            'group_uuids': '',
            'delete_tgtvm': 1,
        }
        
        
        first = First(a)
        r = first.deleteFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'First', 'deleteFirstReplica', body)


if __name__ == '__main__':
    unittest.main()
