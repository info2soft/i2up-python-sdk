
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import SyncRule
from info2soft.stream.v20250630.SyncRule import SyncRule
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


class SyncRuleTestCase(unittest.TestCase):
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

    def testCreateSyncRule(self):
        a = Auth(username, pwd)
        body = {
            'table_map': [{
            'key': 'JonesPerezLopez',
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
            'src_column': 'f',
            'src_field_type': 'INT',
            'dst_field_type': 'VARCHAR(60)',
            'pk': False,
            'flag': 1,},],
            'filter': 1,},],
            'full_sync_settings': {
            'dump_thd': 1,
            'clean_user_before_dump': 0,
            'existing_table': 'drop_to_recycle',
            'full_sync': 0,
            'start_scn': '',
            'load_thd': 1,
            'ld_dir_opt': 0,
            'try_split_part_table': 0,
            'concurrent_table': [{
            'user': '',
            'table': '',},],
            'full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],
            'dump_split': {
            'enable': False,
            'least_rows': 1,
            'least_bytes': 1,
            'expire_seconds': 1,},
            'end_target_db': '',
            'end_target_type': '',
            'end_db_map': [{
            'src_db': '',
            'tar_db': '',},],
            'end_tab_map': [{
            'src_db': '',
            'src_table': '',
            'dst_db': '',
            'dst_table': '',
            'column': [{
            'src_column': '',
            'dst_column': '',},],},],
            'isCreateTable': False,
            'full_max_conn': 1,},
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
            'table_change_info': 1,
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
            'table_space_name': {},},
            'create_pk_col': '',
            'create_pk_col_name': '',
            'timezone_convert_switch': 1,
            'src_timezone_switch': 1,
            'src_timezone': '',
            'mask_sync_switch': '',
            'db_map_uuid': '',
            'byte_extend': 1,
            'char_extend': 1,
            'table_attr_cap_switch': 1,
            'table_attr_cap': '',
            'is_target': 1,
            'lsn_keep_time': 1,
            'lsn_keep_interval': 1,
            'master_allow': 1,
            'virtual_key_settings': {
            'auto_switch': '',
            'manual_switch': '',
            'auto_col_name': '',
            'auto_separate': '',
            'manual_columns': [{
            'user': '',
            'tab': '',
            'col': '',
            'composite_col': '',
            'separator': '',},],},
            'encrypt_column_switch': 1,
            'encrypt_column_method': 1,
            'encrypt_columns': [{
            'user': '',
            'table': '',
            'column': '',},],
            'initrans': 1,
            'memory_settings': {
            'dump_max_memory': 1,
            'track_max_memory': 1,
            'load_max_memory': 1,
            'dump_unit': 1,
            'track_unit': 1,
            'load_unit': 1,},},
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
            'save_json_text': False,
            'message_format': '',
            'full_sync_mode': '',
            'lib_name': '',
            'jnr_name': '',
            'exclude_dbs': [],
            'exclude_dbs_switch': '',
            'start_rule_now': '',
            'ob_sharding_inst': '',
            'distribute_mode': '',
            'ha_switch': '',
            'subscribe_type': '',
            'subscribe_name': '',
            'subscribe_procedure': '',
            'shared_process': False,},
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
            'change_table_structure': False,
            'date_time_column_unique': '',
            'load_date_time_column_unique': False,
            'op_column': '',
            'opv_insert': '',
            'opv_update': '',
            'opv_update_key': '',
            'opv_delete': '',
            'audit': False,
            'audit_prefix': '',
            'audit_appendix': '',
            'identity_column': '',
            'load_date_column': '',
            'load_time_column': '',
            'load_date_time_column': False,
            'keep_deleted_row': False,
            'date_column': '',
            'time_column': '',
            'date_time_column': '',},
            'redo_read_thread': 1,
            'trackmode': '',
            'incre_full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],
            'log_file_retention': 1,
            'incre_max_conn': 1,},
            'compress_encrypt_settings': {
            'compress_switch': 1,
            'compress_algo': '',
            'encrypt': 1,
            'compress': 1,
            'compress_level': 1,
            'encrypt_switch': 1,},
            'column_map': [{
            'user': '',
            'target': '',
            'column': '',},],
            'policy_settings': {
            'policy_type': '',
            'one_time': '',
            'policies': '',},
            'maintenance': 1,
            'is_duplicate': 1,
            'full_map_switch': 1,
            'database_map': [{
            'src_database': '',
            'src_schema': '',
            'tgt_database': '',},],
            'encrypt_column_key': '',
            'incre_cmp_switch': '',
            'incre_cmp_db_uuid': '',
            'incre_cmp_db_type': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.createSyncRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'createSyncRule', body)

    def testResumeOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'A72Dee0E-e0CF-def8-53C7-f3eBFEea5D99',
            'eCc86cA8-De5f-6873-e2ed-C21b0c830FbF',
            'd89F69EB-221e-0E10-7A8B-ab37AF8156BA',
            'fFaf7d2d-961E-Dc1E-dA58-Cdf7196A846F',
            'C123f79c-EedF-Bb85-8db2-e57E01E5b4EB',
            '1d94ee71-e35d-BFbc-72e3-e9bcDceBeE11',
            'b7b9bcf4-1Dcc-dDB1-21Dc-EddcAE3ac26B',
            'fCC88ff8-eE4D-52A8-1DEA-d742bae29dC6',
            'bbB21C8d-E5bE-EC54-1A58-94Ed1fD73EB9',
            '726A4Acb-67EF-45DC-bFDA-81c7b8e122ab',],
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

    def testStopOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            '2d729A3F-A82A-f4DF-ff5D-b399cF9FBAF2',
            'ccd29249-2cFa-4d7c-cb97-8E059d8EF17f',
            '7A6BA122-d5Ce-4BeB-bdD1-62cBFCFC3cC5',
            'DDeB5EbD-CDA7-D2CA-D6c6-6cacdbbd8BDD',
            '868FAf90-Ce55-411e-6De5-4fDDE7555FfD',
            '18c3C4df-eBbD-9d7B-E32E-e71fFEd31b1e',
            '83bDcA2D-1a4B-12A7-b232-cdDd8bf3f951',
            '9b070c2c-8eD8-AfC7-2e24-AF00aCF952fd',
            'C1A93ffC-E2C8-57B5-FBCf-8f254CF0BCEc',
            'DD42d3c3-EfF9-E24b-f225-A26dA79bbbF3',],
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

    def testRestartOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            '36CdDfe2-C2Df-cDBC-B46a-d6cE04eB355A',
            '8BFFDeef-11ED-caaE-803b-4f2c2cB86Bed',
            'BCc7DADE-5F43-A981-d9ef-6A2DcCC9c0bC',
            '880bF85D-65c1-1d7F-EcFd-92bB6bDaBfBD',
            '67f8bFC3-5bAd-ee7d-bA43-D6b4Ee7F517c',
            '34d7A6Da-bbca-4E7c-54C0-aED32Eb1f904',
            'fD43eF20-C167-dcBA-f9eF-5fA8610DDEBb',
            'CEdDAa48-C3A6-6D03-e55a-c0Fd3fDe3772',
            '63583507-E4dD-C91A-2fEb-C291547049c8',
            'A8bDDd8C-e6A2-1b2e-24BE-fc89E6b2ee1C',],
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

    def testStartAnalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'c09E531b-214C-bEc4-E08D-A47acBc20Ad9',
            'becCe9cD-5BAc-fcf6-DA1e-93f0Fb1A33d5',
            'CB3EaAef-c93D-1B3B-75bB-EB7AA09f087d',
            'a97C36F6-C367-0E7c-7C3c-8ACc5155E446',
            'fEaE920d-90b4-Ecc7-7740-dcFDDFD8B8cc',
            'A59dbEbd-1A39-8eAD-5D68-fd593ABF02fF',
            'd49AaBAB-F35f-11aB-4D2b-3C4fE2e6Edb5',
            '5146E87C-62C0-24EC-eDD2-e15f26139B83',
            '8Ac5cc2b-E6F9-E2a2-A2f5-a90BE3E9B1fe',
            '24a41f8c-dd8a-d3E6-2e32-C2C2c6cB57F8',],
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

    def testStopAnalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            '66EDB3CC-d9b5-57AB-EA5F-87bdeeF65129',
            '1DC43eEd-1FF6-Abb7-4c6C-B9d17644e8D8',
            'f48075ed-FA77-3a97-C2Be-dFDc1Ff673A1',
            '4f4842FC-E9DB-3bB4-F65f-9dF06C405C0D',
            '5ccB1FeC-C4e4-75A1-b1ED-F8835738FF30',
            'AFdC1487-Faa2-CbbB-a45c-76f299dfF65D',
            '6BFCCeEF-8bdb-E526-FDAf-de0a74D3A455',
            'Ac2b6BA1-d532-C2cd-39B7-def515c3Dc79',
            'FA2A3B3d-AEB9-ebDd-Ceac-b88F129dec0c',
            'Bb1AbCac-579F-Bde6-FFE0-FFABDFcFE7e2',],
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

    def testResetAnalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'e4Beb5BE-b493-D796-b7AD-9151e6E71Ff7',
            '14EA7EEc-EDc3-Bb5F-6f5a-8c59BFedD9Da',
            'E8FB468d-eFfD-bfa4-4BD7-cAB980d1e2C8',
            '14DfcBcC-fb6C-d93f-33e4-DE6b2edfC871',
            'AbFbf7dB-6e1d-F1d8-7Bc9-fcaD8db161f6',
            'eEd9F152-4eCd-15FD-D568-24502fc6307B',
            '351B4eDD-1C9f-21BD-3f7D-050ffC1192E3',
            '9d7Ad7F2-Fe70-6Cce-9A81-E47add1eeabd',
            '1fc66c69-2E7F-8A6a-66CA-bdBF2Dc9532D',
            'Ef49A4E5-eb1f-f86e-0ecA-Fece6a18d9af',],
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

    def testStopAndStopanalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'f6bCDb6e-A6cd-bD1b-6ab4-55FF36DcEc27',
            '8bA0e436-Ef1d-c1A2-de6c-7fA4c1c60596',
            '8FE21BDB-eE3F-8662-01b6-b25B32f21B3e',
            'E10fA9fe-2edb-c64D-Dfed-8989F8717D7C',
            'CeddCd10-1b31-B96b-9eb4-bA4386C9edD7',
            '6F7d9b3F-DAee-2BE5-2BAE-c964d6fdE5aB',
            'f3dB7eC7-6A8b-cEef-CBEd-FCd83cBe6AbC',
            'E46eEbbA-f60D-cF42-D4c2-eF63511403b3',
            'fcCe6DbA-c70D-76aC-B3b1-EDd625E7B667',
            '9C373b8f-D434-87AA-BC24-93Bb198Cf6f3',],
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

    def testDuplicateOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'C2bc9cBC-fAB6-f773-3A67-Ed90BEC6e8e5',
            'BD513df7-6Ce3-CDe5-5497-e7C2E94CAf0b',
            '1BB2c7D2-F9fB-B559-6C64-C1CEd5Bdd0c6',
            'D2B1dcCA-BEce-B558-C7C3-73ec214cC6F2',
            'bd83e152-75DB-AfB6-c623-2DCc9Fe3AFA6',
            'Efdd3B2b-f7c2-BAB9-Fbff-8d1BEadFaD69',
            'A322b2FA-0De4-6289-F5A1-bc53f3307A98',
            '6b8e35c0-5dB4-44Fe-6FCd-3c3a1E25D725',
            'DC4E1e4f-aC2b-2aE0-F269-2fCAC242eEFC',
            'DDF5fCbD-4F64-92EF-4FC7-39b6Bee8c8eE',],
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
            'rule_uuid': '4A0ecfaD-DcDB-Be48-129c-67a7F471BC17',
            'src_db_type': '',
            'tgt_db_type': '',},
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listSyncRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listSyncRules', body)

    def testCreateBatchSyncRule(self):
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
            'save_json_text': False,
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
            'key': 'WilsonHarrisMartinez',
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
            'load_date_time_column_unique': False,
            'audit_appendix': '',
            'opv_update': '',
            'audit': False,
            'change_table_structure': False,
            'opv_insert': '',
            'keep_deleted_row': False,
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
            'enable': False,
            'date_time_column_unique': False,},],
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
        r = syncRule.createBatchSyncRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'createBatchSyncRule', body)

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
            'save_json_text': False,
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
            'change_table_structure': False,
            'date_time_column_unique': '',
            'load_date_time_column_unique': False,
            'op_column': '',
            'opv_insert': '',
            'opv_update': '',
            'opv_update_key': '',
            'opv_delete': '',
            'audit': False,
            'audit_prefix': '',
            'audit_appendix': '',
            'identity_column': '',
            'load_date_column': '',
            'load_time_column': '',
            'load_date_time_column': False,
            'keep_deleted_row': False,
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
            'key': 'ClarkAllenThompson',
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

    def testDescribeSyncRulesLoadInfo(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeSyncRulesLoadInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeSyncRulesLoadInfo', body)

    def testDeleteSyncRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force': False,
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.deleteSyncRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'deleteSyncRule', body)

    def testDescribeSyncRulesMrtg(self):
        a = Auth(username, pwd)
        body = {
            'set_time_init': '',
            'rule_uuid': '',
            'set_time': 1,
            'type': '',
            'interval': '时间间隔',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeSyncRulesMrtg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeSyncRulesMrtg', body)

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

    def testListRuleSyncTable(self):
        a = Auth(username, pwd)
        body = {
            'row_uuid': 'dCBE6B82-9C0e-7C5C-cF1D-efFfFACc1b2B',
            'limit': 15,
            'offset': 1,
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listRuleSyncTable(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listRuleSyncTable', body)

    def testListSyncRulesSliceStatus(self):
        a = Auth(username, pwd)
        body = {
            'where_args': {
            'src_slice_id': '120000199011117326',
            'status': '',
            'src_slice_ip': '184.8.212.197',
            'src_slice_status': '',
            'src_slice_port': '',
            'cluster_name': '',
            'phy_addr': '',},
            'search_field': 'rule_name',
            'search_value': '',
            'page': 1,
            'limit': 10,
            'rule_uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listSyncRulesSliceStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listSyncRulesSliceStatus', body)

    def testDescribeSyncRulesHasSync(self):
        a = Auth(username, pwd)
        body = {
            'offset': '0',
            'limit': 10,
            'row_uuid': 'dA3F89Db-25d5-A5Fe-DAd7-dcffcfB1efff',
            'search': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeSyncRulesHasSync(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeSyncRulesHasSync', body)

    def testListSyncRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'date_start': '2015-09-29',
            'date_end': '1999-06-23',
            'type': -1,
            'module_type': -1,
            'query_type': 1,
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'search_content': 'test',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listSyncRuleLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listSyncRuleLog', body)

    def testDescribeSyncRulesObjInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': '76d9B8B2-C713-dF88-37f6-a4d735AD2F08',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
            'obj_type': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeSyncRulesObjInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeSyncRulesObjInfo', body)

    def testSwitchSyncRuleMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': '',
            'uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.switchSyncRuleMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'switchSyncRuleMaintenance', body)

    def testDescribeSyncRulesFailObj(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': '73b2D9A7-EF1a-8Bb6-3c1b-C9fe6dFB499d',
            'search': '',
            'type': 1,
            'stage': 1,
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeSyncRulesFailObj(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeSyncRulesFailObj', body)

    def testDescribeRuleZStructure(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '4FCf8ea3-B1cF-9a2C-73bA-994f97ee44bA',
            'level': '',
            'type': '',
            'tab_name': '',
            'type_value': '',
            'auth_uuid': '',
            'slt_subscriber_type': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeRuleZStructure(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeRuleZStructure', body)

    def testDescribeSyncRulesIncreDdl(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': '10',
            'rule_uuid': '9A28F8BF-af71-5bB1-4B8C-AC744ce74FcF',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeSyncRulesIncreDdl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeSyncRulesIncreDdl', body)

    def testRuleTableFix(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'tab': [
            'I2.table',],
            'fix_relation': 0,
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.ruleTableFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'ruleTableFix', body)

    def testListRuleIncreDml(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': '10',
            'rule_uuid': '9448E8Eb-6B7f-BaB3-5cDa-94b855bE2C26',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listRuleIncreDml(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listRuleIncreDml', body)

    def testRuleGetScn(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '0ebe67A5-Fa8f-4Fe4-E6E6-9EE8eFcfdD5b',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.ruleGetScn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'ruleGetScn', body)

    def testDescribeExtractSyncRulesObjInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': 'f87EE3ca-BA5A-4EF7-8Bf3-bA4E3DcF91DE',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
            'obj_type': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeExtractSyncRulesObjInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeExtractSyncRulesObjInfo', body)

    def testRuleGetRpcScn(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.ruleGetRpcScn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'ruleGetRpcScn', body)

    def testDescribeLoadSyncRulesObjInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': 'DD523d29-cCbA-CEbC-9Acb-8b39eCf8Afb6',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
            'obj_type': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeLoadSyncRulesObjInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeLoadSyncRulesObjInfo', body)

    def testRuleGetReverseScn(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.ruleGetReverseScn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'ruleGetReverseScn', body)

    def testDescribeSyncRulesDML(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': '10',
            'usr': '',
            'rule_uuid': 'BEFCE3f5-ec21-e6Df-8dC5-b4F11f95FB8B',
            'sort_order': 'asc',
            'search': '',
            'sort': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeSyncRulesDML(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeSyncRulesDML', body)

    def testListKafkaOffsetInfo(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '44Cb8cBc-c291-9f71-5C44-99C1cedDA8cB',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listKafkaOffsetInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listKafkaOffsetInfo', body)

    def testDeleteSyncRulesDML(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'type': 0,
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.deleteSyncRulesDML(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'deleteSyncRulesDML', body)

    def testGetRuleFullSyncStat(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'offset': '',
            'user': '',
            'table': '',
            'stage': 'total',
            'rule_uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.getRuleFullSyncStat(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'getRuleFullSyncStat', body)

    def testIncreDmlFixAll(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.increDmlFixAll(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'increDmlFixAll', body)

    def testSyncRulePrecheck(self):
        a = Auth(username, pwd)
        body = {
            'table_map': [{
            'src_table': '',
            'src_user': '',
            'dst_table': '',
            'dst_user': '',},],
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'src_db_auth_uuid': '',
            'tgt_db_auth_uuid': '',
            'preview': {
            'alter': {
            'alter_function': False,
            'alter_index': False,
            'alter_procedure': False,
            'alter_queue': False,
            'alter_sequence': False,
            'alter_table': False,
            'alter_tablespace': False,
            'alter_view': False,},
            'create': {
            'create_index': False,
            'create_or_replace_function': False,
            'create_or_replace_procedure': False,
            'create_or_replace_queue': False,
            'create_or_replace_synonym': False,
            'create_or_replace_type': False,
            'create_or_replace_view': False,
            'create_role': False,
            'create_sequence': False,
            'create_table': False,
            'create_tablespace': False,},
            'drop': {
            'drop_function': False,
            'drop_index': False,
            'drop_procedure': False,
            'drop_queue': False,
            'drop_sequence': False,
            'drop_synonym': False,
            'drop_table': False,
            'drop_tablespace': False,
            'drop_type': False,
            'drop_view': False,},},
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.syncRulePrecheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'syncRulePrecheck', body)

    def testGetDbTimezone(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.getDbTimezone(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'getDbTimezone', body)

    def testDescribeRuleDbCheck(self):
        a = Auth(username, pwd)
        body = {
            'isCreateTable': 1,
            'full_map_switch': 1,
            'map_type': '',
            'tab_map': [],
            'map_type_list': [],
            'src_db_uuid': '',
            'dst_db_uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeRuleDbCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeRuleDbCheck', body)

    def testImportSyncRule(self):
        a = Auth(username, pwd)
        body = {
            'file': '',
            'ext': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.importSyncRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'importSyncRule', body)

    def testExportSyncRule(self):
        a = Auth(username, pwd)
        body = {
            'include_active_db': 1,
            'include_active_node': 1,
            'rule_uuids': [],
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.exportSyncRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'exportSyncRule', body)

    def testGetStreamRuleLsn(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 1,
            'rule_uuid': '',
            'date': '2013-03-27 04:22:14',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.getStreamRuleLsn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'getStreamRuleLsn', body)

    def testStatusStreamOverall(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.statusStreamOverall(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'statusStreamOverall', body)

    def testDeleteIncreDML(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'opr_type': 'ddl',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.deleteIncreDML(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'deleteIncreDML', body)

    def testDescribeRuleSelectUser(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': 'ddedEcb7-B16C-C1b7-83Eb-1EbBdC3AFFA2',
            'list_db': 1,
            'db_name': '',
            'auth_uuid': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeRuleSelectUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeRuleSelectUser', body)

    def testListSummaryView(self):
        a = Auth(username, pwd)
        body = {
            'where_args': [{
            'src_db_name': '',
            'tgt_db_name': '',
            'status': '',
            'src_db_type': '',
            'rule_name': '',},],
            'page': 1,
            'limit': 1,
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listSummaryView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listSummaryView', body)

    def testListIncreDmlExtract(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 1,
            'rule_uuid': 'C5bb2ACD-11Fd-B6Ae-be64-DaeF2641BfdD',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listIncreDmlExtract(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listIncreDmlExtract', body)

    def testListIncreDmlLoad(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 1,
            'rule_uuid': 'c7D95C1b-Ad8b-e9EA-CeC0-CE70bB624181',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listIncreDmlLoad(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listIncreDmlLoad', body)

    def testListSummaryMaskView(self):
        a = Auth(username, pwd)
        body = {
            'where_args': [{
            'src_db_name': '',
            'tgt_db_name': '',
            'status': '',
            'src_db_type': '',
            'rule_name': '',},],
            'page': 1,
            'limit': 1,
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listSummaryMaskView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listSummaryMaskView', body)

    def testListExtractHeatMap(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'top': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listExtractHeatMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listExtractHeatMap', body)

    def testListLoadHeatMap(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'top': '',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listLoadHeatMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listLoadHeatMap', body)


if __name__ == '__main__':
    unittest.main()
