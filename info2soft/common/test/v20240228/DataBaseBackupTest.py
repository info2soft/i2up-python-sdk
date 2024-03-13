
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.common.v20240228.DataBaseBackup import DataBaseBackup
# from info2soft.common.v20200722.DataBaseBackup import DataBaseBackup
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


class DataBaseBackupTestCase(unittest.TestCase):

    def testImportConfig(self):
        a = Auth(username, pwd)
        body = {
            'keep_cc_ip': 1,
        }
        
        dataBaseBackup = DataBaseBackup(a)
        r = dataBaseBackup.importConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataBaseBackup', 'importConfig', body)

    def testExportConfig(self):
        a = Auth(username, pwd)
        body = {
        }
        
        dataBaseBackup = DataBaseBackup(a)
        r = dataBaseBackup.exportConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataBaseBackup', 'exportConfig', body)

    def testListBackupHistory(self):
        a = Auth(username, pwd)
        body = {
        }
        
        dataBaseBackup = DataBaseBackup(a)
        r = dataBaseBackup.listBackupHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataBaseBackup', 'listBackupHistory', body)

    def testBackupConfig(self):
        a = Auth(username, pwd)
        body = {
        }
        
        dataBaseBackup = DataBaseBackup(a)
        r = dataBaseBackup.backupConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataBaseBackup', 'backupConfig', body)

    def testDescribeBackupConfig(self):
        a = Auth(username, pwd)
        body = {
        }
        
        dataBaseBackup = DataBaseBackup(a)
        r = dataBaseBackup.describeBackupConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DataBaseBackup', 'describeBackupConfig', body)


if __name__ == '__main__':
    unittest.main()
