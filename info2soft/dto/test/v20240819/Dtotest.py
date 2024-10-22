
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Dto
from info2soft.dto.v20240819.Dto import Dto
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


class DtoTestCase(unittest.TestCase):

    def testCreateDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'enable': 0,
            'rule_name': '',
            'rule_type': 0,
            'sync_uuid': '',
            'policy_type': 0,
            'policy_str': '',
            'wk_uuid': '',
            'wk_path': [],
            'bk_uuid': '',
            'bk_path': [],
            'excl_path': [],
            'file_type_filter_switch': 0,
            'file_type_filter': '',
            'compare_type': 0,
            'oph_policy': 0,
            'bk_name_opt': 0,
            'trans_thread_num': 0,
            'obj_scan_thread_num': 0,
            'cmp_thread_num': 0,
            'cmp_algorithm': 0,
            'cmp_result_limit': 0,
            'band_width': '',
            'app_db_up_switch': 0,
            'app_db_up_type': '0',
            'app_db_up_sql': '0',
            'sync_type': 1,
            'archive_flag': 1,
            'archive_type': 1,
            'archive_days': 1,
            'compress': 0,
            'encrypt': 0,
            'encrypt_pass': '',
            'rc_point': 1,
            'rc_type': 1,
            'scan_obj_flag': 1,
            'archive_object': {
            'name_feature': '',
            'file_type': '',
            'create_time': 1,
            'modify_time': 1,
            'access_time': 1,
            'type': '',},
            'valid_period': 1,
            'rate_type': 1,
            'real_path': [],
            'volume_uuid': '',
            'file_record': 1,
            'encrypt_key_type': 1,
            'encrypt_type': '',
            'file_date_filter_switch': 1,
            'file_date_filter_regex': '',
            'archive_name': 1,
            'acl_sync': 1,
            'file_list_sto_uuid': '',
            'bucket_log_path': '',
            'snapshot_rc_point': '',
        }
        
        
        dto = Dto(a)
        r = dto.createDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'createDtoRule', body)

    def testModifyDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'enable': 0,
            'rule_name': '',
            'sync_uuid': '',
            'policy_type': 0,
            'policy_str': '',
            'wk_uuid': '',
            'wk_path': [],
            'bk_uuid': '',
            'bk_path': [],
            'excl_path': [],
            'file_type_filter_switch': 0,
            'file_type_filter': '',
            'compare_type': 0,
            'oph_policy': 0,
            'bk_name_opt': 0,
            'trans_thread_num': 0,
            'obj_scan_thread_num': 0,
            'cmp_thread_num': 0,
            'cmp_algorithm': 0,
            'cmp_result_limit': 0,
            'band_width': '',
            'app_db_up_switch': 0,
            'app_db_up_type': 0,
            'app_db_up_sql': 0,
            'random_str': '',
            'sync_type': 1,
            'archive_flag': 1,
            'archive_type': 1,
            'archive_days': 1,
            'compress': 0,
            'encrypt': 0,
            'encrypt_pass': '',
            'scan_obj_flag': 1,
            'archive_object': {
            'name_feature': '',
            'file_type': '',
            'create_time': 1,
            'modify_time': 1,
            'access_time': 1,
            'type': '',},
            'real_path': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dto = Dto(a)
        r = dto.modifyDtoRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'modifyDtoRule', body)

    def testDescribeDtoRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dto = Dto(a)
        r = dto.describeDtoRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'describeDtoRule', body)

    def testListDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
            'search_value': '',
            'search_field': '',
            'type': 1,
            'status': 'LIST_STOP',
            'where_args': {
            'rule_uuid': 'D76cF747-B242-B0DC-1894-b349fA71Ef5B',
            'status': 'STOP',},
        }
        
        
        dto = Dto(a)
        r = dto.listDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'listDtoRule', body)

    def testListDtoRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force_refresh': 1,
        }
        
        
        dto = Dto(a)
        r = dto.listDtoRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'listDtoRuleStatus', body)

    def testDeleteDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force': 1,
        }
        
        
        dto = Dto(a)
        r = dto.deleteDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'deleteDtoRule', body)

    def testStartDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [
            'dCf2732A-fBdA-5F3F-cE3f-7989AA8De4cd',
            '17b99b8e-2e11-C1b2-7302-b8ee1BCdF3Bd',],
        }
        
        
        dto = Dto(a)
        r = dto.startDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'startDtoRule', body)

    def testStopDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [
            'dCf2732A-fBdA-5F3F-cE3f-7989AA8De4cd',
            '17b99b8e-2e11-C1b2-7302-b8ee1BCdF3Bd',],
        }
        
        
        dto = Dto(a)
        r = dto.stopDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'stopDtoRule', body)

    def testResumeDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [
            'dCf2732A-fBdA-5F3F-cE3f-7989AA8De4cd',
            '17b99b8e-2e11-C1b2-7302-b8ee1BCdF3Bd',],
        }
        
        
        dto = Dto(a)
        r = dto.resumeDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'resumeDtoRule', body)

    def testRestartDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [
            'dCf2732A-fBdA-5F3F-cE3f-7989AA8De4cd',
            '17b99b8e-2e11-C1b2-7302-b8ee1BCdF3Bd',],
        }
        
        
        dto = Dto(a)
        r = dto.restartDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'restartDtoRule', body)

    def testDisableDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [
            'dCf2732A-fBdA-5F3F-cE3f-7989AA8De4cd',
            '17b99b8e-2e11-C1b2-7302-b8ee1BCdF3Bd',],
        }
        
        
        dto = Dto(a)
        r = dto.disableDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'disableDtoRule', body)

    def testEnableDtoRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [
            'dCf2732A-fBdA-5F3F-cE3f-7989AA8De4cd',
            '17b99b8e-2e11-C1b2-7302-b8ee1BCdF3Bd',],
        }
        
        
        dto = Dto(a)
        r = dto.enableDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'enableDtoRule', body)

    def testListDtoRuleFile(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
            'page': 1,
            'limit': 1,
            'result_id': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dto = Dto(a)
        r = dto.listDtoRuleFile(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'listDtoRuleFile', body)

    def testDeleteDtoRuleFile(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dto = Dto(a)
        r = dto.deleteDtoRuleFile(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'deleteDtoRuleFile', body)

    def testListDtoRuleCmpResult(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dto = Dto(a)
        r = dto.listDtoRuleCmpResult(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'listDtoRuleCmpResult', body)

    def testListDtoRuleSourcePath(self):
        a = Auth(username, pwd)
        body = {
            'host_uuid': '2D4e7d66-7dcc-Ef6f-bDe3-e6BD6522EB5d',
            'timepoint': '@timestamp()',
            'host_ip': '',
            'prefix': '',
            'mapper_path': '',
        }
        
        
        dto = Dto(a)
        r = dto.listDtoRuleSourcePath(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'listDtoRuleSourcePath', body)

    def testGetDtoRecoveryPoint(self):
        a = Auth(username, pwd)
        body = {
            'host_uuid': '',
            'path': [],
            'start': 1,
            'end': 1,
            'page': 1,
            'limit': 1,
        }
        
        
        dto = Dto(a)
        r = dto.getDtoRecoveryPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'getDtoRecoveryPoint', body)

    def testDownloadDtoRuleReport(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'exec_id': '',
        }
        
        
        dto = Dto(a)
        r = dto.downloadDtoRuleReport(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'downloadDtoRuleReport', body)


if __name__ == '__main__':
    unittest.main()
