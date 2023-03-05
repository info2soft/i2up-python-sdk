# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.active.v20230227.Sqlserver import Sqlserver
# from info2soft.active.v20200722.Sqlserver import Sqlserver
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


class SqlserverTestCase(unittest.TestCase):

    def testDescribeSyncRulesDML(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': '10',
            'usr': '',
            'rule_uuid': 'D5BFAfD4-9C9E-F8Be-ed69-CEACA960EA33',
            'sort_order': 'asc',
            'search': '',
            'sort': '',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.describeSyncRulesDML(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'describeSyncRulesDML', body)

    def testDescribeSyncRulesObjInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': 'edF3Bc10-fd2c-caca-EFdB-e6243C88A5eF',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.describeSyncRulesObjInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'describeSyncRulesObjInfo', body)

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
                        'dst_column': '', }, ], }, ],
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
                        'addInfo': '', }, ], },
                'loader': 1,
                'ip': '',
                'datport': '',
                'db_user_map': {},
                'src_connect_user': '',
                'dst_connect_user': '',
                'bw_settings': {
                    'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"', },
                'inc_sync_ddl_data': [],
                'filter_table_settings': {
                    'exclude_table': [], },
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
                        'JAVA SOURCE', ], },
                'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',
                'save_json_text': '',
                'enable_cdc_table': '',
                'publish_sub_switch': 1, },
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
                        'addInfo': '', }, ], }, },
            'rule_list': [{
                'rule_name': '',
                'src_db_uuid': '',
                'tgt_db_uuid': '',
                'mirror_db_uuid': '', }, ],
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
                        'addInfo': '', }, ], },
                'loader': 1,
                'ip': '',
                'datport': '',
                'db_user_map': {},
                'bw_settings': {
                    'bw_limit': '', },
                'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"', },
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

    def testListRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'group_uuid': '',
            'where_args': {
                'rule_uuid': '', },
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.listRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'listRule', body)

    def testCreateTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_name': 'ctt->ctt',
            'src_db_uuid': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuid': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'cmp_type': 'user,table,db',
            'db_user_map': '{"CTT":"CTT"}',
            'filter_table': '[用户.表名]',
            'db_tb_map': '表映射',
            'dump_thd': 1,
            'rule_uuid': '3E3Fe7A3-03EB-D6df-d17B-aE9c273AeAB3',
            'polices': '"0|00:00',
            'policy_type': 'one_time',
            'concurrent_table': [
                'hh.ww', ],
            'try_split_part_table': 0,
            'one_time': '2019-05-27 16:07:08',
            'repair': 0,
            'fix_related': 0,
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.createTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'createTbCmp', body)

    def testListRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'date_start': '1975-07-06',
            'date_end': '1974-09-05',
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

    def testDescribeTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'a3fdBC55-38f3-Bedb-C8e1-3FC3bBC13D29',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        sqlserver = Sqlserver(a)
        r = sqlserver.describeTbCmp(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'describeTbCmp', body)

    def testDeleteTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'force': '',
            'uuids': 'bCdA1DB9-6b5A-45D6-A423-FCa01bece3bf',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.deleteTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'deleteTbCmp', body)

    def testDescribeSyncRulesFailObj(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': 'D899ce8e-a82c-92B7-6727-3C851187FDc9',
            'search': '',
            'type': 1,
            'stage': 1,
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.describeSyncRulesFailObj(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'describeSyncRulesFailObj', body)

    def testListTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.listTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'listTbCmp', body)

    def testListTbCmpStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'de55DF0e-6D45-0023-C8AA-cDcEE2Fbe4C5',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.listTbCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'listTbCmpStatus', body)

    def testListTbCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.listTbCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'listTbCmpResultTimeList', body)

    def testStopTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'f8f7Ba2C-CD59-f1Fe-728C-E8A76Cd1c6Ac',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.stopTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'stopTbCmp', body)

    def testDescribeTbCmpResuluTimeList(self):
        a = Auth(username, pwd)
        body = {
            'time_list': '07EDef69-79D0-ef3d-e1a1-6C3DE9B7AA81',
            'uuid': '',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.describeTbCmpResuluTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'describeTbCmpResuluTimeList', body)

    def testDescribeTbCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': '95b56bbE-c7AC-3DE8-9b4C-A55AED956Aa5',
            'start_time': '',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.describeTbCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'describeTbCmpResult', body)

    def testDescribeTbCmpErrorMsg(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': 'aaB69AFd-f6d8-193e-3df7-2f5Cfff926D2',
            'start_time': '',
            'name': '',
            'owner': 'admin',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.describeTbCmpErrorMsg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'describeTbCmpErrorMsg', body)

    def testDescribeTbCmpCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }

        sqlserver = Sqlserver(a)
        r = sqlserver.describeTbCmpCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'describeTbCmpCmpResult', body)


if __name__ == '__main__':
    unittest.main()
