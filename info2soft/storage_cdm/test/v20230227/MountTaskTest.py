# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.storage_cdm.v20230227.MountTask import MountTask
# from info2soft.mountTask.v20200722.MountTask import MountTask
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


class MountTaskTestCase(unittest.TestCase):

    def testCreateMountTask(self):
        a = Auth(username, pwd)
        body = {
            'task_name': 'task_name',
            'wk_uuid': '1CCDB5EB848C180F02814E96C2909202',
            'if_mount': 0,
            'mount_point': '/dev/sda',
            'protocol': 'iscsi',
            'bk_uuid': '5CC2B5EB848C180F02814E96C2F09202',
            'volume_uuid': '4CC2B52B845C180F02112E96C2F09H02',
            'iscsi_initiator': 'iscsi_initiator',
            'snapshot_name': '',
            'snapshot_time': '',
            'fc_initiator_wwpn': '',
            'fc_target_wwpn': '',
            'volume_type': 1,
            'volume_name': '',
            'remote_volume_uuid': '',
        }

        mountTask = MountTask(a)
        r = mountTask.createMountTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MountTask', 'createMountTask', body)

    def testListMountTask(self):
        a = Auth(username, pwd)
        body = {
        }

        mountTask = MountTask(a)
        r = mountTask.listMountTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MountTask', 'listMountTask', body)

    def testDescribeMountTask(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        mountTask = MountTask(a)
        r = mountTask.describeMountTask(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MountTask', 'describeMountTask', body)

    def testDeleteMountTask(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'force': '',
        }

        mountTask = MountTask(a)
        r = mountTask.deleteMountTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MountTask', 'deleteMountTask', body)

    def testListMountTaskStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'force_refresh': 1,
        }

        mountTask = MountTask(a)
        r = mountTask.listMountTaskStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MountTask', 'listMountTaskStatus', body)

    def testGetIscsiInitiatorInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '1407E778CBFE9C4E9ACB766B94F1E102',
        }

        mountTask = MountTask(a)
        r = mountTask.getIscsiInitiatorInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MountTask', 'getIscsiInitiatorInfo', body)

    def testGetVolumeSnapshotTarget(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '13CB1D17-D0E7-169A-D6DC-9CFB32341989',
            'volume_uuid': '13CB1D17-D0E7-169A-D6DC-9CFB32341989',
            'protocol': 'iscsi',
            'iscsi_acl': 'iscsi initiator name',
            'snapshot_name': '13CB1D17-D0E7-169A-D6DC-9CFB32341989_20200801_180000_00',
        }

        mountTask = MountTask(a)
        r = mountTask.getVolumeSnapshotTarget(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MountTask', 'getVolumeSnapshotTarget', body)

    def testDeleteVolumeSnapshotTarget(self):
        a = Auth(username, pwd)
        body = {
            'protocol': '',
            'target': '',
            'volume_uuid': '',
            'storage': [{
                'storage_name': '',
                'storage_type': '',
                'storage_host': '',
                'storage_pool': '', }, ],
            'partition': [{
                'size': '',
                'fs_type': '',
                'fs_path': '',
                'offset': '', }, ],
            'dev_id': '',
            'bk_uuid': '',
        }

        mountTask = MountTask(a)
        r = mountTask.deleteVolumeSnapshotTarget(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'MountTask', 'deleteVolumeSnapshotTarget', body)


if __name__ == '__main__':
    unittest.main()
