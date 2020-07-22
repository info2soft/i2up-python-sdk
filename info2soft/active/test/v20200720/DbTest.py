
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.active.v20181227.Db import Db
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
            'db_name': 'Larry Martinez',
            'db_uuid': 'E6A8407A-8AAe-299c-F442-Fd5E83dB35FA',
            'node_uuid': 'aFcEAC9D-dcDA-d417-D073-2Ff41FCb509b',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'username': 'Eric Lopez',
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
            'producer_host': '173.73.53.184',
            'producer_port': 1,
            'broker_server': [{
            'ip': '178.54.147.112',
            'port': 1,},],},
            'random_str': '',
        }
        db = Db(a)
        r = db.modifyDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'modifyDb', body)

    def testCheckDbLink(self):
        a = Auth(username, pwd)
        body = {
            'db_name': 'Sharon Hall',
            'node_uuid': 'ceBF6aaF-3F4b-08Af-c28C-EA185CCdB14A',
            'db_type': 'oracle',
            'file_open_type': 'DIRECT',
            'deploy_mode': 'single',
            'log_read_type': 'file',
            'config': {
            'username': 'Robert Miller',
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
            'producer_host': '49.160.23.205',
            'producer_port': 1,
            'broker_server': [{
            'ip': '8.129.109.182',
            'port': 1,},],},
            'db_uuid': 'fFaeCd8F-d482-bdD9-C4e7-79C6BD9e7809',
        }
        db = Db(a)
        r = db.checkDbLink(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'checkDbLink', body)

    def testCreateDb(self):
        a = Auth(username, pwd)
        body = {
            'db_name': 'Charles Thomas',
            'node_uuid': 'f7f7a85B-74b5-5920-3c9d-6fdE838Cbf7B',
            'db_type': 'oracle',
            'file_open_type': '0',
            'deploy_mode': '0',
            'log_read_type': 'file',
            'config': {
            'username': 'Jose Williams',
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
            'disable': 0,},],
            'producer_host': '84.105.70.29',
            'producer_port': 1,
            'broker_server': [{
            'ip': '50.173.70.141',
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
            'db_uuid': 'Fe26e5bb-4567-c877-33Be-16C89A081c46',
            'db_mode': '',
            'cdb': 'E69D3ABf-BbcB-896e-8cF8-bDC95BA9e278',
        }
        db = Db(a)
        r = db.createDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'createDb', body)

    def testDeleteDb(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '7C5B0EDB-6806-94c9-eFDe-99c86cf1e879',
        }
        db = Db(a)
        r = db.deleteDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'deleteDb', body)

    def testListDbStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'b37FFF1d-4E68-8dc8-B4F9-5267a09d3c2B',
        }
        db = Db(a)
        r = db.listDbStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'listDbStatus', body)

    def testDescribeDbHealthInfo(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '2bc48e16-624F-ECda-4E3e-7CB31bdd799d',
        }
        db = Db(a)
        r = db.describeDbHealthInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db', 'describeDbHealthInfo', body)

    def testDescribeDbSpace(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'FAcA8b92-3d15-7bbC-A7B1-19cDBF7dDEB0',
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
        db = Db(a)
        r = db.describeDb(body)
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
