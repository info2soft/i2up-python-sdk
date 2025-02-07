
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import TimingBackup
from info2soft.timing.v20250123.TimingBackup import TimingBackup
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


class TimingBackupTestCase(unittest.TestCase):

    def testDescribeTimingBackupMssqlSource(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '22D03E06-94D0-5E2C-336E-4BEEC2D28EC4',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.describeTimingBackupMssqlSource(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeTimingBackupMssqlSource', body)

    def testVerifyTimingBackupOracleInfo(self):
        a = Auth(username, pwd)
        body = {
            'oracle_settings': {
            'ora_sid_name': '',
            'ora_port': 1,
            'ora_home_path': '',
            'ora_passwd': 'Info1234',},
            'wk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.verifyTimingBackupOracleInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'verifyTimingBackupOracleInfo', body)

    def testDescribeTimingBackupOracleContent(self):
        a = Auth(username, pwd)
        body = {
            'oracle_settings': {
            'ora_passwd': 'Info1234',
            'ora_port': 1,
            'ora_sid_name': '',
            'ora_content_type': 0,},
            'wk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.describeTimingBackupOracleContent(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeTimingBackupOracleContent', body)

    def testDescibeTimingBackupOracleSriptPath(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.descibeTimingBackupOracleSriptPath(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'descibeTimingBackupOracleSriptPath', body)

    def testListTimingBackupMssqlDbList(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'mssql_settings': {
            'win_verify': 0,
            'instance_name': 'MSSQLSERVER',
            'pass_word': '123456',
            'data_source': 'WIN-EGKN86NF3PM',
            'user_id': 'sa',
            'port': '',
            'protocol': 1,},
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingBackupMssqlDbList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingBackupMssqlDbList', body)

    def testVerifyTimingBackupOracleLogin(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
            'oracle_settings': {
            'ora_sid_name': '',
            'ora_login_name': '',
            'ora_login_pwd': '',
            'ora_server_name': '',
            'ora_server_port': '',},
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.verifyTimingBackupOracleLogin(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'verifyTimingBackupOracleLogin', body)

    def testCreateTimingBackup(self):
        a = Auth(username, pwd)
        body = {
            'timing_backup': {
            'mirr_sync_attr': 1,
            'secret_key': '',
            'oracle_settings': {
            'ora_sid_name': '',
            'ora_content_type': 0,
            'ora_use_script': 0,
            'ora_port': 1,
            'ora_script_path': '',
            'ora_passwd': 'Info1234',
            'ora_home_path': '',
            'ora_pdbs_name': '',
            'ora_login_name': '',
            'ora_login_pwd': '',
            'ora_server_name': '',
            'ora_server_port': '',
            'pool_uuid': '',
            'volume_uuid': '',
            'volume_name': '',
            'attach_point': '',
            'pool_name': '',
            'ora_tab_mode': 1,
            'ora_tab_pdb_name': '',
            'ora_tab_names': [{
            'user': '',
            'ori_table': '',
            'tgt_table': '',},],
            'ora_tab_aux_path': '',
            'ora_tab_rctype': 1,
            'ora_tab_time': '',
            'ora_tab_scn': '',
            'ora_tab_log': '',
            'log_ccopy': 1,
            'log_volume_uuid': '',
            'log_mount_point': '',},
            'wk_data_type': 1,
            'task_name': 'testTiming',
            'backup_type': 0,
            'del_policy': 0,
            'mirr_sync_flag': 0,
            'snap_type': 0,
            'oracle_rman_settings': {
            'rman_skip_offline': 0,
            'rman_num_streams_arch': 20,
            'rman_del_arch': 1,
            'rman_include_arch_flag': 1,
            'rman_num_streams_df': 1,
            'rman_filespertset_arch': 20,
            'rman_maxsetsize_df': 0,
            'rman_set_limit_arch_flag': 0,
            'rman_skip_readonly': 0,
            'rman_maxsetsize_arch': 0,
            'rman_cold_bkup': 0,
            'rman_filespertset_df': 20,
            'rman_db_readonly': 0,
            'rman_compress_df': 1,
            'rman_include_spfile_flag': 1,
            'rman_arch_retain': 3,},
            'compress': 0,
            'encrypt_switch': 0,
            'wk_path': [
            'E:\\test\\',],
            'excl_path': [],
            'bk_data_type': 1,
            'mirr_blk_size': 0,
            'bk_path': [
            'E:\\t\\',],
            'blk_direct_copy': 0,
            'mirr_open_type': 0,
            'mssql_settings': {
            'instance_name': 'MSSQLSERVER',
            'time_out': '',
            'data_source': '',
            'win_verify': 1,
            'user_id': '',
            'pass_word': '',
            'port': '',
            'protocol': 1,
            'db_info': [],
            'lanfree': 1,
            'volume_uuid': '',
            'mount_point': '',},
            'wk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'bkup_policy': 2,
            'bkup_window': {
            'sched_time_start': '00:00',
            'sched_time_end': '00:00',},
            'bkup_one_time': 1547538235,
            'bkup_schedule': [{
            'limit': 22,
            'sched_day': 5,
            'sched_every': 2,
            'sched_time': '22:44',
            'sched_gap_min': 39,
            'backup_type': 1,},],
            'task_type': 0,
            'file_check_dir': '',
            'random_str': '11111111-1111-1111-1111-111111111111',
            'file_check_switch': 0,
            'timing_type': 1,
            'data_ip_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'bk_file_crypt': 0,
            'mirr_file_check': 0,
            'mysql_settings': {
            'pool_uuid': '',
            'pool_name': '',
            'volume_uuid': '',
            'volume_name': '',
            'attach_point': '',
            'mysql_port': '',
            'mysql_user': '',
            'mysql_passwd': '',
            'time_out': 1,
            'mysql_path': '',
            'log_ccopy': 1,
            'log_volume_uuid': '',
            'log_mount_point': '',
            'log_volume_name': '',
            'data_dir': '',
            'config_path': '/etc/my.cnf',
            'lanfree': 1,
            'mysql_host': '127.0.0.1',
            'backup_mode': 0,
            'tables': [],},
            'tape_uuid': 'E8566905-411E-B2CD-A742-77B1346D8E84',
            'archive_pen': 0,
            'library_sn': 'SYZZY_A',
            'content_type': 1,
            'db_name': '',
            'tables': '',
            'bk_crypt_key': '',
            'bk_crypt_type': 1,
            'informix_settings': {
            'oper_user': '',
            'is_ori_machine': 1,
            'config_recover': 1,
            'informix_instance': {
            'is_default': 1,
            'install_dir': '',
            'instance_name': '',
            'onconfig_name': '',},
            'verify_only': 1,},
            'encrypt': 1,
            'thread_num': 0,
            'dm_settings': {
            'dm_home': '',
            'host': '',
            'port': '',
            'user': '',
            'password': '',
            'content_type': 1,
            'is_bk_arch': 1,
            'is_del_arch': 1,
            'specify_time': '',
            'time_type': 1,
            'since_time': '',
            'since_lsn': '',
            'compress': 0,
            'compress_switch': 0,
            'encrypt_switch': 0,
            'encrypt_type': 1,
            'encrypt_password': '',
            'encrypt_algorithm': '',
            'parallel_num': 4,
            'thread_num': 4,
            'block_size': 1,
            'parallel_switch': 0,
            'block_unit': '',
            'table_space': '',
            'table_name': '',
            'schema_name': '',
            'system_user': '',},
            'timeout': '',
            'db2_settings': {
            'db2_user': '',
            'db2_group': '',
            'db_info': [{
            'db_name': '',},],},
            'synthetic_bkup_settings': {
            'pool_uuid': '',
            'pool_name': '',
            'volume_uuid': '',
            'volume_name': '',
            'lanfree': '',},
            'pre_backup_script': '',
            'post_backup_script': '',
            'script_timeout': 1,
            'retry_time': 5,
            'retry_num': 5,
            'obs_settings': {
            'sto_uuid': '',
            'bucket_name': '',
            'bucket_path': '',},
            'bk_storage': 1,
            'inc_type': 1,
            'tape_pool_uuid': '',
            'tape_name': '',
            'tape_reserve': 1,
            'tape_pool_name': '',
            'gsdbt_settings': {
            'gsdbt_home': '',
            'oper_user': '',
            'user': '',
            'password': '',
            'port': '',},
            'ukey_crypt_switch': 1,
            'ukey_cred_uuid': '',
            'dedupe_uuid': '',
            'storage_pool_uuid': '',
            'goldendb_settings': {
            'manager_user_name': '',
            'manager_user_home_dir': '',
            'tenant_name': '',
            'db_user_name': '',
            'db_user_passwd': '',},
            'custom_type': 1,
            'kingbasees_settings': {
            'kes_bin': '',
            'kes_data': '',
            'oper_user': '',
            'user': '',
            'password': '',
            'port': '54321',},
            'proxy_uuid': '',},
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.createTimingBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'createTimingBackup', body)

    def testDescribeTimingBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        timingBackup = TimingBackup(a)
        r = timingBackup.describeTimingBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeTimingBackup', body)

    def testModifyTimingBackup(self):
        a = Auth(username, pwd)
        body = {
            'timing_backup': {
            'mirr_sync_attr': 1,
            'secret_key': '',
            'oracle_settings': {
            'ora_sid_name': '',
            'ora_content_type': 0,
            'ora_use_script': 0,
            'ora_port': 1,
            'ora_script_path': '',
            'ora_passwd': 'Info1234',
            'ora_home_path': '',},
            'policy_uuid': '38FFA6E2-2A40-31D6-7A94-E8168EBA9FF1',
            'wk_data_type': 0,
            'task_name': '',
            'backup_type': 1,
            'del_policy': 0,
            'mirr_sync_flag': 0,
            'snap_type': 0,
            'oracle_rman_settings': {
            'rman_skip_offline': 0,
            'rman_num_streams_arch': 1,
            'rman_del_arch': 1,
            'rman_include_arch_flag': 1,
            'rman_num_streams_df': 1,
            'rman_filespertset_arch': 20,
            'rman_maxsetsize_df': 0,
            'rman_set_limit_arch_flag': 0,
            'rman_skip_readonly': 0,
            'rman_maxsetsize_arch': 0,
            'rman_cold_bkup': 0,
            'rman_filespertset_df': 20,},
            'compress': 0,
            'encrypt_switch': 0,
            'wk_path': [],
            'excl_path': [],
            'bk_data_type': 1,
            'mirr_blk_size': 0,
            'bk_path': [],
            'blk_direct_copy': 0,
            'mirr_open_type': 0,
            'mssql_settings': {
            'instance_name': '',
            'time_out': '2',
            'data_source': '',
            'dbsize': '',
            'win_verify': 0,
            'user_id': '',
            'db_info': [{
            'db_name': '',},],
            'pass_word': '',},
            'wk_uuid': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
            'bk_uuid': 'Jane',
            'bkup_policy': 0,
            'bkup_window': {
            'sched_time_start': '15:18',
            'sched_time_end': '14:37',},
            'bkup_one_time': 1515568566,
            'bkup_schedule': [{
            'limit': 25,
            'sched_day': 24,
            'sched_every': 2,
            'sched_time': '04:07',
            'sched_gap_min': 49,},],
            'task_type': 0,
            'random_str': '11111111-1111-1111-1111-111111111111',
            'data_ip_uuid': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
            'db2_settings': {
            'db2_user': '',
            'db2_group': '',
            'db_info': [{
            'db_name': '',
            'task_uuid': '',
            'task_name': '',},],},
            'bk_storage': '',
            'dedupe_uuid': '',},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        timingBackup = TimingBackup(a)
        r = timingBackup.modifyTimingBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'modifyTimingBackup', body)

    def testListTimingBackup(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'limit': 10,
            'page': 1,
            'search_value': '',
            'type': 0,
            'status': '',
            'where_args': {
            'timing_type': 1,},
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingBackup', body)

    def testListTimingBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingBackupStatus', body)

    def testDeleteTimingBackup(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'del_policy': 1,
            'force': 1,
            'recycle': 0,
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.deleteTimingBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'deleteTimingBackup', body)

    def testStartTimingBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'bk_type': 1,
            'new_task_name': '',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.startTimingBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'startTimingBackup', body)

    def testStopTimingBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'bk_type': 1,
            'new_task_name': '',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.stopTimingBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'stopTimingBackup', body)

    def testStartImmediateTimingBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'bk_type': 1,
            'new_task_name': '',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.startImmediateTimingBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'startImmediateTimingBackup', body)

    def testShowTimingBackupDetailInfo(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': '',
            'timing_type': 3,
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.showTimingBackupDetailInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'showTimingBackupDetailInfo', body)

    def testDescibeDmDbInfo(self):
        a = Auth(username, pwd)
        body = {
            'dm_home': '',
            'host': '',
            'port': '',
            'user': '',
            'password': '',
            'type': 1,
            'schema_name': '',
            'node_uuid': '',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.descibeDmDbInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'descibeDmDbInfo', body)

    def testListGaussDBDatabaseTables(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'content_type': 1,
            'page_no': '',
            'page_size': '',
            'top_dir': '',
            'sec_dir': '',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listGaussDBDatabaseTables(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listGaussDBDatabaseTables', body)

    def testListTimingBackupPoint(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': '',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingBackupPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingBackupPoint', body)

    def testDeleteTimingBackupPoint(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': '',
            'time_point': '',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.deleteTimingBackupPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'deleteTimingBackupPoint', body)

    def testListBakVer(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': '',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listBakVer(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listBakVer', body)

    def testBakDataArchive(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': '',
            'list': [{
            'time': '',
            'size': '',
            'data_type': '',
            'list_map': [],},],
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.bakDataArchive(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'bakDataArchive', body)

    def testDescribeGoldebDBInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'is_backup': '',
            'backup_task_uuid': '',
            'tenant_name': '',
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.describeGoldebDBInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeGoldebDBInfo', body)

    def testVerifyGoldebDB(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'bak_dir': '',
            'golden_db_opt': {
            'manager_user_name': '',
            'manager_user_home_dir': '',
            'tenant_name': '',
            'db_user_name': '',
            'db_user_passwd': '',},
            'is_backup': 1,
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.verifyGoldebDB(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'verifyGoldebDB', body)

    def testListCustomTypes(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listCustomTypes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listCustomTypes', body)

    def testListTimingWork(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_field': '',
            'search_value': '',
            'where_args': {
            'task_uuid': '',},
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingWork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingWork', body)

    def testDeleteTimingWork(self):
        a = Auth(username, pwd)
        body = {
            'work_uuids': [],
        }
        
        
        timingBackup = TimingBackup(a)
        r = timingBackup.deleteTimingWork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'deleteTimingWork', body)


if __name__ == '__main__':
    unittest.main()
