
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import FfoMount
from info2soft.cdm.v20240819.FfoMount import FfoMount
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


class FfoMountTestCase(unittest.TestCase):

    def testCreateFfoMount(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'bk_version': '',
            'os_version': '',
            'storage_uuid': '',
            'mount_name': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'vm_disks': [{
            'path': '',
            'size': '',
            'interface': '',
            'isBoot': '',},],
            'protocol': '',
            'fsp_uuid': '',
            'acl': '',
            'by_type': '',
            'wk_address': '',
            'wk_name': '',
            'client_uuid': '',
            'specify_client': 0,
        }
        
        
        ffoMount = FfoMount(a)
        r = ffoMount.createFfoMount(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'createFfoMount', body)

    def testModifyFfoMount(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'bk_version': '',
            'os_version': '',
            'storage_uuid': '',
            'mount_name': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'vm_disks': [{
            'path': '',
            'size': '',
            'interface': '',
            'isBoot': '',},],
            'protocol': '',
            'acl': '',
            'random_str': '',
            'fsp_uuid': '',
            'specify_client': 1,
            'client_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        ffoMount = FfoMount(a)
        r = ffoMount.modifyFfoMount(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'modifyFfoMount', body)

    def testDescribeFfomount(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        ffoMount = FfoMount(a)
        r = ffoMount.describeFfomount(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'describeFfomount', body)

    def testFfoMountList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'search_field': 'mount_name',
            'search_value': 'mount_name',
        }
        
        
        ffoMount = FfoMount(a)
        r = ffoMount.ffoMountList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'ffoMountList', body)

    def testListFfoMountStatus(self):
        a = Auth(username, pwd)
        body = {
            'mount_uuids': [],
            'force_refresh': 1,
        }
        
        
        ffoMount = FfoMount(a)
        r = ffoMount.listFfoMountStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'listFfoMountStatus', body)

    def testDeleteFfoMount(self):
        a = Auth(username, pwd)
        body = {
            'mount_uuids': [],
        }
        
        
        ffoMount = FfoMount(a)
        r = ffoMount.deleteFfoMount(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FfoMount', 'deleteFfoMount', body)


if __name__ == '__main__':
    unittest.main()
