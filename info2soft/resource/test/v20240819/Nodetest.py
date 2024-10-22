
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Node
from info2soft.resource.v20240819.Node import Node
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


class NodeTestCase(unittest.TestCase):

    def testAuthNode(self):
        a = Auth(username, pwd)
        body = {
            'proxy_switch': 0,
            'config_addr': '192.168.72.76',
            'config_port': 26821,
            'node_uuid': '',
            'os_user': 'chenky',
            'os_pwd': '123qwe',
            'i2id': '',
            'use_credential': 0,
            'cred_uuid': '',
            'is_ssl': 1,
        }
        
        
        node = Node(a)
        r = node.authNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'authNode', body)

    def testListNodePackageList(self):
        a = Auth(username, pwd)
        body = {
            'for_download': 1,
        }
        
        
        node = Node(a)
        r = node.listNodePackageList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNodePackageList', body)

    def testCheckCapacity(self):
        a = Auth(username, pwd)
        body = {
            'cache_path': 'C:\\Program Files (x86)\\info2soft\\node\\cache\\',
            'proxy_switch': 0,
            'i2id': '',
            'config_addr': '192.168.72.76',
            'config_port': '26821',
            'is_ssl': 1,
        }
        
        
        node = Node(a)
        r = node.checkCapacity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'checkCapacity', body)

    def testListVg(self):
        a = Auth(username, pwd)
        body = {
            'proxy_switch': 0,
            'i2id': '',
            'config_addr': '192.168.72.76',
            'config_port': '26821',
        }
        
        
        node = Node(a)
        r = node.listVg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listVg', body)

    def testListHostInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_type': 1,
            'config_addr': '',
        }
        
        
        node = Node(a)
        r = node.listHostInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listHostInfo', body)

    def testCheckNodeOnline(self):
        a = Auth(username, pwd)
        body = {
            'proxy_switch': 0,
            'config_port': '26821',
            'i2id': '66F636FE29656416690A62296580EBD9',
            'config_addr': '192.168.72.76',
            'is_ssl': 1,
        }
        
        
        node = Node(a)
        r = node.checkNodeOnline(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'checkNodeOnline', body)

    def testBatchSearchByPort(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
            'port_start': 1,
            'port_end': 1,
        }
        
        
        node = Node(a)
        r = node.batchSearchByPort(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'batchSearchByPort', body)

    def testListNodeBindEcs(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '192.168.72.76',
            'config_port': '26821',
            'platform_uuid': '',
        }
        
        
        node = Node(a)
        r = node.listNodeBindEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNodeBindEcs', body)

    def testCreateNode(self):
        a = Auth(username, pwd)
        body = {
            'node': {
            'bak_client_max': '100',
            'cloud_type': '0',
            'bak_root': '',
            'monitor_switch': 0,
            'node_role': '3',
            'mem_limit': 819,
            'config_port': 26821,
            'mon_save_day': '5',
            'vg': '',
            'os_type': 1,
            'os_pwd': '',
            'log_path': 'C:\\Program Files (x86)\\info2soft\\node\\log\\',
            'mon_data_path': 'C:\\Program Files (x86)\info2soft\\node\\log\\',
            'comment': '',
            'rep_path': [],
            'bak_user_max': '100',
            'cache_path': 'C:\\Program Files (x86)\\info2soft\\node\\cache\\',
            'db_save_day': '3',
            'proxy_switch': 0,
            'data_addr': '192.168.72.76',
            'node_name': 'N4_72.76',
            'config_addr': '192.168.72.76',
            'mon_send_interval': '10',
            'disk_limit': '10240',
            'reboot_sys': '0',
            'bind_lic_list': [],
            'security_check': 0,
            'os_user': 'Kyran',
            'bak_service_type': '',
            'en_snap_switch': 0,
            'rep_excl_path': [],
            'biz_grp_list': [],
            'i2id': '',
            'dtrack_switch': 3,
            'iscsi_as_initiator': 1,
            'iscsi_switch': 1,
            'iscsi_as_target': 1,
            'iscsi_initiator_name': '',
            'use_credential': 0,
            'cred_uuid': '',
            'disk_free_space_limit': 1,
            'node_info': {},
            'cc_ip_uuid': '',
            'maintenance': 0,
            'node_type': 1,
            'cls_node': '',
            'fc_as_initiator': 1,
            'wwpn_info': [],
            'platform_uuid': '',
            'ecs_id': '',
            'ecs_bind': 1,
            'keep_log_days': 180,
            'etcd_url_uuid': '',
            'sys_uuid': '',
            'region_id': '',
            'project_id': '',
            'project_name': '',
            'is_ssl': 1,
            'winstack_pool_id': '',
            'winstack_host_id': '',
            'vm_ref': '',
            'vm_name': '',
            'alarm_switch': 0,
            'cpu_threshold': 80,
            'memory_threshold': 80,
            'monitor_process': 0,
            'snmp_switch': 0,
            'snmp_version': '2c',
            'snmp_ip': '',
            'snmp_port': 1,
            'snmp_community': '',
            'aio_cluster_id': '',
            'aio_host_id': '',
            'rc_protection': 0,
            'guard_data_switch': 0,
            'guard_data_pwd': '',
            'guard_data_threshold': 1,
            'renew_public_key': 1,
            'roles': [
            '1',
            '2',
            '4',
            '8',],
            'log_limit': 1024,
            'bak_meta_data_path': '',
            'bak_meta_data_policy': 1,
            'temp_path': '',
            'roles_info': {
            'role': 1,
            'processes': [],
            'modules': [],},
            'schedule_svr_uuid': '',
            'bak_cache_data_dir': '',
            'bak_cache_disk_lower_limit': 1,
            'bak_cache_data_upper_limit': 1,
            'local_config_switch': 1,
            'auto_move': 1,
            'node_uuid': '',
            'log_interval': 60,
            'rw_server_port': 26820,},
        }
        
        
        node = Node(a)
        r = node.createNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'createNode', body)

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
            'os_type': 2,
            'os_user': 'Kyran',
            'proxy_switch': 0,
            'bind_lic_list': '93AF0C9F-14C8-41A2-31CB-AAA0F65193FA',
            'moni_log_keep_server': '3',
            'node_name': 'aaaa',
            'keep_log_days': 180,
            'monitor_interval': '10',
            'security_check': 1,
            'reboot_sys': '0',
            'bak_client_max': '100',
            'bak_root': '',
            'node_role': '3',
            'monitor_switch': 0,
            'cache_path': 'C:\\Program Files (x86)\\info2soft-i2node\\cache\\',
            'config_port': 26821,
            'bak_user_max': '100',
            'group_uuid': 'F5844651-DB5B-937D-73B1-A2378810F00A',
            'comment': '',
            'biz_grp_list': [],
            'cloud_type': '0',
            'i2id': '',
            'use_credential': 0,
            'cred_uuid': '',
            'en_snap_switch': 0,
            'disk_free_space_limit': 1,
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
            'rep_excl_path': [],
            'batch_cc_ip_uuid': 1,
            'batch_biz_grp_list': 1,
            'batch_log_path': 1,
            'batch_cache_path': 1,
            'batch_mem_limit': 1,
            'batch_disk_limit': 1,
            'batch_disk_free_space_limit': 1,
            'batch_security_check': 1,
            'batch_maintenance': 1,
            'batch_switch': 1,
            'batch_monitor': 1,
            'batch_rep_path': 1,
            'sys_uuid': '',
            'batch_keep_log_days': 1,
            'project_id': '',
            'region_id': '',
            'project_name': '',
            'is_ssl': 1,
            'snmp_switch': 0,
            'snmp_version': '',
            'snmp_community': '',
            'snmp_ip': '',
            'snmp_port': 1,
            'batch_snmp': 1,
            'aio_cluster_id': '',
            'aio_host_id': '',
            'rc_protection': 0,
            'batch_rc_protection': 0,
            'guard_data_switch': 1,
            'guard_data_user': '',
            'guard_data_pwd': '',
            'guard_data_threshold': 1,
            'roles': [
            '1',
            '2',
            '4',
            '8',],
            'log_limit': 1,
            'roles_info': [{
            'role': 1,
            'processes': [],
            'modules': [],},],
            'temp_path': 1,
            'bak_meta_data_path': '',
            'bak_meta_data_policy': 1,
            'monitor_process': 1,
            'batch_log_limit': 0,
            'batch_bak_meta_data_path': 1,
            'batch_temp_path': 1,
            'batch_guard': 1,
            'batch_bak_meta_data_policy': 1,
            'bak_cache_data_dir': '',
            'bak_cache_data_upper_limit': '',
            'bak_cache_disk_lower_limit': '',
            'etcd_url_uuid': '',
            'batch_bak_cache_data_dir': 1,
            'batch_bak_cache_data_upper_limit': 1,
            'batch_bak_cache_disk_lower_limit': 1,
            'batch_etcd_url_uuid': 1,
            'batch_schedule_svr_uuid': 1,
            'schedule_svr_uuid': '',
            'local_config_switch': 1,
            'batch_local_config_switch': 1,
            'rw_server_port': 1,},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        node = Node(a)
        r = node.modifyNode(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'modifyNode', body)

    def testDescribeNode(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        node = Node(a)
        r = node.describeNode(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'describeNode', body)

    def testCreateBatchNode(self):
        a = Auth(username, pwd)
        body = {
            'base_info_list': [{
            'os_pwd': '123qwe',
            'os_user': 'chenky',
            'config_port': 26821,
            'config_addr': '192.168.72.76',
            'node_name': 'N4_72.76',
            'need_install': 0,
            'install_type': 1,
            'install_port_linux': 22,
            'install_path': '',
            'os_type': 1,
            'rep_path': [],
            'installation_mode': 0,
            'bak_meta_data_path': '',},],
            'node': {
            'mem_limit': '819',
            'bind_lic_list': [],
            'disk_limit': '10240',
            'monitor_interval': '10',
            'node_role': '3',
            'monitor_switch': 0,
            'moni_log_keep_node': '5',
            'moni_log_keep_server': '3',
            'security_check': 0,
            'biz_grp_list': [],
            'node_version': '',
            'proxy_ip': '',
            'disk_free_space_limit': 1,
            'proxy_uuid': '',
            'is_ssl': 1,
            'alarm_switch': 1,
            'cpu_threshold': 1,
            'memory_threshold': 1,
            'monitor_process': 1,
            'snmp_switch': 1,
            'snmp_version': '',
            'snmp_community': '',
            'snmp_ip': '',
            'snmp_port': 1,
            'maintenance': 0,
            'rc_protection': 0,
            'roles': [
            '1',
            '2',
            '4',
            '8',],
            'log_limit': 1,
            'roles_info': [{
            'role': 1,
            'processes': [],
            'modules': [],},],
            'temp_path': 1,
            'etcd_url_uuid': '',
            'schedule_svr_uuid': '',
            'local_config_switch': 1,
            'log_interval': 1,
            'proxy_port': '',
            'log_path': '',},
        }
        
        
        node = Node(a)
        r = node.createBatchNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'createBatchNode', body)

    def testDescribeDeviceInfo(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        node = Node(a)
        r = node.describeDeviceInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'describeDeviceInfo', body)

    def testDescribeDriverLetter(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        node = Node(a)
        r = node.describeDriverLetter(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'describeDriverLetter', body)

    def testAddSlaveNode(self):
        a = Auth(username, pwd)
        body = {
            'proxy_switch': '0',
            'config_addr': '',
            'config_port': 1,
            'i2id': '',
            'os_pwd': 'yAZe2Hx6/dCL8GnjiRaro/mayqD24i3bMwZLtRXrHlRDIijGDcNKTqSK4IL91YIaqAGaOpUbnTr+y6VPgJ4UXJQset0se7bQgVrRjVncNeiVNCNyAzLktWYMMGKOWekw5uD2MOVEHhbknG0ZSuFXyywFEG9JTntNerCae7RSI6u2c3kRBCyqbdPc9osMK8YL9ZRqiIE/4K1+BomG9q1RwNEJhDcm/OaMxJCPHANNTImBWWv+Ir3qt20jjv1Fx7of2Fgb14Sj4TwGb7ESrbMiL/fblrfGl+rc6koNucEIRdT+aje+F47pKu4mknubWZ1wo+W2p/yaKyqfzTfeDFJtFQ==',
            'os_user': 'administrator',
            'use_credential': 1,
            'cred_uuid': '',
            'bind_lic_list': [],
            'biz_grp_list': [],
            'comment': '',
            'is_ssl': 1,
            'roles': [
            '1',
            '4',
            '8',],
        }
        
        
        node = Node(a)
        r = node.addSlaveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'addSlaveNode', body)

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
            'i2id': '',
            'rc_protection': 0,},
            'node_uuids': '',
        }
        
        
        node = Node(a)
        r = node.batchModifyNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'batchModifyNode', body)

    def testDescribeNodeInfo(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        node = Node(a)
        r = node.describeNodeInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'describeNodeInfo', body)

    def testListNode(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'limit': 15,
            'page': 1,
            'type': 1,
            'filter_by_biz_grp': 1,
            'order_by': '',
            'direction': '',
            'user_filter': 1,
            'cloud_uuid': '',
            'status': '',
            'status_from': '',
            'is_rc_wk': 0,
            'role': 1,
            'like_args': {
            'xxx': '',},
            'where_args': {
            'xxx': '',},
        }
        
        
        node = Node(a)
        r = node.listNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNode', body)

    def testUpgradeNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
            'operate': 'upgrade',
            'switch': 0,
        }
        
        
        node = Node(a)
        r = node.upgradeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'upgradeNode', body)

    def testMaintainNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
            'operate': 'upgrade',
            'switch': 0,
        }
        
        
        node = Node(a)
        r = node.maintainNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'maintainNode', body)

    def testRenewKeyNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
            'operate': 'upgrade',
            'switch': 0,
        }
        
        
        node = Node(a)
        r = node.renewKeyNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'renewKeyNode', body)

    def testListNodeStatus(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [
            'D66246D7-89C4-DC3A-E9A2-D2FCE4A56307',
            '064B23C1-DF92-8846-4BEA-8517789C35A4',],
            'force_refresh': 1,
        }
        
        
        node = Node(a)
        r = node.listNodeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNodeStatus', body)

    def testDeleteNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [
            'eC24eB0d-6ee5-c6bD-4D6c-DAFCD6D3FF91',],
            'delete_quota': 1,
            'force': 1,
        }
        
        
        node = Node(a)
        r = node.deleteNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'deleteNode', body)

    def testNodeGetOracleInfo(self):
        a = Auth(username, pwd)
        body = {
            'username': '',
            'password': '',
            'sqlplus_path': '',
            'sid': '',
            'timeout': '',
            'port': '',
            'bk_uuid': '',
        }
        
        
        node = Node(a)
        r = node.nodeGetOracleInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'nodeGetOracleInfo', body)

    def testNodeGetMysqlInfo(self):
        a = Auth(username, pwd)
        body = {
            'timeout': '',
            'username': '',
            'password': '',
            'mysql_path': '',
            'port': '',
            'bk_uuid': '',
            'mysql_host': '',
        }
        
        
        node = Node(a)
        r = node.nodeGetMysqlInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'nodeGetMysqlInfo', body)

    def testDataIpList(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
        }
        
        
        node = Node(a)
        r = node.dataIpList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'dataIpList', body)

    def testModifyDataIp(self):
        a = Auth(username, pwd)
        body = {
            'data_ip_list': [{
            'uuid': 'A7EC7CF9-FCA2-D467-ECD6-E028AA9C8319',
            'data_ip': '172.20.15.121',},],
            'node_uuid': 'D6EC7CF9-FCA2-D467-ECD6-E028AA9C8319',
        }
        
        
        node = Node(a)
        r = node.modifyDataIp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'modifyDataIp', body)

    def testListHbaInfo(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '',
            'config_port': '',
            'proxy_switch': 1,
            'i2id': '',
        }
        
        
        node = Node(a)
        r = node.listHbaInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listHbaInfo', body)

    def testCheckUnbindEcs(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        node = Node(a)
        r = node.checkUnbindEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'checkUnbindEcs', body)

    def testGetNodeVersion(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
            'port': 1,
            'add': 1,
            'cls_uuid': '',
        }
        
        
        node = Node(a)
        r = node.getNodeVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'getNodeVersion', body)

    def testActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'node_uuid': '',
            'bind_lic_list': [],},],
        }
        
        
        node = Node(a)
        r = node.activeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'activeNode', body)

    def testListWaitingActiveNode(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        node = Node(a)
        r = node.listWaitingActiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listWaitingActiveNode', body)

    def testDownloadNodeInstallScript(self):
        a = Auth(username, pwd)
        body = {
            'os_type': 0,
        }
        
        
        node = Node(a)
        r = node.downloadNodeInstallScript(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'downloadNodeInstallScript', body)

    def testGetNodePackageUrl(self):
        a = Auth(username, pwd)
        body = {
            'os_type': 1,
        }
        
        
        node = Node(a)
        r = node.getNodePackageUrl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'getNodePackageUrl', body)

    def testListRules(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'page': 1,
            'limit': 10,
        }
        
        
        node = Node(a)
        r = node.listRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listRules', body)

    def testDeleteInactiveNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
        }
        
        
        node = Node(a)
        r = node.deleteInactiveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'deleteInactiveNode', body)

    def testListNodeUkey(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        node = Node(a)
        r = node.listNodeUkey(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNodeUkey', body)

    def testListPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        node = Node(a)
        r = node.listPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listPlatform', body)

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
        
        
        node = Node(a)
        r = node.listMysqlDatabases(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listMysqlDatabases', body)

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
        
        
        node = Node(a)
        r = node.listMysqlTables(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listMysqlTables', body)

    def testListNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        node = Node(a)
        r = node.listNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNodeProcess', body)

    def testStartNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'operate': '',
            'data': [{
            'pid': '',
            'pname': '',},],
        }
        
        
        node = Node(a)
        r = node.startNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'startNodeProcess', body)

    def testStopNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'operate': '',
            'data': [{
            'pid': '',
            'pname': '',},],
        }
        
        
        node = Node(a)
        r = node.stopNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'stopNodeProcess', body)

    def testRestartNodeProcess(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'operate': '',
            'data': [{
            'pid': '',
            'pname': '',},],
        }
        
        
        node = Node(a)
        r = node.restartNodeProcess(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'restartNodeProcess', body)

    def testListKernels(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        node = Node(a)
        r = node.listKernels(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listKernels', body)

    def testBatchAuthNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
            'os_user': '',
            'os_pwd': '',
        }
        
        
        node = Node(a)
        r = node.batchAuthNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'batchAuthNode', body)


if __name__ == '__main__':
    unittest.main()
