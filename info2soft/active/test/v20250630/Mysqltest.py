
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Mysql
from info2soft.active.v20250630.Mysql import Mysql
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


class MysqlTestCase(unittest.TestCase):
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

    def testCreateMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'mysql_name': True,
            'src_db_uuid': ' 1B1153F6-DAD9-BC39-888A-A743FCC208E5',
            'tgt_db_uuid': ' D42BF707-C971-EEA9-521F-BB0F3F7A92FC',
            'tgt_type': 'oracle',
            'start_rule_now': 0,
            'dbmap_topic': '',
            'map_type': 'table',
            'tab_map': [{
            'src_table': 'src_table',
            'dst_table': 'dst_table',
            'src_db': '111',
            'dst_db': '222',
            'topic': '',},],
            'full_sync': 0,
            'incre_sync': 1,
            'model_type': '1:0',
            'full_sync_mode': 'auto',
            'db_set': {
            'binlog_format': 'row',
            'binlog_row_image': 'full',
            'default_storage_engine': 'innoDB',
            'sync_binlog': '1',
            'innodb_flush_log': '2',
            'innodb_flush_method': 'O_DIRECT',
            'max_allowed_packet': '52',
            'open_files_limit': '65535',
            'server_id': '123456',
            'expire_logs_days': '7',
            'nat_mode': 0,
            'ip': '',},
            'full_sync_set': {
            'support_ddl': 1,
            'change_tf_path': '',
            'tf_file_save_time': 7,
            'nat_mode': 0,
            'foreign_ip': '',
            'extraction': 0,
            'start_lsn': 1,},
            'primary_db_one': '',
            'primary_map_type_one': '',
            'primary_map_one': '',
            'primary_db_two': '',
            'primary_map_type_two': '',
            'primary_map_two': '',
            'db_map': [{
            'dst_table': '',
            'src_table': '',},],
            'modify': False,
            'start_src_db_set': 0,
            'dst_db_set': {
            'binlog_format': '',
            'binlog_row_image': '',
            'default_storage_engine': '',
            'sync_binlog': '',
            'innodb_flush_log': '',
            'innodb_flush_method': '',
            'max_allowed_packet': '',
            'open_files_limit': '',
            'server_id': '',
            'expire_logs_days': '',
            'nat_mode': 1,
            'ip': '',},
            'dst_full_sync_set': {
            'support_ddl': 1,
            'change_tf_path': '',
            'tf_file_save_time': '',
            'nat_mode': '',
            'foreign_ip': '',
            'extraction': 0,
            'start_lsn': 1,},
            'start_dst_db_set': 0,
            'config': {
            'dml_track': {
            'delcol': '',
            'drp': 1,
            'enable': 1,
            'tmcol': '',
            'urp': 1,},
            'src_connect_user': '',
            'dst_connect_user': '',
            'bw_settings': {
            'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'full_sync_settings': {
            'clean_user_before_dum': 0,
            'concurrent_table': [],
            'dump_thd': 1,
            'load_thd': 1,
            'existing_table': 'drop_to_recycle',
            'try_split_part_table': 1,
            'table_msg_uuid': '',
            'end_target_type': '',
            'end_target_db': '',
            'end_db_map': '',
            'end_tab_map': '',
            'full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],
            'start_lsn': '',
            'isCreateTable': '',},
            'etl_settings': {
            'etl_table': [{
            'deal_Type': 'IRP',
            'table': '',
            'user': '',
            'obj_fix_type': 'SKIP',
            'field_condition': '',},],
            'is_target': 1,},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': '[CREATE TABLE]',},
            'binary_code': 'hex',
            'table_change_info': 1,
            'message_format': '',
            'json_format': '',
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',
            'jointing': {
            'table': '',
            'op': 'append',
            'content': [],},},
            'part_load_balance': '',
            'kafka_time_out': '',
            'save_json_text': '',
            'exclude_dbs': [],
            'exclude_dbs_switch': 1,
            'other_settings': {
            'dyn_thread': 1,
            'merge_track': 1,
            'keep_incre_time': 1,
            'target_add_columns': [{
            'schema': '',
            'table': '',
            'column': '',
            'function': '',
            'dataType': '',
            'opType': '',},],
            'incre_full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],
            'filter_table_settings': {
            'exclude_tab_with_column': [],
            'exclude_tab_with_column_switch': '',
            'filter_tables': [{
            'db': '',
            'table': '',},],},
            'enable_truncate_frequence': 1,
            'lsn_keep_time': 0,
            'lsn_keep_interval': 0,
            'master_allow': 0,
            'ddl_cv': 1,
            'delete_table_keep_time': 1,
            'delete_table_keep_time_unit': 1,},
            'full_map_switch': 1,
            'map_type_list': [],
            'column_map': [{
            'user': '',
            'target': '',
            'column': '',},],
            'encrypt_column_switch': 1,
            'encrypt_column_method': 1,
            'encrypt_column_key': '',
            'encrypt_columns': [{
            'user': '',
            'table': '',
            'column': '',},],
        }
        
        
        mysql = Mysql(a)
        r = mysql.createMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'createMysqlRule', body)

    def testListStreamRules(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'where_args': {
            'mysql_uuid': '40fFf7dE-A77D-2EE4-C313-c85d330Df134',
            'mysql_name': '',
            'status': '',
            'src_db_name': '',
            'tgt_db_name': '',
            'db_ip': '',
            'node_ip': '',
            'username': '',},
        }
        
        
        mysql = Mysql(a)
        r = mysql.listStreamRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'listStreamRules', body)

    def testModifyMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'mysql_name': 'mysql',
            'src_db_uuid': ' 1B1153F6-DAD9-BC39-888A-A743FCC208E5',
            'tgt_db_uuid': ' D42BF707-C971-EEA9-521F-BB0F3F7A92FC',
            'tgt_type': 'kafka',
            'start_rule_now': 0,
            'node_uuid': ' 6B1153F6-DAD9-BC39-888A-A743FCC208E6',
            'dbmap_topic': '',
            'map_type': 'table',
            'tab_map': [{
            'src_table': 'src_table',
            'topic': 'topic',
            'dst_table': '',
            'src_db': '',
            'dst_db': '',},],
            'full_sync': 0,
            'incre_sync': 1,
            'model_type': '1:0',
            'full_sync_mode': 'auto',
            'db_set': {
            'db_node': '1B1153F6-DAD9-BC39-888A-A743FCC208E5',
            'binlog_format': 'row',
            'binlog_row_image': 'full',
            'default_storage_engine': 'innoDB',
            'sync_binlog': '1',
            'innodb_flush_log': '2',
            'innodb_flush_method': 'O_DIRECT',
            'max_allowed_packet': '52',
            'open_files_limit': '65535',
            'server_id': '123456',
            'expire_logs_days': '7',
            'nat_mode': 0,
            'ip': '',},
            'full_sync_set': {
            'support_ddl': 1,
            'node': ' 6B1153F6-DAD9-BC39-888A-A743FCC208E6',
            'change_tf_path': '',
            'tf_file_save_time': 7,
            'nat_mode': 0,
            'foreign_ip': '',},
            'primary_node_one': '',
            'primary_node_two': '',
            'primary_db_one': '',
            'primary_map_type_one': '',
            'primary_map_one': [],
            'primary_db_two': '',
            'primary_map_type_two': '',
            'primary_map_two': [],
            'db_map': [{
            'src_db': 'src_db',
            'dst_db': 'dst_db',},],
            'mysql_uuid': '5349E2CF-7DBO-OAF2-13CB-BB7DFD8A9D86',
            'config': {
            'dml_track': {
            'urp': '',
            'drp': '',
            'tmcol': '',
            'delcol': '',},
            'bw_settings': {},
            'full_sync_settings': {},
            'etl_settings': {},
            'inc_sync_ddl_filter': {},
            'table_change_info': '',
            'message_format': '',
            'json_format': '',
            'binary_code': '',
            'run_time': '12*00:00-13:00*40M,3*00:00-13:00*40M',},
            'part_load_balanceby_table': '',
            'kafka_time_out': '',
            'save_json_text': False,
        }
        
        
        mysql = Mysql(a)
        r = mysql.modifyMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'modifyMysqlRule', body)

    def testCreateBatchMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'db_map': [{
            'dst_table': '',
            'src_table': '',},],
            'other_settings': {
            'dyn_thread': 1,
            'merge_track': 1,
            'keep_incre_time': 1,},
            'part_load_balance': '',
            'kafka_time_out': '',
            'full_sync_mode': 'auto',
            'db_set': {
            'binlog_format': 'row',
            'binlog_row_image': 'full',
            'default_storage_engine': 'innoDB',
            'sync_binlog': '1',
            'innodb_flush_log': '2',
            'innodb_flush_method': 'O_DIRECT',
            'max_allowed_packet': '52',
            'open_files_limit': '65535',
            'server_id': '123456',
            'expire_logs_days': '7',
            'nat_mode': 0,
            'ip': '',},
            'full_sync_set': {
            'start_lsn': 1,
            'support_ddl': 1,
            'change_tf_path': '',
            'tf_file_save_time': 7,
            'nat_mode': 0,
            'foreign_ip': '',
            'extraction': 0,},
            'modify': False,
            'primary_db_one': '',
            'primary_map_type_one': '',
            'primary_map_one': '',
            'primary_db_two': '',
            'primary_map_type_two': '',
            'start_src_db_set': 0,
            'primary_map_two': '',
            'dst_db_set': {
            'binlog_format': '',
            'binlog_row_image': '',
            'default_storage_engine': '',
            'sync_binlog': '',
            'innodb_flush_log': '',
            'innodb_flush_method': '',
            'max_allowed_packet': '',
            'open_files_limit': '',
            'server_id': '',
            'expire_logs_days': '',
            'nat_mode': 1,
            'ip': '',},
            'dst_full_sync_set': {
            'start_lsn': 1,
            'support_ddl': 1,
            'change_tf_path': '',
            'tf_file_save_time': '',
            'nat_mode': '',
            'foreign_ip': '',
            'extraction': 0,},
            'start_dst_db_set': 0,
            'prefix': True,
            'src_db_uuid': ' 1B1153F6-DAD9-BC39-888A-A743FCC208E5',
            'tgt_db_uuid': ' D42BF707-C971-EEA9-521F-BB0F3F7A92FC',
            'tgt_type': 'oracle',
            'save_json_text': '',
            'start_rule_now': 0,
            'exclude_dbs': [],
            'exclude_dbs_switch': 1,
            'dbmap_topic': '',
            'map_type': 'table',
            'tab_map': [{
            'topic': '',
            'src_table': 'src_table',
            'dst_table': 'dst_table',
            'src_db': '111',
            'dst_db': '222',},],
            'full_sync': 0,
            'incre_sync': 1,
            'model_type': '1:0',
            'config': {
            'src_connect_user': '',
            'dst_connect_user': '',
            'jointing': {
            'table': '',
            'op': 'append',
            'content': [],},
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',
            'binary_code': 'hex',
            'table_change_info': 1,
            'etl_settings': {
            'etl_table': [{
            'deal_Type': 'IRP',
            'table': '',
            'user': '',
            'obj_fix_type': 'SKIP',
            'field_condition': '',},],},
            'bw_settings': {
            'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'full_sync_settings': {
            'table_msg_uuid': '',
            'end_target_type': '',
            'end_target_db': '',
            'end_db_map': '',
            'end_tab_map': '',
            'full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],
            'start_lsn': '',
            'clean_user_before_dum': 0,
            'concurrent_table': [],
            'dump_thd': 1,
            'load_thd': 1,
            'existing_table': 'drop_to_recycle',
            'try_split_part_table': 1,},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': '[CREATE TABLE]',},
            'dml_track': {
            'delcol': '',
            'drp': 1,
            'enable': 1,
            'tmcol': '',
            'urp': 1,},
            'message_format': '',
            'json_format': '',},
            'db_list': [{
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'src_db_auth_uuid': '',
            'tgt_db_auth_uuid': '',},],
        }
        
        
        mysql = Mysql(a)
        r = mysql.createBatchMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'createBatchMysqlRule', body)

    def testBatchModifyMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'config': {
            'run_time': '12*00:00-13:00*40M,3*00:00-13:00*40M',
            'dml_track': {
            'urp': '',
            'drp': '',
            'tmcol': '',
            'delcol': '',},
            'bw_settings': {},
            'full_sync_settings': {},
            'etl_settings': {},
            'inc_sync_ddl_filter': {},
            'table_change_info': '',
            'message_format': '',
            'json_format': '',
            'binary_code': '',},
            'part_load_balanceby_table': '',
            'kafka_time_out': '',
            'save_json_text': False,
            'mysql_rule_uuids': 'mysql',
            'start_rule_now': 0,
            'node_uuid': ' 6B1153F6-DAD9-BC39-888A-A743FCC208E6',
            'dbmap_topic': '',
            'map_type': 'table',
            'tab_map': [{
            'dst_table': '',
            'src_db': '',
            'dst_db': '',
            'src_table': 'src_table',
            'topic': 'topic',},],
            'full_sync': 0,
            'incre_sync': 1,
            'model_type': '1:0',
            'full_sync_mode': 'auto',
            'db_set': {
            'db_node': '1B1153F6-DAD9-BC39-888A-A743FCC208E5',
            'binlog_format': 'row',
            'binlog_row_image': 'full',
            'default_storage_engine': 'innoDB',
            'sync_binlog': '1',
            'innodb_flush_log': '2',
            'innodb_flush_method': 'O_DIRECT',
            'max_allowed_packet': '52',
            'open_files_limit': '65535',
            'server_id': '123456',
            'expire_logs_days': '7',
            'nat_mode': 0,
            'ip': '',},
            'full_sync_set': {
            'support_ddl': 1,
            'node': ' 6B1153F6-DAD9-BC39-888A-A743FCC208E6',
            'change_tf_path': '',
            'tf_file_save_time': 7,
            'nat_mode': 0,
            'foreign_ip': '',},
            'primary_node_one': '',
            'primary_node_two': '',
            'primary_db_one': '',
            'primary_map_type_one': '',
            'primary_map_one': [],
            'primary_db_two': '',
            'primary_map_type_two': '',
            'primary_map_two': [],
            'db_map': [{
            'src_db': 'src_db',
            'dst_db': 'dst_db',},],
            'mysql_uuid': '5349E2CF-7DBO-OAF2-13CB-BB7DFD8A9D86',
            'batch_basic_settings': '',
            'batch_full_sync_settings': '',
            'batch_incre_sync_settings': '',
            'batch_advanced_settings': '',
            'batch_full_sync_obj_filter': '',
            'batch_encrypt_compress': '',
        }
        
        
        mysql = Mysql(a)
        r = mysql.batchModifyMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'batchModifyMysqlRule', body)

    def testDeleteMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'mysql_uuids': [],
            'force': True,
        }
        
        
        mysql = Mysql(a)
        r = mysql.deleteMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'deleteMysqlRule', body)

    def testDescribeMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'mysql_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mysql = Mysql(a)
        r = mysql.describeMysqlRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'describeMysqlRule', body)

    def testResumeMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.resumeMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'resumeMysqlRule', body)

    def testStopMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.stopMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'stopMysqlRule', body)

    def testRestartMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.restartMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'restartMysqlRule', body)

    def testStartParsingMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.startParsingMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'startParsingMysqlRule', body)

    def testStopParsingMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.stopParsingMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'stopParsingMysqlRule', body)

    def testResetParsingMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.resetParsingMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'resetParsingMysqlRule', body)

    def testStartLoadMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.startLoadMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'startLoadMysqlRule', body)

    def testStopLoadMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.stopLoadMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'stopLoadMysqlRule', body)

    def testResetLoadMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.resetLoadMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'resetLoadMysqlRule', body)

    def testDuplicateMysqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '',
            'scn': '',
            'all': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.duplicateMysqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'duplicateMysqlRule', body)

    def testListStreamStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        mysql = Mysql(a)
        r = mysql.listStreamStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'listStreamStatus', body)

    def testCreateStreamTableFix(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'bcf6CFC4-eCAb-Ef6c-d1Df-BACdAeC5DcB0',
            'tab': [{
            'user': '',
            'table': '',},],
            'fix_relation': 0,
        }
        
        
        mysql = Mysql(a)
        r = mysql.createStreamTableFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'createStreamTableFix', body)

    def testGetStreamRuleLsn(self):
        a = Auth(username, pwd)
        body = {
            'mysql_uuid': '',
            'date': '2024-09-20 14:24:42',
            'offset': 1,
            'limit': 1,
        }
        
        
        mysql = Mysql(a)
        r = mysql.getStreamRuleLsn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mysql', 'getStreamRuleLsn', body)


if __name__ == '__main__':
    unittest.main()
