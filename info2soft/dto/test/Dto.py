
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'E:/python-sdk')

import unittest
from info2soft.dto.Dto import Dto
# from info2soft.dto.v20200722.Dto import Dto
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
            'rule_uuids': [],
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
            'rule_uuids': [],
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
            'rule_uuids': [],
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
            'rule_uuids': [],
        }

        dto = Dto(a)
        r = dto.restartDtoRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dto', 'restartDtoRule', body)

    def testListDtoRuleFile(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
            'page': 1,
            'limit': 1,
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
            'host_uuid': 'b6Cb9844-b8Da-Ecab-c3A2-BB924C1586eF',
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


if __name__ == '__main__':
    unittest.main()
