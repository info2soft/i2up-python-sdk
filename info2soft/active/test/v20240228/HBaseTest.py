
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import HBase
from info2soft.active.v20240228.HBase import HBase
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


class HBaseTestCase(unittest.TestCase):

    def testCreateHbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'save_json_text': '',
            'db_map': [{
            'dst_table': '',
            'src_table': '',},],
            'part_load_balance': '',
            'kafka_time_out': '',
            'full_sync_mode': 'auto',
            'modify': '',
            'mysql_name': 1,
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
            'dst_db': '222',},],
            'full_sync': 0,
            'incre_sync': 1,
            'model_type': '1:0',
            'config': {
            'jointing': {
            'op': '',
            'table': '',
            'content': '',},
            'src_connect_user': '',
            'dst_connect_user': '',
            'binary_code': 'hex',
            'table_change_info': 1,
            'etl_settings': {
            'etl_table': [{
            'oprType': 'IRP',
            'table': '',
            'user': '',
            'process': 'SKIP',
            'addInfo': '',},],},
            'bw_settings': {
            'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'full_sync_settings': {
            'clean_user_before_dum': 0,
            'concurrent_table': [],
            'dump_thd': 1,
            'load_thd': 1,
            'existing_table': 'drop_to_recycle',
            'try_split_part_table': 1,},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'INDEX',
            'VIEW',
            'FUNCTION',],},
            'dml_track': {
            'delcol': '',
            'drp': 1,
            'enable': 1,
            'tmcol': '',
            'urp': 1,},
            'rpc_server': {
            'zookeeper': {
            'set': [{
            'ip': '',
            'port': '',
            'zk_node': '',},],},
            'peer': '',},},
        }
        
        hBase = HBase(a)
        r = hBase.createHbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HBase', 'createHbaseRule', body)

    def testDeleteHbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'force': 1,
            'rule_uuids': [],
        }
        
        hBase = HBase(a)
        r = hBase.deleteHbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HBase', 'deleteHbaseRule', body)

    def testDescribeHbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'mysql_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        hBase = HBase(a)
        r = hBase.describeHbaseRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HBase', 'describeHbaseRule', body)

    def testOperateHbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'tf': '',
            'operate': 'restart',
            'mysql_uuid': '6A1Cd2eA-98Eb-Cfed-2019-CE0e63Fbd8Fa',
            'scn': '',
        }
        
        hBase = HBase(a)
        r = hBase.operateHbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HBase', 'operateHbaseRule', body)

    def testListHbaseRules(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }
        
        hBase = HBase(a)
        r = hBase.listHbaseRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HBase', 'listHbaseRules', body)


if __name__ == '__main__':
    unittest.main()
