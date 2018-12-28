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

    def testListTimingRecoveryMssqlTime(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.listTimingRecoveryMssqlTime(body)
        print(r[0])

    def testDescribeTimingRecoveryMssqlInitInfo(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.describeTimingRecoveryMssqlInitInfo(body)
        print(r[0])

    def testListTimingRecoveryPathList(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.listTimingRecoveryPathList(body)
        print(r[0])

    def testVerifyTimingRecoveryMssqlInfo(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.verifyTimingRecoveryMssqlInfo(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.tempFuncName(body)
        print(r[0])

    def testCreateTimingRecovery(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.createTimingRecovery(body)
        print(r[0])

    def testModifyTimingRecovery(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.modifyTimingRecovery(body)
        print(r[0])

    def testDescribeTimingRecovery(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.describeTimingRecovery(body)
        print(r[0])

    def testListTimingRecovery(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.listTimingRecovery(body)
        print(r[0])

    def testListTimingRecoveryStatus(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.listTimingRecoveryStatus(body)
        print(r[0])

    def testDeleteTimingRecovery(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.deleteTimingRecovery(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        timingBackup = TimingBackup(a)
        body = {}
        r = timingBackup.tempFuncName(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()
