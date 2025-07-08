
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import RecoveryRule
from info2soft.recoveryRule.v20250630.RecoveryRule import RecoveryRule
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


class RecoveryRuleTestCase(unittest.TestCase):
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

    def testCreateRecovery(self):
        a = Auth(username, pwd)
        body = {
            'ora_tab_names': [{
            'tgt_table': '',
            'ori_table': '',
            'user': '',},],
            'task_name': '',
            'auto_start': 1,
            'start_time': 1,
            'priority': 90000,
            'rc_mode': 1,
            'biz_grp_list': [],
            'bk_set_uuid': '',
            'bk_path': [],
            'thread_num_max': 1,
            'thread_num_min': 1,
            'wk_uuid': '',
            'mirr_file_check': 1,
            'mirr_sync_flag': 1,
            'wk_path': '',
            'compress_switch': 0,
            'compress': 1,
            'encrypt_switch': 0,
            'rc_path_policy': 1,
            'bk_file_crypt': 0,
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'ora_content_type': 1,
            'encrypt': 1,
            'rman_num_streams_df_min': 1,
            'ora_pdbs_name': [],
            'ora_do_recovery': 0,
            'ora_do_restore': 0,
            'ora_rst_type': 0,
            'ora_rc_type': 0,
            'rman_num_streams_df_max': 1,
            'ora_rst_limit_scn': 0,
            'ora_rc_point_scn': 1,
            'ora_rc_point_log_seq': '',
            'ora_rc_point_date': '',
            'ora_rst_arch_limit_log_seq': 1,
            'ora_rc_point_type': 1,
            'ora_rst_limit_type': 0,
            'ora_rst_endarch_limit_log_seq': 1,
            'ora_rst_limit_date': '',
            'ora_tab_mode': 1,
            'ora_rst_record': {},
            'ora_rst_file_name': '',
            'ora_rst_spfile_path': '',
            'ora_rc_record': {},
            'ora_rst_limit_log_seq': '',
            'ora_rst_arch_limit_type': 2,
            'ora_tab_pdb_name': '',
            'ora_rc_point_thread': '',
            'pre_recover_script': '',
            'ora_home_path': '',
            'wk_path_list': [{
            'wk_path': '',
            'bk_path': '',},],
            'wk_data_type': 1,
            'ora_dbid': '',
            'ora_rc_recory_point': 1,
            'ora_open_mode': 0,
            'hcs_instance_id': '',
            'hcs_name': '',
            'excl_path': [],
            'recovery_to_new': 1,
            'vpc_id': '',
            'security_group_id': '',
            'db_password': '',
            'configuration_id': '',
            'master_az': '',
            'time_zone': '',
            'backup_chain_policy': 1,
            'arbitration_az': '',
            'src_instance_name': '',
            'src_client_uuid': '',
            'src_db_name': '',
            'bk_set_select': 0,
            'ora_rst_limit_thread': '',
            'availability_zone': '',
            'new_hcs_uuid': '',
            'flavor_ref': '',
            'new_instance_name': '',
            'ora_sid_name': '',
            'ora_tab_aux_path': '',
            'subnet_id': '',
            'volume_size': '',
            'volume_type': '',
            'post_recover_script': '',
            'ora_rst_recory_point': 1,
            'tgt_instance_uuid': '',
            'script_timeout': 1,
            'tgt_db_name': '',
            'client_list': [{
            'bmaster': 1,
            'node_uuid': '',},],
            'logic_infos': [{
            'logic_path': '',
            'logic_name': '',
            'db_file_path': '',},],
            'bk_set_point': '',
            'trans_mode': 1,
            'backup_method': 1,
            'db_tables': [
            'db_name.schema_name.table_name',],
            'is_instance_start': 1,
            'content_type': 1,
            'db_names': [],
            'bk_server_uuid': '',
            'bucket_uuid': '',
            'sto_uuid': '',
            'arch_path': '',
            'bk_server_addr': '',
            'bk_encrypt_password': '',
            'rc_point_scn': 1,
            'bk_thread_num': 1,
            'bk_encrypt_algorithm': '',
            'rc_method': 1,
            'bk_encrypt_switch': 1,
            'db_table_spaces': [],
            'data_source': {
            'nbu': {
            'policy_name': '',
            'policy_type': 1,
            'client_name': '',
            'end_datetime': '',
            'start_datetime': '',},},
            'bk_encrypt': 1,
            'custom_cfg': [{
            'value': '',
            'key': '',},],
            'bk_set_uuids': [],
            'db_group_name': '',
            'num_parallel_collections': 1,
            'dst_type': 1,
            'password_bkset': '',
            'restore_strategy': 1,
            'log_archive_concurrency': '',
            'password_bkset_switch': '',
            'backup_thread_score': '',
            'dest_tenant_name': '',
            'nbu_wk_path_list': [],
            'resource_pool': '',
            'concurrency': '',
            'dorado_storage_pool_id': '',
            'clone_task_uuid': '',
            'gtid': '',
            'tables': [{
            'src_table': '',
            'dest_table': '',},],
            'tgt_db_info': [{
            'src_table_name': '',
            'tgt_table_name': '',},],
            'manage_ip': [],
            'os_type': '',
            'arch': '',
            'cpu_spec': '',
            'host_type': '',
            'solution': '',
            'recovery_way': '',
            'restore_path': '',
            'exec_path': '',
            'config_path': '',
            'config_addr': '',
            'config_port': '',
            'link_protocol': '',
            'wwpn': {
            'initiator': '',
            'target': '',},
            'backup_way': 1,
            'parallel_num': 1,
            'parallel_process': 1,
            'active_log_path': '',
            'overwrite': 1,
            'slave_dbs': [{
            'id': '',
            'ip': '',
            'port': '',},],
            'data_path': '',
            'os_user': '',
            'approach': '',
            'series': 1,
            'specs': '',
            'region_id': '',
            'resource_group': '',
            'machine_group': '',
            'compatibility': '',
            'compute_node_specification': '',
            'store_node_specification': '',
            'compute_node_num': 1,
            'store_node_num': 1,
            'single_node_memory_size': 1,
            'single_node_memory_unit': 1,
            'standby_availability_zone': '',
            'secondary_standby_availability_zone': '',
            'main_machine_room': '',
            'standby_machine_room': '',
            'secondary_standby_machine_room': '',
            'store_specification': '',
            'main_availability_zone': '',
            'secondary_standby_region_id': '',
            'eth': '',
            'client_spec': '',
            'machine_spec': '',
            'cpu': '',
            'memory': '',
            'data_volume_size': '',
            'log_volume_size': '',
            'idc_resource': '',
            'master_idc': '',
            'coldback_idc': '',
            'recover_db': 1,
            'set_list': [{
            'id': '',
            'hosts': [],},],
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.createRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'createRecovery', body)

    def testModifyRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'auto_start': 1,
            'start_time': 1,
            'biz_grp_list': [],
            'priority': 90000,
            'rc_mode': 1,
            'bk_set_uuid': '',
            'bk_path': [],
            'wk_uuid': '',
            'rc_tgt_position': 1,
            'rc_tgt_dir_list': [{
            'bk_path': '',
            'wk_path': '',},],
            'thread_num_max': 1,
            'thread_num_min': 1,
            'mirr_file_check': 1,
            'mirr_sync_flag': 1,
            'rc_tgt_dir': '',
            'compress_switch': 0,
            'compress': 1,
            'encrypt_switch': 0,
            'encrypt': 1,
            'bk_file_crypt': 0,
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'ora_content_type': 1,
            'rman_num_streams_df_max': 1,
            'rman_num_streams_df_min': 1,
            'ora_pdbs_name': [],
            'ora_do_restore': 0,
            'ora_do_recovery': 0,
            'ora_rst_type': 0,
            'ora_rc_type': 0,
            'ora_open_mode': 0,
            'ora_rst_limit_type': 0,
            'ora_rst_limit_date': '',
            'ora_rst_limit_scn': 0,
            'ora_rst_limit_log_seq': '',
            'ora_rst_record': {},
            'ora_rc_point_type': 1,
            'ora_rc_record': {},
            'ora_rc_point_scn': 1,
            'ora_rc_point_log_seq': '',
            'ora_rc_point_date': '',
            'ora_rst_ctrl_name': '',
            'ora_rst_arch_limit_type': 2,
            'ora_rst_arch_limit_log_seq': 1,
            'ora_rst_endarch_limit_log_seq': 1,
            'ora_dbid': '',
            'ora_rst_spfile_path': '',
            'ora_rst_spfile_name': '',
            'ora_tab_mode': 1,
            'ora_tab_names': [{
            'user': '',
            'ori_table': '',
            'tgt_table': '',},],
            'ora_tab_aux_path': '',
            'ora_sid_name': '',
            'ora_home_path': '',
            'wk_data_type': 1,
            'ora_rc_point_thread': '',
            'ora_rst_limit_thread': '',
            'random_str': '',
            'trans_mode': 1,
            'dst_type': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.modifyRecoveryRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'modifyRecoveryRule', body)

    def testListRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'filter_by_biz_grp': 1,
            'status': '',
            'where_args': {
            'task_uuid': '',
            'wk_data_type': 1,
            'recovery_way': 1,},
            'like_args': {
            'task_name': '',
            'wk_node_name': '',
            'wk_hostname': '',},
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.listRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'listRecoveryRule', body)

    def testDeleteRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'force': 1,
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.deleteRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'deleteRecoveryRule', body)

    def testStartRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.startRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'startRecoveryRule', body)

    def testStopRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.stopRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'stopRecoveryRule', body)

    def testDescribeRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'version': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.describeRecoveryRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'describeRecoveryRule', body)

    def testListRecoveryRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.listRecoveryRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'listRecoveryRuleStatus', body)

    def testListDir(self):
        a = Auth(username, pwd)
        body = {
            'top_dir': '',
            'page': 1,
            'limit': 1,
            'bk_set_uuid': '',
            'search': '',
            'rc_mode': 1,
            'marker': 1,
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.listDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'listDir', body)

    def testListDirPost(self):
        a = Auth(username, pwd)
        body = {
            'marker': 1,
            'top_dir': '',
            'page': 1,
            'limit': 1,
            'bk_set_uuid': '',
            'rc_mode': 1,
            'search': '',
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.listDirPost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'listDirPost', body)

    def testListSbtContrlFile(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuid': '',
            'ora_content_type': 1,
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.listSbtContrlFile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'listSbtContrlFile', body)

    def testListTimingRecoveryOracleRcPointInfo(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'bk_set_uuid': '',
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.listTimingRecoveryOracleRcPointInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'listTimingRecoveryOracleRcPointInfo', body)

    def testDescribeSbtDbid(self):
        a = Auth(username, pwd)
        body = {
            'file_name': '',
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.describeSbtDbid(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'describeSbtDbid', body)

    def testListVerifyBackupMedia(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuid': '',
            'backup_chain_policy': 1,
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.listVerifyBackupMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'listVerifyBackupMedia', body)

    def testGetRecoveryBkServerAddr(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.getRecoveryBkServerAddr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'getRecoveryBkServerAddr', body)

    def testDescribeCoveringLogBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuid': '',
            'bk_set_point': 1,
        }
        
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.describeCoveringLogBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'describeCoveringLogBackupSet', body)


if __name__ == '__main__':
    unittest.main()
