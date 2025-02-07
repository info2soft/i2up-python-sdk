
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Tenant
from info2soft.common.v20250123.Tenant import Tenant
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
            'tenant_name': 'Brenda',
            'display_name': 'Kimberly',
            'description': 'Scott',
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
            'display_name': 'David',
            'description': 'Sandra',
            'enabled': 0,
            'random_str': '13bc42A2-Aa3e-DFFA-5ce5-A0AF4fe260BC',
            'tenant_name': 'Jose',
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
