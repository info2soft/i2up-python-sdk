
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import MaskRule
from info2soft.stream.v20250630.MaskRule import MaskRule
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


class MaskRuleTestCase(unittest.TestCase):
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

    def testListSummary(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        maskRule = MaskRule(a)
        r = maskRule.listSummary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'listSummary', body)

    def testListSummaryView(self):
        a = Auth(username, pwd)
        body = {
            'src': '',
            'dst': '',
            'status': '',
            'type': '',
            'ip': '',
        }
        
        
        maskRule = MaskRule(a)
        r = maskRule.listSummaryView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'listSummaryView', body)

    def testListMaskRules(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 0,
        }
        
        
        maskRule = MaskRule(a)
        r = maskRule.listMaskRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'listMaskRules', body)

    def testCreateMaskRules(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '1231',
            'node_uuid': 'A6ABF8BC-38AF-41FE-ACF7-DD9F28B0FA3F',
            'tgt_db_uuid': '32C50055-A267-1E9E-65EE-FC6AAB75D390',
            'src_db_uuid': '38F1AD45-5F72-2E51-DC01-0593A14A8D17',
            'other_settings': {
            'can_approve': 0,
            'etl_settings': {
            'etl_table': [{
            'table': '',
            'user': '',
            'addInfo': '',
            'oprType': '',
            'process': '',},],},
            'src_type': 'oracle',
            'tgt_type': 'oracle',
            'src_path': '/var/i2data/cache/',
            'file_names': [],
            'size': 1024,
            'tgt_path': '/var/i2data/cache/',
            'compress_level': 0,
            'policy': {
            'policy_type': 'immediate',
            'one_time': '',
            'time_policy': '',},},
            'table_space_map': {
            'tgt_table_space': '',
            'table_mapping_way': 'ptop',
            'table_path_map': [],
            'table_space_name': [],},
            'full_sync_obj_filter': [
            'INDEX',
            'VIEW',
            'FUNCTION',
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'SYNONYM',
            'TRIGGER',
            'SEQUENCE',
            'JAVA CLASS',
            'TYPE',
            'TYPE BODY',
            'MATERIALIZED VIEW',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],
            'db_user_map': '',
            'table_map': '',
            'map_type': 'db',
            'full_sync_settings': {
            'his_thread': 1,},
            'db_map_uuid': '71D59BCE-17F3-ED0D-BC76-132833F72498',
            'strate': '',
            'modify': False,
            'bw_settings': {
            'bw_limit': '',},
            'mask_algo_id': 1,
        }
        
        
        maskRule = MaskRule(a)
        r = maskRule.createMaskRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'createMaskRules', body)

    def testStartMaskRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        maskRule = MaskRule(a)
        r = maskRule.startMaskRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'startMaskRule', body)

    def testStopMaskRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        
        maskRule = MaskRule(a)
        r = maskRule.stopMaskRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'stopMaskRule', body)

    def testDeleteMaskRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        
        
        maskRule = MaskRule(a)
        r = maskRule.deleteMaskRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'deleteMaskRule', body)

    def testDescribeMaskRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        maskRule = MaskRule(a)
        r = maskRule.describeMaskRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'describeMaskRule', body)

    def testListMaskRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        maskRule = MaskRule(a)
        r = maskRule.listMaskRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'listMaskRuleStatus', body)

    def testImportMaskRuleInfo(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        maskRule = MaskRule(a)
        r = maskRule.importMaskRuleInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MaskRule', 'importMaskRuleInfo', body)


if __name__ == '__main__':
    unittest.main()
