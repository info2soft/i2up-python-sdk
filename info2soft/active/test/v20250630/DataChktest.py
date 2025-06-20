
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import DataChk
from info2soft.active.v20250630.DataChk import DataChk
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


class DataChkTestCase(unittest.TestCase):
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

    def testListDatacheckObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': 'obj_cmp_name',
            'search_value': 'test',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.listDatacheckObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'listDatacheckObjCmp', body)

    def testCreateDatacheckObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'db_user_map': {'src_user':'dst_user'},
            'config': {
            'one_task': 'immediate',},
            'policies': '',
            'policy_type': 'periodic',
            'one_time': '2019-05-27 16:07:08',
            'repair': 1,
            'obj_cmp_name': 'test',
            'src_db_uuid': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuid': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'cal_table_recoders': 1,
            'cmp_type': 'user',
            'rule_uuid': '751A03F5-C97D-645B-82B2-316A5D198528',
            'src_db_auth_uuid': '',
            'tgt_db_auth_uuid': '',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.createDatacheckObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'createDatacheckObjCmp', body)

    def testDeleteDatacheckObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'force': False,
            'uuids': '[@guid]',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.deleteDatacheckObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'deleteDatacheckObjCmp', body)

    def testDescribeDatacheckObjCmp(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dataChk = DataChk(a)
        r = dataChk.describeDatacheckObjCmp(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeDatacheckObjCmp', body)

    def testStopObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.stopObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'stopObjCmp', body)

    def testRestartObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.restartObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'restartObjCmp', body)

    def testCmpStopTimeObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.cmpStopTimeObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'cmpStopTimeObjCmp', body)

    def testCmpResumeTimeObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.cmpResumeTimeObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'cmpResumeTimeObjCmp', body)

    def testCmpImmediateObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.cmpImmediateObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'cmpImmediateObjCmp', body)

    def testListDatacheckObjCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'B83CA2af-8eb6-089A-CbF8-2ca69123FeAE',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.listDatacheckObjCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'listDatacheckObjCmpResultTimeList', body)

    def testDescribeDatacheckObjCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'BackLackOnly': 0,
            'uuid': 'CfAfc3d8-833e-3AFc-AA7d-16f2b7EeF6CC',
            'start_time': '',
            'limit': 1,
            'offset': '',
            'search_value': '',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.describeDatacheckObjCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeDatacheckObjCmpResult', body)

    def testListDatacheckObjCmpStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.listDatacheckObjCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'listDatacheckObjCmpStatus', body)

    def testDescribeDatacheckObjCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '4bc6CceE-7c49-Ff4A-D093-09AEb3cb1E9F',
            'time_list': [],
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.describeDatacheckObjCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeDatacheckObjCmpResultTimeList', body)

    def testListDatacheckObjCmpCmpInfo(self):
        a = Auth(username, pwd)
        body = {
            'filed': '',
            'uuid': '',
            'start_time': '',
            'offset': 1,
            'limit': 10,
            'search_value': '',
            'usr': 'I2',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.listDatacheckObjCmpCmpInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'listDatacheckObjCmpCmpInfo', body)

    def testCreateTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_name': '规则名',
            'src_db_uuids': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuids': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'cmp_type': 'table',
            'filter_table': '[user.table]',
            'db_tb_map': [{
            'regex_switch': '1',
            'src': [{
            'user': 'xpxrgifyfe',
            'tab': 'hjpv',
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
            'col': {
            'col1': 'col2',
            'col3': 'col4',},},{
            'regex_switch': '1',
            'src': [{
            'user': 'wsbitu',
            'tab': 'zhbiv',
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
            'col': {
            'col1': 'col2',
            'col3': 'col4',},},{
            'regex_switch': '1',
            'src': [{
            'user': 'mktckt',
            'tab': 'dlostk',
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
            'col': {
            'col1': 'col2',
            'col3': 'col4',},},{
            'regex_switch': '1',
            'src': [{
            'user': 'tdqfdvwi',
            'tab': 'wocvermtj',
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
            'col': {
            'col1': 'col2',
            'col3': 'col4',},},{
            'regex_switch': '1',
            'src': [{
            'user': 'qflycrek',
            'tab': 'padiohrh',
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
            'col': {
            'col1': 'col2',
            'col3': 'col4',},},],
            'dump_thd': 1,
            'polices': '0|00:00',
            'policy_type': 'one_time',
            'concurrent_table': [
            'hh.ww',],
            'try_split_part_table': 0,
            'one_time': '2019-05-27 16:07:08',
            'config': {
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
            'global_time_limit': False,
            'v_tabmap': [{
            'src_user': '',
            'src_tb': '',
            'src_sql': '',
            'tgt_user': '',
            'tgt_tb': '',
            'tgt_sql': '',
            'key': '',},],},
            'interval': '10m',
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
            'db_map': {
            'src': [{
            'db_uuid': '',
            'auth_uuid': '',},],
            'tgt': [{
            'db_uuid': '',
            'auth_uuid': '',},],},
            'incre_cmp_switch': '',
            'incre_cmp_db_uuid': '',
            'incre_cmp_db_type': '',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.createTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'createTbCmp', body)

    def testDescribeTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '4D810eb3-7E3b-3dDB-D7c1-dCcDeB53518E',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dataChk = DataChk(a)
        r = dataChk.describeTbCmp(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeTbCmp', body)

    def testDeleteTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'force': False,
            'uuids': '9CE0BdAD-D8F8-17dF-bb4b-AfeAC0A245BE',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.deleteTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'deleteTbCmp', body)

    def testListTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': 'tb_cmp_name',
            'search_value': '测试',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.listTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'listTbCmp', body)

    def testListTbCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.listTbCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'listTbCmpResultTimeList', body)

    def testStopTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': '75e99409-ACC3-ebbb-818F-eDFd11A9Bf34',
            'tb_cmp_name': '',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.stopTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'stopTbCmp', body)

    def testRestartTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'E57aeCfF-364e-6aED-A1b8-fdAbae64Af6e',
            'tb_cmp_name': '',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.restartTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'restartTbCmp', body)

    def testResumeTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'bf3cccB0-a1dd-dA03-D737-F1c6c9199A9a',
            'tb_cmp_name': '',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.resumeTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'resumeTbCmp', body)

    def testDescribeTbCmpResuluTimeList(self):
        a = Auth(username, pwd)
        body = {
            'time_list': 'c49daB1B-fc23-9AbC-CE7C-Ec6a4e785Ac3',
            'uuid': '',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.describeTbCmpResuluTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeTbCmpResuluTimeList', body)

    def testDescribeTbCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': '4dFd8d68-875A-A7ee-CF23-48E9dE4d21D2',
            'start_time': '',
            'flag': 1,
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.describeTbCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeTbCmpResult', body)

    def testDescribeTbCmpErrorMsg(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': 'aFfeB7F9-B2eF-45a1-f7bf-a96f8cF48dE4',
            'start_time': '',
            'name': '',
            'owner': 'admin',
        }
        
        
        dataChk = DataChk(a)
        r = dataChk.describeTbCmpErrorMsg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeTbCmpErrorMsg', body)

    def testDescribeTbCmpCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dataChk = DataChk(a)
        r = dataChk.describeTbCmpCmpResult(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeTbCmpCmpResult', body)

    def testDescribeTbCmpCmpDesc(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': '9F12eC79-31cF-cdcE-4Ffd-f1CEdD79528F',
            'start_time': '',
            'name': '',
            'owner': 'admin',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dataChk = DataChk(a)
        r = dataChk.describeTbCmpCmpDesc(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeTbCmpCmpDesc', body)

    def testDescribeTbCmpStart(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dataChk = DataChk(a)
        r = dataChk.describeTbCmpStart(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'describeTbCmpStart', body)


if __name__ == '__main__':
    unittest.main()
