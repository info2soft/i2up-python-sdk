
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.active.v20181227.Node import Node
from info2soft import Auth
from info2soft.fileWriter import write
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

    def testListInactiveNodes(self):
        a = Auth(username, pwd)
        body = {
        }
        node = Node(a)
        r = node.listInactiveNodes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listInactiveNodes', body)

    def testListNodes(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
            'nodetype': '@pick{"name","source","backup"]}',
            'search_field': '',
            'order_by': '',
            'sort': '@pick{'name',address}',
            'search_value': '',
        }
        node = Node(a)
        r = node.listNodes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNodes', body)

    def testListNodeStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            '76BEbF87-ACE5-e4F7-Cff5-a6CDf1CAbDDf',
            '028BAfb3-82bC-dFfC-1fFb-6fe6EbDC36EA',],
        }
        node = Node(a)
        r = node.listNodeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'listNodeStatus', body)

    def testDescriptNode(self):
        a = Auth(username, pwd)
        body = {
            'registered': 1,
            'node_uuid': 'eFd4542f-CD9F-180E-Fc2c-3a8A6eCB7f95',
        }
        node = Node(a)
        r = node.descriptNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'descriptNode', body)

    def testActiveNode(self):
        a = Auth(username, pwd)
        body = {
            'node_name': 'Dorothy Hernandez',
            'address': '22.67.77.42',
            'data_port': '26804',
            'cache_dir': '/var/i2data/cache/',
            'ipctoken': 'EDbd2d9A-Da3c-1cC1-7F63-e2AffaB2Cfc8',
            'log_dir': '/var/i2data/log/',
            'node_uuid': 'd1Ef6ABF-639e-6b86-62F9-2aEEFcBDE42f',
            'registered': 0,
            'relay_node': 0,
            'source_node': 0,
            'back_node': 0,
            'active_flag': '0',
            'comment': 'string',
            'web_uuid': 'FCc6b45B-DFfE-B031-5CBe-E72477eeFeB6',
            'port': {
            'iawork': '',
            'iaback': '',
            'iarelay': '',
            'iatrack': '',
            'iamsk': '',
            'iaload': '',
            'iamsg': '',
            'iagauss': '',},
        }
        node = Node(a)
        r = node.activeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'activeNode', body)

    def testDeleteNode(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'e623BB5f-23A6-EA4b-Bd30-Eb7E43571670',
            'cCEB1D8B-bAde-6D3e-d74B-6Eb6ec4BEC2F',],
        }
        node = Node(a)
        r = node.deleteNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'deleteNode', body)

    def testDescriptNodeDebugInfo(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '41D1C1E8-60AE-4853-9694-5599560EEB0F',
        }
        node = Node(a)
        r = node.descriptNodeDebugInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'descriptNodeDebugInfo', body)

    def testModifyNode(self):
        a = Auth(username, pwd)
        body = {
            'node_name': 'Michael Rodriguez',
            'address': '19.2.98.158',
            'data_port': '26804',
            'cache_dir': '/var/i2data/cache/',
            'iptoken': '6c58C56D-7A3b-d8C1-98cA-544417dAde8a',
            'logdir': '/var/i2data/log/',
            'node_uuid': '763a7ce7-A58b-709a-2A4A-Ff9D4eB8622D',
            'registered': 1,
            'relay_node': 0,
            'source_node': 1,
            'back_node': 1,
            'active_flag': '0',
            'comment': 'string',
            'web_uuid': 'a46Db2b3-A848-8be6-afED-DDBBdaDF69ce',
            'port': {
            'iawork': '26804',
            'iaback': '26805',
            'iarelay': '26806',
            'iatrack': '26807',
            'iamask': '26808',
            'iaload': '26809',
            'iamsg': '26810',
            'iaguass': '',},
        }
        node = Node(a)
        r = node.modifyNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'modifyNode', body)

    def testUpgradeNode(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        node = Node(a)
        r = node.upgradeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Node', 'upgradeNode', body)


if __name__ == '__main__':
    unittest.main()
