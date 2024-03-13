
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import RecoveryRule
from info2soft.recoveryRule.v20240228.RecoveryRule import RecoveryRule
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


class RecoveryRuleTestCase(unittest.TestCase):

    def testCreateRecovery(self):
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
            'rc_path_policy': 1,
            'thread_num_max': 1,
            'thread_num_min': 1,
            'mirr_file_check': 1,
            'mirr_sync_flag': 1,
            'wk_path': '',
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
            'ora_rst_file_name': '',
            'ora_rst_arch_limit_type': 2,
            'ora_rst_arch_limit_log_seq': 1,
            'ora_rst_endarch_limit_log_seq': 1,
            'ora_dbid': '',
            'ora_rst_spfile_path': '',
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
            'ora_tab_pdb_name': '',
            'wk_path_list': [{
            'bk_path': '',
            'wk_path': '',},],
            'pre_recover_script': '',
            'post_recover_script': '',
            'script_timeout': 1,
            'ora_rst_recory_point': 1,
            'ora_rc_recory_point': 1,
            'excl_path': [],
            'trans_mode': 1,
            'hcs_name': '',
            'hcs_instance_id': '',
            'recovery_to_new': 1,
            'new_hcs_uuid': '',
            'new_instance_name': '',
            'availability_zone': '',
            'flavor_ref': '',
            'volume_type': '',
            'volume_size': '',
            'vpc_id': '',
            'subnet_id': '',
            'security_group_id': '',
            'db_password': '',
            'configuration_id': '',
            'time_zone': '',
            'master_az': '',
            'arbitration_az': '',
            'backup_chain_policy': 1,
            'client_list': [{
            'node_uuid': '',
            'bmaster': 1,},],
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
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.modifyRecoveryRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'modifyRecoveryRule', body)

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

    def testListRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'filter_by_biz_grp': 1,
            'status': ''
        }
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.listRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'listRecoveryRule', body)

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

    def teststartRecoveryRule(self):
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

    def teststopRecoveryRule(self):
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

    def testcancelRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'task_uuids': [],
        }

        recoveryRule = RecoveryRule(a)
        r = recoveryRule.cancelRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'cancelRecoveryRule', body)

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
        }
        
        recoveryRule = RecoveryRule(a)
        r = recoveryRule.listDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RecoveryRule', 'listDir', body)

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


if __name__ == '__main__':
    unittest.main()
