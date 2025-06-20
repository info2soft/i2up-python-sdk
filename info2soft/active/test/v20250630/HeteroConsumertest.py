
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import HeteroConsumer
from info2soft.active.v20250630.HeteroConsumer import HeteroConsumer
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


class HeteroConsumerTestCase(unittest.TestCase):
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

    def testListConsumerRules(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'limit': 1,
            'page': 1,
            'search_field': 'tgt_type',
            'where_args': {
            'status': '',
            'src_db_name': 'test',
            'tgt_db_name': '',
            'db_ip': '',
            'node_ip': '',
            'username': '',
            'name': '',
            'uuid': '9EFE6FC2-7CDc-bab8-c5cd-6b17FcAecC7f',},
        }
        
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.listConsumerRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'listConsumerRules', body)

    def testCreateConsumerRule(self):
        a = Auth(username, pwd)
        body = {
            'config': {
            'machine_num': 1,
            'target_user': 'oracle',
            'target_db_name': 'Eric Young',
            'error_deal': '',
            'db_name': 'Maria Williams',
            'kerberos_certify': False,
            'goldendb_config': {
            'machine_number': 1,
            'distribute_type': '',},
            'insert_date_config': {
            'enable': False,
            'column_name': 'ETL_INSERT_DATE',},
            'primary_key_config': {
            'primary_key_config': 'primaryKey',
            'use_insert_date': False,
            'use_rowid': False,
            'use_source_table_key': False,},
            'table_engine': '',
            'existing_table': '',
            'target_user_map': '{}',
            'binary_code': '',
            'hudi_config': {
            'capacity': 20000,
            'table_type': '',
            'merge_commits': 1,
            'delay_time': 1,
            'batch_size': 1,
            'hive_schema': 'default',},
            'hdfs_config': {
            'auth': '',
            'principal': '',
            'keytab': '',
            'kbsuser': '',},
            'error_handling': {
            'load_err_set': 'continue',},
            'load_err_set': '',
            'part_config': [{
            'part_index': 0,
            'part_col_name': 'null',
            'part_type': 'ALL',
            'part_from_col_name': 'null',
            'part_from_date_format': 'null',},{
            'part_index': 1,
            'part_col_name': 'null',
            'part_type': 'ALL',
            'part_from_col_name': 'null',
            'part_from_date_format': 'null',},],
            'dmltrack': {
            'enable': False,
            'tmcol': '1',},},
            'kudu_partition_config': [],
            'impala_connected': False,
            'init_offset_type': 'earlist',
            'encrypt_column_switch': 1,
            'encrypt_column_method': 1,
            'encrypt_column_key': '',
            'encrypt_columns': [{
            'user': '',
            'table': '',
            'column': '',},],
            'tabmap': [{
            'src_table': 'src_t',
            'dst_table': 'dst_t',
            'kudu_partition_config': {
            'hashSetting': False,
            'hash_definitions': [],
            'rangSetting': False,
            'range_definition': {
            'range_columns': '',
            'range_partitions': [],},},
            'column': [{
            'dst_column': '',
            'src_column': '',},],},],
            'consumer_thread_num': 2,
            'actload_thread_num': 4,
            'tgt_db_uuid': '1C5F3C4B-7333-9518-7349-9712BC9ED664',
            'name': 'James Wilson',
            'src_db_uuid': 'B5CED857-275C-77C4-0561-887F7C890FF2',
            'tgt_type': 'oracle',
            'init_offset': [{
            'topic': 'test',
            'offset': '1',
            'partition': '1',},],
            'topic': 'test1',
            'dst_topic': 'topic1',
        }
        
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.createConsumerRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'createConsumerRule', body)

    def testModifyConsumerRule(self):
        a = Auth(username, pwd)
        body = {
            'kudu_partition_config': [{
            'hashSetting': False,
            'hash_definitions': [],
            'rangSetting': False,
            'rang_definition': [{
            'range_colums': '',
            'range_partitions': 1,},],},],
            'impala_connected': False,
            'config': {
            'error_deal': '',
            'goldendb_config': {
            'machine_number': 1,
            'distribute_type': '',},
            'insert_date_config': {
            'enable': False,
            'column_name': '',},
            'primary_key_config': {
            'primary_key_config': '',
            'use_insert_date': False,
            'use_rowid': False,
            'use_source_table_key': False,},
            'target_user': 'oracle',
            'target_db_name': 'Mark Lewis',
            'db_name': 'Eric Jackson',
            'kerberos_certify': False,
            'dmltrack': {
            'enable': False,
            'tmcol': '',},
            'target_user_map': '',
            'part_config': 'none',
            'machine_num': 1,
            'existing_table': '',
            'error_handling': {
            'load_err_set': '',},
            'load_err_set': '',
            'binary_code': '',},
            'init_offset_type': 'seek',
            'modify': True,
            'tabmap': [{
            'src_table': 'src-t6',
            'dst_table': 'dst-t6',},],
            'consumer_thread_num': 41,
            'actload_thread_num': 41,
            'tgt_db_uuid': '773AE76A-7DB6-E465-2508-3919C875916E',
            'name': 'm-k-hive',
            'src_db_uuid': '86A56D69-72DE-AA2F-1C7E-C0A843F1D9EA',
            'tgt_type': 'hive',
            'init_offset': [{
            'topic': 'test4',
            'offset': '18684815',
            'partition': '0',},],
            'dst_topic': 'dst_topic',
            'uuid': '356FF271-0D32-C35A-75A2-C68AD3A70FB3',
            'start_rule_now': 1,
            'topic': 'test4',
            'user_uuid': '1BCFCAA3-E3C8-3E28-BDC5-BE36FDC2B5DC',
        }
        
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.modifyConsumerRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'modifyConsumerRule', body)

    def testDeleteConsumerRules(self):
        a = Auth(username, pwd)
        body = {
            'force': True,
            'uuids': [
            'E0b16C61-B0CF-DCB0-27Be-D959908Db11A',
            'FC83c727-5828-DfdA-B425-cc92E31815fA',],
        }
        
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.deleteConsumerRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'deleteConsumerRules', body)

    def testListConsumerStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.listConsumerStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'listConsumerStatus', body)

    def testStopConsumerRule(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '5D52f329-56dc-A4AB-Fbd4-e39A5E37B6Ed',
            'operate': 'resume',
        }
        
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.stopConsumerRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'stopConsumerRule', body)

    def testResumeConsumerRule(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'B3050940-49d9-AA8c-F3CC-C1AbadBfd14A',
            'operate': 'resume',
        }
        
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.resumeConsumerRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'resumeConsumerRule', body)

    def testDescribeConsumerRules(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '75DF8EA3-6480-4137-451B-731F04F368AF',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.describeConsumerRules(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'describeConsumerRules', body)

    def testExportConsumerRule(self):
        a = Auth(username, pwd)
        body = {
            'include_active_db': 1,
            'include_active_node': 1,
            'rule_uuids': [],
        }
        
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.exportConsumerRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'exportConsumerRule', body)

    def testImportHeteroConsumerTopicMapping(self):
        a = Auth(username, pwd)
        body = {
            'file': '',
        }
        
        
        heteroConsumer = HeteroConsumer(a)
        r = heteroConsumer.importHeteroConsumerTopicMapping(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HeteroConsumer', 'importHeteroConsumerTopicMapping', body)


if __name__ == '__main__':
    unittest.main()
