
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import CloudPlatform
# from info2soft.cloud.v20200722.CloudPlatform import CloudPlatform
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
    
                
class CloudPlatformTestCase(unittest.TestCase):

    def testListCloudPlatformRegion(self):
        a = Auth(username, pwd)
        body = {
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
            'project_id': '',
            'user_domain_id': '',
            'cloud_name': '',
            'config_addr': '192.168.66.66',
            'register_type': '',
            'iam_user': '',
            'cloud_type': 1,
            'user_domain_name': '',
            'region': '',
            'vp_addr': '',
            'bind_lic_list': [],
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
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.modifyCloudPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'modifyCloudPlatform', body)

    def testDeleteCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.deleteCloudPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'deleteCloudPlatform', body)

    def testListCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }
        
        cloudPlatform = CloudPlatform(a)
        r = cloudPlatform.listCloudPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudPlatform', 'listCloudPlatform', body)

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

    def testSyncEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
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

if __name__ == '__main__':
    unittest.main()
