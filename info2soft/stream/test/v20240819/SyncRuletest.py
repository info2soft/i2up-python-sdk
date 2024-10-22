
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import SyncRule
from info2soft.stream.v20240819.SyncRule import SyncRule
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
            'rule_uuid': 'dCedbCCe-5Fd1-fDA6-3eb6-2499aaEC1dC0',
            'src_db_type': '',
            'tgt_db_type': '',},
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listSyncRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listSyncRules', body)

    def testResumeOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'scn': '1',
            'rule_name': '',
            'operate': 'restart',
            'rule_uuids': [
            'bEcC752C-4C5D-dEEC-1F1e-ef6AEE68B897',
            'CCb2E4e2-c95d-34A6-De2B-c4fABEB5feAb',
            '6c8Bd1dd-E7ef-1147-A46b-2A72d1EaabA5',
            '8580A4CE-48c8-dE6E-223c-6AF9FABE11BE',
            '2ACCBd4B-c1CE-9D2C-5D9f-ebe5C4231fe9',
            '133cbeb7-1b47-5d2f-22Df-c36fA7fedd12',
            '76E4cCCc-0d9f-83E9-66C0-0B4DE9B962f1',
            '7F7b38Dc-d2Ca-dbdA-b365-9af6cd85c40b',
            '1DFB8ff8-baAE-1f7f-A3e0-7B1B6Ef5eDeB',
            '3d5f2A15-D647-83Cb-6b88-ec0c62E67eF2',],
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
            'A87AAE49-C2E8-ae73-Ec9e-E28ADcD7fC62',
            '803631FD-6DA5-7f8e-dF4e-b9f3c2cEabEf',
            'a1Ae59bB-Fb5c-3b87-e3ED-E7B71dadB978',
            '1c9ACE75-F3c7-96Cb-C1Da-cbd4dc8b7C09',
            'EE537bAe-1fE0-C273-fbA8-0132Ac5f9FCD',
            'dcFFcFcA-FB66-5212-DCdE-DBBB0Fbf6dDa',
            'fBebA573-5A26-5Bfd-abB9-653e38eA54d1',
            'C26Ed5bE-dFf9-C3E7-1244-BeDB68CE7Ad0',
            'c94AE3fc-c7F8-b77C-D4c2-F1f289Bbb42a',
            '6BE22681-d718-2EBD-38ec-5dE2fBC4Ad65',],
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
            'BF37A9E1-BB66-0c81-C258-2AC2BC65FF55',
            'BDA62CC6-4b17-8dE8-35Da-5bFFC457CC58',
            'ee3e2DdE-592B-d29f-ea7b-2908DCdFFc49',
            'D1cedF28-1CEa-dD25-fAC1-6B4dfFdE7F9e',
            '3B0B5AD1-b931-2d9D-F8De-735658DEcCdF',
            '9Fdc96dC-8830-4FE8-15CE-d57CF96d8296',
            'D1A5fD7b-3E55-6224-cA8a-471F9DBFAE48',
            '7EC12e8D-f232-CBD1-Fd58-d13bFDf8cfb1',
            '85BF3fF2-Be16-3b7f-BD16-9Af85E2A2E87',
            'cb3Aa67f-ecEf-49A7-696f-e75fCcb3Fd40',],
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
            'E8ADE77D-4F72-E90d-C111-cd2cCfD7c9FE',
            'c8ec4EBA-6b07-946f-fD3A-C2Cd9Fb2c3eB',
            'Cc6767cF-fDd2-EFec-b5b8-2C5B7Bc25A1E',
            'B10EBF7d-2b3E-5fbD-c438-7E6e2d7E4cD7',
            'e3F39512-BC4b-eAAd-43Cf-bF8d71E1E328',
            'b64B65F6-504c-EE3B-Ae99-4C6f9B0d2dE7',
            'aE4A2DDB-544d-aD1F-C7F4-cC58b1F671f5',
            'E1fe5CDA-23fc-43Aa-d6F3-6E830Cc1336b',
            'd992aEed-a2eA-8BfF-c3E3-A630AD8D9fDF',
            '8f5712cc-1863-F791-c17E-a6e4D6186c1C',],
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
            '9eB9F4A5-EFCa-C5eB-Ef7D-f6dcf7c5F5e4',
            '9a56570A-fDfD-c86D-33ea-f6FAFdCcfdB0',
            'EEBfFdEB-b25C-1aC9-45f5-BeeeEcAC6cbE',
            'fAA5e2Db-F15D-2c29-1dCB-67166DDDFceE',
            'Bc9e204b-41fB-6D32-Ef32-1FB2Bb4C167a',
            'c65FEe5E-FDFb-6F7c-737A-6ee3bd3bb1bF',
            'A1cEd4ee-8f99-bfAE-Ff4C-2DDCcC4A73CD',
            'eFbf1d6F-6D1B-8ECD-b1c9-CFcf45BD4a8B',
            'Ccf95A8f-9Fa4-bC1d-8B4E-BB491a7C8576',
            'F7Cb8b34-Efc5-29AC-C7cC-47AB49ffA6Eb',],
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
            'E4f0eE45-30D3-CD19-eeb9-88FFad2e9af2',
            'FaAAd0EF-360b-b37A-c5EF-eE8c9fdB22c5',
            'd7CfdAF3-eAaf-dc85-CE02-8fbfA3AfCEc0',
            'Bdb9C8DC-27d2-50b1-5FcA-dB5314a288c2',
            '147EBDeC-D2fc-38e8-FC1C-B2FfefF86E94',
            '79bdb7b3-4f3d-48f2-5D4A-27410AEdB79d',
            'aefc7E7d-AadC-d2E3-27fb-2c3b995Ca40E',
            'DaD7Ce7C-fA59-26eb-56FD-f81526cA9c5D',
            'a1a353dB-eE97-B1D6-d62E-bf2AB1F3E16E',
            'D3EF6Cd3-B9fE-BE89-D761-912eBFcB5BEf',],
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
            'b77bfbAF-D1d4-9319-9703-3093175c7A74',
            '220fB4FD-3A7d-a5DA-984F-89ae6a9AAbC9',
            '1Db4CaFD-B6dE-BbF5-9249-ED1522fecBF3',
            '18dced62-47cf-Af3e-D6fa-8ECeFf73a0BD',
            '73a89ded-6d68-83D7-688e-2bDF7e2127ce',
            '70e61c9f-7dBf-d641-bBe7-37ab579b135d',
            'e2C45f8B-be28-f2dF-d41E-F5B5Fcbfe3D9',
            '1cE66426-0B2A-AcDB-762B-C1DbcC0ADA26',
            '0EC9F56a-E8D1-39d9-90Db-061E5c22bBdA',
            '9A5194cA-cFB7-C1B1-35bD-DdeffD4f4332',],
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
            'daC3d53e-aBc3-50D7-B02f-2DFdd58C337D',
            'EeF2E9F9-eF6D-5F82-3EaE-8e64297098AF',
            'ae5c25dA-5A29-cAFF-5324-ABd1FcdDFd62',
            '67BD1ab6-fE24-7D1c-F771-a8bdb9A2aA2B',
            '4f73E972-BfAE-5dB5-0fea-2F71FB03dFb5',
            'C4AE234e-ede2-d61a-68A3-B3E0CAAbD42c',
            'D7332b76-2A0e-17E3-a2F9-25eBefc22EB7',
            '64e21FE5-742f-7dD1-5F22-c8d9Ec60E475',
            '97b2BCe4-FBC3-7fcb-384b-1F3beED18E15',
            'BEFA128a-1BBf-cA29-a9eF-d5BEE4DE767e',],
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

    def testCreateSyncRule(self):
        a = Auth(username, pwd)
        body = {
            'table_map': [{
            'key': 'WalkerMartinezRodriguez',
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
            'table_space_name': {},},
            'create_pk_col': '',
            'create_pk_col_name': '',
            'timezone_convert_switch': 1,
            'src_timezone_switch': 1,
            'src_timezone': '',
            'mask_sync_switch': '',
            'db_map_uuid': '',},
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
            'distribute_mode': '',},
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
            'compress_switch': '',
            'compress_algo': '',
            'encrypt': '',
            'compress': '',
            'compress_level': '',
            'encrypt_switch': '',},
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
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.createSyncRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'createSyncRule', body)

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
            'key': 'HallWilliamsWalker',
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
            'key': 'LeeSmithLewis',
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

    def testListSyncRulesSliceStatus(self):
        a = Auth(username, pwd)
        body = {
            'where_args': {
            'src_slice_id': '500000200507163357',
            'status': '',
            'src_slice_ip': '89.138.152.239',
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

    def testListRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'date_start': '2010-05-11',
            'date_end': '1994-05-31',
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

    def testDescribeRuleUser(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '15dB2565-6DCC-4069-5E15-34D79AF1E35B',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.describeRuleUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'describeRuleUser', body)

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

    def testRuleGetScn(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'dFe8Ba41-66d1-F276-2B29-6FdB8CCbbB61',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.ruleGetScn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'ruleGetScn', body)

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

    def testListKafkaOffsetInfo(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'AdAcFF1F-eeFD-41a2-e6ec-1d57c535CF68',
        }
        
        
        syncRule = SyncRule(a)
        r = syncRule.listKafkaOffsetInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SyncRule', 'listKafkaOffsetInfo', body)


if __name__ == '__main__':
    unittest.main()
