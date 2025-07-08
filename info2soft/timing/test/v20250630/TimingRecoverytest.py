
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import TimingRecovery
from info2soft.timing.v20250630.TimingRecovery import TimingRecovery
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


class TimingRecoveryTestCase(unittest.TestCase):
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

    def testListTimingRecoveryMssqlTime(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_data_path': 'E:\\mssqlBK\\ts-11111111-1111-1111-1111-111111111111\\',
            'bk_storage': 1,
            'obs_settings': {},
            'tape_pool_uuid': '',
            'tape_name': '',
            'library_sn': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listTimingRecoveryMssqlTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listTimingRecoveryMssqlTime', body)

    def testDescribeTimingRecoveryMssqlInitInfo(self):
        a = Auth(username, pwd)
        body = {
            'rc_point_in_time': '2017-12-21_13-16-53',
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_data_path': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.describeTimingRecoveryMssqlInitInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'describeTimingRecoveryMssqlInitInfo', body)

    def testListTimingRecoveryPathList(self):
        a = Auth(username, pwd)
        body = {
            'rc_data_path': 'C:\\back\\',
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'backup_task_uuid': '11111111-1111-1111-1111-111111111111',
            'volume_uuid': '',
            'bk_storage': '',
            'tape_pool_uuid': '',
            'tape_name': '',
            'library_sn': '',
            'dedupe_uuid': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listTimingRecoveryPathList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listTimingRecoveryPathList', body)

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
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.verifyTimingRecoveryMssqlInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'verifyTimingRecoveryMssqlInfo', body)

    def testListTimingRecoveryOracleRcPointInfo(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'bk_uuid': '',
            'bk_path': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listTimingRecoveryOracleRcPointInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listTimingRecoveryOracleRcPointInfo', body)

    def testDescribeRcMysqlInfo(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_data_path': 'E:\\mssqlBK\\ts-11111111-1111-1111-1111-111111111111\\',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.describeRcMysqlInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'describeRcMysqlInfo', body)

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
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listSbtContrlFile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listSbtContrlFile', body)

    def testDescribeSbtDbid(self):
        a = Auth(username, pwd)
        body = {
            'file_name': '',
            'bk_uuid': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.describeSbtDbid(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'describeSbtDbid', body)

    def testCreateTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'timing_recovery': {
            'bk_path': [
            'E:\\t\\2019-01-15_15-49-00\\E\\test\\',],
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
            'ora_rst_endarch_limit_log_seq': 1,
            'log_ccopy': 1,
            'log_volume_uuid': '',
            'log_mount_point': '',},
            'task_name': 'task',
            'rc_data_path': 'E:\\t\\',
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
            'lgc_path': 'C:\\Program Files\\Microsoft SQL Server\\MSSQL12.MSSQLSERVER\\MSSQL\\DATA\\test.mdf',},],
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
            'E:\\test\\',],
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
            'custom_rc_point': False,
            'resultset_datetime': '',
            'backup_task_uuid': '',
            'backup_task_name': '',},
            'custom_type': 1,
            'kingbasees_settings': {
            'kes_bin': '',
            'kes_data': '',
            'oper_user': '',},},
            'force': False,
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.createTimingRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'createTimingRecovery', body)

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
            'rc_data_path': 'C:\\back\\',
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
            'force': False,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.modifyTimingRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'modifyTimingRecovery', body)

    def testDescribeTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.describeTimingRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'describeTimingRecovery', body)

    def testListTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'page': 1,
            'limit': 1,
            'search_field': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listTimingRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listTimingRecovery', body)

    def testDeleteTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force': 1,
            'del_clone': 0,
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.deleteTimingRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'deleteTimingRecovery', body)

    def testListTimingRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listTimingRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listTimingRecoveryStatus', body)

    def testStartTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'operate': 'start',
            'force': 1,
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.startTimingRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'startTimingRecovery', body)

    def testStopTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'operate': 'start',
            'force': 1,
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.stopTimingRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'stopTimingRecovery', body)

    def testDescribeGroupTimingRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.describeGroupTimingRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'describeGroupTimingRecovery', body)

    def testTimingRecoveryCheckDir(self):
        a = Auth(username, pwd)
        body = {
            'check_type': 1,
            'file_dir': [],
            'node_uuid': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.timingRecoveryCheckDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'timingRecoveryCheckDir', body)

    def testListTimingRecoveryDbInfo(self):
        a = Auth(username, pwd)
        body = {
            'rc_data_path': '',
            'bk_uuid': '',
            'wk_data_type': '4',
            'bk_storage': 1,
            'obs_settings': {},
            'tape_uuid': '',
            'tape_pool_uuid': '',
            'tape_name': '',
            'library_sn': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listTimingRecoveryDbInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listTimingRecoveryDbInfo', body)

    def testListTimingRecoveryDb2Time(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_data_path': 'E:\\mssqlBK\\ts-11111111-1111-1111-1111-111111111111\\',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listTimingRecoveryDb2Time(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listTimingRecoveryDb2Time', body)

    def testListTimingRecoveryGaussTime(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'bk_path': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listTimingRecoveryGaussTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listTimingRecoveryGaussTime', body)

    def testDescribeTimingRecoveryDmBackupInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'bk_path': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.describeTimingRecoveryDmBackupInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'describeTimingRecoveryDmBackupInfo', body)

    def testMountVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
            'node_uuid': '',
            'operate': 'mount',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.mountVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'mountVolume', body)

    def testStatusVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
            'node_uuid': '',
            'operate': 'mount',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.statusVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'statusVolume', body)

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
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.taskMountDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'taskMountDir', body)

    def testListFileSnapshot(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listFileSnapshot(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listFileSnapshot', body)

    def testListDbNames(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
            'rc_point_in_time': '',
            'mount_point': '',
            'lanfree': 1,
            'node_uuid': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listDbNames(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listDbNames', body)

    def testListMysqlDbTableInfo(self):
        a = Auth(username, pwd)
        body = {
            'rc_time': '',
            'bk_path': '',
            'bk_uuid': '',
        }
        
        
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listMysqlDbTableInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingRecovery', 'listMysqlDbTableInfo', body)


if __name__ == '__main__':
    unittest.main()
