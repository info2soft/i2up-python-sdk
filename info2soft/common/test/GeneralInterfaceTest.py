
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.GeneralInterface import GeneralInterface
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
    
                
class GeneralInterfaceTestCase(unittest.TestCase):

    def testDescribeVersion(self):
        a = Auth(username, pwd)
        generalInterface = GeneralInterface(a)
        body = {}
        r = generalInterface.describeVersion(body)
        print(r[0])

    def testUpdateDatabase(self):
        a = Auth(username, pwd)
        generalInterface = GeneralInterface(a)
        body = {}
        r = generalInterface.updateDatabase(body)
        print(r[0])

    def testListStatistics(self):
        a = Auth(username, pwd)
        generalInterface = GeneralInterface(a)
        body = {}
        r = generalInterface.listStatistics(body)
        print(r[0])

    def testDescribeStatistics(self):
        a = Auth(username, pwd)
        generalInterface = GeneralInterface(a)
        body = {}
        r = generalInterface.describeStatistics(body)
        print(r[0])

    def testReadStatistics(self):
        a = Auth(username, pwd)
        generalInterface = GeneralInterface(a)
        body = {}
        r = generalInterface.readStatistics(body)
        print(r[0])

    def testOverall(self):
        a = Auth(username, pwd)
        generalInterface = GeneralInterface(a)
        body = {}
        r = generalInterface.overall(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
