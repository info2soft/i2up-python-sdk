
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Redis
from info2soft.active.v20250123.Redis import Redis
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


class RedisTestCase(unittest.TestCase):

    def testCreateRedisRule(self):
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
            'kafka': {},
            'sync_mode': '是否全量同步',
        }
        
        
        redis = Redis(a)
        r = redis.createRedisRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Redis', 'createRedisRule', body)

    def testModifyRedisRule(self):
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
        
        redis = Redis(a)
        r = redis.modifyRedisRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Redis', 'modifyRedisRule', body)

    def testDeleteRedisRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 'true',
        }
        
        
        redis = Redis(a)
        r = redis.deleteRedisRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Redis', 'deleteRedisRule', body)

    def testResumeRedisRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        redis = Redis(a)
        r = redis.resumeRedisRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Redis', 'resumeRedisRule', body)

    def testStopRedisRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        redis = Redis(a)
        r = redis.stopRedisRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Redis', 'stopRedisRule', body)

    def testRestartRedisRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        redis = Redis(a)
        r = redis.restartRedisRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Redis', 'restartRedisRule', body)

    def testListRedisRule(self):
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
        
        
        redis = Redis(a)
        r = redis.listRedisRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Redis', 'listRedisRule', body)

    def testDescribeRedisRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        redis = Redis(a)
        r = redis.describeRedisRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Redis', 'describeRedisRule', body)


if __name__ == '__main__':
    unittest.main()
