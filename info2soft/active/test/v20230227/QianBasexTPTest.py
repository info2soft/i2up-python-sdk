# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.active.v20230227.QianBasexTP import QianBasexTP
# from info2soft.active.v20200722.QianBasexTP import QianBasexTP
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


class QianBasexTPTestCase(unittest.TestCase):

    def testListQianbasexTPRule(self):
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

        qianBasexTP = QianBasexTP(a)
        r = qianBasexTP.listQianbasexTPRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBasexTP', 'listQianbasexTPRule', body)

    def testCreateQianbasexTPRule(self):
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
                    'sync_col': '', }, ], },
        }

        qianBasexTP = QianBasexTP(a)
        r = qianBasexTP.createQianbasexTPRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBasexTP', 'createQianbasexTPRule', body)

    def testModifyQianbasexTPRule(self):
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

        qianBasexTP = QianBasexTP(a)
        r = qianBasexTP.modifyQianbasexTPRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBasexTP', 'modifyQianbasexTPRule', body)

    def testDeleteQianbasexTPRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 'true',
        }

        qianBasexTP = QianBasexTP(a)
        r = qianBasexTP.deleteQianbasexTPRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBasexTP', 'deleteQianbasexTPRule', body)

    def testListQianbasexTPStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }

        qianBasexTP = QianBasexTP(a)
        r = qianBasexTP.listQianbasexTPStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBasexTP', 'listQianbasexTPStatus', body)

    def testListQianbasexTPRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'date_start': '',
            'date_end': '',
            'type': 1,
            'module_type': 1,
            'query_type': 1,
            'rule_uuid': '15ABA15e-348d-87Ed-5f67-21bDD7cc58fb',
        }

        qianBasexTP = QianBasexTP(a)
        r = qianBasexTP.listQianbasexTPRuleLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBasexTP', 'listQianbasexTPRuleLog', body)


if __name__ == '__main__':
    unittest.main()
