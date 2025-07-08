
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Tidb
from info2soft.active.v20250630.Tidb import Tidb
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


class TidbTestCase(unittest.TestCase):
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

    def testCreateTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'db_map': [{
            'dst_table': '',
            'src_table': '',},],
            'part_load_balance': '',
            'kafka_time_out': '',
            'full_sync_mode': 'auto',
            'db_set': {
            'binlog_format': 'row',
            'binlog_row_image': 'full',
            'default_storage_engine': 'innoDB',
            'sync_binlog': '1',
            'innodb_flush_log': '2',
            'innodb_flush_method': 'O_DIRECT',
            'max_allowed_packet': '52',
            'open_files_limit': '65535',
            'server_id': '123456',
            'expire_logs_days': '7',
            'nat_mode': 0,
            'ip': '',},
            'full_sync_set': {
            'start_lsn': 1,
            'support_ddl': 1,
            'change_tf_path': '',
            'tf_file_save_time': 7,
            'nat_mode': 0,
            'foreign_ip': '',
            'extraction': 0,},
            'modify': False,
            'primary_db_one': '',
            'primary_map_type_one': '',
            'primary_map_one': '',
            'primary_db_two': '',
            'primary_map_type_two': '',
            'start_src_db_set': 0,
            'primary_map_two': '',
            'dst_db_set': {
            'binlog_format': '',
            'binlog_row_image': '',
            'default_storage_engine': '',
            'sync_binlog': '',
            'innodb_flush_log': '',
            'innodb_flush_method': '',
            'max_allowed_packet': '',
            'open_files_limit': '',
            'server_id': '',
            'expire_logs_days': '',
            'nat_mode': 1,
            'ip': '',},
            'dst_full_sync_set': {
            'start_lsn': 1,
            'support_ddl': 1,
            'change_tf_path': '',
            'tf_file_save_time': '',
            'nat_mode': '',
            'foreign_ip': '',
            'extraction': 0,},
            'start_dst_db_set': 0,
            'mysql_name': True,
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
            'jointing': {
            'op': '',
            'table': '',
            'content': '',},},
            'save_json_text': False,
        }
        
        
        tidb = Tidb(a)
        r = tidb.createTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'createTidbRule', body)

    def testModifyTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'config': {
            'kafka_time_out': '',
            'part_load_balance': '',},
            'mysql_name': 'mysql',
            'src_db_uuid': ' 1B1153F6-DAD9-BC39-888A-A743FCC208E5',
            'tgt_db_uuid': ' D42BF707-C971-EEA9-521F-BB0F3F7A92FC',
            'tgt_type': 'kafka',
            'start_rule_now': 0,
            'node_uuid': ' 6B1153F6-DAD9-BC39-888A-A743FCC208E6',
            'dbmap_topic': '',
            'map_type': 'table',
            'tab_map': [{
            'src_table': 'src_table',
            'topic': 'topic',},],
            'full_sync': 0,
            'incre_sync': 1,
            'model_type': '1:0',
            'full_sync_mode': 'auto',
            'db_set': {
            'db_node': '1B1153F6-DAD9-BC39-888A-A743FCC208E5',
            'binlog_format': 'row',
            'binlog_row_image': 'full',
            'default_storage_engine': 'innoDB',
            'sync_binlog': '1',
            'innodb_flush_log': '2',
            'innodb_flush_method': 'O_DIRECT',
            'max_allowed_packet': '52',
            'open_files_limit': '65535',
            'server_id': '123456',
            'expire_logs_days': '7',
            'nat_mode': 0,
            'ip': '',},
            'full_sync_set': {
            'support_ddl': 1,
            'node': ' 6B1153F6-DAD9-BC39-888A-A743FCC208E6',
            'change_tf_path': '',
            'tf_file_save_time': 7,
            'nat_mode': 0,
            'foreign_ip': '',},
            'primary_node_one': '',
            'primary_node_two': '',
            'primary_db_one': '',
            'primary_map_type_one': '',
            'primary_map_one': [],
            'primary_db_two': '',
            'primary_map_type_two': '',
            'primary_map_two': [],
            'db_map': [{
            'src_db': 'src_db',
            'dst_db': 'dst_db',},],
            'mysql_uuid': '5349E2CF-7DBO-OAF2-13CB-BB7DFD8A9D86',
        }
        
        
        tidb = Tidb(a)
        r = tidb.modifyTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'modifyTidbRule', body)

    def testDeleteTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'force': True,
            'mysql_uuids': [],
        }
        
        
        tidb = Tidb(a)
        r = tidb.deleteTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'deleteTidbRule', body)

    def testDescribeTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'mysql_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        tidb = Tidb(a)
        r = tidb.describeTidbRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'describeTidbRule', body)

    def testResumeTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': 'b1443Fbf-FEc2-Bd3f-fD5f-CEAF758cC6E2',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.resumeTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'resumeTidbRule', body)

    def testStopTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': 'f6DF576e-D6e5-CDEA-3FbC-7eb8B8dbcf9f',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.stopTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'stopTidbRule', body)

    def testRestartTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': 'bC659fb4-B9f8-7834-963F-ed3B4Fc689b4',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.restartTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'restartTidbRule', body)

    def testStartParsingTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': 'b0b4eccE-Fcd3-564D-7fD1-9cADdA132Ca1',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.startParsingTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'startParsingTidbRule', body)

    def testStopParsingTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': 'dAb95aac-214D-51da-EdCA-71c6a7DDeD0D',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.stopParsingTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'stopParsingTidbRule', body)

    def testResetParsingTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': 'd80DE12e-cD7d-E943-0Ac1-b6ADA5f2b9Fa',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.resetParsingTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'resetParsingTidbRule', body)

    def testStartLoadTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': 'B3DaFFC2-661A-7197-bc7f-DBc950b2CE0e',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.startLoadTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'startLoadTidbRule', body)

    def testStopLoadTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '57B188b9-3d7c-D8df-25fA-f5f8C6d2d7bA',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.stopLoadTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'stopLoadTidbRule', body)

    def testResetLoadTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': 'd1cf9f16-9E7A-5ADD-869d-aDABAe384eD1',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.resetLoadTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'resetLoadTidbRule', body)

    def testRemoveTidbRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'mysql_uuid': '5dBD6AF4-34B3-cefe-f2C5-87bD312BdAc8',
            'scn': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.removeTidbRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'removeTidbRule', body)

    def testListTidbRules(self):
        a = Auth(username, pwd)
        body = {
            'where_args': {
            'mysql_uuid': 'cc5B9E39-40DC-62cf-e53f-8A4915D536fF',},
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }
        
        
        tidb = Tidb(a)
        r = tidb.listTidbRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tidb', 'listTidbRules', body)


if __name__ == '__main__':
    unittest.main()
