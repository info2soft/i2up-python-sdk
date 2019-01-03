
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.v20181227.Dir import Dir
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
    
                
class DirTestCase(unittest.TestCase):

    def testListDir(self):
        a = Auth(username, pwd)
        dir = Dir(a)
        body = {}
        r = dir.listDir(body)
        print(r[0])

    def testCreateDir(self):
        a = Auth(username, pwd)
        dir = Dir(a)
        body = {}
        r = dir.createDir(body)
        print(r[0])

    def testCheckDir(self):
        a = Auth(username, pwd)
        dir = Dir(a)
        body = {}
        r = dir.checkDir(body)
        print(r[0])

    def testListDir(self):
        a = Auth(username, pwd)
        dir = Dir(a)
        body = {}
        r = dir.listDir(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
