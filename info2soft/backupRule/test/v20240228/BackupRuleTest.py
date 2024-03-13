
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import BackupRule
from info2soft.backupRule.v20240228.BackupRule import BackupRule
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


class BackupRuleTestCase(unittest.TestCase):

    def testCreateBackup(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'biz_grp_list': [],
            'wk_data_type': 1,
            'timeout': 1,
            'priority': 1,
            'trans_mode': 1,
            'unit_uuid': '',
            'tape_pool_uuid': '',
            'client_list': [{
            'node_uuid': '',
            'init_main_client': 1,},],
            'wk_path': [],
            'excl_path': [],
            'mirr_file_check': 1,
            'mirr_sync_flag': '1',
            'mirr_open_type': 0,
            'mirr_sync_attr': 1,
            'ora_sid_name': '',
            'ora_home_path': '',
            'ora_content_type': 0,
            'rman_compress_df': 0,
            'rman_num_streams_df_max': 4,
            'rman_filespertset_df': 20,
            'rman_arch_retain': 3,
            'rman_include_arch_flag': 1,
            'rman_db_readonly': 0,
            'rman_del_arch': 1,
            'rman_filespertset_arch': 20,
            'rman_include_spfile_flag': 1,
            'rman_num_streams_arch': 4,
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
            'bkup_one_time': 1,
            'bkup_policy': 1,
            'exclude_days': [
            '2023-06-02',],
            'cron_policies': '',},],
            'replica_uuids': [],
            'thread_num_max': 1,
            'pre_backup_script': '',
            'post_backup_script': '',
            'script_timeout': 1,
            'expire_policy': 0,
            'thread_num_min': 1,
            'compress': 1,
            'compress_switch': 0,
            'encrypt_switch': 1,
            'encrypt': 1,
            'bk_file_crypt': 1,
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'band_width': '',
            'ora_pdbs_name': [],
            'retry_time': 5,
            'retry_num': 5,
            'rman_num_streams_df_min': 4,
            'disable': 1,
            'effective_time_switch': 1,
            'effective_time': 1,
            'hcs_uuid': '',
            'hcs_instance_uuid': '',
        }
        
        backupRule = BackupRule(a)
        r = backupRule.createBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'createBackup', body)

    def testModifyBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'biz_grp_list': [],
            'wk_data_type': 1,
            'timeout': 1,
            'priority': 1,
            'trans_mode': 1,
            'unit_uuid': '',
            'tape_pool_uuid': '',
            'client_list': [{
            'node_uuid': '',},],
            'wk_path': [],
            'excl_path': [],
            'mirr_file_check': 1,
            'mirr_sync_flag': '1',
            'mirr_open_type': 0,
            'mirr_sync_attr': 1,
            'ora_sid_name': '',
            'ora_home_path': '',
            'ora_content_type': 0,
            'rman_compress_df': 0,
            'rman_num_streams_df_max': 4,
            'rman_filespertset_df': 20,
            'rman_arch_retain': 3,
            'rman_include_arch_flag': 1,
            'rman_db_readonly': 0,
            'rman_del_arch': 1,
            'rman_filespertset_arch': 20,
            'rman_include_spfile_flag': 1,
            'rman_num_streams_arch': 4,
            'bkup_schedule': [{
            'sched_name': '',
            'backup_type': 1,
            'retention': 1,
            'start_window': [{
            'wday': '',
            'from': '',
            'to': '',},],
            'bkup_window': [{
            'wday': '',
            'from': '',
            'to': '',},],
            'bkup_one_time': 1,
            'bkup_policy': 1,
            'cron_type': 1,
            'exclude_days': [
            '2023-06-02',],
            'cron_policies': '',},],
            'replica_uuid': '',
            'thread_num_max': 1,
            'pre_backup_script': '',
            'post_backup_script': '',
            'script_timeout': 1,
            'expire_policy': 0,
            'thread_num_min': '',
            'compress': 1,
            'compress_switch': 0,
            'encrypt_switch': 1,
            'encrypt': 1,
            'secret_key': '',
            'bk_file_crypt': 1,
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'ukey_crypt_switch': 1,
            'ukey_cred_uuid': '',
            'band_width': '',
            'random_str': '',
            'rman_num_streams_df_min': 1,
            'disable': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        backupRule = BackupRule(a)
        r = backupRule.modifyBackupRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'modifyBackupRule', body)

    def testDescribeBackupRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        backupRule = BackupRule(a)
        r = backupRule.describeBackupRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'describeBackupRule', body)

    def testListBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_value': 'test',
            'search_field': 'task_name',
            'order_by': 'task_name',
            'direction': 'DESC',
            'filter_by_biz_grp': 1,
            'status': '',
            'node_name': '',
            'hostname': ''
        }
        
        backupRule = BackupRule(a)
        r = backupRule.listBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'listBackupRule', body)

    def testDeleteBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'client_list': [{
            'task_uuid': '',
            'node_uuid': [],},],
            'force': 0,
        }
        
        backupRule = BackupRule(a)
        r = backupRule.deleteBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'deleteBackupRule', body)

    def testenableBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
            'client_list': [{
            'task_uuid': '',
            'node_uuid': '',},],
            'sched_name': '',
            'new_task_name': '',
        }
        
        backupRule = BackupRule(a)
        r = backupRule.enableBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'enableBackupRule', body)

    def testdisableBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
            'client_list': [{
            'task_uuid': '',
            'node_uuid': '',},],
            'sched_name': '',
            'new_task_name': '',
        }

        backupRule = BackupRule(a)
        r = backupRule.disableBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'disableBackupRule', body)

    def testmanualStartBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
            'client_list': [{
            'task_uuid': '',
            'node_uuid': '',},],
            'sched_name': '',
            'new_task_name': '',
        }

        backupRule = BackupRule(a)
        r = backupRule.manualStartBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'manualStartBackupRule', body)

    def testcloneBackupRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
            'client_list': [{
            'task_uuid': '',
            'node_uuid': '',},],
            'sched_name': '',
            'new_task_name': '',
        }

        backupRule = BackupRule(a)
        r = backupRule.cloneBackupRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'cloneBackupRule', body)

    def testGetNextTaskName(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
        }
        
        backupRule = BackupRule(a)
        r = backupRule.getNextTaskName(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'getNextTaskName', body)

    def testListBackupRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
        }
        
        backupRule = BackupRule(a)
        r = backupRule.listBackupRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupRule', 'listBackupRuleStatus', body)


if __name__ == '__main__':
    unittest.main()
