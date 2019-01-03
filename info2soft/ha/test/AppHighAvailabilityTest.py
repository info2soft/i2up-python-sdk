
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.ha.v20181227.AppHighAvailability import AppHighAvailability
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
    
                
class AppHighAvailabilityTestCase(unittest.TestCase):

    def testListHA(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.listHA(body)
        print(r[0])

    def testStartHA(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.startHA(body)
        print(r[0])

    def testStopHA(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.stopHA(body)
        print(r[0])

    def testForceSwitchHA(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.forceSwitchHA(body)
        print(r[0])

    def testDeleteHA(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.deleteHA(body)
        print(r[0])

    def testListHAStatus(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.listHAStatus(body)
        print(r[0])

    def testDescribeHAScriptPath(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.describeHAScriptPath(body)
        print(r[0])

    def testModifyHA(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.modifyHA(body)
        print(r[0])

    def testCreateHA(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.createHA(body)
        print(r[0])

    def testListNicInfo(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.listNicInfo(body)
        print(r[0])

    def testDescribeHA(self):
        a = Auth(username, pwd)
        appHighAvailability = AppHighAvailability(a)
        body = {}
        r = appHighAvailability.describeHA(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
