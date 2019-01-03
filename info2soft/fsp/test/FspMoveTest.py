
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.fsp.v20181227.FspMove import FspMove
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
    
                
class FspMoveTestCase(unittest.TestCase):

    def testListFspMoveNic(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.listFspMoveNic(body)
        print(r[0])

    def testListFspMoveDir(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.listFspMoveDir(body)
        print(r[0])

    def testVerifyFspMoveLicense(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.verifyFspMoveLicense(body)
        print(r[0])

    def testVerifyFspMoveOldRule(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.verifyFspMoveOldRule(body)
        print(r[0])

    def testVerifyFspMoveVolumeSpace(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.verifyFspMoveVolumeSpace(body)
        print(r[0])

    def testVerifyFspMoveOsVersion(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.verifyFspMoveOsVersion(body)
        print(r[0])

    def testCreateFspMove(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.createFspMove(body)
        print(r[0])

    def testModifyFspMove(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.modifyFspMove(body)
        print(r[0])

    def testDescribeFspMove(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.describeFspMove(body)
        print(r[0])

    def testDeleteFspMove(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.deleteFspMove(body)
        print(r[0])

    def testListFspMove(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.listFspMove(body)
        print(r[0])

    def testStartFspMove(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.startFspMove(body)
        print(r[0])

    def testStopFspMove(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.stopFspMove(body)
        print(r[0])

    def testMoveFspMove(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.moveFspMove(body)
        print(r[0])

    def testRebootFspMove(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.rebootFspMove(body)
        print(r[0])

    def testListFspMoveStatus(self):
        a = Auth(username, pwd)
        fspMove = FspMove(a)
        body = {}
        r = fspMove.listFspMoveStatus(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
