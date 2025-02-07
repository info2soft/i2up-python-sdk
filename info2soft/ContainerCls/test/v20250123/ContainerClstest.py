
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import ContainerCls
from info2soft.ContainerCls.v20250123.ContainerCls import ContainerCls
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


class ContainerClsTestCase(unittest.TestCase):

    def testCreateContinerClusterBackup(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'biz_grp_list': [],
            'cls_type': 1,
            'cls_uuid': '',
            'location_uuid': '',
            'resource_type': [],
            'resource_label': '',
            'resource_namespace': [],
            'callback_uuid_list': [],
            'tag': '',
            'backup_one_time': 1,
            'backup_schedule': [],
            'backup_policy': 1,
            'save_days': 1,
            'task_type': 1,
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.createContinerClusterBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'createContinerClusterBackup', body)

    def testListContainerClusterBackup(self):
        a = Auth(username, pwd)
        body = {
            'where_args': {
            'task_type': '',},
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.listContainerClusterBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'listContainerClusterBackup', body)

    def testDescribeContainerClusterBackup(self):
        a = Auth(username, pwd)
        body = {
            'sub_time': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        containerCls = ContainerCls(a)
        r = containerCls.describeContainerClusterBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'describeContainerClusterBackup', body)

    def testModifyContainerClusterBackup(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'biz_grp_list': [],
            'cls_type': 1,
            'cls_uuid': '',
            'location_uuid': '',
            'resource_type': '',
            'resource_label': '',
            'resource_namespace': '',
            'callback_uuid': '',
            'tag': '',
            'backup_type': 1,
            'bkup_one_time': '',
            'bkup_schedule': {
            'limit': '',
            'sched_day': '',
            'sched_every': '',
            'sched_time': '',
            'sched_gap_min': '',
            'backup_type': '',},
            'bkup_policy': 1,
            'save_days': 1,
            'bkup_window': {
            'sched_time_start': '',
            'sched_time_end': '',},
            'task_uuid': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        containerCls = ContainerCls(a)
        r = containerCls.modifyContainerClusterBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'modifyContainerClusterBackup', body)

    def testDeleteContainerClusterBackup(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'sub_task_uuid': '',
            'force': 1,
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.deleteContainerClusterBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'deleteContainerClusterBackup', body)

    def testListContainerClusterBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.listContainerClusterBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'listContainerClusterBackupStatus', body)

    def testBackupImmediateContainerClusterBackup(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'operate': 'start',
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.backupImmediateContainerClusterBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'backupImmediateContainerClusterBackup', body)

    def testListContainerClusterBackupSubTask(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': '681D716B-D3CE-4E35-A018-E2E3D3C5743E',
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.listContainerClusterBackupSubTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'listContainerClusterBackupSubTask', body)

    def testGetContainerClusterBackupInfo(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': '',
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.getContainerClusterBackupInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'getContainerClusterBackupInfo', body)

    def testCreateContainerClusterRecovery(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'task_type': '',
            'biz_grp_list': [],
            'cls_type': 1,
            'cls_uuid': '',
            'location_uuid': '',
            'backup_task_uuid': '',
            'rc_point_in_time': '',
            'callback_uuid_list': [],
            'save_nodeport': 1,
            'tag': '',
            'namespace_mapping': '',
            'src_cls_uuid': '',
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.createContainerClusterRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'createContainerClusterRecovery', body)

    def testListContainerClusterRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.listContainerClusterRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'listContainerClusterRecovery', body)

    def testDescribeContainerClusterRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        containerCls = ContainerCls(a)
        r = containerCls.describeContainerClusterRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'describeContainerClusterRecovery', body)

    def testModifyContainerClusterRecovery(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'task_type': '',
            'biz_grp_list': [],
            'cls_type': 1,
            'cls_uuid': '',
            'location_uuid': '',
            'backup_task_uuid': '',
            'rc_point_in_time': '',
            'callback_uuid': '',
            'save_nodeport': 1,
            'tag': '',
            'user_uuid': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        containerCls = ContainerCls(a)
        r = containerCls.modifyContainerClusterRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'modifyContainerClusterRecovery', body)

    def testDeleteContainerClusterRecovery(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'force': 1,
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.deleteContainerClusterRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'deleteContainerClusterRecovery', body)

    def testListContainerClusterRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.listContainerClusterRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'listContainerClusterRecoveryStatus', body)

    def testListContainerClusterRecoveryPoint(self):
        a = Auth(username, pwd)
        body = {
            'backup_task_uuid': '',
            'cls_uuid': '',
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.listContainerClusterRecoveryPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'listContainerClusterRecoveryPoint', body)

    def testStartContainerClusterRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.startContainerClusterRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'startContainerClusterRecovery', body)

    def testStopContainerClusterRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'task_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.stopContainerClusterRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'stopContainerClusterRecovery', body)

    def testGetContainerClusterRecoveryInfo(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': '',
        }
        
        
        containerCls = ContainerCls(a)
        r = containerCls.getContainerClusterRecoveryInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCls', 'getContainerClusterRecoveryInfo', body)


if __name__ == '__main__':
    unittest.main()
