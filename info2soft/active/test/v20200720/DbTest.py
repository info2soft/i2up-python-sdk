
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import Db
# from info2soft.active.v20200722.Db import Db
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
    
                
class DbTestCase(unittest.TestCase):

    def testListDbs(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'type': 'all',
        }
        
        db = Db(a)
        r = db.listDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'listDbs', body)

    def testModifyDb(self):
        a = Auth(username, pwd)
        body = {
            'db_name': 'Jeffrey Anderson',
            'db_uuid': '81d7CeD8-FdE6-C3C2-1FFE-d8b3B2aFB2fc',
            'node_uuid': 'aD84af1f-FcFb-3d11-BbeC-Bf04E8FF9B2e',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'username': 'Kevin Martinez',
            'password': '',
            'server_name': '',
            'port': 1,
            'log_read': {
            'os_auth': 1,
            'asm_instance': '',
            'asm_username': '',
            'asm_port': 1,
            'asm_password': '12323131',},
            'filter_session': 1,
            'relay': {
            'enable': 1,
            'relay_node_uuid': '',},
            'remote_file_agent': {
            'enable': 1,
            'port': 1,
            'compress': 'no',},
            'db_list': [{
            'ip': '',
            'thread': '',},],
            'producer_host': '251.122.55.221',
            'producer_port': 1,
            'broker_server': [{
            'ip': '169.157.35.84',
            'port': 1,},],},
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        db = Db(a)
        r = db.modifyDb(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'modifyDb', body)

    def testCheckDbLink(self):
        a = Auth(username, pwd)
        body = {
            'db_name': 'Jason Harris',
            'node_uuid': 'B5587B58-2A7f-E8fc-edCB-4Ac5BE3f46A4',
            'db_type': 'oracle',
            'file_open_type': 'DIRECT',
            'deploy_mode': 'single',
            'log_read_type': 'file',
            'config': {
            'username': 'Larry Garcia',
            'password': '',
            'server_name': '',
            'port': 1,
            'log_read': {
            'os_auth': 1,
            'asm_instance': '',
            'asm_username': '',
            'asm_port': 1,
            'asm_password': '12323131',},
            'filter_session': 1,
            'relay': {
            'enable': 1,
            'relay_node_uuid': '',},
            'remote_file_agent': {
            'enable': 1,
            'port': 1,
            'compress': 'none',},
            'db_list': [{
            'ip': '',
            'thread': '',
            'disable': '',},],
            'producer_host': '176.6.142.208',
            'producer_port': 1,
            'broker_server': [{
            'ip': '148.131.32.35',
            'port': 1,},],},
            'db_uuid': 'Acc6B7E9-8f6D-fEfd-F13b-dcC26AB5DADf',
        }
        
        db = Db(a)
        r = db.checkDbLink(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'checkDbLink', body)

    def testCreateDb(self):
        a = Auth(username, pwd)
        body = {
            'db_name': 'Sarah Thomas',
            'node_uuid': 'F8C8f87d-f2be-469B-E2dB-CEEE8BEB1d9E',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'username': 'Sandra Wilson',
            'password': '',
            'server_name': '',
            'port': 1,
            'log_read': {
            'os_auth': 1,
            'asm_instance': '',
            'asm_username': '',
            'asm_port': 1,
            'asm_password': '12323131',},
            'filter_session': 1,
            'relay': {
            'enable': 1,
            'relay_node_uuid': '',},
            'remote_file_agent': {
            'enable': 1,
            'port': 1,
            'compress': 'no',},
            'db_list': [{
            'ip': '',
            'thread': '',
            'disable': 1,},],
            'producer_host': '13.206.45.18',
            'producer_port': 1,
            'broker_server': [{
            'ip': '111.184.153.42',
            'port': 1,},],
            'authentication': 'none',
            'principal': '',
            'keytabfile': '',
            'kafka_auth_type': '',
            'kerberos_keytab_path': '',
            'kerberos_principal': '',
            'kerberos_service_name': '',
            'sasl_plain_user': '',
            'sasl_plain_pass': '',
            'sqlserver': {
            'ip': '',
            'port': 1,
            'usr': '',
            'pwd': '',
            'db': '',
            'dacport': '',},},
            'db_uuid': 'dCcBdaCa-cD9D-CD1B-FbDB-cAbD14Ce6B49',
            'db_mode': '',
            'cdb': 'FC8f8BfD-5618-bEf7-7BE3-38f7c9BebA2d',
        }
        
        db = Db(a)
        r = db.createDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'createDb', body)

    def testDeleteDb(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '3F5f266A-4cF4-2DD8-ADc9-1d3f04832c88',
        }
        
        db = Db(a)
        r = db.deleteDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'deleteDb', body)

    def testListDbStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '0bA6d94f-7EC3-F4AA-ab1D-Bc61434Cefcc',
        }
        
        db = Db(a)
        r = db.listDbStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'listDbStatus', body)

    def testDescribeDbHealthInfo(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '80FbF65E-452E-64DF-F2A3-68Bfb28BBA5e',
        }
        
        db = Db(a)
        r = db.describeDbHealthInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'describeDbHealthInfo', body)

    def testDescribeDbSpace(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'fEfacB2b-d6eD-208D-a6c2-3dbEaadA27fc',
        }
        
        db = Db(a)
        r = db.describeDbSpace(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'describeDbSpace', body)

    def testDescribeDb(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        db = Db(a)
        r = db.describeDb(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'describeDb', body)

    def testImportTemplate(self):
        a = Auth(username, pwd)
        body = {
            'type': 'db_csv',
        }
        
        db = Db(a)
        r = db.importTemplate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'importTemplate', body)

    def testBatchCreateDbs(self):
        a = Auth(username, pwd)
        body = {
        }
        
        db = Db(a)
        r = db.batchCreateDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'batchCreateDbs', body)


if __name__ == '__main__':
    unittest.main()
