# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.active.v20230227.QianBaseSync import QianBaseSync
# from info2soft.active.v20200722.QianBaseSync import QianBaseSync
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


class QianBaseSyncTestCase(unittest.TestCase):

    def testListQianbaseRule(self):
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

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.listQianbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'listQianbaseRule', body)

    def testCreateQianbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': 'test',
            'src_db_uuid': '7B1BE386-4CB1-86AA-D39D-B644C2EADD57',
            'map_type': 'table',
            'config': {
                'start_rule_now': 1,
                'db_set': [{
                    'tgt_db_uuid': 'CD52E44B-D25A-4CE3-126F-6F5A460731E4',
                    'filter_type': '[1:filter_table,0:no_fileter]',
                    'table_map': [{
                        'src_table': '',
                        'dst_table': '', }, ],
                    'custom_config': [{
                        'key': '',
                        'value': '', }, ],
                    'tgt_type': '', }, ],
                'all_custom_config': [{
                    'key': '',
                    'value': '', }, ],
                'sync_content': [{
                    'sync_col': '', }, ],
                'jointing': {
                    'table': '',
                    'op': '',
                    'content': '', },
                'save_json_text': '',
                'kafka_db_uuid': '',
                'conn_num': 1,
                'loader': 1,
                'schema_name': '', },
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.createQianbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'createQianbaseRule', body)

    def testModifyQianbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'tgt_type': 'sqlserver',
            'map_type': 'db',
            'config': {
                'start_rule_now': 1,
                'table_map': [],
                'full_sync': 0,
                'incre_sync': 1,
                ' full_sync_mode': '1',
                'db_user_map': '',
                'dbmap_topic': '',
                'row_map_mode': '',
                'kafka_time_out': '',
                'part_load_balance': '',
                'kafka_message_encoding': '',
                'db_set': [{
                    'tgt_db_uuid': '',
                    'filter_type': '',
                    'tgt_type': '',
                    'table_map': [{
                        'src_table': '',
                        'dst_table': '', }, ],
                    'custom_config': [{
                        'key': '',
                        'value': '', }, ], }, ],
                'all_custom_config': [{
                    'key': '',
                    'value': '', }, ],
                'sync_content': [{
                    'sync_col': '', }, ], },
            'rule_uuid': '',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.modifyQianbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'modifyQianbaseRule', body)

    def testDeleteQianbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 'true',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.deleteQianbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'deleteQianbaseRule', body)

    def testListQianbaseStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.listQianbaseStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'listQianbaseStatus', body)

    def testResumeQianbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
            'scn': '',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.resumeQianbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'resumeQianbaseRule', body)

    def testListQianbaseRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'date_start': '',
            'date_end': '',
            'type': 1,
            'module_type': 1,
            'query_type': 1,
            'rule_uuid': '94cD6bEC-9f8c-6CBe-0dBf-24F8d9Bb49Cd',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.listQianbaseRuleLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'listQianbaseRuleLog', body)

    def testDescribeQianbaseRules(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.describeQianbaseRules(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'describeQianbaseRules', body)

    def testCreateQbTbCmp(self):
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
            'rule_uuid': 'D9C753cc-e8fd-0f3E-F2d9-88aCCBC9ef05',
            'polices': '"0|00:00',
            'policy_type': 'one_time',
            'concurrent_table': [
                'hh.ww', ],
            'try_split_part_table': 0,
            'one_time': '2019-05-27 16:07:08',
            'repair': 0,
            'fix_related': 0,
            'config': {
                'tab_cmp_filter': [{
                    'user': 'test',
                    'table': 'test',
                    'condition': 'select * from xxx', }, ], },
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.createQbTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'createQbTbCmp', body)

    def testListQbTbCmpStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'EFe4DeC4-46A5-Abe1-2fc5-faE88FdF4eFD',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.listQbTbCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'listQbTbCmpStatus', body)

    def testDescribeQbTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '6D34ecd2-BD53-d570-D813-D71fEdbDde5e',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.describeQbTbCmp(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'describeQbTbCmp', body)

    def testDeleteQbTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'force': '',
            'uuids': 'D27e7675-CEba-E4bd-DbD5-D3fE3d96e29c',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.deleteQbTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'deleteQbTbCmp', body)

    def testListQbTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.listQbTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'listQbTbCmp', body)

    def testListQbTbCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.listQbTbCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'listQbTbCmpResultTimeList', body)

    def testStopQbTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'bfA0eB17-b5D5-B78E-0691-36dDebB949A5',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.stopQbTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'stopQbTbCmp', body)

    def testDescribeQbTbCmpResuluTimeList(self):
        a = Auth(username, pwd)
        body = {
            'time_list': 'dd328BBF-FB44-EfdB-D1FA-2D5f939BB3D6',
            'uuid': '',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.describeQbTbCmpResuluTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'describeQbTbCmpResuluTimeList', body)

    def testDescribeQbTbCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': '85d1ECCC-D0ce-6485-50bc-516Af289C675',
            'start_time': '',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.describeQbTbCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'describeQbTbCmpResult', body)

    def testDescribeQbTbCmpErrorMsg(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': 'c26fEbAA-00F2-04eb-eEcf-9875A1e0faf5',
            'start_time': '',
            'name': '',
            'owner': 'admin',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.describeQbTbCmpErrorMsg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'describeQbTbCmpErrorMsg', body)

    def testDescribeQbTbCmpCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }

        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.describeQbTbCmpCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'describeQbTbCmpCmpResult', body)


if __name__ == '__main__':
    unittest.main()
