
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import HDR
from info2soft.hw.v20250630.HDR import HDR
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


class HDRTestCase(unittest.TestCase):
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

    def testUpdateSetting(self):
        a = Auth(username, pwd)
        body = {
            'hcs_url': '',
        }
        
        
        hDR = HDR(a)
        r = hDR.updateSetting(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'updateSetting', body)

    def testModifyProfile(self):
        a = Auth(username, pwd)
        body = {
            'hcs_username': '',
            'hcs_password': '',
        }
        
        
        hDR = HDR(a)
        r = hDR.modifyProfile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'modifyProfile', body)

    def testListProfile(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        hDR = HDR(a)
        r = hDR.listProfile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'listProfile', body)

    def testGetOpLogUsers(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        hDR = HDR(a)
        r = hDR.getOpLogUsers(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'getOpLogUsers', body)

    def testGetLicenseData(self):
        a = Auth(username, pwd)
        body = {
            'controlItems': [{
            'itemType': 1,
            'itemCode': '',},],
        }
        
        
        hDR = HDR(a)
        r = hDR.getLicenseData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'getLicenseData', body)

    def testGetLicenseItems(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        hDR = HDR(a)
        r = hDR.getLicenseItems(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'getLicenseItems', body)

    def testGetLicenseDescribe(self):
        a = Auth(username, pwd)
        body = {
            'num': 1,
            'sn': [
            '10-4167409378-01',
            '10-4167409378-02',
            '10-4167409378-03',
            '10-4167409378-04',
            '10-4167409378-05',],
            'key': 'z2fpC6',
            'sign': '',
            'feature': {
            'ha': '10-4167409378-01',
            'move': '10-4167409378-02',
            'active': '10-4167409378-03',
            'nas': '10-4167409378-04',
            'dto': '10-4167409378-05',},
            'license': {
            '10-4167409378-01': {
            'feature': '',
            'lic': '',
            'v2lic': '',},
            '10-4167409378-02': {
            'feature': '',
            'lic': '',
            'v2lic': '',},
            '10-4167409378-03': {
            'feature': '',
            'lic': '',
            'v2lic': '',},
            '10-4167409378-04': {
            'feature': '',
            'lic': '',
            'v2lic': '',},
            '10-4167409378-05': {
            'feature': '',
            'lic': '',
            'v2lic': '',},},
        }
        
        
        hDR = HDR(a)
        r = hDR.getLicenseDescribe(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'getLicenseDescribe', body)

    def testGetLicenseFiles(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        hDR = HDR(a)
        r = hDR.getLicenseFiles(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'getLicenseFiles', body)

    def testUpdateLicenseFile(self):
        a = Auth(username, pwd)
        body = {
            'lsn': '',
            'regionId': '',
            'systemId': '',
            'esn': '',
            'applyType': 0,
            'revoke': 'true',
            'fileContent': [{
            'feature': '',
            'lic': '',
            'v2lic': '',},],
        }
        
        
        hDR = HDR(a)
        r = hDR.updateLicenseFile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'HDR', 'updateLicenseFile', body)


if __name__ == '__main__':
    unittest.main()
