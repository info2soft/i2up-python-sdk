
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import TbCmp
from info2soft.stream.v20240228.TbCmp import TbCmp
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
            'dkdbsource_diff_only_key_columns': '',
            'dkmagic_plan_max_diffs': 10000,
            'dkfilesink_enable_sqlpatch_file': '',
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
            'tolerance': '',
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
            'global_time_limit': '',},
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
            'user': 'nvhwpmbdxg',
            'tab': 'xyufebbs',
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
            'user': 'utum',
            'tab': 'kzgsvhpseq',
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
            'user': 'bqnrmua',
            'tab': 'srmh',
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
            'user': 'hvezk',
            'tab': 'noxzj',
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
            'user': 'sbxvtrs',
            'tab': 'vmuwepg',
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

    def testStopTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'e8b6a69b-a32C-B1Ee-bc7F-a12bfBe4fbbB',
            'tab': [
            'd.a',],
            'fix_relation': 1,
        }
        
        tbCmp = TbCmp(a)
        r = tbCmp.stopTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'stopTbCmp', body)

    def testrestartTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'e8b6a69b-a32C-B1Ee-bc7F-a12bfBe4fbbB',
            'tab': [
            'd.a',],
            'fix_relation': 1,
        }

        tbCmp = TbCmp(a)
        r = tbCmp.restartTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'restartTbCmp', body)

    def testcmpStopTime(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'e8b6a69b-a32C-B1Ee-bc7F-a12bfBe4fbbB',
            'tab': [
            'd.a',],
            'fix_relation': 1,
        }

        tbCmp = TbCmp(a)
        r = tbCmp.cmpStopTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'cmpStopTime', body)

    def testcmpResumeTime(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'e8b6a69b-a32C-B1Ee-bc7F-a12bfBe4fbbB',
            'tab': [
            'd.a',],
            'fix_relation': 1,
        }

        tbCmp = TbCmp(a)
        r = tbCmp.cmpResumeTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TbCmp', 'cmpResumeTime', body)


if __name__ == '__main__':
    unittest.main()
