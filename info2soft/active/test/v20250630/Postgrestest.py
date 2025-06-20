
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Postgres
from info2soft.active.v20250630.Postgres import Postgres
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


class PostgresTestCase(unittest.TestCase):
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

    def testCreatePgsqlRule(self):
        a = Auth(username, pwd)
        body = {
            'user_uuid': '1BCFCAA3-E3C8-3E28-BDC5-BE36FDC2B5DC',
            'rule_name': '带宽cron测试',
            'src_db_uuid': '1309A716-239E-4724-8E7D-45D0666C9742',
            'tgt_db_uuid': 'D64E1A3A-227C-4E21-8B73-AAB37BDA1020',
            'node_uuid': '',
            'map_type': 'table',
            'rule_type': 41,
            'config': {
            'full_sync_obj_filter': {
            'full_sync_obj_data': [
            'TAB',
            'CHECK',
            'FK',
            'PK',
            'UK',
            'INDEX',
            'SEQUENCE',],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'CREATE TABLE',
            'DROP TABLE',
            'TABLE RENAME',
            'TRUNCATE TABLE',
            'ALTER TABLE',
            'TABLE ADD',
            'TABLE DROP',
            'TABLE MODIFY',
            'CREATE COMMENT',
            'ADD PARTITION',
            'DROP PARTITION',
            'RENAME PARTITION',
            'EXCHANGE PARTITION',
            'SPLIT PARTITION',
            'MERGE PARTITION',
            'MOVE PARTITION',
            'CREATE INDEX',
            'DROP INDEX',
            'ALTER INDEX',
            'RENAME INDEX',
            'REINDEX INDEX',
            'CREATE TYPE',
            'DROP TYPE',
            'ALTER TYPE',
            'ADD CONSTRAINT',
            'DROP CONSTRAINT',
            'ALTER CONSTRAINT',
            'CREATE SEQUENCE',
            'DROP SEQUENCE',
            'ALTER SEQUENCE',
            'DROP VIEW',
            'CREATE VIEW',
            'ALTER VIEW',
            'CREATE PROCEDURE',
            'DROP PROCEDURE',
            'ALTER PROCEDURE',
            'CREATE TABLESPACE',
            'DROP TABLESPACE',
            'ALTER TABLESPACE',
            'CREATE SCHEMA',
            'DROP SCHEMA',
            'ALTER SCHEMA',
            'ADD HASH PARTITION',
            'ADD CONSTRAINTS',],},
            'full_sync_settings': {
            'clean_user_before_dump': 0,
            'dump_thd': 1,
            'load_thd': 1,
            'full_sync_custom_cfg': [{
            'key': '1',
            'value': '2',},],
            'full_sync_source_db': '1309A716-239E-4724-8E7D-45D0666C9742',
            'end_db_map': '',
            'end_tab_map': '',
            'end_target_db': '',
            'table_msg_uuid': '1309A716-239E-4724-8E7D-45D0666C9742',
            'full_sync_mode': 'logic',
            'load_mode': 'direct',
            'ld_dir_opt': 0,
            'try_split_part_table': 1,
            'existing_table': 'truncate',
            'concurrent_table': [],
            'sync_mode': 0,
            'start_scn': 'lsn123',
            'start_lsn': 'lsn123',},
            'other_settings': {
            'incre_full_sync_custom_cfg': [{
            'key': 'key1',
            'value': 'value1',},],
            'dyn_thread': 1,
            'incre_sync': 1,
            'pg_thread_decode_multi_enable': '',},
            'error_handling': {
            'irp': 'irpafterdel',
            'urp': 'ignore',
            'drp': 'ignore',
            'load_err_set': 'continue',},
            'dml_track': {
            'enable': False,
            'keep_deleted_row': False,
            'change_table_structure': False,
            'identity_column': '',
            'time_column': '',
            'date_column': '',
            'date_time_column_unique': False,
            'load_date_time_column_unique': False,
            'date_time_column': '',
            'load_time_column': '',
            'load_date_column': '',
            'load_date_time_column': '',
            'audit': False,
            'audit_prefix': '',
            'audit_appendix': '',
            'op_column': '',
            'opv_update_key': 'UPK',
            'opv_update': 'U',
            'opv_delete': 'D',
            'opv_insert': 'I',},
            'start_rule_now': 0,
            'db_user_map': '',
            'table_map': [{
            'src_user': '1',
            'src_table': '1',
            'dst_user': '1',
            'dst_table': '1',
            'column': [],},],
            'dbmap_topic': '',
            'full_sync': 0,
            'incre_sync': 1,
            'full_sync_mode': 'logic',
            'row_map_mode': 'rowid',
            'kafka_time_out': '120000',
            'part_load_balance': 'by_table',
            'kafka_message_encoding': 'UTF-8',
            'kafka': {
            'binary_code': 'hex',},
            'etl_settings': {
            'etl_table': [],},
            'run_time': '024*00:00:00-23:59:00*1,16*00:01:00-22:59:00*1',
            'save_json_text': False,
            'jointing': [],
            'src_connect_user': 'postgres',
            'dst_connect_user': '',
            'filter_table_settings': {
            'exclude_table': [],},},
            'create_time': 1704349540,
            'encrypt': 1,
            'encrypt_switch': 1,
            'secret_key': '',
            'compress': 0,
            'compress_switch': 0,
            'src_db_auth_uuid': '82B30A78-A86D-41CC-9246-CF8FE3AF943E',
            'tgt_db_auth_uuid': '',
            'comment': '',
            'is_duplicate': 0,
            'maintenance': 1,
            'search_script_name': '',
            'biz_grp_list': [],
            'encrypt_column_switch': 1,
            'encrypt_column_method': 1,
            'encrypt_column_key': '',
            'encrypt_columns': [{
            'user': '',
            'table': '',
            'column': '',},],
        }
        
        
        postgres = Postgres(a)
        r = postgres.createPgsqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'createPgsqlRule', body)

    def testListPgsqlRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'group_uuid': '',
            'where_args': {
            'rule_uuid': '',},
        }
        
        
        postgres = Postgres(a)
        r = postgres.listPgsqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'listPgsqlRule', body)

    def testModifyPgsqlRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'tgt_type': 'sqlserver',
            'map_type': 'db',
            'config': {
            'start_rule_now': 1,
            'table_map': '',
            'full_sync': 0,
            'incre_sync': 1,
            'full_sync_mode': '1',},
            'rule_uuid': '',
        }
        
        
        postgres = Postgres(a)
        r = postgres.modifyPgsqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'modifyPgsqlRule', body)

    def testDeletePgsqlRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 'true',
        }
        
        
        postgres = Postgres(a)
        r = postgres.deletePgsqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'deletePgsqlRule', body)

    def testResumePgsqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [
            '65CEFE4E-DC17-D323-4E04-169EBF151448',
            '8871F59D-B796-4313-AB28-9960EA97804C',],
            'scn': '',
            'all': 1,
        }
        
        
        postgres = Postgres(a)
        r = postgres.resumePgsqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'resumePgsqlRule', body)

    def testStopPgsqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [
            '65CEFE4E-DC17-D323-4E04-169EBF151448',
            '8871F59D-B796-4313-AB28-9960EA97804C',],
            'scn': '',
            'all': 1,
        }
        
        
        postgres = Postgres(a)
        r = postgres.stopPgsqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'stopPgsqlRule', body)

    def testRestartPgsqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [
            '65CEFE4E-DC17-D323-4E04-169EBF151448',
            '8871F59D-B796-4313-AB28-9960EA97804C',],
            'scn': '',
            'all': 1,
        }
        
        
        postgres = Postgres(a)
        r = postgres.restartPgsqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'restartPgsqlRule', body)

    def testDuplicatePgsqlRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [
            '65CEFE4E-DC17-D323-4E04-169EBF151448',
            '8871F59D-B796-4313-AB28-9960EA97804C',],
            'scn': '',
            'all': 1,
        }
        
        
        postgres = Postgres(a)
        r = postgres.duplicatePgsqlRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'duplicatePgsqlRule', body)

    def testListRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        postgres = Postgres(a)
        r = postgres.listRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'listRuleStatus', body)

    def testDescribePgsqlRules(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        postgres = Postgres(a)
        r = postgres.describePgsqlRules(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Postgres', 'describePgsqlRules', body)


if __name__ == '__main__':
    unittest.main()
