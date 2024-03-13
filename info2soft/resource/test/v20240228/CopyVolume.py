# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.resource.v20240228.CopyVolume import CopyVolume
# from info2soft.resource.v20200722.CopyVolume import CopyVolume
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


class CopyVolumeTestCase(unittest.TestCase):

    def testCreateCopyVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_name': '',
            'bk_uuid': '',
            'pool_uuid': '',
            'volume_size': '',
            'link_protocol': '',
            'create_fs': 1,
            'fs_type': '',
            'attach_point': [],
            'fc_initiator_wwpn': '',
            'fc_target_wwpn': '',
            'exclusive': 1,
            'bk_type': '',
            'auto_switch': 1,
            'sparse_switch': 1,
            'raw_uuid': '',
            'volume_type': 0,
        }

        copyVolume = CopyVolume(a)
        r = copyVolume.createCopyVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CopyVolume', 'createCopyVolume', body)

    def testModifyCopyVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_name': '',
            'bk_uuid': '',
            'volume_size': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        copyVolume = CopyVolume(a)
        r = copyVolume.modifyCopyVolume(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CopyVolume', 'modifyCopyVolume', body)

    def testDescribeCopyVolume(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        copyVolume = CopyVolume(a)
        r = copyVolume.describeCopyVolume(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CopyVolume', 'describeCopyVolume', body)

    def testCopyVolumeList(self):
        a = Auth(username, pwd)
        body = {
        }

        copyVolume = CopyVolume(a)
        r = copyVolume.copyVolumeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CopyVolume', 'copyVolumeList', body)

    def testDeleteCopyVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuids': [],
            'force': 1,
        }

        copyVolume = CopyVolume(a)
        r = copyVolume.deleteCopyVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CopyVolume', 'deleteCopyVolume', body)

    def testListCopyVolumeStatus(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuids': [],
            'force_refresh': 1,
        }

        copyVolume = CopyVolume(a)
        r = copyVolume.listCopyVolumeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CopyVolume', 'listCopyVolumeStatus', body)

    def testListSnapshotList(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'from': 0,
            'to': 0,
            'volume_type': 0,
            'storage_uuid': '',
            'storage_pool_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        copyVolume = CopyVolume(a)
        r = copyVolume.listSnapshotList(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CopyVolume', 'listSnapshotList', body)

    def testListCopyCdmVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
            'volume_type': 1,
            'bk_uuid': '',
        }

        copyVolume = CopyVolume(a)
        r = copyVolume.listCopyCdmVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CopyVolume', 'listCopyCdmVolume', body)

    def testListCopyVolumeClient(self):
        a = Auth(username, pwd)
        body = {
            'limit': 300,
            'page': 1,
            'type': 1,
        }

        copyVolume = CopyVolume(a)
        r = copyVolume.listCopyVolumeClient(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CopyVolume', 'listCopyVolumeClient', body)


if __name__ == '__main__':
    unittest.main()
