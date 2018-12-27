
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.rep.v20181227.RepRecovery import RepRecovery
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
    
                
class RepRecoveryTestCase(unittest.TestCase):

    def testCreateRepRecovery(self):
        a = Auth(username, pwd)
        repRecovery = RepRecovery(a)
        body = {}
        r = repRecovery.createRepRecovery(body)
        print(r[0])

    def testDescribeRepRecovery(self):
        a = Auth(username, pwd)
        repRecovery = RepRecovery(a)
        body = {}
        r = repRecovery.describeRepRecovery(body)
        print(r[0])

    def testDeleteRepRecovery(self):
        a = Auth(username, pwd)
        repRecovery = RepRecovery(a)
        body = {}
        r = repRecovery.deleteRepRecovery(body)
        print(r[0])

    def testListRepRecovery(self):
        a = Auth(username, pwd)
        repRecovery = RepRecovery(a)
        body = {}
        r = repRecovery.listRepRecovery(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        repRecovery = RepRecovery(a)
        body = {}
        r = repRecovery.tempFuncName(body)
        print(r[0])

    def testListRepRecoveryStatus(self):
        a = Auth(username, pwd)
        repRecovery = RepRecovery(a)
        body = {}
        r = repRecovery.listRepRecoveryStatus(body)
        print(r[0])

    def testListRepRecoveryCdpRange(self):
        a = Auth(username, pwd)
        repRecovery = RepRecovery(a)
        body = {}
        r = repRecovery.listRepRecoveryCdpRange(body)
        print(r[0])

    def testListRepRecoveryCdpLog(self):
        a = Auth(username, pwd)
        repRecovery = RepRecovery(a)
        body = {}
        r = repRecovery.listRepRecoveryCdpLog(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
