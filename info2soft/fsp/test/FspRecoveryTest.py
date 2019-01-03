# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.fsp.v20181227.FspBackup import FspBackup
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


class FspBackupTestCase(unittest.TestCase):

    def testListFspRecoveryDir(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.listFspRecoveryDir(body)
        print(r[0])

    def testListFspRecoveryNic(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.listFspRecoveryNic(body)
        print(r[0])

    def testListFspRecoveryPoint(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.listFspRecoveryPoint(body)
        print(r[0])

    def testVerifyFspRecoveryVolumeSpace(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.verifyFspRecoveryVolumeSpace(body)
        print(r[0])

    def testVerifyFspRecoveryOldRule(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.verifyFspRecoveryOldRule(body)
        print(r[0])

    def testVerifyFspRecoveryLicense(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.verifyFspRecoveryLicense(body)
        print(r[0])

    def testVerifyFspRecoveryOsVersion(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.verifyFspRecoveryOsVersion(body)
        print(r[0])

    def testCreateFspRecovery(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.createFspRecovery(body)
        print(r[0])

    def testModifyFspRecovery(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.modifyFspRecovery(body)
        print(r[0])

    def testDesribeFspRecovery(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.desribeFspRecovery(body)
        print(r[0])

    def testDeleteFspRecovery(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.deleteFspRecovery(body)
        print(r[0])

    def testListFspRecovery(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.listFspRecovery(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.tempFuncName(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.tempFuncName(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()
