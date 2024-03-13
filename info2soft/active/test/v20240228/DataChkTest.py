# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import DataChk
from info2soft.active.v20240228.DataChk import DataChk
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


class DataChkTestCase(unittest.TestCase):

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
            'config': {
                'one_task': 'immediate', },
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

    def testcmpResumeTimeObjCmp(self):
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

    def testrestartObjCmp(self):
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

    def testcmpImmediateObjCmp(self):
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

    def testcmpStopTimeObjCmpp(self):
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

    def testListDatacheckObjCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'c1CE0CEc-D733-c811-7DC0-61e3ca61852B',
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
            'uuid': 'F8fF0dc8-9BEF-ee3d-d8eA-EAFe7CD10589',
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
            'uuid': 'D7B77A11-E528-a9FA-2bce-91FB1Dff3aAb',
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
        }

        dataChk = DataChk(a)
        r = dataChk.createTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'createTbCmp', body)

    def testDescribeTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'dB87b773-6e4f-2e9D-C9F6-E90EAE3e29b6',
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
                   'force':0,
               'uuids': 'F8da6FFe-E5E6-481A-bC2b-d3b6dee5AC7E',
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
            'tb_cmp_uuids': '639E1886-FAb9-80D3-611d-BCf68B845BcA',
        }

        dataChk = DataChk(a)
        r = dataChk.stopTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'stopTbCmp', body)

    def testrestartTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'eff2C655-5f9B-2d3e-2eCA-D73Bf976D982',
        }

        dataChk = DataChk(a)
        r = dataChk.restartTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'restartTbCmp', body)

    def testresumeTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'eff2C655-5f9B-2d3e-2eCA-D73Bf976D982',
        }

        dataChk = DataChk(a)
        r = dataChk.resumeTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'resumeTbCmp', body)

    def testRestartTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'tb_cmp_uuids': 'eff2C655-5f9B-2d3e-2eCA-D73Bf976D982',
        }

        dataChk = DataChk(a)
        r = dataChk.restartTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataChk', 'restartTbCmp', body)

    def testDescribeTbCmpResuluTimeList(self):
        a = Auth(username, pwd)
        body = {
            'time_list': 'f7c8E6FE-d0E5-6bbb-62CF-3413aDAfB87c',
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
            'uuid': '052ECA2c-D6B7-ebfd-C5C7-AAebB94A6D84',
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
            'uuid': 'E222b479-15A9-03fA-0A1d-8fB0431C2b87',
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
            'uuid': '590Baddb-2BFB-b1ff-FFCd-1EC40Dba8c53',
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
