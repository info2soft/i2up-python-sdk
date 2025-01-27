
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import VpBackupRule
from info2soft.vpBackupRule.v20250123.VpBackupRule import VpBackupRule
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


class VpBackupRuleTestCase(unittest.TestCase):

    def testCreateVpBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'biz_grp_list': [],
            'unit_uuid': '',
            'replica_uuids': [],
            'vp_uuid': '',
            'auto_discovery': 0,
            'match_policy': {
            'vm_name': [{
            'type': '',
            'value': '',
            'label': '',
            'and': False,},],
            'location': [{
            'type': '',
            'value': '',
            'label': '',
            'and': False,},],
            'folder': [{
            'type': '',
            'value': '',
            'label': '',
            'and': False,},],},
            'vm_list': [{
            'vm_name': '',
            'vm_ref': '',
            'disk_list': [{
            'id': '',
            'disk_dir': '',
            'disk_name': '',
            'size': '',
            'datastore': '',
            'is_ignored': 1,
            'datastore_type': '',},],
            'new_vm_name': '',
            'scripts_type': 1,
            'scripts': '',
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'os_type': 1,
            'is_set': False,
            'vm_uuid': '',
            'priority': 1,},],
            'quiet_snap': 1,
            'instant_recovery': 1,
            'consolidate_switch': 1,
            'consolidate_disks_time': '01:02',
            'src_trans_mode': 31,
            'concurrent_disk_threads': 2,
            'fail_retry': 0,
            'retry_times': 0,
            'retry_interval': 0,
            'bkup_schedule': [{
            'sched_name': '',
            'backup_type': 1,
            'retention': 1,
            'start_window': [{
            'wday': 1,
            'from': '',
            'to': '',},],
            'bkup_window': [{
            'wday': 1,
            'from': '',
            'to': '',},],
            'bkup_policy': 1,
            'bkup_one_time': 1,
            'cron_policies': '',
            'exclude_days': [],},],
            'effective_time_switch': 1,
            'effective_time': 1,
            'compress_switch': 1,
            'compress': 1,
            'bk_file_crypt': 1,
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'bk_file_compress_switch': 1,
            'bk_file_compress': 1,
            'band_width': '',
            'add_drill': 1,
            'drill_plat_uuid': '',
            'timeout': 1,
            'disable': 1,
            'priority': 1,
            'tape_pool_uuid': '',
            'is_fusion_storage': '',
            'quick_back': 1,
            'data_verify': 1,
            'source_region_id': '',
            'source_project_id': '',
            'winstack_pool_id': '',
            'winstack_host_id': '',
            'trans_type': '',
            'cred_uuid': '',
            'ftp_path': '',
            'agent_uuid': '',
            'trans_port': 1,
            'encrypt_switch': 0,
            'trans_mode': 1,
            'encrypt': 1,
            'source_region_name': '',
            'source_project_name': '',
            'block_stor_format': 1,
            'data_encrypt_compress_switch': '',
            'data_encrypt_compress_thread_num': '',
            'data_encrypt_source': '',
            'data_compress_level': '',
            'data_encrypt_type': '',
            'thread_num_max': 1,
            'thread_num_min': 1,
        }
        
        
        vpBackupRule = VpBackupRule(a)
        r = vpBackupRule.createVpBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpBackupRule', 'createVpBackupRule', body)

    def testModifyVpBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'biz_grp_list': [],
            'unit_uuid': '',
            'replica_uuids': [],
            'vp_uuid': '',
            'auto_discovery': 0,
            'match_policy': {
            'vm_name': [{
            'type': '',
            'value': '',
            'label': '',
            'and': False,},],
            'location': [{
            'type': '',
            'value': '',
            'label': '',
            'and': False,},],
            'folder': [{
            'type': '',
            'value': '',
            'label': '',
            'and': False,},],},
            'vm_list': [{
            'vm_name': '',
            'vm_ref': '',
            'disk_list': [{
            'id': '',
            'disk_dir': '',
            'disk_name': '',
            'size': '',
            'datastore': '',
            'is_ignored': 1,
            'datastore_type': '',},],
            'new_vm_name': '',
            'scripts_type': 1,
            'scripts': '',
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'os_type': 1,
            'is_set': 1,
            'vm_uuid': '',
            'priority': 1,},],
            'quiet_snap': 1,
            'instant_recovery': 1,
            'consolidate_switch': 1,
            'consolidate_disks_time': '01:02',
            'src_trans_mode': 31,
            'concurrent_disk_threads': 2,
            'fail_retry': 0,
            'retry_times': 0,
            'retry_interval': 0,
            'bkup_schedule': [{
            'sched_name': '',
            'backup_type': 1,
            'retention': 1,
            'start_window': [{
            'wday': 1,
            'from': '',
            'to': '',},],
            'bkup_window': [{
            'wday': 1,
            'from': '',
            'to': '',},],
            'bkup_policy': 1,
            'bkup_one_time': 1,
            'cron_policies': '',
            'exclude_days': [],},],
            'effective_time_switch': 1,
            'effective_time': 1,
            'compress_switch': 1,
            'compress': 1,
            'bk_file_crypt': 1,
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'bk_file_compress_switch': 1,
            'bk_file_compress': 1,
            'band_width': '',
            'add_drill': '',
            'drill_plat_uuid': '',
            'random_str': '',
            'timeout': 1,
            'priority': 1,
            'disable': 1,
            'tape_pool_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        vpBackupRule = VpBackupRule(a)
        r = vpBackupRule.modifyVpBackupRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpBackupRule', 'modifyVpBackupRule', body)

    def testListVpBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'vm_name': '',
            'status': '',
            'filter_by_biz_grp': 0,
            'where_args': {
            'task_uuid': '',
            'vp_type': 1,},
            'like_args': {
            'task_name': '',
            'unit_name': '',
            'vp_name': '',},
        }
        
        
        vpBackupRule = VpBackupRule(a)
        r = vpBackupRule.listVpBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpBackupRule', 'listVpBackupRule', body)

    def testDescribeVpBackupRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        vpBackupRule = VpBackupRule(a)
        r = vpBackupRule.describeVpBackupRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpBackupRule', 'describeVpBackupRule', body)

    def testDeleteVpBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'force': 0,
            'vm_list': [{
            'task_uuid': '',
            'vm_ref': '',},],
        }
        
        
        vpBackupRule = VpBackupRule(a)
        r = vpBackupRule.deleteVpBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpBackupRule', 'deleteVpBackupRule', body)

    def testOperateVpBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
            'vm_list': [],
            'sched_name': '',
            'new_task_name': '',
        }
        
        
        vpBackupRule = VpBackupRule(a)
        r = vpBackupRule.operateVpBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpBackupRule', 'operateVpBackupRule', body)

    def testListVpBackupRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
        }
        
        
        vpBackupRule = VpBackupRule(a)
        r = vpBackupRule.listVpBackupRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpBackupRule', 'listVpBackupRuleStatus', body)

    def testTaskAddVms(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': '',
            'vm_refs': [],
        }
        
        
        vpBackupRule = VpBackupRule(a)
        r = vpBackupRule.taskAddVms(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VpBackupRule', 'taskAddVms', body)


if __name__ == '__main__':
    unittest.main()
