
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.resource.v20230227.Ukey import Ukey
# from info2soft.resource.v20200722.Ukey import Ukey
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


class UkeyTestCase(unittest.TestCase):

    def testCreateUkey(self):
        a = Auth(username, pwd)
        body = {
            'ukey_name': '',
            'ukey_type': '',
            'node_uuid': '',
            'ukey_id': '',
            'ukey_pwd': '',
            'comment': '',
            'import_pwd_switch': 1,
        }
        
        ukey = Ukey(a)
        r = ukey.createUkey(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'createUkey', body)

    def testModifyUkey(self):
        a = Auth(username, pwd)
        body = {
            'ukey_name': '',
            'comment': '',
            'ukey_pwd': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        ukey = Ukey(a)
        r = ukey.modifyUkey(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'modifyUkey', body)

    def testDiscribeUkey(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        ukey = Ukey(a)
        r = ukey.discribeUkey(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'discribeUkey', body)

    def testListUkey(self):
        a = Auth(username, pwd)
        body = {
        }
        
        ukey = Ukey(a)
        r = ukey.listUkey(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'listUkey', body)

    def testDeleteUkey(self):
        a = Auth(username, pwd)
        body = {
            'ukey_uuids': [
            '81296F62-C542-5D68-3282-9B5815742290',],
            'force': 0,
        }
        
        ukey = Ukey(a)
        r = ukey.deleteUkey(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'deleteUkey', body)

    def testOperateUkey(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'node_uuid': '',
            'ukey_id': '',
            'ukey_name': '',
            'ukey_pwd': '',
            'ukey_uuid': '',
        }
        
        ukey = Ukey(a)
        r = ukey.operateUkey(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'operateUkey', body)

    def testListUkeyStatus(self):
        a = Auth(username, pwd)
        body = {
            'ukey_uuids': [],
        }
        
        ukey = Ukey(a)
        r = ukey.listUkeyStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'listUkeyStatus', body)

    def testListUkeyNodeList(self):
        a = Auth(username, pwd)
        body = {
            'ukey_uuid': '',
        }
        
        ukey = Ukey(a)
        r = ukey.listUkeyNodeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'listUkeyNodeList', body)

    def testScanUkey(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'ukey_type': '',
        }
        
        ukey = Ukey(a)
        r = ukey.scanUkey(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'scanUkey', body)

    def testExportUkeyInfo(self):
        a = Auth(username, pwd)
        body = {
            'export_pwd': '',
            'ukey_uuids': [],
        }
        
        ukey = Ukey(a)
        r = ukey.exportUkeyInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'exportUkeyInfo', body)

    def testImportUkeyInfo(self):
        a = Auth(username, pwd)
        body = {
            'export_pwd': '',
            'import_pwd': '',
            'ukey_info': [{
            'ukey_name': '',
            'ukey_type': '',
            'node_list': [{
            'node_name': '',
            'config_addr': '',},],
            'ukey_id': '',
            'ukey_pwd': '',
            'Ukey_uuid': '',},],
        }
        
        ukey = Ukey(a)
        r = ukey.importUkeyInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Ukey', 'importUkeyInfo', body)


if __name__ == '__main__':
    unittest.main()
