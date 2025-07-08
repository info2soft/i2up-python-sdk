
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import RocketMq
from info2soft.active.v20250630.RocketMq import RocketMq
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


class RocketMqTestCase(unittest.TestCase):
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

    def testCreateRocketMqRule(self):
        a = Auth(username, pwd)
        body = {
            'map_type': '',
            'user_map': [],
            'tgt_db_uuid': '1C5F3C4B-7333-9518-7349-9712BC9ED664',
            'name': 'Carol Wilson',
            'src_db_uuid': 'B5CED857-275C-77C4-0561-887F7C890FF2',
            'tgt_type': 'oracle',
        }
        
        
        rocketMq = RocketMq(a)
        r = rocketMq.createRocketMqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RocketMq', 'createRocketMqRule', body)

    def testModifyRocketMqRule(self):
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
            'target_db_name': 'Barbara Jones',
            'db_name': 'John Walker',
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
        
        
        rocketMq = RocketMq(a)
        r = rocketMq.modifyRocketMqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RocketMq', 'modifyRocketMqRule', body)

    def testDeleteRocketMqRules(self):
        a = Auth(username, pwd)
        body = {
            'force': True,
            'uuids': [
            'A3699EC9-ff51-a4bd-52b6-b5dFEEf6fbFc',
            '10FB7DFA-C9c1-9F96-fA73-7Fd912EaA0eA',],
        }
        
        
        rocketMq = RocketMq(a)
        r = rocketMq.deleteRocketMqRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RocketMq', 'deleteRocketMqRules', body)

    def testListRocketMqStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        rocketMq = RocketMq(a)
        r = rocketMq.listRocketMqStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RocketMq', 'listRocketMqStatus', body)

    def testStopRocketMqRule(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'FB6194fe-13A2-3FE4-Ee2D-033BB6D1A442',
            'operate': 'resume',
        }
        
        
        rocketMq = RocketMq(a)
        r = rocketMq.stopRocketMqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RocketMq', 'stopRocketMqRule', body)

    def testResumeRocketMqRule(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '7173DBBE-b8fe-DCfD-13Bc-6FFA1FDbcc82',
            'operate': 'resume',
        }
        
        
        rocketMq = RocketMq(a)
        r = rocketMq.resumeRocketMqRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RocketMq', 'resumeRocketMqRule', body)

    def testListRocketMqRules(self):
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
            'uuid': '2b3e1549-efC6-1DA2-3d79-125e8673CFDd',},
        }
        
        
        rocketMq = RocketMq(a)
        r = rocketMq.listRocketMqRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RocketMq', 'listRocketMqRules', body)

    def testDescribeRocketMqRules(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '75DF8EA3-6480-4137-451B-731F04F368AF',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        rocketMq = RocketMq(a)
        r = rocketMq.describeRocketMqRules(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RocketMq', 'describeRocketMqRules', body)


if __name__ == '__main__':
    unittest.main()
