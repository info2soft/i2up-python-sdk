
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.v20181227.Qr import Qr
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
    
                
class QrTestCase(unittest.TestCase):

    def testDescribeTimeStamp(self):
        a = Auth(username, pwd)
        qr = Qr(a)
        body = {}
        r = qr.describeTimeStamp(body)
        print(r[0])

    def testCreateQrPic(self):
        a = Auth(username, pwd)
        qr = Qr(a)
        body = {}
        r = qr.createQrPic(body)
        print(r[0])

    def testConfirmLogin(self):
        a = Auth(username, pwd)
        qr = Qr(a)
        body = {}
        r = qr.confirmLogin(body)
        print(r[0])

    def testObtainQrContent(self):
        a = Auth(username, pwd)
        qr = Qr(a)
        body = {}
        r = qr.obtainQrContent(body)
        print(r[0])

    def testCheckQrStatus(self):
        a = Auth(username, pwd)
        qr = Qr(a)
        body = {}
        r = qr.checkQrStatus(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
