# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.vp.v20240228.VirtualizationSupport import VirtualizationSupport
# from info2soft.vp.v20200722.VirtualizationSupport import VirtualizationSupport
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


class VirtualizationSupportTestCase(unittest.TestCase):

    def testDescribeVpRuleRate(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'wk_uuid': 'F28BA5A6-4FF9-E596-4371-1ED203D45143',
            'mode': 'month',
            'type': 'I2VP_BK',
            'group_uuid': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpRuleRate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpRuleRate', body)

    def testDescribeVmProtectRate(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': 'F28BA5A6-4FF9-E596-4371-1ED203D45143',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVmProtectRate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVmProtectRate', body)

    def testCreateVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'del_bkup_data': 0,
            'quiet_snap': 0,
            'quick_back': 1,
            'vp_uuid': 'C6335F62-2565-1957-4BB9-587F2FF46B00',
            'bk_path': 'E:/vp_bk5/',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'lan_free': 23,
            'rule_name': 'vp_bk cky',
            'bkup_policy': 1,
            'bkup_one_time': 1546831899,
            'biz_grp_list': [],
            'rule_type': 0,
            'band_width': '-1',
            'compress': 0,
            'mem_snap': 0,
            'random_str': '11111111-1111-1111-1111-111111111111',
            'instant_recovery': 1,
            'auto': 0,
            'add_drill': 1,
            'drill_plat_uuid': '',
            'data_ip_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'cred_uuid': '',
            'trans_type': '',
            'data_verify': 0,
            'ftp_path': '',
            'agent_uuid': '',
            'auto_discovery': 0,
            'encrypt_type': 1,
            'encrypt_key': '',
            'encrypt_switch': 1,
            'src_trans_mode': 31,
            'transfer_compression': 0,
            'is_limit_backuptime': 0,
            'consolidate_disks_time': '',
            'consolidate_switch': 0,
            'fail_retry': 1,
            'retry_times': 1,
            'retry_interval': 1,
            'concurrent_disk_threads': 1,
            'backup_method': 0,
            'transfer_encrypt': 0,
            'bk_type': 0,
            'bucket': '',
            'sto_uuid': '',
            'bucket_path': '',
            'source_project_id': '',
            'source_region_id': '',
            'is_fusion_storage': 0,
            'winstack_pool_id': '',
            'winstack_host_id': '',
            'pool_uuid': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.createVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpBackup', body)

    def testModifyVpBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.modifyVpBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'modifyVpBackup', body)

    def testDescribeVpBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpBackup', body)

    def testDescribeVpBackupGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpBackupGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpBackupGroup', body)

    def testListVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'type': 0,
            'status': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpBackup', body)

    def testListVpBackupGroup(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'type': 0
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpBackupGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpBackupGroup', body)

    def testListVpBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'force_refresh': 1,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpBackupStatus', body)

    def testStartVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'group_uuids': [],
            'bkup_type': '',
            'force': 0,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.startVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'startVpBackup', body)

    def testDeleteVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'group_uuids': [],
            'force': 1,
            'delete_bk_data': 0,
            'recycle': 0,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.deleteVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpBackup', body)

    def testDeleteVpBackupPoint(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'version_list': [],
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.deleteVpBackupPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpBackupPoint', body)

    def testCreateVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'bk_path_view': 'H:/vp_bk5/testRC1_BAK_99_192.168.85.139',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'new_ds': 'datastore1',
            'new_hostname': 'localhost.localdomain',
            'new_dc': 'ha-datacenter',
            'is_create': 0,
            'vp_uuid': '928B88A6-CDBA-6F55-ADCB-15A8A935C9C2',
            'new_ds_path': '/',
            'new_vp_uuid': '928B88A6-CDBA-6F55-ADCB-15A8A935C9C2',
            'rule_name': 'testRC cky',
            'lan_free': 23,
            'rule_type': 0,
            'auto_startup': 0,
            'new_dc_mor': 'ha-datacenter',
            'api_type': 'HostAgent',
            'biz_grp_list': [],
            'group_recovery': 0,
            'backup_rule_name': 'testRC1',
            'band_width': '-1',
            'for_vp_file_rc': 1,
            'del_vm': 1,
            'network_id': '',
            'network_name': '',
            'data_ip_uuid': '928B88A6-CDBA-6F55-ADCB-15A8A935C9C1',
            'cred_uuid': '',
            'trans_type': '',
            'agent_uuid': '',
            'agent_data_ip_uuid': '',
            'parent_flavor_id': '',
            'ip_address': '',
            'dest_trans_mode': 31,
            'concurrent_disk_threads': 1,
            'backup_method': 0,
            'is_start_order': 0,
            'transfer_compression': 0,
            'transfer_encrypt': 0,
            'location': '',
            'bk_type': 0,
            'sto_uuid': '',
            'bucket': '',
            'bucket_path': '',
            'target_region_id': '',
            'target_project_id': '',
            'is_fusion_storage': 1,
            'winstack_pool_id': '',
            'winstack_host_id': '',
            'new_archtype': '',
            'new_machine': '',
            'new_host_id': '',
            'rc_method': '',
            'backup_task_uuid': '',
            'pool_uuid': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.createVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpRecovery', body)

    def testDescribeVpRecoveryGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpRecoveryGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpRecoveryGroup', body)

    def testListVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'type': 0,
            'limit': 10,
            'page': 1
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpRecovery', body)

    def testListVpRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'force_refresh': 1,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpRecoveryStatus', body)

    def testStartVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rule_uuids': '641A27BB-B4D1-F482-1FB8-E856898626DA',
            'rule_type': 0,
            'group_uuids': [],
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.startVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'startVpRecovery', body)

    def testDeleteVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'group_uuids': [],
            'delete_tgtvm': 1,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.deleteVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpRecovery', body)

    def testCreateVpMove(self):
        a = Auth(username, pwd)
        body = {
            'new_ds': '103-数据盘',
            'tgt_uuid': '7F16E670-1A61-D565-6905-9C68B9520907',
            'src_uuid': '7F16E670-1A61-D565-6905-9C68B9520907',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'automate': 0,
            'rule_name': 'testMove1 cky',
            'new_dc': 'i2test',
            'bk_path': 'H:/vp_rep/',
            'backup_type': 'i',
            'new_host': '192.168.88.103',
            'quiet_snap': 1,
            'quick_back': 1,
            'lan_free': 23,
            'new_dc_mor': 'datacenter-2',
            'bkup_policy': 0,
            'band_width': '-1',
            'rule_type': 1,
            'auto_shutdown': 0,
            'auto_startup': 0,
            'biz_grp_list': [],
            'auto': '',
            'add_drill': 1,
            'drill_plat_uuid': '',
            'mem_snap': 1,
            'overwrite': 1,
            'network_id': '',
            'network_name': '',
            'agent_uuid': '',
            'data_ip_uuid': '7F16E670-1A61-D565-6905-9C68B9520901',
            'ip_address': '',
            'src_trans_mode': 31,
            'dest_trans_mode': 31,
            'transfer_compression': 0,
            'consolidate_switch': 0,
            'consolidate_disks_time': '',
            'concurrent_disk_threads': 1,
            'transfer_encrypt': 0,
            'target_project_id': '',
            'source_region_id': '',
            'target_region_id': '',
            'source_project_id': '',
            'auto_start': 1,
            'bkup_one_time': '',
            'auto_shutdown_before_incremental': 0,
            'location': '',
            'location_name': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.createVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpMove', body)

    def testBatchCreateVpRep(self):
        a = Auth(username, pwd)
        body = {
            'base_info_list': {
                'rule_type': 0,
                'biz_grp_list': '',
                'quick_back': 1,
                'quiet_snap': 1,
                'lan_free': 23,
                'mem_snap': 1,
                'band_width': '-1',
                'auto_shutdown': 1,
                'auto_startup': 0,
                'overwrite': 1,
                'bkup_schedule': {
                    'sched_time_start': '',
                    'limit': 1,
                    'sched_day': '',
                    'sched_every': 1,
                    'sched_time': [],
                    'sched_gap_min': 0, },
                'bkup_policy': 1,
                'backup_type': 'i',
                'automate': 0,
                'tgt_uuid': '',
                'new_dc': '',
                'new_dc_mor': '',
                'new_host': '',
                'new_ds': '',
                'network_id': '',
                'network_name': '', },
            'common_params': {
                'batch_name': '',
                'rep_prefix': '',
                'rep_sufix': '',
                'variable_type': 1, },
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.batchCreateVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'batchCreateVpRep', body)

    def testModifyVpRepGroup(self):
        a = Auth(username, pwd)
        body = {
            'new_ds': '103-数据盘',
            'support_cbt': 1,
            'tgt_uuid': '7F16E670-1A61-D565-6905-9C68B9520907',
            'del_bkup_swap': 0,
            'src_uuid': '7F16E670-1A61-D565-6905-9C68B9520907',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'automate': 0,
            'rule_name': 'testMove1 cky',
            'new_dc': 'i2test',
            'bk_path': 'H:/vp_rep/',
            'backup_type': 'i',
            'new_host': '192.168.88.103',
            'quiet_snap': 1,
            'quick_back': 1,
            'del_bkup_data': 0,
            'lan_free': 23,
            'time_window': '',
            'new_dc_mor': 'datacenter-2',
            'bkup_policy': 0,
            'band_width': '-1',
            'rule_type': 1,
            'auto_shutdown': 1,
            'data_ip_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.modifyVpRepGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'modifyVpRepGroup', body)

    def testDescribeVpMove(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpMove(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpMove', body)

    def testModifyVpMove(self):
        a = Auth(username, pwd)
        body = {
            'new_ds': '',
            'support_cbt': 1,
            'tgt_uuid': '',
            'del_bkup_swap': 1,
            'src_uuid': '4C9beAfD-d55E-9Fee-e11A-3F76044eBadb',
            'bk_uuid': '',
            'automate': 1,
            'rule_name': '',
            'new_dc': '',
            'bk_path': '',
            'backup_type': '',
            'new_host': '',
            'quiet_snap': 1,
            'bkup_schedule': {},
            'quick_back': 1,
            'del_bkup_data': 1,
            'lan_free': 1,
            'vm_list': [],
            'time_window': '',
            'new_dc_mor': '',
            'bkup_policy': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.modifyVpMove(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'modifyVpMove', body)

    def testListVpMove(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'type': '',
            'status': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpMove', body)

    def testListVpMoveStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'force_refresh': 1,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpMoveStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpMoveStatus', body)

    def testStopVpMove(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rule_uuids': '1C89A121-6B03-24B2-9273-D4B93C0687AD',
            'snap_point': '',
            'op_code': '',
            'group_uuids': [],
            'power_on': 1,
            'power_off': 1,
            'bkup_type': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.stopVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'stopVpMove', body)

    def testDeleteVpMove(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'group_uuids': [],
            'delete_tgtvm': 1,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.deleteVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpMove', body)

    def testListVpRepPointList(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
            'all': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpRepPointList(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpRepPointList', body)

    def testListVpDrill(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpDrill', body)

    def testCreateVpDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 0,
            'vp_uuid': '',
            'auto': 0,
            'vm_list': [{
                'vm_name': '',
                'new_vm_name': '',
                'vm_ref': '99',
                'cpu': 1,
                'ver_sig': '',
                'core_per_sock': 1,
                'mem_mb': 1024,
                'scripts': '',
                'bk_uuid': '',
                'bk_path': '',
                'time': '',
                'original_rule_uuid': '',
                'scripts_type': 1,
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
                    'id': '', }, ],
                'networks': [{
                    'source_network_name': '',
                    'source_network_id': '',
                    'mac_address': '',
                    'keep_mac': '',
                    'network_id': '',
                    'network_name': '',
                    'ip_address': '',
                    'subnet_name': '',
                    'auto_ip': 1,
                    'ip': '',
                    'security_group_name': '', }, ], }, ],
            'quick_back': 1,
            'backup_type': 'i',
            'lan_free': 23,
            'del_bkup_data': 0,
            'automate': 0,
            'auto_shutdown': 1,
            'bkup_policy': 0,
            'bkup_schedule': {
                'sched_time_start': '0',
                'limit': 0,
                'sched_day': 6,
                'sched_every': 0,
                'sched_time': [],
                'sched_gap_min': 0, },
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.createVpDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpDrill', body)

    def testDescribeVpDrill(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpDrill(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpDrill', body)

    def testDeleteVpDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'group_uuids': [],
            'delete_tgtvm': 0,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.deleteVpDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpDrill', body)

    def testListVpDrillStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'force_refresh': 1,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpDrillStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpDrillStatus', body)

    def testGetConsoleUrl(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.getConsoleUrl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'getConsoleUrl', body)

    def testStopVpDrill(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'group_uuids': [],
            'status': '',
            'msg': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.stopVpDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'stopVpDrill', body)

    def testCreateVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'attach_dir': '',
            'config_addr': '',
            'config_port': '',
            'bk_uuid': '',
            'bk_path': '',
            'vm_name': '',
            'version_id': '',
            'tgt_uuid': '',
            'tgt_path': '',
            'files': [],
            'version_time': '',
            'bk_type': 0,
            'sto_uuid': '',
            'bucket': '',
            'bucket_path': '',
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.createVpFileRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpFileRecovery', body)

    def testModifyVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'rule_name': '',
            'config_addr': '',
            'config_port': '',
            'attach_dir': '',
            'bk_uuid': '',
            'bk_path': '',
            'vm_name': '',
            'version_id': '',
            'tgt_uuid': '',
            'random_str': '',
            'attach_path': '',
            'tgt_path': '',
            'files': [],
            'version_time': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.modifyVpFileRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'modifyVpFileRecovery', body)

    def testListVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpFileRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpFileRecovery', body)

    def testDescribeVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpFileRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpFileRecovery', body)

    def testAttachVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.attachVpFileRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'attachVpFileRecovery', body)

    def testListVpFileRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force_refresh': 1,
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpFileRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpFileRecoveryStatus', body)

    def testDeleteVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }

        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.deleteVpFileRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpFileRecovery', body)


if __name__ == '__main__':
    unittest.main()
