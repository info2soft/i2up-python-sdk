
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import DiskPool
from info2soft.resource.v20240819.DiskPool import DiskPool
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


class DiskPoolTestCase(unittest.TestCase):

    def testListDiskPool(self):
        a = Auth(username, pwd)
        body = {
            'like_args': {
            'pool_name': '',},
            'where_args': {
            'pool_type': 1,
            'bk_uuid': [],},
        }
        
        
        diskPool = DiskPool(a)
        r = diskPool.listDiskPool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DiskPool', 'listDiskPool', body)

    def testCreateDiskPool(self):
        a = Auth(username, pwd)
        body = {
            'pool_name': '',
            'pool_uuid': '',
            'pool_type': 1,
            'bk_uuid': '',
            'storage_path': '',
            'rootfs': 1,
            'zfs_pool_uuid': '',
            'auto_expand': 1,
            'zfs_fs_uuid': '',
            'max_concurrent': 1,
            'dedupe_sto_uuid': '',
            'domain_uuid': '',
            'sto_uuid': '',
            'bucket_uuid': '',
            'nas_type': 'NFS',
            'export_path': '',
        }
        
        
        diskPool = DiskPool(a)
        r = diskPool.createDiskPool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DiskPool', 'createDiskPool', body)

    def testModifyDiskPool(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuid': '',
            'pool_name': '',
            'random_str': '',
            'bk_uuid': '',
            'max_concurrent': 1,
            'zfs_pool_uuid': '',
            'auto_expand': '',
            'zfs_fs_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        diskPool = DiskPool(a)
        r = diskPool.modifyDiskPool(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DiskPool', 'modifyDiskPool', body)

    def testDescribeDiskPool(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        diskPool = DiskPool(a)
        r = diskPool.describeDiskPool(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DiskPool', 'describeDiskPool', body)

    def testDeleteDiskPool(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuids': [],
        }
        
        
        diskPool = DiskPool(a)
        r = diskPool.deleteDiskPool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DiskPool', 'deleteDiskPool', body)

    def testCheckDiskPool(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
            'storage_path': '',
            'pool_uuid': '',
        }
        
        
        diskPool = DiskPool(a)
        r = diskPool.checkDiskPool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DiskPool', 'checkDiskPool', body)


if __name__ == '__main__':
    unittest.main()
