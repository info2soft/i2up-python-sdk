
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import TbCmp
from info2soft.stream.v20250630.TbCmp import TbCmp
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


class TbCmpTestCase(unittest.TestCase):
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

    def testCreateTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'db_user_map': [{
            'src': [{
            'user': '',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'tgt': [{
            'user': '',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},],},],},],
            'config': {
            'v_tabmap': [{
            'src_user': '',
            'src_tb': '',
            'src_sql': '',
            'tgt_user': '',
            'tgt_tb': '',
            'tgt_sql': '',
            'key': '',},],
            'globalConfig': {
            'dkdiff_enable_step_count_table': '""',
            'dkdbsource_diff_only_key_columns': False,
            'dkmagic_plan_max_diffs': 10000,
            'dkfilesink_enable_sqlpatch_file': False,
            'dkmagic_plan_number_tolerance_type': 'absolute',
            'dkmagic_plan_number_tolerance': 1,
            'dkmagic_plan_datetime_tolerance': 1,
            'split_table_schedule_cron': '""',
            'split_table_single_segment_max_rows': 5000000,
            'split_table_result_expire_in_seconds': 0,
            'dkdiffengine_recursion_max_steps': 1,
            'dkdiffengine_recursion_interval_step_delay': 0,
            'dkdbsource_left_ignore_type_names': '""',
            'dkdbsource_right_ignore_type_names': '""',
            'dkdbsource_left_ignore_column_names': '""',
            'dkdbsource_right_ignore_column_names': '',
            'globalconfig': [{
            'key': '',
            'value': '',},],
            'tolerance': False,
            'execute_patch_after_complete': '',},
            'data_select': [{
            'src_user': '',
            'src_tb': '',
            'src_query': '',
            'dst_user': '',
            'dst_tb': '',
            'dst_query': '',},],
            'compare_key': [{
            'src_user': '',
            'src_tb': '',
            'dst_user': '',
            'dst_tb': '',
            'src_dst_key': '',},],
            'globals': [{
            'src_user': '',
            'dst_user': '',
            'src_query': '',
            'dst_query': '',},],
            'exclude_tables': [{
            'src_user': '',
            'src_tb': '',
            'dst_user': '',
            'dst_tb': '',},],
            'timestamps': {
            'column_name': '',
            'back_delay_in_seconds': 1,
            'end_time': '',},
            'global_time_limit': False,},
            'db_map': {
            'src': [{
            'db_uuid': '',
            'auth_uuid': '',},],
            'tgt': [{
            'db_uuid': '',
            'auth_uuid': '',},],},
            'interval': '10m',
            'tb_cmp_name': '规则名',
            'src_db_uuids': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuids': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'cmp_type': 'table',
            'filter_table': '[user.table]',
            'db_tb_map': [{
            'src': [{
            'user': 'xljv',
            'tab': 'fhdhz',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'tgt': [{
            'user': '',
            'tab': '',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'regex_switch': '1',
            'col': '{"col1":"col2", "col3":"col4"}',},{
            'src': [{
            'user': 'ajhwj',
            'tab': 'tblqbo',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'tgt': [{
            'user': '',
            'tab': '',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'regex_switch': '1',
            'col': '{"col1":"col2", "col3":"col4"}',},{
            'src': [{
            'user': 'pthft',
            'tab': 'xkldvlq',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'tgt': [{
            'user': '',
            'tab': '',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'regex_switch': '1',
            'col': '{"col1":"col2", "col3":"col4"}',},{
            'src': [{
            'user': 'xeomtjcc',
            'tab': 'etbefx',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'tgt': [{
            'user': '',
            'tab': '',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'regex_switch': '1',
            'col': '{"col1":"col2", "col3":"col4"}',},{
            'src': [{
            'user': 'qqoomeufl',
            'tab': 'guj',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'tgt': [{
            'user': '',
            'tab': '',
            'dbs': [{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},{
            'db_uuid': '',
            'auth_uuid': '',},],},],
            'regex_switch': '1',
            'col': '{"col1":"col2", "col3":"col4"}',},],
            'dump_thd': 1,
            'polices': '"0|00:00',
            'policy_type': 'one_time',
            'concurrent_table': [
            'hh.ww',],
            'try_split_part_table': 0,
            'one_time': '2019-05-27 16:07:08',
            'tb_cmp_type': '',
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.createTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'createTbCmp', body)

    def testListSyncTbCmpStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'bf0c71AE-6278-dfbe-E4CA-BC1d1Acf352D',],
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.listSyncTbCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'listSyncTbCmpStatus', body)

    def testStopTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': '168AD53b-a9eE-B161-09fa-15CEe1E21D7D',
            'tab': '[\"asda.asdsa\"]',
            'fix_relation': 1,
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.stopTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'stopTbCmp', body)

    def testRestartTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': '26D6d4eC-bE84-2Ed3-eB8d-4EE17B52bdb1',
            'tab': '[\"asda.asdsa\"]',
            'fix_relation': 1,
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.restartTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'restartTbCmp', body)

    def testCmpStopTime(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': '16Be3A0E-133c-5Ab6-f7cD-68EA1bCf4e46',
            'tab': '[\"asda.asdsa\"]',
            'fix_relation': 1,
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.cmpStopTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'cmpStopTime', body)

    def testCmpResumeTime(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': '483Bce9C-3e2f-F96B-89c1-A10b45D9ED89',
            'tab': '[\"asda.asdsa\"]',
            'fix_relation': 1,
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.cmpResumeTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'cmpResumeTime', body)

    def testCmpImmediate(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'fbbBCAcd-7D32-f6a8-2fBC-2AAfBC063EeD',
            'tab': '[\"asda.asdsa\"]',
            'fix_relation': 1,
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.cmpImmediate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'cmpImmediate', body)

    def testDescribeSyncTbCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'uuid': 'AaB8F2aA-5fFB-49eB-91Bb-2CE9eCefCfaB',
            'start_time': '',
            'flag': 1,
            'user': '',
            'table': '',
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.describeSyncTbCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'describeSyncTbCmpResult', body)

    def testDescribeTbCmpErrorMsg(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'uuid': 'AD21c46C-ec77-56AE-3d8e-eED004996B93',
            'start_time': '',
            'key_name': '',
            'column_name': '',
            'src_db': '',
            'tgt_db': '',
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.describeTbCmpErrorMsg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'describeTbCmpErrorMsg', body)

    def testExportSyncTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'include_active_db': 1,
            'include_active_node': 1,
            'rule_uuids': [],
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.exportSyncTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'exportSyncTbCmp', body)

    def testListSyncTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'where_args': '',
        }
        
        
        tbCmp = TbCmp(a)
        r = tbCmp.listSyncTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'listSyncTbCmp', body)


if __name__ == '__main__':
    unittest.main()
