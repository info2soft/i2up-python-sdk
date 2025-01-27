
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import BackupSetRulePolicy
from info2soft.backupSetRulePolicy.v20250123.BackupSetRulePolicy import BackupSetRulePolicy
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


class BackupSetRulePolicyTestCase(unittest.TestCase):

    def testCreateReplicaTask(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'task_type': '',
            'src_unit_uuid': '',
            'dst_unit_uuid': '',
            'pool_uuid': '',
            'retention': 1,
            'priority': 1,
            'bkup_window': [{
            'wday': 1,
            'from': '',
            'to': '',},],
            'bandwidth': '',
            'disable': 1,
            'next_replica_uuid': '',
            'encrypt_setting': {
            'encrypt': 1,
            'encrypt_switch': 1,},
            'compress_setting': {
            'compress': 1,
            'compress_switch': 1,},
            'network_type': 1,
            'thread_num': 1,
            'concurrent_mode': 1,
            'retry_switch': 1,
            'retry_times': 1,
            'retry_interval': 1,
            'domain_uuid': '',
            'bk_set_import_uuid': '',
        }
        
        
        backupSetRulePolicy = BackupSetRulePolicy(a)
        r = backupSetRulePolicy.createReplicaTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSetRulePolicy', 'createReplicaTask', body)

    def testModifyReplicaTask(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'task_type': '',
            'src_unit_uuid': '',
            'dst_unit_uuid': '',
            'tape_uuid': '',
            'retention': 1,
            'priority': 1,
            'trans_mode': 1,
            'bkup_window': '',
            'bandwidth': '',
            'task_uuid': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        backupSetRulePolicy = BackupSetRulePolicy(a)
        r = backupSetRulePolicy.modifyReplicaTask(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSetRulePolicy', 'modifyReplicaTask', body)

    def testListReplicaTask(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
            'like_args': {
            'task_name': '',
            'src_unit_name': '',
            'dst_unit_name': '',},
        }
        
        
        backupSetRulePolicy = BackupSetRulePolicy(a)
        r = backupSetRulePolicy.listReplicaTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSetRulePolicy', 'listReplicaTask', body)

    def testDescribeReplicaTask(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        backupSetRulePolicy = BackupSetRulePolicy(a)
        r = backupSetRulePolicy.describeReplicaTask(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSetRulePolicy', 'describeReplicaTask', body)

    def testDeleteReplicaTask(self):
        a = Auth(username, pwd)
        body = {
            'task_uuids': [],
            'force': 1,
        }
        
        
        backupSetRulePolicy = BackupSetRulePolicy(a)
        r = backupSetRulePolicy.deleteReplicaTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSetRulePolicy', 'deleteReplicaTask', body)


if __name__ == '__main__':
    unittest.main()
