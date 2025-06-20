
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Lic
from info2soft.common.v20250630.Lic import Lic
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


class LicTestCase(unittest.TestCase):
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

    def testDescribeActivateInfo(self):
        a = Auth(username, pwd)
        body = {
            'group_sn': '20-4570098558',
        }
        
        
        lic = Lic(a)
        r = lic.describeActivateInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'describeActivateInfo', body)

    def testCdmCapacity(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        
        lic = Lic(a)
        r = lic.cdmCapacity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'cdmCapacity', body)

    def testUnsubscribeLic(self):
        a = Auth(username, pwd)
        body = {
            'sn': '',
            'operate': 'unsubscribe',
        }
        
        
        lic = Lic(a)
        r = lic.unsubscribeLic(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'unsubscribeLic', body)

    def testHdfsCapacity(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        lic = Lic(a)
        r = lic.hdfsCapacity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'hdfsCapacity', body)

    def testListNearExpirationLicenses(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        lic = Lic(a)
        r = lic.listNearExpirationLicenses(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'listNearExpirationLicenses', body)

    def testUpdateLic(self):
        a = Auth(username, pwd)
        body = {
            'config': {
            'warn_sw': 1,
            'usage_threshold': 1,},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        lic = Lic(a)
        r = lic.updateLic(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'updateLic', body)

    def testDescribeVpAuthDetail(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        
        lic = Lic(a)
        r = lic.describeVpAuthDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'describeVpAuthDetail', body)

    def testGetNodeListForLicense(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        lic = Lic(a)
        r = lic.getNodeListForLicense(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'getNodeListForLicense', body)

    def testListLicBackupAuthDetail(self):
        a = Auth(username, pwd)
        body = {
            'page': '',
            'limit': '',
        }
        
        
        lic = Lic(a)
        r = lic.listLicBackupAuthDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'listLicBackupAuthDetail', body)

    def testListLicAlert(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        lic = Lic(a)
        r = lic.listLicAlert(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'listLicAlert', body)

    def testAvoidAlert(self):
        a = Auth(username, pwd)
        body = {
            'lic_uuids': [],
        }
        
        
        lic = Lic(a)
        r = lic.avoidAlert(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'avoidAlert', body)

    def testDescribeLatestExpireLicense(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        lic = Lic(a)
        r = lic.describeLatestExpireLicense(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Lic', 'describeLatestExpireLicense', body)


if __name__ == '__main__':
    unittest.main()
