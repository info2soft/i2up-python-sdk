
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.resource.v20181227.Node import Node
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
    
                
class NodeTestCase(unittest.TestCase):

    def testAuthNode(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {"config_addr":"192.168.25.11","config_port":"26821","os_pwd":"QBECXJCmZUjsn+DubEWv3/m1ZKSPVxQcxLYW09ZruVGbMU4nS7htN31EjBMPfZ591/7yPZPst9ZLpuYZM6zELmgu1wzQA75AHZ5kCrLUNJ0HQohHdY5sgIWXwzH8uyRjpYRKrd5Uv/6gIvhXA5SHZ7ViPkSFSHEFVKFeilWsIYsVSGrqGUQGS38Maea0WhghpLUslgrsAm4/AsyOfXjqgieVfR+QH8BCeCToqxh0ntOrTh3oywZQDcEP7wzpWX428D38rnSxE41WQDwhwjeXL5Lq6EkuUHicJ865JX7fdcxELUjlh9MEWPufKgSdFfLr9Uq2jGd2La4r7QvuM7immw==","os_user":"root","auth_type":0,"node_uuid":"","i2id":""}
        r = node.authNode(body)
        print(r[0])

    def testCheckCapacity(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.checkCapacity(body)
        print(r[0])

    def testListVg(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.listVg(body)
        print(r[0])

    def testCheckNodeOnline(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.checkNodeOnline(body)
        print(r[0])

    def testCreateNode(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.createNode(body)
        print(r[0])

    def testModifyNode(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.modifyNode(body)
        print(r[0])

    def testDescribeNode(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.describeNode(body)
        print(r[0])

    def testCreateBatchNode(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.createBatchNode(body)
        print(r[0])

    def testDescribeDeviceInfo(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.describeDeviceInfo(body)
        print(r[0])

    def testListNode(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.listNode(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.tempFuncName(body)
        print(r[0])

    def testListNodeStatus(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.listNodeStatus(body)
        print(r[0])

    def testDeleteNode(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.deleteNode(body)
        print(r[0])

    def testNode(self):
        a = Auth(username, pwd)
        node = Node(a)
        body = {}
        r = node.node(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
