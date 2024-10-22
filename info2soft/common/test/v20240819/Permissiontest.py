
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Permission
from info2soft.common.v20240819.Permission import Permission
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


class PermissionTestCase(unittest.TestCase):

    def testListPermission(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        permission = Permission(a)
        r = permission.listPermission(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Permission', 'listPermission', body)

    def testListCategory(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        permission = Permission(a)
        r = permission.listCategory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Permission', 'listCategory', body)

    def testListCatPerms(self):
        a = Auth(username, pwd)
        body = {
            'interface_type': 0,
        }
        
        
        permission = Permission(a)
        r = permission.listCatPerms(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Permission', 'listCatPerms', body)

    def testListCatPerms9(self):
        a = Auth(username, pwd)
        body = {
            'interface_type': 0,
        }
        
        
        permission = Permission(a)
        r = permission.listCatPerms9(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Permission', 'listCatPerms9', body)


if __name__ == '__main__':
    unittest.main()
