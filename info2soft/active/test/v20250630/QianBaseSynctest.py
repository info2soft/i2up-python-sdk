
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import QianBaseSync
from info2soft.active.v20250630.QianBaseSync import QianBaseSync
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


class QianBaseSyncTestCase(unittest.TestCase):
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

    def testListQianbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'group_uuid': '',
            'where_args': {
            'rule_uuid': '',
            'status': '',
            'src_db_name': '',
            'tgt_db_name': '',
            'db_ip': '',
            'node_ip': '',
            'username': '',
            'rule_name': '',},
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
            'dst_table': '',},],
            'custom_config': [{
            'key': '',
            'value': '',},],
            'tgt_type': '',},],
            'all_custom_config': [{
            'key': '',
            'value': '',},],
            'sync_content': [{
            'sync_col': '',},],
            'jointing': {
            'table': '',
            'op': '',
            'content': '',},
            'save_json_text': '',
            'kafka_db_uuid': '',
            'conn_num': 1,
            'loader': 1,
            'schema_name': '',},
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
            'full_sync_mode': '1',
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
            'dst_table': '',},],
            'custom_config': [{
            'key': '',
            'value': '',},],},],
            'all_custom_config': [{
            'key': '',
            'value': '',},],
            'sync_content': [{
            'sync_col': '',},],},
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

    def testStopQianbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
            'scn': '',
        }
        
        
        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.stopQianbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'stopQianbaseRule', body)

    def testRestartQianbaseRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': [],
            'scn': '',
        }
        
        
        qianBaseSync = QianBaseSync(a)
        r = qianBaseSync.restartQianbaseRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'QianBaseSync', 'restartQianbaseRule', body)

    def testListQianbaseRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'date_start': 1,
            'date_end': 1,
            'type': 1,
            'module_type': 1,
            'query_type': 1,
            'rule_uuid': '4E70Db1B-86C8-bAd3-FE7e-7cAF4f589d7c',
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


if __name__ == '__main__':
    unittest.main()
