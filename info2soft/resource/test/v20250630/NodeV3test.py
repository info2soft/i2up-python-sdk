
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import NodeV3
from info2soft.resource.v20250630.NodeV3 import NodeV3
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


class NodeV3TestCase(unittest.TestCase):
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

    def testAuthNode(self):
        a = Auth(username, pwd)
        body = {
            'os_pwd': '123qwe',
            'proxy_id': '',
            'use_credential': 0,
            'proxy_switch': 0,
            'is_ssl': 1,
            'cred_uuid': '',
            'config_addr': '192.168.72.76',
            'config_port': 26821,
            'node_uuid': '',
            'os_user': 'chenky',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.authNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'authNode', body)

    def testListNodePackageList(self):
        a = Auth(username, pwd)
        body = {
            'for_download': 1,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listNodePackageList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listNodePackageList', body)

    def testCheckCapacity(self):
        a = Auth(username, pwd)
        body = {
            'proxy_id': '',
            'is_ssl': 1,
            'config_addr': '192.168.72.76',
            'config_port': '26821',
            'cache_path': 'C:\\Program Files (x86)\\info2soft\\node\\cache\\',
            'proxy_switch': 0,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.checkCapacity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'checkCapacity', body)

    def testListVg(self):
        a = Auth(username, pwd)
        body = {
            'proxy_switch': 0,
            'proxy_id': '',
            'config_addr': '192.168.72.76',
            'config_port': '26821',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listVg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listVg', body)

    def testListHostInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_type': 1,
            'config_addr': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listHostInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listHostInfo', body)

    def testCheckNodeOnline(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '192.168.72.76',
            'proxy_switch': 0,
            'is_ssl': 1,
            'config_port': '26821',
            'proxy_id': '66F636FE29656416690A62296580EBD9',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.checkNodeOnline(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'checkNodeOnline', body)

    def testBatchSearchByPort(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
            'port_start': 1,
            'port_end': 1,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.batchSearchByPort(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'batchSearchByPort', body)

    def testListNodeBindEcs(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '192.168.72.76',
            'config_port': '26821',
            'platform_uuid': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listNodeBindEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listNodeBindEcs', body)

    def testCreateNode(self):
        a = Auth(username, pwd)
        body = {
            'node': {
            'comment': '',
            'alarm_switch': 0,
            'cpu_threshold': 80,
            'memory_threshold': 80,
            'monitor_process': 0,
            'rep_path': [],
            'cloud_type': '0',
            'guard_data_switch': 0,
            'bak_user_max': '100',
            'guard_data_pwd': '',
            'fc_as_target': 1,
            'wwpn_info_target': [],
            'cache_path': 'C:\\Program Files (x86)\\info2soft\\node\\cache\\',
            'rw_server_port': 26820,
            'bak_root': '',
            'db_save_day': '3',
            'snmp_switch': 0,
            'snmp_version': '2c',
            'snmp_ip': '',
            'snmp_port': 1,
            'snmp_community': '',
            'aio_cluster_id': '',
            'aio_host_id': '',
            'proxy_switch': 0,
            'data_addr': '192.168.72.76',
            'project_name': '',
            'etcd_url_uuid': '',
            'monitor_switch': 0,
            'node_name': 'N4_72.76',
            'config_addr': '192.168.72.76',
            'mon_send_interval': '10',
            'keep_log_days': 180,
            'node_role': '3',
            'disk_limit': '10240',
            'reboot_sys': '0',
            'rc_protection': 0,
            'bind_lic_list': [],
            'security_check': 0,
            'mem_limit': 819,
            'os_user': 'Kyran',
            'guard_data_threshold': 1,
            'ecs_id': '',
            'ecs_bind': 1,
            'bak_service_type': '',
            'is_ssl': 1,
            'en_snap_switch': 0,
            'config_port': 26821,
            'rep_excl_path': [],
            'biz_grp_list': [],
            'proxy_id': '',
            'mon_save_day': '5',
            'dtrack_switch': 3,
            'bak_cache_data_dir': '',
            'bak_cache_disk_lower_limit': 1,
            'bak_cache_data_upper_limit': 1,
            'winstack_pool_id': '',
            'winstack_host_id': '',
            'roles': [
            '1',
            '2',
            '4',
            '8',],
            'vm_ref': '',
            'auto_move': 1,
            'log_limit': 1024,
            'iscsi_as_initiator': 1,
            'bak_meta_data_path': '',
            'bak_meta_data_policy': 1,
            'iscsi_switch': 1,
            'renew_public_key': 1,
            'vm_name': '',
            'schedule_svr_uuid': '',
            'vg': '',
            'iscsi_as_target': 1,
            'log_interval': 60,
            'iscsi_initiator_name': '',
            'use_credential': 0,
            'os_type': 1,
            'cred_uuid': '',
            'local_config_switch': 1,
            'disk_free_space_limit': 1,
            'node_info': {},
            'os_pwd': '',
            'cc_ip_uuid': '',
            'maintenance': 0,
            'node_type': 1,
            'cls_node': '',
            'node_uuid': '',
            'sys_uuid': '',
            'fc_as_initiator': 1,
            'wwpn_info': [],
            'platform_uuid': '',
            'log_path': 'C:\\Program Files (x86)\\info2soft\\node\\log\\',
            'region_id': '',
            'temp_path': '',
            'project_id': '',
            'roles_info': {
            'modules': [],
            'role': 1,
            'processes': [],},
            'bak_client_max': '100',
            'mon_data_path': 'C:\\Program Files (x86)\\info2soft\\node\\log\\',},
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.createNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'createNode', body)

    def testPrecreateNode(self):
        a = Auth(username, pwd)
        body = {
            'node': {
            'comment': '',
            'alarm_switch': 0,
            'cpu_threshold': 80,
            'memory_threshold': 80,
            'monitor_process': 0,
            'rep_path': [],
            'cloud_type': '0',
            'guard_data_switch': 0,
            'bak_user_max': '100',
            'guard_data_pwd': '',
            'cache_path': 'C:\\Program Files (x86)\\info2soft\\node\\cache\\',
            'rw_server_port': 26820,
            'bak_root': '',
            'db_save_day': '3',
            'snmp_switch': 0,
            'snmp_version': '2c',
            'snmp_ip': '',
            'snmp_port': 1,
            'snmp_community': '',
            'aio_cluster_id': '',
            'aio_host_id': '',
            'proxy_switch': 0,
            'data_addr': '192.168.72.76',
            'project_name': '',
            'etcd_url_uuid': '',
            'monitor_switch': 0,
            'node_name': 'N4_72.76',
            'config_addr': '192.168.72.76',
            'mon_send_interval': '10',
            'keep_log_days': 180,
            'node_role': '3',
            'disk_limit': '10240',
            'reboot_sys': '0',
            'rc_protection': 0,
            'bind_lic_list': [],
            'security_check': 0,
            'mem_limit': 819,
            'os_user': 'Kyran',
            'guard_data_threshold': 1,
            'ecs_id': '',
            'ecs_bind': 1,
            'bak_service_type': '',
            'is_ssl': 1,
            'en_snap_switch': 0,
            'config_port': 26821,
            'rep_excl_path': [],
            'biz_grp_list': [],
            'proxy_id': '',
            'mon_save_day': '5',
            'dtrack_switch': 3,
            'bak_cache_data_dir': '',
            'bak_cache_disk_lower_limit': 1,
            'bak_cache_data_upper_limit': 1,
            'winstack_pool_id': '',
            'winstack_host_id': '',
            'roles': [
            '1',
            '2',
            '4',
            '8',],
            'vm_ref': '',
            'auto_move': 1,
            'log_limit': 1024,
            'iscsi_as_initiator': 1,
            'bak_meta_data_path': '',
            'bak_meta_data_policy': 1,
            'iscsi_switch': 1,
            'renew_public_key': 1,
            'vm_name': '',
            'schedule_svr_uuid': '',
            'vg': '',
            'iscsi_as_target': 1,
            'log_interval': 60,
            'iscsi_initiator_name': '',
            'use_credential': 0,
            'os_type': 1,
            'cred_uuid': '',
            'local_config_switch': 1,
            'disk_free_space_limit': 1,
            'node_info': {},
            'os_pwd': '',
            'cc_ip_uuid': '',
            'maintenance': 0,
            'node_type': 1,
            'cls_node': '',
            'node_uuid': '',
            'sys_uuid': '',
            'fc_as_initiator': 1,
            'wwpn_info': [],
            'platform_uuid': '',
            'log_path': 'C:\\Program Files (x86)\\info2soft\\node\\log\\',
            'region_id': '',
            'temp_path': '',
            'project_id': '',
            'roles_info': {
            'modules': [],
            'role': 1,
            'processes': [],},
            'bak_client_max': '100',
            'mon_data_path': 'C:\\Program Files (x86)\\info2soft\\node\\log\\',},
            'register': 1,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.precreateNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'precreateNode', body)

    def testModifyNode(self):
        a = Auth(username, pwd)
        body = {
            'node': {
            'moni_log_keep_node': '5',
            '_path': [],
            'log_path': 'C:\\Program Files (x86)\\info2soft-i2node\\log\\',
            'disk_limit': '40960',
            'bak_service_type': '',
            'config_addr': '192.168.74.25',
            'mem_limit': '13041',
            'batch_cc_ip_uuid': 1,
            'os_type': 2,
            'batch_biz_grp_list': 1,
            'os_user': 'Kyran',
            'batch_log_path': 1,
            'proxy_switch': 0,
            'batch_cache_path': 1,
            'bind_lic_list': '93AF0C9F-14C8-41A2-31CB-AAA0F65193FA',
            'batch_mem_limit': 1,
            'moni_log_keep_server': '3',
            'batch_disk_limit': 1,
            'node_name': 'aaaa',
            'batch_disk_free_space_limit': 1,
            'keep_log_days': 180,
            'batch_security_check': 1,
            'monitor_interval': '10',
            'batch_maintenance': 1,
            'security_check': 1,
            'batch_switch': 1,
            'reboot_sys': '0',
            'bak_client_max': '100',
            'bak_root': '',
            'node_role': '3',
            'monitor_switch': 0,
            'guard_data_switch': 1,
            'cache_path': 'C:\\Program Files (x86)\\info2soft-i2node\\cache\\',
            'guard_data_user': '',
            'config_port': 26821,
            'guard_data_pwd': '',
            'bak_user_max': '100',
            'group_uuid': 'F5844651-DB5B-937D-73B1-A2378810F00A',
            'comment': '',
            'biz_grp_list': [],
            'fc_as_target': 1,
            'cloud_type': '0',
            'wwpn_info_target': [],
            'i2id': '',
            'use_credential': 0,
            'cred_uuid': '',
            'en_snap_switch': 0,
            'batch_monitor': 1,
            'disk_free_space_limit': 1,
            'batch_rep_path': 1,
            'rw_server_port': 1,
            'platform_uuid': '',
            'maintenance': 0,
            'os_pwd': 'EnEyGDJF==',
            'ecs_bind': 0,
            'ecs_id': '',
            'fc_as_initiator': 0,
            'vg': '',
            'wwpn_info': [],
            'monitor_log_path': 'C:\\Program Files (x86)\\info2soft-i2node\\log\\',
            'data_addr': '192.168.74.25',
            'snmp_switch': 0,
            'rep_excl_path': [],
            'snmp_version': '',
            'aio_cluster_id': '',
            'snmp_community': '',
            'aio_host_id': '',
            'snmp_ip': '',
            'snmp_port': 1,
            'batch_snmp': 1,
            'project_name': '',
            'rc_protection': 0,
            'batch_rc_protection': 0,
            'guard_data_threshold': 1,
            'is_ssl': 1,
            'batch_bak_meta_data_policy': 1,
            'bak_cache_data_dir': '',
            'roles': [
            '1',
            '2',
            '4',
            '8',],
            'bak_cache_data_upper_limit': '',
            'log_limit': 1,
            'bak_cache_disk_lower_limit': '',
            'roles_info': [{
            'modules': [],
            'role': 1,
            'processes': [],},],
            'etcd_url_uuid': '',
            'temp_path': 1,
            'batch_bak_cache_data_dir': 1,
            'bak_meta_data_path': '',
            'batch_guard': 1,
            'batch_keep_log_days': 1,
            'batch_bak_cache_data_upper_limit': 1,
            'bak_meta_data_policy': 1,
            'batch_bak_cache_disk_lower_limit': 1,
            'monitor_process': 1,
            'batch_etcd_url_uuid': 1,
            'batch_schedule_svr_uuid': 1,
            'schedule_svr_uuid': '',
            'batch_log_limit': 0,
            'local_config_switch': 1,
            'batch_bak_meta_data_path': 1,
            'batch_local_config_switch': 1,
            'sys_uuid': '',
            'project_id': '',
            'region_id': '',
            'batch_temp_path': 1,},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        nodeV3 = NodeV3(a)
        r = nodeV3.modifyNode(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'modifyNode', body)

    def testDescribeNode(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        nodeV3 = NodeV3(a)
        r = nodeV3.describeNode(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'describeNode', body)

    def testCreateBatchNode(self):
        a = Auth(username, pwd)
        body = {
            'base_info_list': [{
            'os_pwd': '123qwe',
            'os_user': 'chenky',
            'config_port': 26821,
            'config_addr': '192.168.72.76',
            'cache_path': '',
            'bak_meta_data_path': '',
            'node_name': 'N4_72.76',
            'need_install': 0,
            'temp_path': '',
            'install_type': 1,
            'install_port_linux': 22,
            'install_path': '',
            'os_type': 1,
            'rep_path': [],
            'installation_mode': 0,},],
            'node': {
            'bind_lic_list': [],
            'disk_limit': '10240',
            'alarm_switch': 1,
            'cpu_threshold': 1,
            'memory_threshold': 1,
            'monitor_process': 1,
            'monitor_interval': '10',
            'log_interval': 1,
            'node_role': '3',
            'etcd_url_uuid': '',
            'monitor_switch': 0,
            'schedule_svr_uuid': '',
            'moni_log_keep_node': '5',
            'snmp_switch': 1,
            'snmp_version': '',
            'snmp_community': '',
            'snmp_ip': '',
            'snmp_port': 1,
            'moni_log_keep_server': '3',
            'security_check': 0,
            'biz_grp_list': [],
            'node_version': '',
            'proxy_ip': '',
            'disk_free_space_limit': 1,
            'proxy_uuid': '',
            'maintenance': 0,
            'rc_protection': 0,
            'log_path': '',
            'is_ssl': 1,
            'proxy_port': '',
            'roles': [
            '1',
            '2',
            '4',
            '8',],
            'log_limit': 1,
            'roles_info': [{
            'modules': [],
            'role': 1,
            'processes': [],},],
            'local_config_switch': 1,
            'mem_limit': '819',},
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.createBatchNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'createBatchNode', body)

    def testDescribeDeviceInfo(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        nodeV3 = NodeV3(a)
        r = nodeV3.describeDeviceInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'describeDeviceInfo', body)

    def testDescribeDriverLetter(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        nodeV3 = NodeV3(a)
        r = nodeV3.describeDriverLetter(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'describeDriverLetter', body)

    def testAddSlaveNode(self):
        a = Auth(username, pwd)
        body = {
            'os_user': 'administrator',
            'use_credential': 1,
            'cred_uuid': '',
            'is_ssl': 1,
            'proxy_switch': '0',
            'bind_lic_list': [],
            'config_addr': '',
            'biz_grp_list': [],
            'config_port': 1,
            'comment': '',
            'roles': [
            '1',
            '4',
            '8',],
            'proxy_id': '',
            'os_pwd': 'yAZe2Hx6/dCL8GnjiRaro/mayqD24i3bMwZLtRXrHlRDIijGDcNKTqSK4IL91YIaqAGaOpUbnTr+y6VPgJ4UXJQset0se7bQgVrRjVncNeiVNCNyAzLktWYMMGKOWekw5uD2MOVEHhbknG0ZSuFXyywFEG9JTntNerCae7RSI6u2c3kRBCyqbdPc9osMK8YL9ZRqiIE/4K1+BomG9q1RwNEJhDcm/OaMxJCPHANNTImBWWv+Ir3qt20jjv1Fx7of2Fgb14Sj4TwGb7ESrbMiL/fblrfGl+rc6koNucEIRdT+aje+F47pKu4mknubWZ1wo+W2p/yaKyqfzTfeDFJtFQ==',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.addSlaveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'addSlaveNode', body)

    def testBatchModifyNode(self):
        a = Auth(username, pwd)
        body = {
            'node': {
            'rep_excl_path': [],
            'log_path': 'C:\\Program Files (x86)\\info2soft-i2node\\log\\',
            'config_addr': '192.168.74.25',
            'proxy_switch': 0,
            'security_check': 1,
            'node_role': '3',
            'bak_user_max': '100',
            'cloud_type': '0',
            'en_snap_switch': 0,
            'os_pwd': 'EnEyGDJF==',
            'vg': '',
            'monitor_log_path': 'C:\\Program Files (x86)\\info2soft-i2node\\log\\',
            'data_addr': '192.168.74.25',
            'moni_log_keep_node': '5',
            'wk_path': [],
            'disk_limit': '40960',
            'bak_service_type': '',
            'mem_limit': '13041',
            'os_type': 2,
            'os_user': 'Kyran',
            'bind_lic_list': '93AF0C9F-14C8-41A2-31CB-AAA0F65193FA',
            'moni_log_keep_server': '3',
            'node_name': 'aaaa',
            'monitor_interval': '10',
            'maintenance': 0,
            'bak_client_max': '100',
            'bak_root': '',
            'monitor_switch': 0,
            'reboot_sys': '0',
            'config_port': 26821,
            'rc_protection': 0,
            'cred_uuid': '',
            'cache_path': 'C:\\Program Files (x86)\\info2soft-i2node\\cache\\',
            'fc_as_initiator': 0,
            'wwpn_info': [],
            'keep_log_days': 180,
            'group_uuid': 'F5844651-DB5B-937D-73B1-A2378810F00A',
            'biz_grp_list': [],
            'ecs_bind': 0,
            'platform_uuid': '',
            'ecs_id': '',
            'comment': '',
            'use_credential': 0,
            'disk_free_space_limit': 1,
            'i2id': '',},
            'node_uuids': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.batchModifyNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'batchModifyNode', body)

    def testDescribeNodeInfo(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        nodeV3 = NodeV3(a)
        r = nodeV3.describeNodeInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'describeNodeInfo', body)

    def testListNode(self):
        a = Auth(username, pwd)
        body = {
            'like_args': {
            'xxx': '',},
            'where_args': {
            'xxx': '',},
            'type': 1,
            'status': '',
            'status_from': '',
            'is_rc_wk': 0,
            'filter_by_biz_grp': 1,
            'order_by': '',
            'search_value': '',
            'direction': '',
            'search_field': '',
            'role': 1,
            'user_filter': 1,
            'limit': 15,
            'cloud_uuid': '',
            'page': 1,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listNode', body)

    def testUpgradeNode(self):
        a = Auth(username, pwd)
        body = {
            'switch': 0,
            'node_uuids': [],
            'operate': 'upgrade',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.upgradeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'upgradeNode', body)

    def testMaintainNode(self):
        a = Auth(username, pwd)
        body = {
            'switch': 0,
            'node_uuids': [],
            'operate': 'upgrade',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.maintainNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'maintainNode', body)

    def testRenewKeyNode(self):
        a = Auth(username, pwd)
        body = {
            'switch': 0,
            'node_uuids': [],
            'operate': 'upgrade',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.renewKeyNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'renewKeyNode', body)

    def testListNodeStatus(self):
        a = Auth(username, pwd)
        body = {
            'force_refresh': 1,
            'node_uuids': [
            'D66246D7-89C4-DC3A-E9A2-D2FCE4A56307',
            '064B23C1-DF92-8846-4BEA-8517789C35A4',],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listNodeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listNodeStatus', body)

    def testDeleteNode(self):
        a = Auth(username, pwd)
        body = {
            'force': 1,
            'node_uuids': [
            '31BE7E41-6d55-eaa7-E51d-f7E6703c4219',],
            'delete_quota': 1,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.deleteNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'deleteNode', body)

    def testNodeGetOracleInfo(self):
        a = Auth(username, pwd)
        body = {
            'sqlplus_path': '',
            'sid': '',
            'timeout': '',
            'port': '',
            'bk_uuid': '',
            'username': '',
            'password': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.nodeGetOracleInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'nodeGetOracleInfo', body)

    def testNodeGetMysqlInfo(self):
        a = Auth(username, pwd)
        body = {
            'username': '',
            'password': '',
            'mysql_path': '',
            'port': '',
            'bk_uuid': '',
            'mysql_host': '',
            'timeout': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.nodeGetMysqlInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'nodeGetMysqlInfo', body)

    def testDataIpList(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.dataIpList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'dataIpList', body)

    def testModifyDataIp(self):
        a = Auth(username, pwd)
        body = {
            'data_ip_list': [{
            'uuid': 'A7EC7CF9-FCA2-D467-ECD6-E028AA9C8319',
            'data_ip': '172.20.15.121',},],
            'node_uuid': 'D6EC7CF9-FCA2-D467-ECD6-E028AA9C8319',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.modifyDataIp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'modifyDataIp', body)

    def testListHbaInfo(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '',
            'config_port': '',
            'proxy_switch': 1,
            'proxy_id': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listHbaInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listHbaInfo', body)

    def testCheckUnbindEcs(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.checkUnbindEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'checkUnbindEcs', body)

    def testGetNodeVersion(self):
        a = Auth(username, pwd)
        body = {
            'add': 1,
            'cls_uuid': '',
            'ip': '',
            'port': 1,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.getNodeVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'getNodeVersion', body)

    def testActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'node_uuid': '',
            'bind_lic_list': [],},],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.activeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'activeNode', body)

    def testListWaitingActiveNode(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listWaitingActiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listWaitingActiveNode', body)

    def testDownloadNodeInstallScript(self):
        a = Auth(username, pwd)
        body = {
            'os_type': 0,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.downloadNodeInstallScript(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'downloadNodeInstallScript', body)

    def testGetNodePackageUrl(self):
        a = Auth(username, pwd)
        body = {
            'os_type': 1,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.getNodePackageUrl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'getNodePackageUrl', body)

    def testListRules(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'page': 1,
            'limit': 10,
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listRules', body)

    def testDeleteInactiveNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.deleteInactiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'deleteInactiveNode', body)

    def testListNodeUkey(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listNodeUkey(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listNodeUkey', body)

    def testListPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listPlatform', body)

    def testListMysqlDatabases(self):
        a = Auth(username, pwd)
        body = {
            'mysql_host': '',
            'port': '',
            'username': '',
            'password': '',
            'timeout': '',
            'mysql_path': '',
            'node_uuid': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listMysqlDatabases(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listMysqlDatabases', body)

    def testListMysqlTables(self):
        a = Auth(username, pwd)
        body = {
            'username': '',
            'password': '',
            'mysql_host': '',
            'port': '',
            'timeout': '',
            'mysql_path': '',
            'node_uuid': '',
            'db_name': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listMysqlTables(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listMysqlTables', body)

    def testListNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listNodeProcess', body)

    def testStartNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'operate': '',
            'data': [{
            'pid': '',
            'pname': '',
            'module_name': '',},],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.startNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'startNodeProcess', body)

    def testStopNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'operate': '',
            'data': [{
            'pid': '',
            'pname': '',
            'module_name': '',},],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.stopNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'stopNodeProcess', body)

    def testRestartNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'operate': '',
            'data': [{
            'pid': '',
            'pname': '',
            'module_name': '',},],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.restartNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'restartNodeProcess', body)

    def testInsmodNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'operate': '',
            'data': [{
            'pid': '',
            'pname': '',
            'module_name': '',},],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.insmodNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'insmodNodeProcess', body)

    def testRmmodNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'operate': '',
            'data': [{
            'pid': '',
            'pname': '',
            'module_name': '',},],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.rmmodNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'rmmodNodeProcess', body)

    def testInstallNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'operate': '',
            'data': [{
            'pid': '',
            'pname': '',
            'module_name': '',},],
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.installNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'installNodeProcess', body)

    def testBatchAuthNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
            'os_user': '',
            'os_pwd': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.batchAuthNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'batchAuthNode', body)

    def testListKernels(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        nodeV3 = NodeV3(a)
        r = nodeV3.listKernels(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NodeV3', 'listKernels', body)


if __name__ == '__main__':
    unittest.main()
