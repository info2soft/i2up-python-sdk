
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Tenant
from info2soft.common.v20250630.Tenant import Tenant
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


class TenantTestCase(unittest.TestCase):
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

    def testListTenant(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'limit': 1,
            'page': 1,
            'order_by': '',
            'direction': '',
            'like_args': {
            'xxx': '',},
            'where_args': {
            'xxx': '',},
        }
        
        
        tenant = Tenant(a)
        r = tenant.listTenant(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tenant', 'listTenant', body)

    def testCreateTenant(self):
        a = Auth(username, pwd)
        body = {
            'tenant_name': 'Eric',
            'display_name': 'Anna',
            'description': 'Kimberly',
            'enabled': 1,
            'password': '',
        }
        
        
        tenant = Tenant(a)
        r = tenant.createTenant(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tenant', 'createTenant', body)

    def testModifyTenant(self):
        a = Auth(username, pwd)
        body = {
            'display_name': 'Helen',
            'description': 'Mark',
            'enabled': 0,
            'random_str': '9Ecd8617-7eaD-EbeD-7F67-265BbCcb4192',
            'tenant_name': 'Donna',
            'password': '',
        }
        
        id = 123456
        tenant = Tenant(a)
        r = tenant.modifyTenant(body, id)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tenant', 'modifyTenant', body)

    def testDeleteTenant(self):
        a = Auth(username, pwd)
        body = {
            'ids': [],
        }
        
        
        tenant = Tenant(a)
        r = tenant.deleteTenant(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tenant', 'deleteTenant', body)


if __name__ == '__main__':
    unittest.main()
