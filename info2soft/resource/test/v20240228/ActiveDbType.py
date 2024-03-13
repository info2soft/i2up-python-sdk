
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import ActiveDbType
from info2soft.resource.v20240228.ActiveDbType import ActiveDbType
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


class ActiveDbTypeTestCase(unittest.TestCase):

    def testListActiveDbType(self):
        a = Auth(username, pwd)
        body = {
        }
        
        activeDbType = ActiveDbType(a)
        r = activeDbType.listActiveDbType(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveDbType', 'listActiveDbType', body)

    def testListActiveDbTypeAvailMappingType(self):
        a = Auth(username, pwd)
        body = {
        }
        
        activeDbType = ActiveDbType(a)
        r = activeDbType.listActiveDbTypeAvailMappingType(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveDbType', 'listActiveDbTypeAvailMappingType', body)

    def testCreateActiveDbType(self):
        a = Auth(username, pwd)
        body = {
            'type_name': '',
            'mapping_type_uuid': '',
            'is_source': 1,
        }
        
        activeDbType = ActiveDbType(a)
        r = activeDbType.createActiveDbType(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveDbType', 'createActiveDbType', body)

    def testModifyActiveDbType(self):
        a = Auth(username, pwd)
        body = {
            'type_name': '',
            'is_source': '',
            'mapping_type_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        activeDbType = ActiveDbType(a)
        r = activeDbType.modifyActiveDbType(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveDbType', 'modifyActiveDbType', body)

    def testDeleteActiveDbType(self):
        a = Auth(username, pwd)
        body = {
            'type_uuid': '',
        }
        
        activeDbType = ActiveDbType(a)
        r = activeDbType.deleteActiveDbType(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveDbType', 'deleteActiveDbType', body)

    def testListAvailActiveDbType(self):
        a = Auth(username, pwd)
        body = {
            'where_args': {
            'type_uuid': '',},
        }
        
        activeDbType = ActiveDbType(a)
        r = activeDbType.listAvailActiveDbType(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveDbType', 'listAvailActiveDbType', body)

    def testModifyAvailActiveDbType(self):
        a = Auth(username, pwd)
        body = {
            'type_uuid': '',
            'dst_type_uuid_list': [],
        }
        
        activeDbType = ActiveDbType(a)
        r = activeDbType.modifyAvailActiveDbType(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ActiveDbType', 'modifyAvailActiveDbType', body)


if __name__ == '__main__':
    unittest.main()
