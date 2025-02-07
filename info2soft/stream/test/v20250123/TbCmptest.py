
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import TbCmp
from info2soft.stream.v20250123.TbCmp import TbCmp
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
            'user': 'umsmohae',
            'tab': 'wscl',
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
            'user': 'hbyvjc',
            'tab': 'finrugw',
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
            'user': 'wwxy',
            'tab': 'vfvu',
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
            'user': 'fgofigrz',
            'tab': 'yhfp',
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
            'user': 'tlpidws',
            'tab': 'mdcthcqvt',
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
            'tb_cmp_uuids': 'eC7fb5F1-e217-929F-79Db-AbFbe383F6b6',
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
            'tb_cmp_uuids': 'aCC1f8bD-c3c3-8E39-E1F4-be06f94d7daf',
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
            'tb_cmp_uuids': '5AbCCa91-6d26-79Ec-944B-82599bDf7c8E',
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
            'tb_cmp_uuids': 'b1D8BE75-2c23-aaDD-BC52-5DEcda2A8A7e',
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
            'tb_cmp_uuids': 'DB5755eC-49EB-FEfB-451E-fC8FbC24916A',
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
            'uuid': '8EDFe474-CBe0-1b6e-16d8-2f68f9c582E9',
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
            'uuid': '42cABbDB-F1D7-7e82-FD5b-37FdEd7Feb28',
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


if __name__ == '__main__':
    unittest.main()
