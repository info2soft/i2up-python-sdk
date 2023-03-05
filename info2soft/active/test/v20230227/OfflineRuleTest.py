# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.active.v20230227.OfflineRule import OfflineRule
# from info2soft.active.v20200722.OfflineRule import OfflineRule
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


class OfflineRuleTestCase(unittest.TestCase):

    def testListOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'search_field': '',
            'search_value': '',
            'group_uuid': '',
            'where_args': [{
                'rule_uuid': '', }, ],
        }

        offlineRule = OfflineRule(a)
        r = offlineRule.listOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'listOfflineRule', body)

    def testCreateActiveOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'map_type': '',
            'src_db_uuid': '',
            'src_db_auth_uuid': '',
            'tgt_db_uuid': '',
            'tgt_db_auth_uuid': '',
            'tgt_file_path': '',
            'table_map': [{
                'src': {
                    'user': '',
                    'tab': '', },
                'tgt': {
                    'user': '',
                    'tab': '', },
                'column': {
                    'sync_by_default': 1,
                    'column_map_list': [{
                        'operate': 'a',
                        'expression': 'col1+col2',
                        'column_name': 'newCol',
                        'column_type': 'int', }, ], }, }, ],
            'db_user_map': [{
                'src': {
                    'user': '', },
                'tgt': {
                    'user': '', }, }, ],
            'advanced_settings': {
                'dump_thd': 1,
                'load_thd': 1, },
            'etl_settings': {
                'etl_table': [{
                    'oprType': '',
                    'table': '',
                    'user': '',
                    'process': '',
                    'addInfo': '', }, ], },
            'full_sync_custom_cfg': [{
                'key': '',
                'value': '', }, ],
            'policies': [],
            'policy_type': '',
            'tgt_type': '',
            'src_type': '',
            'node_uuid': '',
            'format': {
                'header': 1,
                'delimiter': '',
                'quote': '',
                'force_quote': '',
                'escape': '',
                'null': '',
                'date_format': '',
                'datetime_format': '',
                'timestamp_format': '',
                'time_format': '',
                'byte_encode': '',
                'encode': '',
                'outpath': '', },
            'full_map_switch': 1,
            'virtual_table': [{
                'user': '',
                'tab': '',
                'sql': '', }, ],
        }

        offlineRule = OfflineRule(a)
        r = offlineRule.createActiveOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'createActiveOfflineRule', body)

    def testModifyActiveOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'map_type': '',
            'src_db_uuid': '',
            'src_db_auth_uuid': '',
            'tgt_db_uuid': '',
            'tgt_db_auth_uuid': '',
            'tgt_file_path': '',
            'charset': '',
            'separator': '',
            'tb_map': [{
                'src': {
                    'user': '',
                    'tab': '', },
                'tgt': {
                    'user': '',
                    'tab': '', },
                'column': [{
                    'src_column': '',
                    'dst_column': '', }, ], }, ],
            'db_user_map': [{
                'src': {
                    'user': '', },
                'tgt': {
                    'user': '', }, }, ],
            'advanced_settings': {
                'dump_thd': 1,
                'load_thd': 1, },
            'etl_settings': {
                'etl_table': [{
                    'oprType': '',
                    'table': '',
                    'user': '',
                    'process': '',
                    'addInfo': '', }, ], },
            'full_sync_custom_cfg': [{
                'key': '',
                'value': '', }, ],
            'policies': '',
            'policy_type': '',
            'rule_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        offlineRule = OfflineRule(a)
        r = offlineRule.modifyActiveOfflineRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'modifyActiveOfflineRule', body)

    def testListOfflineRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }

        offlineRule = OfflineRule(a)
        r = offlineRule.listOfflineRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'listOfflineRuleStatus', body)

    def testDeleteOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }

        offlineRule = OfflineRule(a)
        r = offlineRule.deleteOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'deleteOfflineRule', body)

    def testOperateOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'operate': '',
        }

        offlineRule = OfflineRule(a)
        r = offlineRule.operateOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'operateOfflineRule', body)

    def testGetOfflineRuleCharset(self):
        a = Auth(username, pwd)
        body = {
        }

        offlineRule = OfflineRule(a)
        r = offlineRule.getOfflineRuleCharset(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'getOfflineRuleCharset', body)


if __name__ == '__main__':
    unittest.main()
