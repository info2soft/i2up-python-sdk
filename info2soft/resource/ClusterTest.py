
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.resource.v20181227.Cluster import Cluster
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
    
                
class ClusterTestCase(unittest.TestCase):

    def testAuthCls(self):
        a = Auth(username, pwd)
        cluster = Cluster(a)
        body = {}
        r = cluster.authCls(body)
        print(r[0])

    def testVerifyClsNode(self):
        a = Auth(username, pwd)
        cluster = Cluster(a)
        body = {}
        r = cluster.verifyClsNode(body)
        print(r[0])

    def testCreateCls(self):
        a = Auth(username, pwd)
        cluster = Cluster(a)
        body = {}
        r = cluster.createCls(body)
        print(r[0])

    def testDescribeCls(self):
        a = Auth(username, pwd)
        cluster = Cluster(a)
        body = {}
        r = cluster.describeCls(body)
        print(r[0])

    def testModifyCls(self):
        a = Auth(username, pwd)
        cluster = Cluster(a)
        body = {}
        r = cluster.modifyCls(body)
        print(r[0])

    def testListCls(self):
        a = Auth(username, pwd)
        cluster = Cluster(a)
        body = {}
        r = cluster.listCls(body)
        print(r[0])

    def testListClsStatus(self):
        a = Auth(username, pwd)
        cluster = Cluster(a)
        body = {}
        r = cluster.listClsStatus(body)
        print(r[0])

    def testDeleteCls(self):
        a = Auth(username, pwd)
        cluster = Cluster(a)
        body = {}
        r = cluster.deleteCls(body)
        print(r[0])

    def testClsDetail(self):
        a = Auth(username, pwd)
        cluster = Cluster(a)
        body = {}
        r = cluster.clsDetail(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
