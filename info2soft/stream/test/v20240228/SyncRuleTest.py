
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import SyncRule
from info2soft.stream.v20240228.SyncRule import SyncRule
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


class SyncRuleTestCase(unittest.TestCase):

    def testListSyncRules(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': 'rule_name',
            'search_value': '',
            'group_uuid': '',
            'where_args': {
            'rule_name': '',
            'status': '',
            'src_db_name': '',
            'tgt_db_name': '',
            'db_ip': '',
            'username': '',
            'node_ip': '',
            'rule_uuid': '43DbAe53-EbB9-DdBC-fEEd-E0B6CDCeFC8F',
            'src_db_type': '',
            'tgt_db_type': '',},
        }
        
        syncRule = SyncRule(a)
        r = syncRule.listSyncRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listSyncRules', body)

    def testCreateSyncRule(self):
        a = Auth(username, pwd)
        body = {
            'table_map': [{
            'key': 'AllenMartinPerez',
            'split_dst_table': [{
            'condition': '',
            'dst_table': '',
            'dst_user': '',},],
            'dst_table': 'a',
            'dst_user': 'b',
            'src_table': 'c',
            'src_user': 'd',
            'column': [{
            'dst_column': 'e',
            'src_column': 'f',},],},],
            'full_sync_settings': {
            'dump_thd': 1,
            'clean_user_before_dump': 0,
            'existing_table': 'drop_to_recycle',
            'full_sync': 0,
            'start_scn': '',
            'keep_exist_table': 0,
            'keep_table': 0,
            'load_thd': 1,
            'ld_dir_opt': 0,
            'try_split_part_table': 0,
            'concurrent_table': [
            'hello.world',],
            'full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],
            'dump_split': {
            'enable': '',
            'least_rows': 1,
            'least_bytes': 1,
            'expire_seconds': 1,},},
            'full_sync_obj_filter': {
            'full_sync_obj_data': [
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'DATABASE LINK',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'INDEX',
            'VIEW',
            'FUNCTION',],},
            'other_settings': {
            'keep_usr_pwd': 1,
            'enable_truncate_frequence': 1,
            'keep_dyn_data': 0,
            'zip_level': 0,
            'table_change_info': 1,
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',
            'dly_constraint_load': 0,
            'ddl_cv': 0,
            'keep_bad_act': 0,
            'ignore_foreign_key': 0,
            'jointing': {
            'table': '',
            'op': 'append',
            'content': [],},
            'dyn_thread': 1,
            'convert_urp_of_key': 0,
            'table_delay_load': [],
            'tgt_extern_table': '',
            'bw_limit': '',
            'etl_table': [{
            'oprType': '',
            'table': '',
            'user': '',
            'process': '',
            'addInfo': '',},],
            'filter_table_settings': {
            'exclude_table': [{
            'user': '',
            'table': '',},],
            'exclude_tab_with_column': '',
            'exclude_tab_with_column_switch': 1,},
            'table_space_map': {
            'tgt_table_space': '',
            'table_mapping_way': '',
            'table_path_map': {},
            'table_space_name': {},},},
            'biz_grp_list': [],
            'map_type_list': [],
            'src_db_auth_uuid': '',
            'tgt_db_auth_uuid': '',
            'comment': '',
            'rule_name': 'ctt->ctt',
            'src_db_uuid': ' 6C4AEF37-6496-6DCD-E085-DD640001E4EC',
            'tgt_db_uuid': ' 1C5F3C4B-7333-9518-7349-9712BC9ED664',
            'user_map': {
            'src_user': 'user1',
            'tgt_user': 'user2',},
            'base_settings': {
            'dbmap_topic': '',
            'json_template': '',
            'binary_code': '',
            'kafka_message_encoding': '',
            'kafka_time_out': 1,
            'part_load_balance': '',
            'row_map_mode': '',
            'save_json_text': '',
            'message_format': '',
            'full_sync_mode': '',
            'lib_name': '',
            'jnr_name': '',
            'exclude_dbs': [],
            'exclude_dbs_switch': '',
            'start_rule_now': '',},
            'inc_sync_settings': {
            'incre_sync': 1,
            'dyn_thread': 1,
            'convert_urp_of_key': '',
            'sync_lob': 1,
            'gen_txn': 1,
            'merge_track': 1,
            'keep_bad_act': 1,
            'fill_lob_column': 1,
            'ddl_cv': 1,
            'keep_seq_sync': '',
            'storage_settings': {
            'keep_incre_time': 1,
            'src_max_mem': 1,
            'src_max_disk': 1,
            'txn_max_mem': 1,
            'tf_max_size': 1,
            'max_ld_mem': 1,},
            'error_handling': {
            'load_err_set': '',
            'drp': '',
            'irp': '',
            'urp': '',
            'info': '',
            'report_failed_dml': '',},
            'dml_track': {
            'change_table_structure': '',
            'date_time_column_unique': '',
            'load_date_time_column_unique': '',
            'op_column': '',
            'opv_insert': '',
            'opv_update': '',
            'opv_update_key': '',
            'opv_delete': '',
            'audit': '',
            'audit_prefix': '',
            'audit_appendix': '',
            'identity_column': '',
            'load_date_column': '',
            'load_time_column': '',
            'load_date_time_column': '',
            'keep_deleted_row': '',
            'date_column': '',
            'time_column': '',
            'date_time_column': '',},
            'redo_read_thread': 1,},
            'compress_encrypt_settings': {
            'compress_switch': '',
            'compress_algo': '',
            'encrypt': '',
            'compress': '',
            'compress_level': '',
            'encrypt_switch': '',},
            'column_map': {
            'user': '',
            'target': '',
            'column': '',},
            'policy_settings': {
            'policy_type': '',
            'one_time': '',
            'policies': '',},
            'maintenance': 1,
            'is_duplicate': 1,
            'full_map_switch': 1,
        }
        
        syncRule = SyncRule(a)
        r = syncRule.createSyncRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'createSyncRule', body)

    def testCreateBatchOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'base_settings': {
            'dbmap_topic': '',
            'json_template': '',
            'binary_code': '',
            'kafka_message_encoding': '',
            'kafka_time_out': 1,
            'part_load_balance': '',
            'row_map_mode': '',
            'save_json_text': '',
            'message_format': '',},
            'incre_sync_settings': {
            'incre_sync': 1,
            'dyn_thread': 1,
            'convert_urp_of_key': 1,
            'sync_lob': 1,
            'gen_txn': 1,
            'merge_track': 1,
            'keep_bad_act': 1,},
            'compress_encrypt_settings': {
            'compress_switch': '',
            'compress_algo': '',
            'encrypt': '',
            'compress': '',
            'compress_level': '',
            'encrypt_switch': '',},
            'column_map': {
            'include_tab_with_column': [{
            'user': '',
            'target': '',
            'column': '',},],
            'include_tab_with_column_switch': '',},
            'table_map': [{
            'key': 'WilliamsHallGonzalez',
            'split_dst_table': [{
            'condition': '',
            'dst_table': '',
            'dst_user': '',},],
            'dst_table': 'a',
            'dst_user': 'b',
            'src_table': 'c',
            'src_user': 'd',
            'column': [{
            'dst_column': 'e',
            'src_column': 'f',},],},],
            'full_sync_settings': {
            'dump_thd': 1,
            'clean_user_before_dump': 0,
            'existing_table': 'drop_to_recycle',
            'sync_mode': 0,
            'start_scn': '',
            'keep_exist_table': 0,
            'keep_table': 0,
            'load_thd': 1,
            'ld_dir_opt': 0,
            'try_split_part_table': 0,
            'his_thread': 1,
            'concurrent_table': [
            'hello.world',],
            'full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],},
            'full_sync_obj_filter': {
            'full_sync_obj_data': [
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'DATABASE LINK',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'INDEX',
            'VIEW',
            'FUNCTION',],},
            'filter_table_settings': {
            'exclude_tab_with_column': [],
            'exclude_table': [{
            'table': '',
            'user': '',},],
            'exclude_tab_with_column_switch': 1,},
            'etl_settings': {
            'etl_table': [{
            'user': '',
            'oprType': 'IRP',
            'table': '',
            'addInfo': '',
            'process': 'SKIP',},],},
            'start_rule_now': 0,
            'storage_settings': {
            'src_max_mem': 512,
            'keep_incre_time': '',
            'src_max_disk': 5000,
            'max_ld_mem': '',
            'tf_max_size': 100,
            'tgt_extern_table': '',
            'txn_max_mem': 10000,},
            'table_space_map': {
            'table_path_map': {
            'ddd': 'sss',
            'ddd1': 'sss1',},
            'table_mapping_way': 'ptop',
            'tgt_table_space': '',
            'table_space_name': {
            'qq': 'ss',},},
            'other_settings': {
            'dly_constraint_load': 0,
            'keep_seq_sync': '',
            'ddl_cv': 0,
            'keep_bad_act': 0,
            'gen_txn': '',
            'ignore_foreign_key': 0,
            'jointing': {
            'table': '',
            'op': 'append',
            'content': [],},
            'dyn_thread': 1,
            'convert_urp_of_key': 0,
            'message_format': '',
            'table_delay_load': [],
            'json_format': '',
            'keep_usr_pwd': 1,
            'encrypt_switch': 1,
            'enable_truncate_frequence': 1,
            'encrypt_type': 1,
            'fill_lob_column': '',
            'merge_track': '',
            'keep_dyn_data': 0,
            'zip_level': 0,
            'table_change_info': 1,
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'bw_settings': {
            'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'biz_grp_list': [],
            'map_type_list': [],
            'error_handling': {
            'load_err_set': 'continue',
            'drp': 'ignore',
            'irp': 'irpafterdel',
            'urp': 'toirp',
            'report_failed_dml': 1,
            'info': '',},
            'comment': '',
            'dml_track': [{
            'opv_update_key': '',
            'load_date_time_column_unique': '',
            'audit_appendix': '',
            'opv_update': '',
            'audit': '',
            'change_table_structure': '',
            'opv_insert': '',
            'keep_deleted_row': '',
            'date_column': '',
            'time_column': '',
            'date_time_column': '',
            'opv_delete': '',
            'audit_prefix': '',
            'op_column': '',
            'identity_column': 'AUTO_INCR',
            'load_date_column': '',
            'load_time_column': '',
            'load_date_time_column': '',
            'enable': '',
            'date_time_column_unique': '',},],
            'user_map': {
            'CTT': 'CTT',},
            'prefix': '',
            'db_list': [{
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'src_auth_db_uuid': '',
            'tgt_auth_db_uuid': '',
            'rule_uuid': '',},],
        }
        
        syncRule = SyncRule(a)
        r = syncRule.createBatchOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'createBatchOracleRule', body)

    def testBatchModifySyncRule(self):
        a = Auth(username, pwd)
        body = {
            'base_settings': {
            'dbmap_topic': '',
            'json_template': '',
            'binary_code': '',
            'kafka_message_encoding': '',
            'kafka_time_out': 1,
            'part_load_balance': '',
            'row_map_mode': '',
            'save_json_text': '',
            'message_format': '',
            'start_rule_now': '',
            'full_sync_mode': '',
            'lib_name': '',
            'jnr_name': '',
            'exclude_dbs': [],
            'exclude_dbs_switch': '',},
            'inc_sync_settings': {
            'incre_sync': 1,
            'dyn_thread': 1,
            'convert_urp_of_key': '',
            'sync_lob': 1,
            'gen_txn': 1,
            'merge_track': 1,
            'keep_bad_act': 1,
            'fill_lob_column': 1,
            'ddl_cv': 1,
            'keep_seq_sync': '',
            'storage_settings': {
            'keep_incre_time': 1,
            'src_max_mem': 1,
            'src_max_disk': 1,
            'txn_max_mem': 1,
            'tf_max_size': 1,
            'max_ld_mem': 1,},
            'error_handling': {
            'load_err_set': '',
            'drp': '',
            'irp': '',
            'urp': '',
            'info': '',
            'report_failed_dml': '',},
            'dml_track': {
            'change_table_structure': '',
            'date_time_column_unique': '',
            'load_date_time_column_unique': '',
            'op_column': '',
            'opv_insert': '',
            'opv_update': '',
            'opv_update_key': '',
            'opv_delete': '',
            'audit': '',
            'audit_prefix': '',
            'audit_appendix': '',
            'identity_column': '',
            'load_date_column': '',
            'load_time_column': '',
            'load_date_time_column': '',
            'keep_deleted_row': '',
            'date_column': '',
            'time_column': '',
            'date_time_column': '',},},
            'compress_encrypt_settings': {
            'compress_switch': '',
            'compress_algo': '',
            'encrypt': '',
            'compress': '',
            'compress_level': '',
            'encrypt_switch': '',},
            'column_map': {
            'user': '',
            'target': '',
            'column': '',},
            'policy_settings': {
            'policy_type': '',
            'one_time': '',
            'policies': '',},
            'table_map': [{
            'key': 'HallAllenThompson',
            'split_dst_table': [{
            'condition': '',
            'dst_table': '',
            'dst_user': '',},],
            'dst_table': 'a',
            'dst_user': 'b',
            'src_table': 'c',
            'src_user': 'd',
            'column': [{
            'dst_column': 'e',
            'src_column': 'f',},],},],
            'full_sync_settings': {
            'dump_thd': 1,
            'clean_user_before_dump': 0,
            'existing_table': 'drop_to_recycle',
            'full_sync': 0,
            'start_scn': '',
            'keep_exist_table': 0,
            'keep_table': 0,
            'load_thd': 1,
            'ld_dir_opt': 0,
            'try_split_part_table': 0,
            'concurrent_table': [
            'hello.world',],
            'full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],},
            'full_sync_obj_filter': {
            'full_sync_obj_data': [
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'DATABASE LINK',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'INDEX',
            'VIEW',
            'FUNCTION',],},
            'other_settings': {
            'dly_constraint_load': 0,
            'ddl_cv': 0,
            'keep_bad_act': 0,
            'ignore_foreign_key': 0,
            'jointing': {
            'table': '',
            'op': 'append',
            'content': [],},
            'dyn_thread': 1,
            'convert_urp_of_key': 0,
            'table_delay_load': [],
            'tgt_extern_table': '',
            'bw_limit': '',
            'keep_usr_pwd': 1,
            'etl_table': [{
            'oprType': '',
            'table': '',
            'user': '',
            'process': '',
            'addInfo': '',},],
            'filter_table_settings': {
            'exclude_table': [{
            'user': '',
            'table': '',},],
            'exclude_tab_with_column': '',
            'exclude_tab_with_column_switch': 1,},
            'table_space_map': {
            'tgt_table_space': '',
            'table_mapping_way': '',
            'table_path_map': {},
            'table_space_name': {},},
            'enable_truncate_frequence': 1,
            'keep_dyn_data': 0,
            'zip_level': 0,
            'table_change_info': 1,
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'biz_grp_list': [],
            'map_type_list': [],
            'user_map': {
            'src_user': 'user1',
            'tgt_user': 'user2',},
            'maintenance': 1,
            'is_duplicate': 1,
            'full_map_switch': 1,
            'rule_uuids': [],
            'batch_base_settings': '',
            'batch_full_sync_settings': '',
            'batch_inc_sync_settings': '',
            'batch_full_sync_obj_filter': '',
            'batch_inc_sync_ddl_filter': '',
            'batch_other_settings': '',
            'batch_compress_encrypt_settings': '',
        }
        
        syncRule = SyncRule(a)
        r = syncRule.batchModifySyncRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'batchModifySyncRule', body)

    def testResumeOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'BC8e0ab1-4BEe-4cE7-333E-1E7DbBA0fDb8',],
            'all': 1,
            'tab': [{
            'user': '',
            'table': '',},],
            'fix_relation': 1,
        }
        
        syncRule = SyncRule(a)
        r = syncRule.resumeOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'resumeOracleRule', body)

    def teststopOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'BC8e0ab1-4BEe-4cE7-333E-1E7DbBA0fDb8',],
            'all': 1,
            'tab': [{
            'user': '',
            'table': '',},],
            'fix_relation': 1,
        }

        syncRule = SyncRule(a)
        r = syncRule.stopOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'stopOracleRule', body)

    def testrestartOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'BC8e0ab1-4BEe-4cE7-333E-1E7DbBA0fDb8',],
            'all': 1,
            'tab': [{
            'user': '',
            'table': '',},],
            'fix_relation': 1,
        }

        syncRule = SyncRule(a)
        r = syncRule.restartOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'restartOracleRule', body)

    def teststartAnalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'BC8e0ab1-4BEe-4cE7-333E-1E7DbBA0fDb8',],
            'all': 1,
            'tab': [{
            'user': '',
            'table': '',},],
            'fix_relation': 1,
        }

        syncRule = SyncRule(a)
        r = syncRule.startAnalysisOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'startAnalysisOracleRule', body)

    def teststopAnalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'BC8e0ab1-4BEe-4cE7-333E-1E7DbBA0fDb8',],
            'all': 1,
            'tab': [{
            'user': '',
            'table': '',},],
            'fix_relation': 1,
        }

        syncRule = SyncRule(a)
        r = syncRule.stopAnalysisOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'stopAnalysisOracleRule', body)

    def testresetAnalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'BC8e0ab1-4BEe-4cE7-333E-1E7DbBA0fDb8',],
            'all': 1,
            'tab': [{
            'user': '',
            'table': '',},],
            'fix_relation': 1,
        }

        syncRule = SyncRule(a)
        r = syncRule.resetAnalysisOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'resetAnalysisOracleRule', body)

    def teststopAndStopanalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'BC8e0ab1-4BEe-4cE7-333E-1E7DbBA0fDb8',],
            'all': 1,
            'tab': [{
            'user': '',
            'table': '',},],
            'fix_relation': 1,
        }

        syncRule = SyncRule(a)
        r = syncRule.stopAndStopanalysisOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'stopAndStopanalysisOracleRule', body)

    def testduplicateOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'BC8e0ab1-4BEe-4cE7-333E-1E7DbBA0fDb8',],
            'all': 1,
            'tab': [{
            'user': '',
            'table': '',},],
            'fix_relation': 1,
        }

        syncRule = SyncRule(a)
        r = syncRule.duplicateOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'duplicateOracleRule', body)

    def testDeleteOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': {},
            'force': '',
        }
        
        syncRule = SyncRule(a)
        r = syncRule.deleteOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'deleteOracleRule', body)

    def testDescribeSyncRules(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        syncRule = SyncRule(a)
        r = syncRule.describeSyncRules(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeSyncRules', body)

    def testListSyncRulesStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        syncRule = SyncRule(a)
        r = syncRule.listSyncRulesStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listSyncRulesStatus', body)

    def testListRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'date_start': '2010-12-05',
            'date_end': '1987-01-09',
            'type': -1,
            'module_type': -1,
            'query_type': 1,
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'search_content': 'test',
        }
        
        syncRule = SyncRule(a)
        r = syncRule.listRuleLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listRuleLog', body)

    def testSwitchActiveRuleMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': '',
            'uuid': '',
        }
        
        syncRule = SyncRule(a)
        r = syncRule.switchActiveRuleMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'switchActiveRuleMaintenance', body)

    def testDescribeRuleSelectUser(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '90fEE6bc-e1AD-e8Af-4abd-d322EaA02E51',
        }
        
        syncRule = SyncRule(a)
        r = syncRule.describeRuleSelectUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeRuleSelectUser', body)

    def testDescribeRuleTableFix(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'tab': [
            'I2.table',],
            'fix_relation': 0,
        }
        
        syncRule = SyncRule(a)
        r = syncRule.describeRuleTableFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeRuleTableFix', body)

    def testDescribeRuleGetScn(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '98d6dccd-7D9b-180F-D649-C63F35F58FBe',
        }
        
        syncRule = SyncRule(a)
        r = syncRule.describeRuleGetScn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeRuleGetScn', body)

    def testListKafkaOffsetInfo(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'B1Cb5e26-8E5B-EC3f-aED4-FBC720EfcBCb',
        }
        
        syncRule = SyncRule(a)
        r = syncRule.listKafkaOffsetInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listKafkaOffsetInfo', body)


if __name__ == '__main__':
    unittest.main()
