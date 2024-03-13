
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import BackupSet
from info2soft.backupSet.v20240228.BackupSet import BackupSet
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


class BackupSetTestCase(unittest.TestCase):

    def testListBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limt': 10,
            'show_all_copy': 1,
        }
        
        backupSet = BackupSet(a)
        r = backupSet.listBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'listBackupSet', body)

    def testListQueryArgsBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'search_value': '',
            'delete': 1,
        }
        
        backupSet = BackupSet(a)
        r = backupSet.listQueryArgsBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'listQueryArgsBackupSet', body)

    def testextendBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': '',
        }

        backupSet = BackupSet(a)
        r = backupSet.extendBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'extendBackupSet', body)

    def testexpireBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': '',
        }

        backupSet = BackupSet(a)
        r = backupSet.expireBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'expireBackupSet', body)

    def testsetPrimaryBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': '',
        }

        backupSet = BackupSet(a)
        r = backupSet.setPrimaryBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'setPrimaryBackupSet', body)

    def testDeleteDbBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': '',
        }
        
        backupSet = BackupSet(a)
        r = backupSet.deleteDbBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'deleteDbBackupSet', body)

    def testDeleteBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_list': [{
            'bk_set_id': '',
            'bk_rule_uuid': '',},],
        }
        
        backupSet = BackupSet(a)
        r = backupSet.deleteBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'deleteBackupSet', body)

    def testDeleteBackupSetFromDb(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_list': [{
            'bk_set_id': '',
            'bk_rule_uuid': '',
            'copy_id': '',},],
        }
        
        backupSet = BackupSet(a)
        r = backupSet.deleteBackupSetFromDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'deleteBackupSetFromDb', body)

    def testCreateBackupSetRepRule(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuids': [],
            'unit_uuid': '',
            'tape_pool_uuid': '',
            'retention_level': '',
            'start_time': 1,
        }
        
        backupSet = BackupSet(a)
        r = backupSet.createBackupSetRepRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'createBackupSetRepRule', body)

    def testDescribeDeletedBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuid': '',
        }
        
        backupSet = BackupSet(a)
        r = backupSet.describeDeletedBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'describeDeletedBackupSet', body)

    def testDescribeBackupSetCopy(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limt': 10,
            'search_field': '',
            'search_value': '',
            'bk_set_uuid': '',
        }
        
        backupSet = BackupSet(a)
        r = backupSet.describeBackupSetCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'describeBackupSetCopy', body)

    def testListBackupSetRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limt': 10,
            'search_field': 'primary_copy',
            'search_value': '1',
        }
        
        backupSet = BackupSet(a)
        r = backupSet.listBackupSetRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'listBackupSetRule', body)

    def testValidateBackupSet(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuids': '',
            'mode': '',
        }
        
        backupSet = BackupSet(a)
        r = backupSet.validateBackupSet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'validateBackupSet', body)

    def testListBackupChain(self):
        a = Auth(username, pwd)
        body = {
            'bk_set_uuid': '',
            'backup_chain_policy': 1,
        }
        
        backupSet = BackupSet(a)
        r = backupSet.listBackupChain(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupSet', 'listBackupChain', body)


if __name__ == '__main__':
    unittest.main()
