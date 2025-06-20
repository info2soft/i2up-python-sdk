
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import VpRecoveryRule
from info2soft.vpRecoveryRule.v20250630.VpRecoveryRule import VpRecoveryRule
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


class VpRecoveryRuleTestCase(unittest.TestCase):
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

    def testCreateVpRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'task_type': 1,
            'auto_start': 1,
            'start_time': 1,
            'priority': 1,
            'biz_grp_list': [],
            'bk_set_uuids': [],
            'vp_uuid': '',
            'new_dc': '',
            'new_dc_mor': '',
            'new_hostname': '',
            'new_resource_pool_id': '',
            'new_resource_pool_name': '',
            'location': '',
            'location_name': '',
            'new_ds': '',
            'network_id': '',
            'network_name': '',
            'vm_list': [{
            'vm_name': '',
            'vm_ref': '',
            'new_vm_name': '',
            'bk_set_uuid': '',
            'common_custom': 1,
            'disk_custom': 1,
            'disk_list': [{
            'id': '',
            'disk_path': '',
            'disk_name': '',
            'is_same': 1,
            'new_ds': '',
            'boot_index': 1,
            'disk_type': '',
            'datastore_type': '',
            'src_disk_name': '',
            'is_ignored': '',
            'disk_provision_type': 1,
            'replica_num': '',
            'cache': 1,},],
            'networks': [{
            'source_network_name': '',
            'source_network_id': '',
            'mac_address': '',
            'keep_mac': 1,
            'network_name': '',
            'network_id': '',
            'ip_address': '',
            'source_physical_interface_id': '',
            'source_physical_interface_name': '',
            'physical_interface_id': '',
            'physical_interface_name': '',
            'network_type': '',
            'vpc_id': '',},],
            'cpu': 1,
            'core_per_sock': 1,
            'mem_mb': 1,
            'dynamic_mem': 1,
            'flavor_id': '',
            'start_order': 0,
            'new_archtype': '',
            'new_machine': '',
            'new_vm_sec_grp_id': '',
            'new_vm_vpc_id': '',
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'flavor_name': '',},],
            'auto_startup': 1,
            'dest_trans_mode': 31,
            'concurrent_disk_threads': 2,
            'compress_switch': 1,
            'compress': 1,
            'band_width': '',
            'new_vp_uuid': '',
            'new_ds_path': '',
            'api_type': '',
            'is_create': 0,
            'is_start_order': 1,
            'is_fusion_storage': 1,
            'driver_injection': 1,
            'driver_injection_policy': 0,
            'parent_flavor_id': '',
            'ip_address': '',
            'target_region_id': '',
            'target_project_id': '',
            'winstack_pool_id': '',
            'winstack_host_id': '',
            'new_machine': '',
            'new_archtype': '',
            'new_host_id': '',
            'physical_interface_id': '',
            'physical_interface_name': '',
            'new_sec_grp_id': '',
            'trans_type': '',
            'cred_uuid': '',
            'target_availability_zone': '',
            'new_vpc_id': '',
            'agent_uuid': '',
            'trans_port': 1,
            'encrypt_switch': 0,
            'wk_uuid': '',
            'encrypt': 1,
            'source_project_id': '',
            'source_region_id': '',
            'vm_name': '',
            'vm_ref': '',
            'target_project_name': '',
            'target_region_name': '',
            'source_project_name': '',
            'source_region_name': '',
            'parent_flavor_name': '',
            'backup_chain_policy': 1,
            'bk_server_addr': '',
            'bk_server_uuid': '',
            'new_cluster_id': '',
            'network_type': '',
            'vpc_id': '',
            'vp_type': 1,
            'dst_path': '',
            'excl_path': [],
            'rc_path_policy': 1,
            'wk_path_list': [{
            'bk_path': '',
            'wk_path': '',},],
            'bk_path': [],
            'thread_num_max': 1,
            'thread_num_min': 1,
            'type_flag': '',
            'backup_way': 1,
        }
        
        
        vpRecoveryRule = VpRecoveryRule(a)
        r = vpRecoveryRule.createVpRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpRecoveryRule', 'createVpRecoveryRule', body)

    def testModifyVpRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'task_type': 1,
            'auto_start': 1,
            'start_time': 1,
            'priority': '',
            'biz_grp_list': [],
            'bk_set_uuids': [],
            'vp_uuid': '',
            'new_dc': '',
            'new_dc_mor': '',
            'new_hostname': '',
            'new_resource_pool_id': '',
            'new_resource_pool_name': '',
            'location': '',
            'location_name': '',
            'new_ds': '',
            'network_id': '',
            'network_name': '',
            'vm_list': [{
            'vm_name': '',
            'vm_ref': '',
            'new_vm_name': '',
            'bk_set_uuid': '',
            'bk_start_tm': '',
            'bk_type': 1,
            'encrypt_type': 1,
            'encrypt_key': '',
            'common_custom': 1,
            'disk_custom': 1,
            'disk_list': [{
            'id': '',
            'disk_path': '',
            'disk_name': '',
            'is_same': 1,
            'new_ds': '',
            'boot_index': 1,
            'disk_type': '',
            'datastore_type': '',
            'src_disk_name': '',
            'is_ignored': '',},],
            'networks': [{
            'source_network_name': '',
            'source_network_id': '',
            'mac_address': '',
            'keep_mac': 1,
            'network_name': '',
            'network_id': '',
            'ip_address': '',
            'source_physical_interface_id': '',
            'source_physical_interface_name': '',
            'physical_interface_id': '',
            'physical_interface_name': '',},],
            'cpu': 1,
            'core_per_sock': 1,
            'mem_mb': 1,
            'dynamic_mem': 1,
            'flavor_id': '',
            'start_order': 0,
            'archtype': '',
            'machine': '',
            'new_vm_sec_grp_id': '',
            'new_vm_vpc_id': '',},],
            'auto_startup': '',
            'dest_trans_mode': 31,
            'concurrent_disk_threads': 2,
            'compress_switch': 1,
            'compress': 1,
            'band_width': '',
            'new_vp_uuid': '',
            'npsvr_uuid': '',
            'tgt_uuid': '',
            'files': [],
            'tgt_path': '',
            'random_str': '',
            'attach_path': '',
            'backup_way': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        vpRecoveryRule = VpRecoveryRule(a)
        r = vpRecoveryRule.modifyVpRecoveryRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpRecoveryRule', 'modifyVpRecoveryRule', body)

    def testListVpRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'vm_name': '',
            'filter_by_biz_grp': 1,
            'where_args': {
            'task_uuid': '',
            'task_type': 1,
            'new_vp_type': 1,
            'status': '',},
            'like_args': {
            'new_vp_name': '',
            'task_name': '',},
            'object_name': '',
            'bk_set_id': '',
        }
        
        
        vpRecoveryRule = VpRecoveryRule(a)
        r = vpRecoveryRule.listVpRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpRecoveryRule', 'listVpRecoveryRule', body)

    def testDescribeVpRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        vpRecoveryRule = VpRecoveryRule(a)
        r = vpRecoveryRule.describeVpRecoveryRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpRecoveryRule', 'describeVpRecoveryRule', body)

    def testDeleteVpRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'force': 1,
        }
        
        
        vpRecoveryRule = VpRecoveryRule(a)
        r = vpRecoveryRule.deleteVpRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpRecoveryRule', 'deleteVpRecoveryRule', body)

    def testOperateVpRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
        }
        
        
        vpRecoveryRule = VpRecoveryRule(a)
        r = vpRecoveryRule.operateVpRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpRecoveryRule', 'operateVpRecoveryRule', body)

    def testListVpRecoveryRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
        }
        
        
        vpRecoveryRule = VpRecoveryRule(a)
        r = vpRecoveryRule.listVpRecoveryRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpRecoveryRule', 'listVpRecoveryRuleStatus', body)


if __name__ == '__main__':
    unittest.main()
