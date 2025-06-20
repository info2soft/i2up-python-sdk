
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import CloudPlatform
from info2soft.cloud.v20250630.CloudPlatform import CloudPlatform
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


class CloudPlatformTestCase(unittest.TestCase):
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

    def testListCloudPlatformRegion(self):
        a = Auth(username, pwd)
        body = {
            'cloud_type': 1,
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.listCloudPlatformRegion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'listCloudPlatformRegion', body)

    def testRegisterCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'authurl': '',
            'os_user': '',
            'os_pwd': '',
            'user_domain_id': '',
            'cloud_name': '',
            'config_addr': '192.168.66.66',
            'register_type': '',
            'iam_user': '',
            'cloud_type': 1,
            'user_domain_name': '',
            'region': '',
            'bind_lic_list': [],
            'maintenance': 0,
            'cc_ip_uuid': '',
            'access_key': '',
            'secret_access_key': '',
            'mfa_switch': 1,
            'connect_port': 5000,
            'project_id': '',
            'npsvr_uuid': '',
            'resource_id': '',
            'manage_addr': '',
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.registerCloudPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'registerCloudPlatform', body)

    def testModifyCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'os_user': '',
            'os_pwd': '',
            'user_domain_id': '',
            'register_type': '',
            'iam_user': '',
            'cloud_uuid': '',
            'bind_lic_list': '',
            'https://apiref.info2soft.com/repository/editor?id=28&itf=824': 0,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.modifyCloudPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'modifyCloudPlatform', body)

    def testDescribeCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.describeCloudPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'describeCloudPlatform', body)

    def testListCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'where_args': {
            'vp_type': 1,},
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.listCloudPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'listCloudPlatform', body)

    def testDeleteCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force': 1,
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.deleteCloudPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'deleteCloudPlatform', body)

    def testListCloudPlatformStatus(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuids': [],
            'force_refresh': 1,
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.listCloudPlatformStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'listCloudPlatformStatus', body)

    def testSyncEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'region_id': '',
            'project_id': '',
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.syncEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'syncEcs', body)

    def testSyncVolume(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.syncVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'syncVolume', body)

    def testListFlavor(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'server_zone': 'cn-east-2a',
            'region_id': '',
            'project_id': '',
            'nic_count': '',
            'cpu': '',
            'mem_mb': '',
            'flavor_id': '',
            'image_id': '',
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.listFlavor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'listFlavor', body)

    def testListRelativeNode(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'cloud_uuid': '',
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.listRelativeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'listRelativeNode', body)

    def testSwitchMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'switch': 0,
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.switchMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'switchMaintenance', body)

    def testListRegions(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.listRegions(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'listRegions', body)

    def testListProjects(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }
        
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.listProjects(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'listProjects', body)


if __name__ == '__main__':
    unittest.main()
