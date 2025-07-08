
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import FingerprintDomain
from info2soft.fingerprintDomain.v20250630.FingerprintDomain import FingerprintDomain
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


class FingerprintDomainTestCase(unittest.TestCase):
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

    def testCreateFingerprintDomain(self):
        a = Auth(username, pwd)
        body = {
            'domain_name': '',
            'sto_uuid': '',
            'chunk_type': 1,
            'chunk_size': 1,
            'chunk_max': 1,
            'chunk_min': 1,
            'compress': 1,
            'description': '',
            'fp_server_uuid': '',
        }
        
        
        fingerprintDomain = FingerprintDomain(a)
        r = fingerprintDomain.createFingerprintDomain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FingerprintDomain', 'createFingerprintDomain', body)

    def testModifyFingerprintDomain(self):
        a = Auth(username, pwd)
        body = {
            'domain_name': '',
            'sto_uuid': '',
            'chunk_type': 1,
            'chunk_size': 1,
            'chunk_max': 1,
            'chunk_min': 1,
            'compress': 1,
            'description': '',
            'domain_uuid': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fingerprintDomain = FingerprintDomain(a)
        r = fingerprintDomain.modifyFingerprintDomain(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FingerprintDomain', 'modifyFingerprintDomain', body)

    def testDeleteFingerprintDomain(self):
        a = Auth(username, pwd)
        body = {
            'domain_uuids': [],
            'force': 1,
        }
        
        
        fingerprintDomain = FingerprintDomain(a)
        r = fingerprintDomain.deleteFingerprintDomain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FingerprintDomain', 'deleteFingerprintDomain', body)

    def testListFingerprintDomain(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_field': '',
            'search_value': '',
            'status': '',
        }
        
        
        fingerprintDomain = FingerprintDomain(a)
        r = fingerprintDomain.listFingerprintDomain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FingerprintDomain', 'listFingerprintDomain', body)

    def testDescribeFingerprintDomain(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fingerprintDomain = FingerprintDomain(a)
        r = fingerprintDomain.describeFingerprintDomain(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FingerprintDomain', 'describeFingerprintDomain', body)

    def testListFingerprintDomainStatus(self):
        a = Auth(username, pwd)
        body = {
            'domain_uuids': [],
            'force_refresh': 0,
        }
        
        
        fingerprintDomain = FingerprintDomain(a)
        r = fingerprintDomain.listFingerprintDomainStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FingerprintDomain', 'listFingerprintDomainStatus', body)

    def testOperateFingerprintDomain(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'domain_uuids': [],
            'fp_server_uuid': '',
        }
        
        
        fingerprintDomain = FingerprintDomain(a)
        r = fingerprintDomain.operateFingerprintDomain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FingerprintDomain', 'operateFingerprintDomain', body)


if __name__ == '__main__':
    unittest.main()
