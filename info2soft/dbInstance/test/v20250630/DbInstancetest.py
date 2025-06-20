
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import DbInstance
from info2soft.dbInstance.v20250630.DbInstance import DbInstance
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


class DbInstanceTestCase(unittest.TestCase):
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

    def testDiscoveryDbInstances(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'instance_type': '',
        }
        
        
        dbInstance = DbInstance(a)
        r = dbInstance.discoveryDbInstances(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'discoveryDbInstances', body)

    def testVerifyDbInstances(self):
        a = Auth(username, pwd)
        body = {
            'instance_type': 1,
            'protocol': 1,
            'win_verify': 1,
            'user': '',
            'password': '',
            'timeout': 1,
            'driver': '',
            'port': 1,
            'data_source': '',
            'node_uuid': '',
            'instance_name': '',
            'host': '',
            'bin_path': '',
            'config_path': '',
            'data_path': '',
            'sys_user': '',
            'hostname': '',
            'sys_password': '',
            'install_dir': '',
            'is_default': '',
            'onconfig_name': '',
            'auth_type': 1,
            'login_path': '',
            'login_type': 1,
        }
        
        
        dbInstance = DbInstance(a)
        r = dbInstance.verifyDbInstances(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'verifyDbInstances', body)

    def testCreateDbInstance(self):
        a = Auth(username, pwd)
        body = {
            'instance_type': 1,
            'node_uuid': '',
            'data_source': '',
            'instance_list': [{
            'instance_name': '',
            'version_info': {
            'version': '',},
            'is_verified': 1,
            'protocol': 1,
            'port': 1,
            'win_verify': 1,
            'user': '',
            'password': '',
            'timeout': 1,
            'driver': '',
            'host': '',
            'bin_path': '',
            'config_path': '',
            'data_path': '',
            'sys_user': '',
            'hostname': '',
            'sys_password': '',
            'shards': [{
            'id': '',},],
            'replica_sets': [{
            'id': '',
            'ip': '',
            'port': 1,
            'master': False,
            'node_uuid': '',
            'shard_id': '',},],
            'is_default': 1,
            'install_dir': '',
            'onconfig_name': '',
            'auth_type': 1,
            'db_name': '',
            'managers': [{
            'ip': '',
            'master': False,
            'node_uuid': '',},],
            'gtms': [{
            'ip': '',
            'master': False,
            'node_uuid': '',},],
            'type': '',
            'sub_instance': [],
            'dmdcr_ini_path': '',
            'dmdsc_uuid': '',
            'instance_id': '',
            'archive_path': '',
            'login_type': 1,
            'login_path': '',},],
            'scan_ip': '',
        }
        
        
        dbInstance = DbInstance(a)
        r = dbInstance.createDbInstance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'createDbInstance', body)

    def testListDbInstances(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'search_value': '',
            'page': 1,
            'limit': 1,
            'type': 1,
            'where_args': [{
            'node_uuid': '',},],
        }
        
        
        dbInstance = DbInstance(a)
        r = dbInstance.listDbInstances(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'listDbInstances', body)

    def testDescribeDbInstance(self):
        a = Auth(username, pwd)
        body = {
            'instance_uuid': '',
            'instance_type': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dbInstance = DbInstance(a)
        r = dbInstance.describeDbInstance(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'describeDbInstance', body)

    def testModifyDbInstance(self):
        a = Auth(username, pwd)
        body = {
            'instance_type': 1,
            'node_uuid': '',
            'data_source': '',
            'instance_list': [{
            'instance_name': '',
            'version_info': {
            'version': '',},
            'is_verified': 1,
            'protocol': 1,
            'port': 1,
            'win_verify': 1,
            'user': '',
            'password': '',
            'timeout': 1,
            'driver': '',
            'instance_uuid': '',
            'random_str': '',
            'sys_user': '',
            'hostname': '',},],
        }
        
        
        dbInstance = DbInstance(a)
        r = dbInstance.modifyDbInstance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'modifyDbInstance', body)

    def testDeleteDbInstances(self):
        a = Auth(username, pwd)
        body = {
            'instance_uuids': [],
            'force': 1,
        }
        
        
        dbInstance = DbInstance(a)
        r = dbInstance.deleteDbInstances(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'deleteDbInstances', body)

    def testListDbs(self):
        a = Auth(username, pwd)
        body = {
            'instance_uuid': '',
        }
        
        
        dbInstance = DbInstance(a)
        r = dbInstance.listDbs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'listDbs', body)

    def testListTables(self):
        a = Auth(username, pwd)
        body = {
            'instance_uuid': '',
            'db_name': '',
        }
        
        
        dbInstance = DbInstance(a)
        r = dbInstance.listTables(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'listTables', body)

    def testListTableSpaces(self):
        a = Auth(username, pwd)
        body = {
            'instance_uuid': '',
            'db_name': '',
        }
        
        
        dbInstance = DbInstance(a)
        r = dbInstance.listTableSpaces(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DbInstance', 'listTableSpaces', body)


if __name__ == '__main__':
    unittest.main()
