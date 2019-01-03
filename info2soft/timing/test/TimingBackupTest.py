
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.timing.v20181227.TimingBackup import TimingBackup
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
    
                
class TimingBackupTestCase(unittest.TestCase):

    def testDescribeTimingBackupMssqlSource(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.describeTimingBackupMssqlSource(body)
        print(r[0])

    def testVerifyTimingBackupOracleInfo(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.verifyTimingBackupOracleInfo(body)
        print(r[0])

    def testDescribeTimingBackupOracleContent(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.describeTimingBackupOracleContent(body)
        print(r[0])

    def testDescibeTimingBackupOracleSriptPath(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.descibeTimingBackupOracleSriptPath(body)
        print(r[0])

    def testListTimingBackupMssqlDbList(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.listTimingBackupMssqlDbList(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.tempFuncName(body)
        print(r[0])

    def testCreateTimingBackup(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.createTimingBackup(body)
        print(r[0])

    def testDescribeTimingBackup(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.describeTimingBackup(body)
        print(r[0])

    def testModifyTimingBackup(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.modifyTimingBackup(body)
        print(r[0])

    def testListTimingBackup(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.listTimingBackup(body)
        print(r[0])

    def testListTimingBackupStatus(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.listTimingBackupStatus(body)
        print(r[0])

    def testDeleteTimingBackup(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.deleteTimingBackup(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.tempFuncName(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.tempFuncName(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
