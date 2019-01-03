# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.fsp.v20181227.FspRecovery import FspRecovery
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
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.listFspRecoveryDir(body)
        print(r[0])

    def testListFspRecoveryNic(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.listFspRecoveryNic(body)
        print(r[0])

    def testListFspRecoveryPoint(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.listFspRecoveryPoint(body)
        print(r[0])

    def testVerifyFspRecoveryVolumeSpace(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.verifyFspRecoveryVolumeSpace(body)
        print(r[0])

    def testVerifyFspRecoveryOldRule(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.verifyFspRecoveryOldRule(body)
        print(r[0])

    def testVerifyFspRecoveryLicense(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.verifyFspRecoveryLicense(body)
        print(r[0])

    def testVerifyFspRecoveryOsVersion(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.verifyFspRecoveryOsVersion(body)
        print(r[0])

    def testCreateFspRecovery(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.createFspRecovery(body)
        print(r[0])

    def testModifyFspRecovery(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.modifyFspRecovery(body)
        print(r[0])

    def testDesribeFspRecovery(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.desribeFspRecovery(body)
        print(r[0])

    def testDeleteFspRecovery(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.deleteFspRecovery(body)
        print(r[0])

    def testListFspRecovery(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.listFspRecovery(body)
        print(r[0])

    def testStartFspRecovery(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.startFspRecovery(body)
        print(r[0])

    def testStopFspRecovery(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.stopFspRecovery(body)
        print(r[0])

    def testMoveFspRecovery(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.moveFspRecovery(body)
        print(r[0])

    def testRebootFspRecovery(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.rebootFspRecovery(body)
        print(r[0])

    def testListFspRecoveryStatus(self):
        a = Auth(username, pwd)
        fspRecovery = FspRecovery(a)
        body = {}
        r = fspRecovery.listFspRecoveryStatus(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()
