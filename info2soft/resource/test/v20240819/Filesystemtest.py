
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Filesystem
from info2soft.resource.v20240819.Filesystem import Filesystem
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


class FilesystemTestCase(unittest.TestCase):

    def testCreateFilesystem(self):
        a = Auth(username, pwd)
        body = {
            'name': '',
            'pool_uuid': '',
            'fs_name': '',
            'quota_switch': 1,
            'quota_size': 1,
            'compress': 1,
            'dedup': 1,
            'zfs_params': [],
        }
        
        
        filesystem = Filesystem(a)
        r = filesystem.createFilesystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Filesystem', 'createFilesystem', body)

    def testModifyFilesystem(self):
        a = Auth(username, pwd)
        body = {
            'name': '',
            'quota_switch': 1,
            'quota_size': 1,
            'compress': 1,
            'dedup': 1,
            'zfs_params': [],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        filesystem = Filesystem(a)
        r = filesystem.modifyFilesystem(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Filesystem', 'modifyFilesystem', body)

    def testDescribeFilesystem(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        filesystem = Filesystem(a)
        r = filesystem.describeFilesystem(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Filesystem', 'describeFilesystem', body)

    def testListFilesystemStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force_refresh': '',
        }
        
        
        filesystem = Filesystem(a)
        r = filesystem.listFilesystemStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Filesystem', 'listFilesystemStatus', body)

    def testDeleteFilesystem(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 1,
        }
        
        
        filesystem = Filesystem(a)
        r = filesystem.deleteFilesystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Filesystem', 'deleteFilesystem', body)

    def testListFilesystem(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        filesystem = Filesystem(a)
        r = filesystem.listFilesystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Filesystem', 'listFilesystem', body)

    def testLoadFilesystemList(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuid': '',
        }
        
        
        filesystem = Filesystem(a)
        r = filesystem.loadFilesystemList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Filesystem', 'loadFilesystemList', body)

    def testImportFilesystemList(self):
        a = Auth(username, pwd)
        body = {
            'filesystem_list': [{
            'name': '',
            'fs_name': '',
            'quota_switch': 1,
            'quota_size': 1,
            'compress': 1,
            'dedup': 1,
            'pool_uuid': '',},],
        }
        
        
        filesystem = Filesystem(a)
        r = filesystem.importFilesystemList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Filesystem', 'importFilesystemList', body)


if __name__ == '__main__':
    unittest.main()
