
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.v20181227.DataBaseBackup import DataBaseBackup
from info2soft import Auth
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
        dataBaseBackup = DataBaseBackup(a)
        body = {}
        r = dataBaseBackup.importConfig(body)
        print(r[0])

    def testExportConfig(self):
        a = Auth(username, pwd)
        dataBaseBackup = DataBaseBackup(a)
        body = {}
        r = dataBaseBackup.exportConfig(body)
        print(r[0])

    def testListBackupHistory(self):
        a = Auth(username, pwd)
        dataBaseBackup = DataBaseBackup(a)
        body = {}
        r = dataBaseBackup.listBackupHistory(body)
        print(r[0])

    def testBackupConfig(self):
        a = Auth(username, pwd)
        dataBaseBackup = DataBaseBackup(a)
        body = {}
        r = dataBaseBackup.backupConfig(body)
        print(r[0])

    def testDescribeBackupConfig(self):
        a = Auth(username, pwd)
        dataBaseBackup = DataBaseBackup(a)
        body = {}
        r = dataBaseBackup.describeBackupConfig(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
