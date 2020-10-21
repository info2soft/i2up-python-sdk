
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import Sqlserver
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

    def testCreateRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': 'test',
            'src_db_uuid': '7B1BE386-4CB1-86AA-D39D-B644C2EADD57',
            'tgt_db_uuid': 'CD52E44B-D25A-4CE3-126F-6F5A460731E4',
            'tgt_type': 'sqlserver',
            'map_type': 'table',
            'config': {
            'start_rule_now': 1,
            'table_map': [{
            'src_user': '1',
            'src_table': '2',
            'dst_user': '1',
            'dst_table': '2',
            'column': [],},],
            'enable_cdc': 0,
            'mirror_db_uuid': '',
            'sync_mode': 1,
            'dump_thd': 1,
            'drop_old_tab': 1,},
            '_': '95f4e88ab554',
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
            'table_map': '',},
            'rule_list': [{
            'rule_name': '',
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'mirror_db_uuid': '',},],
        }
        
        sqlserver = Sqlserver(a)
        r = sqlserver.batchCreateRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'batchCreateRule', body)

    def testModifyRule(self):
        a = Auth(username, pwd)
        body = {
            'table_map': [{
            'src_user': '1',
            'src_table': '2',
            'dst_user': '1',
            'dst_table': '2',
            'column': [],},],
            'rule_name': 'test',
            'src_db_uuid': '7B1BE386-4CB1-86AA-D39D-B644C2EADD57',
            'tgt_db_uuid': 'CD52E44B-D25A-4CE3-126F-6F5A460731E4',
            'tgt_type': 'sqlserver',
            'map_type': 'table',
            'config': {},
            'start_rule_now': 1,
            'enable_cdc': 0,
            'mirror_db_uuid': '',
            'sync_mode': 1,
            'dump_thd': 1,
            'drop_old_tab': 1,
            '_': '95f4e88ab554',
            'uuid': '',
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
        }
        
        sqlserver = Sqlserver(a)
        r = sqlserver.deleteRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'deleteRule', body)

    def testOperateRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        sqlserver = Sqlserver(a)
        r = sqlserver.operateRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'operateRule', body)

    def testListRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
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
            'rule_uuid': '',},
        }
        
        sqlserver = Sqlserver(a)
        r = sqlserver.listRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Sqlserver', 'listRule', body)

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
