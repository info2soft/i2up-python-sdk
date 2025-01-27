
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import DtoHost
from info2soft.resource.v20250123.DtoHost import DtoHost
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


class DtoHostTestCase(unittest.TestCase):

    def testAuthDtoHost(self):
        a = Auth(username, pwd)
        body = {
            'host_ip': '192.168.72.70',
            'host_user': 'exampleuser',
            'host_pwd': 'dN5BejxqJsnEQOBRig7OBeZzQb1SEYAfs0keD+6z1l658pc/drceaMJa29FDdQpW6FfLLmb1cG1DWvOOGz9sZRUY4wnKNhpHQjVE4wAlLOnVZPGlYSgtURhbIOeLl5uZCWgCSGTbQFMTCD/wql4/8/cMgWspQBvwO/5UbYqcW64Sj8wnuWf6qt4KGqrP9ua2yDFj+5S0MgMLWnAXhBwCCFVBmmmngNr5CUMe4Hqm1/d4OhvTzqTWecLNFnr9NmN4fp1zAQMZstUiedgWGg7uU9Aez2Xf8RsekMeo3O7bnZXyHZL5wpOtiq3gD/12H4bNrgDYuShsGDfEEqzfwXpoew==',
            'host_port': '',
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.authDtoHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'authDtoHost', body)

    def testCreateDtoHost(self):
        a = Auth(username, pwd)
        body = {
            'host_name': '',
            'host_ip': '',
            'host_user': '',
            'host_pwd': '',
            'sto_uuid': 'CCF36C5F-CBA6-8A55-3CA2-C07CF8E0EC4F',
            'comment': '',
            'cc_ip': '',
            'cc_ip_uuid': '',
            'maintenance': 0,
            'syncdb_host': '',
            'syncdb_username': '',
            'syncdb_password': '',
            'host_type': 1,
            'syncdb_type': 1,
            'node_list': [{
            'address': '',
            'port': '',
            'uuid': '',},],
            'host_cluster_type': '',
            'syncdb_port': '',
            'syncdb_name': '',
            'host_port': '',
            'archive_db_type': 1,
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.createDtoHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'createDtoHost', body)

    def testModifyDtoHost(self):
        a = Auth(username, pwd)
        body = {
            'host_uuid': '',
            'host_name': '',
            'host_ip': '',
            'host_user': '',
            'host_pwd': '',
            'sto_uuid': 0,
            'random_str': '',
            'cc_ip': '',
            'cc_ip_uuid': '',
            'maintenance': 0,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoHost = DtoHost(a)
        r = dtoHost.modifyDtoHost(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'modifyDtoHost', body)

    def testDescribeDtoHost(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoHost = DtoHost(a)
        r = dtoHost.describeDtoHost(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'describeDtoHost', body)

    def testListDtoHost(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
            'search_value': '',
            'search_field': '',
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.listDtoHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'listDtoHost', body)

    def testListDtoHostStatus(self):
        a = Auth(username, pwd)
        body = {
            'host_uuids': [],
            'force_refresh': 1,
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.listDtoHostStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'listDtoHostStatus', body)

    def testDeleteDtoHost(self):
        a = Auth(username, pwd)
        body = {
            'force': 1,
            'host_uuids': [],
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.deleteDtoHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'deleteDtoHost', body)

    def testListDtoHostClusterNode(self):
        a = Auth(username, pwd)
        body = {
            'where_args': {
            'host_uuid': '',},
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.listDtoHostClusterNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'listDtoHostClusterNode', body)

    def testDeleteDtoHostClusterNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'force': 1,
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.deleteDtoHostClusterNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'deleteDtoHostClusterNode', body)

    def testListArchiveDate(self):
        a = Auth(username, pwd)
        body = {
            'type': 0,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoHost = DtoHost(a)
        r = dtoHost.listArchiveDate(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'listArchiveDate', body)

    def testListRcTimePoint(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoHost = DtoHost(a)
        r = dtoHost.listRcTimePoint(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'listRcTimePoint', body)

    def testListArchiveFile(self):
        a = Auth(username, pwd)
        body = {
            'data_source': '2019',
            'page': 1,
            'limit': 100,
            'wk_path': '',
            'file_name': '',
            'create_begin_time': 1,
            'create_end_time': 1,
            'modify_begin_time': 1,
            'modify_end_time': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoHost = DtoHost(a)
        r = dtoHost.listArchiveFile(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'listArchiveFile', body)

    def testListLoadRules(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoHost = DtoHost(a)
        r = dtoHost.listLoadRules(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'listLoadRules', body)

    def testListBakRecord(self):
        a = Auth(username, pwd)
        body = {
            'file_name': '',
            'wk_path': '',
            'bk_path': '',
            'begin_backup_time': 1,
            'end_backup_time': 1,
            'page': '1',
            'limit': '100',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoHost = DtoHost(a)
        r = dtoHost.listBakRecord(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'listBakRecord', body)

    def testUpgradeDtoHost(self):
        a = Auth(username, pwd)
        body = {
            'host_uuids': [],
            'operate': '',
            'switch': 0,
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.upgradeDtoHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'upgradeDtoHost', body)

    def testMaintainDtoHost(self):
        a = Auth(username, pwd)
        body = {
            'host_uuids': [],
            'operate': '',
            'switch': 0,
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.maintainDtoHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'maintainDtoHost', body)

    def testRenewKeyDtoHost(self):
        a = Auth(username, pwd)
        body = {
            'host_uuids': [],
            'operate': '',
            'switch': 0,
        }
        
        
        dtoHost = DtoHost(a)
        r = dtoHost.renewKeyDtoHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'renewKeyDtoHost', body)

    def testRevertFile(self):
        a = Auth(username, pwd)
        body = {
            'ids': [{
            '': '',},],
            'data_source': '2021',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoHost = DtoHost(a)
        r = dtoHost.revertFile(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'revertFile', body)

    def testListRevertRecord(self):
        a = Auth(username, pwd)
        body = {
            'data_source': '2019',
            'page': 1,
            'limit': 100,
            'wk_path': '',
            'file_name': '',
            'create_begin_time': 1,
            'create_end_time': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoHost = DtoHost(a)
        r = dtoHost.listRevertRecord(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoHost', 'listRevertRecord', body)


if __name__ == '__main__':
    unittest.main()
