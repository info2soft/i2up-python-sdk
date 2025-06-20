
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import MongoDB
from info2soft.active.v20250630.MongoDB import MongoDB
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


class MongoDBTestCase(unittest.TestCase):
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

    def testCreateMongoRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'tgt_type': 'sqlserver',
            'map_type': 'db',
            'config': {
            'start_rule_now': 1,
            'table_map': '',
            'full_sync': 0,
            'incre_sync': 1,
            'kafka': {
            'binary_code': '',},
            'kafka_time_out': '',
            'part_load_balance': '',
            'kafka_message_encoding': '',
            'dbmap_topic': '',
            'db_user_map': '',},
        }
        
        
        mongoDB = MongoDB(a)
        r = mongoDB.createMongoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MongoDB', 'createMongoRule', body)

    def testModifyMongoRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'tgt_type': 'sqlserver',
            'map_type': 'db',
            'config': {
            'start_rule_now': 1,
            'table_map': '',
            'full_sync': 0,
            'incre_sync': 1,
            'kafka': {
            'binary_code': '',},
            'kafka_time_out': '',
            'part_load_balance': '',
            'kafka_message_encoding': '',},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mongoDB = MongoDB(a)
        r = mongoDB.modifyMongoRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MongoDB', 'modifyMongoRule', body)

    def testDeleteMongoRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 'true',
        }
        
        
        mongoDB = MongoDB(a)
        r = mongoDB.deleteMongoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MongoDB', 'deleteMongoRule', body)

    def testResumeMongoRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        mongoDB = MongoDB(a)
        r = mongoDB.resumeMongoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MongoDB', 'resumeMongoRule', body)

    def testStopMongoRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        mongoDB = MongoDB(a)
        r = mongoDB.stopMongoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MongoDB', 'stopMongoRule', body)

    def testRestartMongoRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        mongoDB = MongoDB(a)
        r = mongoDB.restartMongoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MongoDB', 'restartMongoRule', body)

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
        
        
        mongoDB = MongoDB(a)
        r = mongoDB.listRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MongoDB', 'listRule', body)

    def testDescribeListRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        mongoDB = MongoDB(a)
        r = mongoDB.describeListRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MongoDB', 'describeListRule', body)


if __name__ == '__main__':
    unittest.main()
