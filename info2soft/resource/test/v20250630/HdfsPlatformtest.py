
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import HdfsPlatform
from info2soft.resource.v20250630.HdfsPlatform import HdfsPlatform
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


class HdfsPlatformTestCase(unittest.TestCase):
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

    def testCreateHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
            'hdfs_name': '',
            'hdfs_type': '0',
            'config_addr': '',
            'config_port': 1,
            'end_point': '',
            'conf_path': '',
            'user': '',
            'kerberos_switch': 0,
            'keytab': '',
            'principal': '',
            'comment': '',
            'bind_lic_list': [],
            'cc_ip_uuid': '',
            'hdfs_role': 1,
            'maintenance': 0,
            'hive_end_point': '',
            'hive_conf_path': '',
        }
        
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.createHdfsPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'createHdfsPlatform', body)

    def testModifyHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
            'random_str': '',
            'hdfs_name': '',
            'hdfs_type': '0',
            'config_addr': '',
            'config_port': 1,
            'end_point': '',
            'conf_path': '',
            'user': '',
            'kerberos_switch': 0,
            'keytab': '',
            'principal': '',
            'comment': '',
            'bind_lic_list': [],
            'cc_ip_uuid': '',
            'hdfs_role': 1,
            'maintenance': 0,
            'hive_end_point': '',
            'hive_conf_path': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.modifyHdfsPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'modifyHdfsPlatform', body)

    def testListHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'limit': 15,
            'page': 1,
        }
        
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listHdfsPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listHdfsPlatform', body)

    def testDescribeHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.describeHdfsPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'describeHdfsPlatform', body)

    def testDeleteHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 0,
        }
        
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.deleteHdfsPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'deleteHdfsPlatform', body)

    def testListHdfsPath(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'path': '/',
        }
        
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listHdfsPath(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listHdfsPath', body)

    def testListHdfsHiveEntity(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'database': '',
            'page': 1,
            'limit': 1,
            'search_name': '',
        }
        
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listHdfsHiveEntity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listHdfsHiveEntity', body)

    def testRefreshHdfsHiveEntity(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'database': '',
        }
        
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.refreshHdfsHiveEntity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'refreshHdfsHiveEntity', body)

    def testMaintainHdfsPlatform(self):
        a = Auth(username, pwd)
        body = {
            'hdfs_uuids': [],
            'operate': '',
            'switch': 0,
        }
        
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.maintainHdfsPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'maintainHdfsPlatform', body)

    def testListHdfsPlatformStatus(self):
        a = Auth(username, pwd)
        body = {
            'hdfs_uuids': [],
        }
        
        
        hdfsPlatform = HdfsPlatform(a)
        r = hdfsPlatform.listHdfsPlatformStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HdfsPlatform', 'listHdfsPlatformStatus', body)


if __name__ == '__main__':
    unittest.main()
