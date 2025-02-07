
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Sqlserver
from info2soft.active.v20250123.Sqlserver import Sqlserver
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


class SqlserverTestCase(unittest.TestCase):

    def testCreateRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'tgt_type': 'sqlserver',
            'map_type': 'db',
            'config': {
            'start_rule_now': 1,
            'table_map': [{
            'src_table': '',
            'dst_table': '',
            'src_user': '',
            'dst_user': '',
            'column': [{
            'src_column': '',
            'dst_column': '',},],},],
            'enable_cdc': 0,
            'mirror_db_uuid': '',
            'sync_mode': 1,
            'dump_thd': 1,
            'drop_old_tab': 1,
            'lsn': '',
            'etl_settings': {
            'etl_table': [{
            'oprType': '',
            'table': '',
            'user': '',
            'process': '',
            'addInfo': '',},],},
            'loader': 1,
            'ip': '',
            'datport': '',
            'src_connect_user': '',
            'dst_connect_user': '',
            'bw_settings': {
            'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'inc_sync_ddl_data': [],
            'filter_table_settings': {
            'exclude_table': [],},
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
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',
            'save_json_text': False,
            'enable_cdc_table': '',
            'publish_sub_switch': 1,
            'incre_sync': 1,
            'db_user_map': '{"user1":"user2","user3":"user4"}',
            'ddl_cv': 1,
            'delete_table_keep_time': 1,
            'delete_table_keep_time_unit': 1,},
            'encrypt_column_switch': '',
            'encrypt_column_method': '',
            'encrypt_column_key': '',
            'encrypt_columns': [{
            'user': '',
            'table': '',
            'column': '',},],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.createRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'createRule', body)

    def testBatchCreateRule(self):
        a = Auth(username, pwd)
        body = {
            'tgt_type': 'sqlserver',
            'map_type': 'db',
            'config': {
            'enable_cdc': 0,
            'start_rule_now': 1,
            'dump_thd': 1,
            'sync_mode': 1,
            'drop_old_tab': 1,
            'table_map': '',
            'etl_settings': {
            'etl_table': [{
            'oprType': '',
            'table': '',
            'user': '',
            'process': '',
            'addInfo': '',},],},},
            'rule_list': [{
            'rule_name': '',
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'mirror_db_uuid': '',
            'src_db_auth_uuid': '',
            'tgt_db_auth_uuid': '',},],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.batchCreateRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'batchCreateRule', body)

    def testModifyRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': 'test',
            'src_db_uuid': '7B1BE386-4CB1-86AA-D39D-B644C2EADD57',
            'tgt_db_uuid': 'CD52E44B-D25A-4CE3-126F-6F5A460731E4',
            'tgt_type': 'sqlserver',
            'map_type': 'table',
            'config': {
            'etl_settings': {
            'etl_table': [{
            'oprType': '',
            'table': '',
            'user': '',
            'process': '',
            'addInfo': '',},],},
            'loader': 1,
            'ip': '',
            'datport': '',
            'db_user_map': {},
            'bw_settings': {
            'bw_limit': '',},
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'start_rule_now': 1,
            'table_map': '[{"src_user":"1","src_table":"2","dst_user":"1","dst_table":"2","column":[]}]',
            'enable_cdc': 0,
            'mirror_db_uuid': '',
            'sync_mode': 1,
            'dump_thd': 1,
            'drop_old_tab': 1,
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.modifyRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'modifyRule', body)

    def testDeleteRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 'true',
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.deleteRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'deleteRule', body)

    def testResumeSqlserverRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.resumeSqlserverRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'resumeSqlserverRule', body)

    def testStopSqlserverRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.stopSqlserverRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'stopSqlserverRule', body)

    def testRestartSqlserverRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.restartSqlserverRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'restartSqlserverRule', body)

    def testDuplicateSqlserverRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.duplicateSqlserverRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'duplicateSqlserverRule', body)

    def testStopAndStopAnalysisSqlserverRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.stopAndStopAnalysisSqlserverRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'stopAndStopAnalysisSqlserverRule', body)

    def testStartAnalysisSqlserverRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.startAnalysisSqlserverRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'startAnalysisSqlserverRule', body)

    def testStopAnalysisSqlserverRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.stopAnalysisSqlserverRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'stopAnalysisSqlserverRule', body)

    def testListRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.listRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'listRuleStatus', body)

    def testCheckName(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.checkName(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'checkName', body)

    def testListTbCmpStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'BB58C57b-C346-deb2-C782-C1Ee4333FA4c',
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.listTbCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'listTbCmpStatus', body)

    def testListRule(self):
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
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.listRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'listRule', body)

    def testListRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'date_start': 1,
            'date_end': 1,
            'type': -1,
            'module_type': -1,
            'query_type': 1,
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
        }
        
        
        sqlserver = Sqlserver(a)
        r = sqlserver.listRuleLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'listRuleLog', body)

    def testDescribeListRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '6FBC9EB9-A10A-E226-9F2B-A77B3CF1D337',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        sqlserver = Sqlserver(a)
        r = sqlserver.describeListRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'describeListRule', body)


if __name__ == '__main__':
    unittest.main()
