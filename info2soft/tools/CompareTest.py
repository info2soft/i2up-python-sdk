
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.tools.v20181227.Compare import Compare
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
    
                
class CompareTestCase(unittest.TestCase):

    def testCreateCompare(self):
        a = Auth(username, pwd)
        compare = Compare(a)
        body = {}
        r = compare.createCompare(body)
        print(r[0])

    def testDescribeCompare(self):
        a = Auth(username, pwd)
        compare = Compare(a)
        body = {}
        r = compare.describeCompare(body)
        print(r[0])

    def testDescribeCompareResults(self):
        a = Auth(username, pwd)
        compare = Compare(a)
        body = {}
        r = compare.describeCompareResults(body)
        print(r[0])

    def testListCompare(self):
        a = Auth(username, pwd)
        compare = Compare(a)
        body = {}
        r = compare.listCompare(body)
        print(r[0])

    def testListCompareStatus(self):
        a = Auth(username, pwd)
        compare = Compare(a)
        body = {}
        r = compare.listCompareStatus(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        compare = Compare(a)
        body = {}
        r = compare.tempFuncName(body)
        print(r[0])

    def testDeleteCompare(self):
        a = Auth(username, pwd)
        compare = Compare(a)
        body = {}
        r = compare.deleteCompare(body)
        print(r[0])

    def testListCircleCompareResult(self):
        a = Auth(username, pwd)
        compare = Compare(a)
        body = {}
        r = compare.listCircleCompareResult(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
