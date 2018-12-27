
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.resource.v20181227.BizGroup import BizGroup
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
    
                
class BizGroupTestCase(unittest.TestCase):

    def testCreateBizGroup(self):
        a = Auth(username, pwd)
        bizGroup = BizGroup(a)
        body = {}
        r = bizGroup.createBizGroup(body)
        print(r[0])

    def testModifyBizGroup(self):
        a = Auth(username, pwd)
        bizGroup = BizGroup(a)
        body = {}
        r = bizGroup.modifyBizGroup(body)
        print(r[0])

    def testDescribeBizGroup(self):
        a = Auth(username, pwd)
        bizGroup = BizGroup(a)
        body = {}
        r = bizGroup.describeBizGroup(body)
        print(r[0])

    def testDeleteBizGroup(self):
        a = Auth(username, pwd)
        bizGroup = BizGroup(a)
        body = {}
        r = bizGroup.deleteBizGroup(body)
        print(r[0])

    def testListBizGroup(self):
        a = Auth(username, pwd)
        bizGroup = BizGroup(a)
        body = {}
        r = bizGroup.listBizGroup(body)
        print(r[0])

    def testUpdateBizGroupBind(self):
        a = Auth(username, pwd)
        bizGroup = BizGroup(a)
        body = {}
        r = bizGroup.updateBizGroupBind(body)
        print(r[0])

    def testListBizGroupBind(self):
        a = Auth(username, pwd)
        bizGroup = BizGroup(a)
        body = {}
        r = bizGroup.listBizGroupBind(body)
        print(r[0])

    def testListBizGroupResource(self):
        a = Auth(username, pwd)
        bizGroup = BizGroup(a)
        body = {}
        r = bizGroup.listBizGroupResource(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
