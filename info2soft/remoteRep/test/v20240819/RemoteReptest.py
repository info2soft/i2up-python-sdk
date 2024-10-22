
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import RemoteRep
from info2soft.remoteRep.v20240819.RemoteRep import RemoteRep
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


class RemoteRepTestCase(unittest.TestCase):

    def testCreateRemoteRep(self):
        a = Auth(username, pwd)
        body = {
            'rep_name': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'rep_type': 0,
            'wk_pool_uuid': '',
            'bk_pool_uuid': '',
            'rule_uuid': '',
            'file_system': '',
            'volume_uuid': '',
            'snapshot': '',
            'clone_uuid': '',
            'sec_snapshot': '',
            'sec_clone_uuid': '',
            'bkup_policy': 1,
            'bkup_one_time': 1,
            'bkup_schedule': {
            'limit': 1,
            'sched_day': [],
            'sched_every': 1,
            'sched_time': [],
            'sched_gap_min': 1,
            'backup_type': 1,},
            'bkup_window': {
            'sched_time_start': '',
            'sched_time_end': '',},
            'encrypt_switch': 0,
            'encrypt': '',
            'compress_switch': 0,
            'compress': 1,
            'secret_key': '',
            'remote_volume_uuid': '',
            'band_width': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.createRemoteRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'createRemoteRep', body)

    def testModifyRemoteRep(self):
        a = Auth(username, pwd)
        body = {
            'rep_name': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'rep_type': 0,
            'wk_pool_uuid': '',
            'bk_pool_uuid': '',
            'rule_uuid': '',
            'file_system': '',
            'volume_uuid': '',
            'snapshot': '',
            'clone_uuid': '',
            'sec_snapshot': '',
            'sec_clone_uuid': '',
            'bkup_policy': 1,
            'bkup_one_time': 1,
            'bkup_schedule': {
            'limit': 1,
            'sched_day': [],
            'sched_every': 1,
            'sched_time': [],
            'sched_gap_min': 1,
            'backup_type': 1,},
            'bkup_window': {
            'sched_time_start': '',
            'sched_time_end': '',},
            'random_str': '',
            'remote_volume_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        remoteRep = RemoteRep(a)
        r = remoteRep.modifyRemoteRep(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'modifyRemoteRep', body)

    def testListRemoteRep(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'limit': 10,
            'page': 1,
            'search_value': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.listRemoteRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'listRemoteRep', body)

    def testDescribeRemoteRep(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        remoteRep = RemoteRep(a)
        r = remoteRep.describeRemoteRep(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'describeRemoteRep', body)

    def testStartRemoteRep(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.startRemoteRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'startRemoteRep', body)

    def testStopRemoteRep(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.stopRemoteRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'stopRemoteRep', body)

    def testStartImmediatelyRemoteRep(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.startImmediatelyRemoteRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'startImmediatelyRemoteRep', body)

    def testDeleteRemoteRep(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'force': 1,
            'del_policy': 1,
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.deleteRemoteRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'deleteRemoteRep', body)

    def testListRemoteRepStatus(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'force_refresh': 1,
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.listRemoteRepStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'listRemoteRepStatus', body)

    def testListStoragePoolRuleList(self):
        a = Auth(username, pwd)
        body = {
            'rep_type': 1,
            'pool_uuid': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.listStoragePoolRuleList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'listStoragePoolRuleList', body)

    def testListFileSystem(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuid': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.listFileSystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'listFileSystem', body)

    def testListFirstCloneVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.listFirstCloneVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'listFirstCloneVolume', body)

    def testDescribeCloneVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '',
            'snapshot_time': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.describeCloneVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'describeCloneVolume', body)

    def testFilterStorageNode(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.filterStorageNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'filterStorageNode', body)

    def testListFileSnapshot(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'pool_uuid': '',
        }
        
        
        remoteRep = RemoteRep(a)
        r = remoteRep.listFileSnapshot(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteRep', 'listFileSnapshot', body)


if __name__ == '__main__':
    unittest.main()
