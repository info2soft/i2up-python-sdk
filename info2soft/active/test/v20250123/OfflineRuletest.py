
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import OfflineRule
from info2soft.active.v20250123.OfflineRule import OfflineRule
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
            'rule_uuid': 'A5FCE3EF-432d-869B-de12-Ca6E7118FbF9',
            'status': 'dump',},],
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
            'advanced_table_map': [{
            'src': {
            'user': '',
            'tab': '',},
            'tgt': {
            'user': '',
            'tab': '',},
            'column': {
            'sync_by_default': 1,
            'column_map_list': [{
            'operate': 'a',
            'expression': 'col1+col2',
            'column_name': 'newCol',
            'column_type': 'int',
            'src_column_name': '',},],},},],
            'db_user_map': [{
            'src': {
            'user': '',},
            'tgt': {
            'user': '',},},],
            'advanced_settings': {
            'dump_thd': 1,
            'load_thd': 1,
            'exclude_table_by_features': {
            'PK': False,
            'UK': False,
            'FK': False,
            'INDEX': False,},},
            'etl_settings': {
            'etl_table': [{
            'oprType': '',
            'table': '',
            'user': '',
            'process': '',
            'addInfo': '',},],},
            'full_sync_custom_cfg': [{
            'key': '',
            'value': '',
            'enable': '',},],
            'policies': [],
            'policy_type': '',
            'tgt_type': '',
            'src_type': '',
            'node_uuid': '',
            'format': {
            'header': 1,
            'delimiter': '',
            'quote': '',
            'force_quote': 1,
            'escape': '',
            'null': '',
            'date_format': '',
            'datetime_format': '',
            'timestamp_format': '',
            'time_format': '',
            'byte_encode': '',
            'encode': '',
            'outpath': '',
            'datatag': '',
            'line_break': '',},
            'full_map_switch': 1,
            'virtual_table': [{
            'user': '',
            'tab': '',
            'sql': '',
            'srcuser': '',
            'srctab': '',},],
            'table_map': [{
            'src_table': '',
            'tgt_table': '',
            'src_db': '',
            'dst_db': '',
            'column': [{
            'dst_column': '',
            'src_column': '',},],},],
            'file_map': [{
            'src_file_path': '',
            'src_file_name': '',
            'tgt_topic': '',},],
            'src_file_path': '',
            'src_node_uuid': '',
            'maintenance': 1,
            'comment': '',
            'start_rule_now': 1,
        }
        
        
        offlineRule = OfflineRule(a)
        r = offlineRule.createActiveOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'createActiveOfflineRule', body)

    def testUpdateActiveOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'tgt_type': '',
            'src_type': '',
            'node_uuid': '',
            'table_map': [{
            'src_table': '',
            'tgt_table': '',
            'src_db': '',
            'dst_db': '',
            'column': [{
            'dst_column': '',
            'src_column': '',},],},],
            'format': {
            'header': 1,
            'delimiter': '',
            'quote': '',
            'force_quote': 1,
            'escape': '',
            'null': '',
            'date_format': '',
            'datetime_format': '',
            'timestamp_format': '',
            'time_format': '',
            'byte_encode': '',
            'encode': '',
            'datatag': '',
            'outpath': '',
            'line_break': '',},
            'full_map_switch': 1,
            'virtual_table': [{
            'user': '',
            'tab': '',
            'sql': '',},],
            'rule_name': '',
            'map_type': '',
            'src_db_uuid': '',
            'src_db_auth_uuid': '',
            'tgt_db_uuid': '',
            'tgt_db_auth_uuid': '',
            'tgt_file_path': '',
            'advanced_table_map': [{
            'column': {
            'sync_by_default': 1,
            'column_map_list': [{
            'src_column_name': '',
            'operate': 'a',
            'expression': 'col1+col2',
            'column_name': 'newCol',
            'column_type': 'int',},],},
            'src': {
            'user': '',
            'tab': '',},
            'tgt': {
            'user': '',
            'tab': '',},},],
            'db_user_map': [{
            'src': {
            'user': '',},
            'tgt': {
            'user': '',},},],
            'advanced_settings': {
            'dump_thd': 1,
            'load_thd': 1,},
            'etl_settings': {
            'etl_table': [{
            'oprType': '',
            'table': '',
            'user': '',
            'process': '',
            'addInfo': '',},],},
            'full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],
            'policies': [],
            'policy_type': '',
            'file_map': 5,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        offlineRule = OfflineRule(a)
        r = offlineRule.updateActiveOfflineRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'updateActiveOfflineRule', body)

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

    def testResumeOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'operate': '',
        }
        
        
        offlineRule = OfflineRule(a)
        r = offlineRule.resumeOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'resumeOfflineRule', body)

    def testStopOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'operate': '',
        }
        
        
        offlineRule = OfflineRule(a)
        r = offlineRule.stopOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'stopOfflineRule', body)

    def testRestartOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'operate': '',
        }
        
        
        offlineRule = OfflineRule(a)
        r = offlineRule.restartOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'restartOfflineRule', body)

    def testStopScheduleOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'operate': '',
        }
        
        
        offlineRule = OfflineRule(a)
        r = offlineRule.stopScheduleOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'stopScheduleOfflineRule', body)

    def testResumeScheduleOfflineRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'operate': '',
        }
        
        
        offlineRule = OfflineRule(a)
        r = offlineRule.resumeScheduleOfflineRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'resumeScheduleOfflineRule', body)

    def testGetOfflineRuleCharset(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        offlineRule = OfflineRule(a)
        r = offlineRule.getOfflineRuleCharset(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'getOfflineRuleCharset', body)

    def testDescribeOfflineRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        offlineRule = OfflineRule(a)
        r = offlineRule.describeOfflineRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'describeOfflineRule', body)

    def testGetOfflineRuleGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        offlineRule = OfflineRule(a)
        r = offlineRule.getOfflineRuleGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'getOfflineRuleGroup', body)

    def testUpdateOfflineRuleGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        offlineRule = OfflineRule(a)
        r = offlineRule.updateOfflineRuleGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'updateOfflineRuleGroup', body)

    def testSwitchOfflineRuleMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': 1,
            'uuid': '',
        }
        
        
        offlineRule = OfflineRule(a)
        r = offlineRule.switchOfflineRuleMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OfflineRule', 'switchOfflineRuleMaintenance', body)


if __name__ == '__main__':
    unittest.main()
