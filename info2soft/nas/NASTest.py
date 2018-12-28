
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.nas.v20181227.NAS import NAS
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
    
                
class NASTestCase(unittest.TestCase):

    def testCreateNAS(self):
        a = Auth(username, pwd)
        nAS = NAS(a)
        body = {}
        r = nAS.createNAS(body)
        print(r[0])

    def testDescribeNASGroup(self):
        a = Auth(username, pwd)
        nAS = NAS(a)
        body = {}
        r = nAS.describeNASGroup(body)
        print(r[0])

    def testModifyNAS(self):
        a = Auth(username, pwd)
        nAS = NAS(a)
        body = {}
        r = nAS.modifyNAS(body)
        print(r[0])

    def testListNAS(self):
        a = Auth(username, pwd)
        nAS = NAS(a)
        body = {}
        r = nAS.listNAS(body)
        print(r[0])

    def testListNASStatus(self):
        a = Auth(username, pwd)
        nAS = NAS(a)
        body = {}
        r = nAS.listNASStatus(body)
        print(r[0])

    def testDeleteNAS(self):
        a = Auth(username, pwd)
        nAS = NAS(a)
        body = {}
        r = nAS.deleteNAS(body)
        print(r[0])

    def testStartNAS(self):
        a = Auth(username, pwd)
        nAS = NAS(a)
        body = {}
        r = nAS.startNAS(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
