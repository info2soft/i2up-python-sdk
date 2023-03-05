# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.storage_cdm.v20230227.SnapshotTask import SnapshotTask
# from info2soft.snapshotTask.v20200722.SnapshotTask import SnapshotTask
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


class SnapshotTaskTestCase(unittest.TestCase):

    def testCreateSnapshotTask(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'bk_uuid': '',
            'copy_volume_list': [],
            'quiet_switch': 1,
            'quiet_obj_type': 1,
            'quiet_obj_config': {},
            'schedule': {
                'interval': 1,
                'retetion_days': 1,
                'limit': 1,
                'type': 'interval',
                'unit': 1, },
            'volume_type': 1,
            'script': {
                'before_snapshot': '',
                'after_snapshot': '', },
            'bkup_schedule': {
                'sched_every': '',
                'sched_day': '',
                'sched_time': '', },
        }

        snapshotTask = SnapshotTask(a)
        r = snapshotTask.createSnapshotTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SnapshotTask', 'createSnapshotTask', body)

    def testModifySnapshotTask(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        snapshotTask = SnapshotTask(a)
        r = snapshotTask.modifySnapshotTask(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SnapshotTask', 'modifySnapshotTask', body)

    def testListSnapshotTask(self):
        a = Auth(username, pwd)
        body = {
            'status': '',
        }

        snapshotTask = SnapshotTask(a)
        r = snapshotTask.listSnapshotTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SnapshotTask', 'listSnapshotTask', body)

    def testDeleteSnapshotTask(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [
                '16CB63E1-13FA-FB32-EB49-D790682C9648', ],
            'force': '',
            'del_snap': 1,
        }

        snapshotTask = SnapshotTask(a)
        r = snapshotTask.deleteSnapshotTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SnapshotTask', 'deleteSnapshotTask', body)

    def testListSnapshotTaskStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force_refresh': 1,
        }

        snapshotTask = SnapshotTask(a)
        r = snapshotTask.listSnapshotTaskStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SnapshotTask', 'listSnapshotTaskStatus', body)

    def testDescribeSnapshotTask(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        snapshotTask = SnapshotTask(a)
        r = snapshotTask.describeSnapshotTask(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SnapshotTask', 'describeSnapshotTask', body)

    def testListSnapshotList(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'from': 0,
            'to': 0,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        snapshotTask = SnapshotTask(a)
        r = snapshotTask.listSnapshotList(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SnapshotTask', 'listSnapshotList', body)

    def testDeleteSnapshotList(self):
        a = Auth(username, pwd)
        body = {
            'snapshot_list': [{
                'volume_uuid': '',
                'snapshot_name': '',
                'snapshot_time': '', }, ],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        snapshotTask = SnapshotTask(a)
        r = snapshotTask.deleteSnapshotList(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'SnapshotTask', 'deleteSnapshotList', body)


if __name__ == '__main__':
    unittest.main()
