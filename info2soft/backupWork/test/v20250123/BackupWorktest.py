
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import BackupWork
from info2soft.backupWork.v20250123.BackupWork import BackupWork
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


class BackupWorkTestCase(unittest.TestCase):

    def testListBackupWork(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'filter_uuid': '',
        }
        
        
        backupWork = BackupWork(a)
        r = backupWork.listBackupWork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'listBackupWork', body)

    def testDescribeBackupWork(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        backupWork = BackupWork(a)
        r = backupWork.describeBackupWork(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'describeBackupWork', body)

    def testRebootBackupWork(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'work_uuids': [],
        }
        
        
        backupWork = BackupWork(a)
        r = backupWork.rebootBackupWork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'rebootBackupWork', body)

    def testStopBackupWork(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'work_uuids': [],
        }
        
        
        backupWork = BackupWork(a)
        r = backupWork.stopBackupWork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'stopBackupWork', body)

    def testDeleteBackupWork(self):
        a = Auth(username, pwd)
        body = {
            'work_uuids': [],
            'force': 1,
        }
        
        
        backupWork = BackupWork(a)
        r = backupWork.deleteBackupWork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'deleteBackupWork', body)

    def testListBackupWorkLogs(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'start': 1,
            'end': 1,
            'level': 1,
            'search_content': '',
            'type': 1,
            'node_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        backupWork = BackupWork(a)
        r = backupWork.listBackupWorkLogs(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'listBackupWorkLogs', body)

    def testListBackupWorkKeyEvents(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        backupWork = BackupWork(a)
        r = backupWork.listBackupWorkKeyEvents(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'listBackupWorkKeyEvents', body)

    def testDescribeBackupWorkResult(self):
        a = Auth(username, pwd)
        body = {
            'work_uuids': [],
            'op_switch': 1,
            'barcode_list': [],
        }
        
        
        backupWork = BackupWork(a)
        r = backupWork.describeBackupWorkResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'describeBackupWorkResult', body)

    def testListBackupWorkFilter(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        backupWork = BackupWork(a)
        r = backupWork.listBackupWorkFilter(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'listBackupWorkFilter', body)

    def testCreateBackupWorkFilter(self):
        a = Auth(username, pwd)
        body = {
            'filter_name': '',
            'description': '',
            'and_or': 1,
            'rules': [{
            'key': '',
            'operator': '',
            'value': '',},],
        }
        
        
        backupWork = BackupWork(a)
        r = backupWork.createBackupWorkFilter(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'createBackupWorkFilter', body)

    def testDescribeBackupWorkFilter(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        backupWork = BackupWork(a)
        r = backupWork.describeBackupWorkFilter(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'describeBackupWorkFilter', body)

    def testModifyBackupWorkFilter(self):
        a = Auth(username, pwd)
        body = {
            'filter_name': '',
            'description': '',
            'and_or': 1,
            'rules': [{
            'key': '',
            'operator': '',
            'value': '',},],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        backupWork = BackupWork(a)
        r = backupWork.modifyBackupWorkFilter(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'modifyBackupWorkFilter', body)

    def testDeleteBackupWorkFilter(self):
        a = Auth(username, pwd)
        body = {
            'filter_uuids': [],
            'force': 0,
        }
        
        
        backupWork = BackupWork(a)
        r = backupWork.deleteBackupWorkFilter(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BackupWork', 'deleteBackupWorkFilter', body)


if __name__ == '__main__':
    unittest.main()
