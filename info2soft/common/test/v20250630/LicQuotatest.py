
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import LicQuota
from info2soft.common.v20250630.LicQuota import LicQuota
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


class LicQuotaTestCase(unittest.TestCase):
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

    def testQuotaOverview(self):
        a = Auth(username, pwd)
        body = {
            'limit': '15',
            'page': '1',
        }
        
        
        licQuota = LicQuota(a)
        r = licQuota.quotaOverview(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LicQuota', 'quotaOverview', body)

    def testCreateLicQuota(self):
        a = Auth(username, pwd)
        body = {
            'user_uuid': '',
            'quota_list': [{
            'feature': 'backup9',
            'vm_num': 1,
            'db_num': 1,
            'sqlserver_num': 1,
            'mysql_num': 1,
            'phy_num': 1,
            'move_num': 1,
            'postgresql_num': 0,
            'dm_num': 0,
            'mongodb_num': 0,
            'redis_num': 0,
            'kafka_num': 0,},],
            'split_license': 1,
        }
        
        
        licQuota = LicQuota(a)
        r = licQuota.createLicQuota(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LicQuota', 'createLicQuota', body)

    def testUnsubscribeLicQuota(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        licQuota = LicQuota(a)
        r = licQuota.unsubscribeLicQuota(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LicQuota', 'unsubscribeLicQuota', body)

    def testListLicQuota(self):
        a = Auth(username, pwd)
        body = {
            'user_uuid': 'E2e77feF-9bbd-45fd-eB54-ee84FAE8Ff9b',
            'search_field': 'quota_uuid',
            'search_value': 'f8E3E455-B836-9cAe-bc63-7D41Be3F882F',
            'limit': 15,
            'page': 1,
        }
        
        
        licQuota = LicQuota(a)
        r = licQuota.listLicQuota(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LicQuota', 'listLicQuota', body)

    def testDescribeLicQuota(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        licQuota = LicQuota(a)
        r = licQuota.describeLicQuota(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LicQuota', 'describeLicQuota', body)

    def testUpdateLicQuota(self):
        a = Auth(username, pwd)
        body = {
            'vm_num': 1,
            'db_num': 1,
            'sqlserver_num': 1,
            'mysql_num': 1,
            'phy_num': 1,
            'move_num': 1,
            'postgresql_num': 1,
            'dm_num': 1,
            'mongodb_num': 1,
            'redis_num': 1,
            'kafka_num': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        licQuota = LicQuota(a)
        r = licQuota.updateLicQuota(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LicQuota', 'updateLicQuota', body)

    def testGetLicQuotaBindList(self):
        a = Auth(username, pwd)
        body = {
            'quota_uuid': '',
        }
        
        
        licQuota = LicQuota(a)
        r = licQuota.getLicQuotaBindList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LicQuota', 'getLicQuotaBindList', body)


if __name__ == '__main__':
    unittest.main()
