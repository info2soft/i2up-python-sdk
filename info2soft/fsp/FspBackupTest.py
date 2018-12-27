
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

    def testListFspBackupNic(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.listFspBackupNic(body)
        print(r[0])

    def testListFspBackupDir(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.listFspBackupDir(body)
        print(r[0])

    def testVerifyFspBackupCoopySpace(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.verifyFspBackupCoopySpace(body)
        print(r[0])

    def testVerifyFspBackupLicense(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.verifyFspBackupLicense(body)
        print(r[0])

    def testVerifyFspBackupOldRule(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.verifyFspBackupOldRule(body)
        print(r[0])

    def testVerifyFspBackupOsVersion(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.verifyFspBackupOsVersion(body)
        print(r[0])

    def testCreateFspBackup(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.createFspBackup(body)
        print(r[0])

    def testModifyFspBackup(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.modifyFspBackup(body)
        print(r[0])

    def testDescribeFspBackup(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.describeFspBackup(body)
        print(r[0])

    def testDeleteFspBackup(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.deleteFspBackup(body)
        print(r[0])

    def testListFspBackup(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.listFspBackup(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.tempFuncName(body)
        print(r[0])

    def testListFspBackupStatus(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.listFspBackupStatus(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {}
        r = fspBackup.tempFuncName(body)
        print(r[0])

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
