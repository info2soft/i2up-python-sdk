
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.timing.v20240228.TimingBackup import TimingBackup
# from info2soft.timing.v20200722.TimingBackup import TimingBackup
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
            'ora_tab_log': '',},
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
            'E:/test/',],
            'excl_path': [],
            'bk_data_type': 1,
            'mirr_blk_size': 0,
            'bk_path': [
            'E:/t/',],
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
            'limit': 13,
            'sched_day': 23,
            'sched_every': 2,
            'sched_time': '07:15',
            'sched_gap_min': 24,
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
            'schema_name': '',},
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
            'db_user_passwd': '',},},
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
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.startTimingBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'startTimingBackup', body)

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
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listGaussDBDatabaseTables(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listGaussDBDatabaseTables', body)

    def testListTimingRecoveryMssqlTime(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_data_path': 'E://mssqlBK//ts-11111111-1111-1111-1111-111111111111//',
            'bk_storage': 1,
            'tape_pool_uuid': '',
            'tape_name': '',
            'library_sn': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingRecoveryMssqlTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingRecoveryMssqlTime', body)

    def testDescribeTimingRecoveryMssqlInitInfo(self):
        a = Auth(username, pwd)
        body = {
            'rc_point_in_time': '2017-12-21_13-16-53',
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_data_path': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.describeTimingRecoveryMssqlInitInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeTimingRecoveryMssqlInitInfo', body)

    def testListTimingRecoveryPathList(self):
        a = Auth(username, pwd)
        body = {
            'rc_data_path': 'C://back//',
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'backup_task_uuid': '11111111-1111-1111-1111-111111111111',
            'volume_uuid': '',
            'bk_storage': '',
            'tape_pool_uuid': '',
            'tape_name': '',
            'library_sn': '',
            'dedupe_uuid': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingRecoveryPathList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingRecoveryPathList', body)

    def testVerifyTimingRecoveryMssqlInfo(self):
        a = Auth(username, pwd)
        body = {
            'mssql_settings': {
            'win_verify': 0,
            'pass_word': '123456',
            'instance_name': 'MSSQLSERVER',
            'user_id': 'sa',
            'data_source': '',
            'port': '',
            'protocol': 1,},
            'wk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.verifyTimingRecoveryMssqlInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'verifyTimingRecoveryMssqlInfo', body)

    def testListTimingRecoveryOracleRcPointInfo(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'bk_uuid': '',
            'bk_path': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingRecoveryOracleRcPointInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingRecoveryOracleRcPointInfo', body)

    def testDescribeRcMysqlInfo(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_data_path': 'E://mssqlBK//ts-11111111-1111-1111-1111-111111111111//',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.describeRcMysqlInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeRcMysqlInfo', body)

    def testListSbtContrlFile(self):
        a = Auth(username, pwd)
        body = {
            'rc_data_path': '',
            'ora_content_type': 1,
            'bk_uuid': '',
            'bk_storage': '',
            'tape_pool_uuid': '',
            'tape_name': '',
            'library_sn': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listSbtContrlFile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listSbtContrlFile', body)

    def testDescribeSbtDbid(self):
        a = Auth(username, pwd)
        body = {
            'file_name': '',
            'bk_uuid': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.describeSbtDbid(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeSbtDbid', body)

    def testCreateTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'timing_recovery': {
            'bk_path': [
            'E:/t/2019-01-15_15-49-00/E/test/',],
            'bk_data_type': 1,
            'wk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'backup_type': 0,
            'backup_task_uuid': '',
            'wk_data_type': 1,
            'oracle_settings': {
            'ora_rst_limit_scn': 0,
            'ora_rc_point_scn': 0,
            'ora_rst_limit_thread': 1,
            'ora_rc_point_log_seq': '',
            'ora_rst_limit_date': '2017-12-21 13:26:00',
            'ora_rst_limit_type': 0,
            'ora_home_path': '',
            'ora_rc_point_type': 0,
            'ora_passwd': 'Info1234',
            'ora_port': 1,
            'ora_rc_point_date': '2017-12-21 13:26:00',
            'ora_do_restore': 0,
            'ora_rst_limit_log_seq': '',
            'ora_content_type': 0,
            'ora_rc_point_thread': 1,
            'ora_sid_name': '',
            'ora_do_recovery': 0,
            'ora_rc_type': 0,
            'ora_rst_type': 0,
            'ora_pdbs_name': '',
            'ora_rst_arch_limit_type': 1,
            'ora_rst_arch_limit_log_seq': 1,
            'ora_dbid': '',
            'ora_rst_ctrl_name': '',
            'ora_rst_spfile_path': '',
            'ora_rst_spfile_name': '',
            'ora_rst_record': {},
            'ora_rc_record': {},
            'ora_rst_recory_point': 1,
            'ora_rc_recory_point': 1,
            'ora_login_pwd': '',
            'ora_login_name': '',
            'snapshot_time': '',
            'snapshot_name': '',
            'rst_control': 1,
            'ora_tab_mode': 0,
            'ora_tab_pdb_name': '',
            'ora_tab_names': [{
            'user': '',
            'ori_table': '',
            'tgt_table': '',},],
            'ora_tab_aux_path': '',
            'ora_open_mode': 0,
            'ora_rst_endarch_limit_log_seq': 1,},
            'task_name': 'task',
            'rc_data_path': 'E://t//',
            'mssql_settings': {
            'pass_word': '',
            'instance_name': '',
            'win_verify': 0,
            'user_id': '',
            'time_out': '',
            'data_source': '',
            'port': '',
            'protocol': 1,
            'db_info': [{
            'src_db_name': '',
            'new_db_name': '',
            'lgc_infos': [{
            'lgc_name': 'test',
            'lgc_path': 'C:/Program Files/Microsoft SQL Server/MSSQL12.MSSQLSERVER/MSSQL/DATA/test.mdf',},],
            'check_out': '0',
            'db_size': '',
            'tab_num': '',
            'tab_info': '',
            'ln_num': '',
            'db_file_save_path': '',
            'rc_point_in_time': '2019-01-15_15-49-00',
            'db_name': '',
            'ldf_name': '',
            'mdf_name': '',},],
            'lanfree': 0,
            'volume_uuid': '',
            'mount_point': '',
            'data_fetch': 0,
            'rep_dir': '',},
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_style': 1,
            'wk_path': [
            'E:/test/',],
            'rc_point_in_time': '2019-01-15_15-49-00',
            'db2_settings': {
            'log_file_dir': '',
            'db_info': [{
            'new_db_name': '',
            'db_path': '',
            'rc_point_in_time': '',
            'db_name': '',},],
            'db2_user': '',
            'db2_group': '',},
            'excl_path': [],
            'blk_direct_copy': 1,
            'compress': '',
            'encrypt_switch': '',
            'secret_key': '',
            'data_ip_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'mysql_settings': {
            'pool_uuid': '',
            'pool_name': '',
            'volume_uuid': '',
            'volume_name': '',
            'attach_point': '',
            'mysql_port': '',
            'mysql_user': '',
            'mysql_passwd': '',
            'snapshot_time': '',
            'mysql_rc_type': 1,
            'mysql_rc_time': '',
            'time_out': 1,
            'mysql_path': '',
            'snapshot_name': '',
            'log_ccopy': 1,
            'log_volume_uuid': '',
            'log_mount_point': '',
            'data_dir': '',
            'lanfree': 1,
            'mysql_host': '127.0.0.1',
            'mysql_startup_instance': 1,
            'backup_mode': 0,
            'tables': [],},
            'oracle_rman_settings': {
            'rman_num_streams_df': 1,},
            'synthetic_bkup_settings': {
            'mount_dir': '',
            'storage': {},
            'volume_uuid': 'BE54F165-107C-4435-18E0-0D6471A87FDE',
            'rc_dir': '',},
            'db_name': '',
            'content_type': 0,
            'tables': '',
            'res_by_path': '',
            'informix_settings': {
            'oper_user': '',
            'is_ori_machine': 1,},
            'thread_num': 1,
            'protocol': '',
            'fc_initiator_wwpn': '',
            'fc_target_wwpn': '',
            'data_return': 0,
            'data_dir': '',
            'dm_settings': {
            'dm_home': '',
            'host': '',
            'port': 1,
            'user': '',
            'password': '',
            'is_create': '',
            'ini_path': '',
            'intance_name': '',
            'db_name': '',
            'data_dir': '',
            'content_type': '',
            'bk_type': 1,
            'restore_switch': 1,
            'recover_switch': 1,
            'is_restore_resent': 1,
            'rt_point': '',
            'is_restore_arch': '',
            'arch_type': 1,
            'restore_time_type': 1,
            'restore_until_time': '',
            'restore_until_lsn': '',
            'is_rt_arch_to_dir': 1,
            'table_space': '',
            'arch_dir': '',
            'table_name': '',
            'schema_name': '',
            'arch_from': 0,
            'is_force': 0,
            'log_dirs': [],
            'magic_num': '',
            'recover_time_type': 0,
            'recover_until_time': '',
            'recover_until_lsn': '',
            'encrypt_switch': 1,
            'encrypt_password': '',
            'encrypt_algorithm': '',
            'thread_num': 4,
            'is_index': 0,
            'is_constraint': 1,
            'is_table_struct': 0,
            'is_table_data': 1,
            'system_user': '',},
            'rc_path_policy': 0,
            'bk_storage': 1,
            'obs_settings': {},
            'storage_uuid': '',
            'storage_pool_uuid': '',
            'is_remote_rc': 0,
            'gsdbt_settings': {
            'gsdbt_home': '',
            'oper_user': '',
            'user': '',
            'password': '',
            'port': '',},
            'bk_crypt_type': '',
            'bk_file_crypt': '',
            'bk_crypt_key': '',
            'tape_uuid': '',
            'tape_pool_uuid': '',
            'tape_pool_name': '',
            'tape_name': '',
            'library_sn': '',
            'ukey_crypt_switch': 1,
            'ukey_cred_uuid': '',
            'dedupe_uuid': '',
            'rc_method': 1,
            'select_data_path': '',
            'pre_recover_script': '',
            'post_recover_script': '',
            'goldendb_settings': {
            'manager_user_name': '',
            'manager_user_home_dir': '',
            'tenant_name': '',
            'db_user_name': '',
            'db_user_passwd': '',
            'custom_rc_point': '',
            'resultset_datetime': '',},},
            'force': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.createTimingRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'createTimingRecovery', body)

    def testModifyTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'timing_recovery': {
            'wk_uuid': '7AD64D7A-7D1D-AC51-5DF1-29A58345A288',
            'task_name': 'task',
            'random_str': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
            'wk_path': [],
            'bk_data_type': 1,
            'bk_path': [],
            'backup_type': 0,
            'oracle_settings': {
            'ora_rc_point_thread': 1,
            'ora_rc_point_date': '2017-12-21 13:26:00',
            'ora_passwd': 'Info1234',
            'ora_port': 1,
            'ora_rc_point_type': 0,
            'ora_do_recovery': 0,
            'ora_do_restore': 0,
            'ora_home_path': '',
            'ora_rst_type': 0,
            'ora_rst_limit_type': 0,
            'ora_sid_name': '',
            'ora_rst_limit_thread': 1,
            'ora_rst_limit_date': '2017-12-21 13:26:00',
            'ora_content_type': 0,
            'ora_rst_limit_log_seq': '',
            'ora_rst_limit_scn': 0,
            'ora_rc_type': 0,
            'ora_rc_point_log_seq': '',
            'ora_rc_point_scn': 0,},
            'bk_uuid': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
            'task_uuid': '7AD64D7A-7D1D-AC51-5DF1-29A58345A288',
            'backup_task_uuid': '',
            'mssql_settings': {
            'win_verify': 0,
            'mdf_name': '',
            'src_db_name': '',
            'user_id': '',
            'ldf_name': '',
            'ldf_path': '',
            'instance_name': '',
            'pass_word': '',
            'db_file_save_path': '',
            'mdf_path': '',
            'new_db_name': '',},
            'rc_data_path': 'C://back//',
            'rc_style': 1,
            'wk_data_type': 0,
            'rc_point_in_time': '2017-12-21_13-16-53',
            'db2_settings': {
            'db2_user': '',
            'db2_group': '',
            'log_file_dir': '',
            'db_info': [{
            'db_name': '',
            'new_db_name': '',
            'db_path': '',
            'rc_point_in_time': '',
            'task_uuid': '',
            'task_name': '',},],},
            'excl_path': [],
            'data_ip_uuid': '7AD64D7A-7D1D-AC51-5DF1-29A58345A288',
            'res_by_path': '',
            'data_dir': '',
            'data_return': 0,
            'rc_path_policy': 0,
            'bk_storage': '',
            'dedupe_uuid': '',},
            'force': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        timingBackup = TimingBackup(a)
        r = timingBackup.modifyTimingRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'modifyTimingRecovery', body)

    def testDescribeTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        timingBackup = TimingBackup(a)
        r = timingBackup.describeTimingRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeTimingRecovery', body)

    def testListTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'page': 1,
            'limit': 1,
            'search_field': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingRecovery', body)

    def testDeleteTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force': 1,
            'del_clone': 0,
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.deleteTimingRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'deleteTimingRecovery', body)

    def testListTimingRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingRecoveryStatus', body)

    def testStartTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'operate': 'start',
            'force': 1,
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.startTimingRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'startTimingRecovery', body)

    def testDescribeGroupTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        timingBackup = TimingBackup(a)
        r = timingBackup.describeGroupTimingRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeGroupTimingRecovery', body)

    def testTimingRecoveryCheckDir(self):
        a = Auth(username, pwd)
        body = {
            'check_type': 1,
            'file_dir': [],
            'node_uuid': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.timingRecoveryCheckDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'timingRecoveryCheckDir', body)

    def testListTimingRecoveryDbInfo(self):
        a = Auth(username, pwd)
        body = {
            'rc_data_path': '',
            'bk_uuid': '',
            'wk_data_type': '4',
            'bk_storage': 1,
            'tape_uuid': '',
            'tape_pool_uuid': '',
            'tape_name': '',
            'library_sn': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingRecoveryDbInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingRecoveryDbInfo', body)

    def testListTimingRecoveryDb2Time(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_data_path': 'E://mssqlBK//ts-11111111-1111-1111-1111-111111111111//',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingRecoveryDb2Time(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingRecoveryDb2Time', body)

    def testListTimingRecoveryGaussTime(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'bk_path': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listTimingRecoveryGaussTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingRecoveryGaussTime', body)

    def testDescribeTimingRecoveryDmBackupInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'bk_path': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.describeTimingRecoveryDmBackupInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'describeTimingRecoveryDmBackupInfo', body)

    def testOperateVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
            'node_uuid': '',
            'operate': 'mount',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.operateVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'operateVolume', body)

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

    def testTaskMountDir(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'bakdir': '',
            'rc_point': '',
            'bk_storage': '',
            'tape_pool_uuid': '',
            'tape_name': '',
            'library_sn': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.taskMountDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'taskMountDir', body)

    def testListFileSnapshot(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listFileSnapshot(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listFileSnapshot', body)

    def testListDbNames(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
            'rc_point_in_time': '',
            'mount_point': '',
            'lanfree': 1,
            'node_uuid': '',
        }
        
        timingBackup = TimingBackup(a)
        r = timingBackup.listDbNames(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listDbNames', body)

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
