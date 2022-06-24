
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
# from info2soft import DistributorGroup as Group
from info2soft.distributor.v20220622.Group import Group
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
pwd = '12345678'
    
                
class GroupTestCase(unittest.TestCase):

    def testCreateNodeGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_name': '2',
            'group_type': 2,
            'group_parent': 'AB7813ED-F9D2-BC45-B3A6-E13E409E8A13',
            'group_desc': 'xxx',
            'send_files': [{
            'name': '港交所行情',
            'group': 0,
            'enable': 0,
            'dir': 0,
            'recursive': 0,
            'path': 'C:\HGInfo\HGHQ.DBF',
            'filter_by_fn': '',
            'event_trigger': 0,
            'time_check': 0,
            'checksum_func': 'block',
            'scan': 200,
            'compress': 4,
            'filter_by_ft': '0|0',
            'work_time': '00-00-00|23-59-59',
            'play': 0,},],
            'recv_files': [{
            'name': '港交所行情',
            'path': '',
            'timeout': 0,
            'chk_tm_am': '09-00-00|11-30-00',
            'chk_tm_pm': '13-00-00|15-30-00',
            'record': 0,
            'group': 1,
            'enable': 0,
            'guard': 0,
            'watch': 0,},],
        }
        
        group = Group(a)
        r = group.createNodeGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'createNodeGroup', body)

    def testListNodeGroup(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
            'limit': 1,
            'page': 1,
        }
        
        group = Group(a)
        r = group.listNodeGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'listNodeGroup', body)

    def testDescribeNodeGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        group = Group(a)
        r = group.describeNodeGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'describeNodeGroup', body)

    def testModifyNodeGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_name': '2',
            'group_type': '2',
            'group_parent': 'AB7813ED-F9D2-BC45-B3A6-E13E409E8A13',
            'group_desc': 'xxx',
            'send_files': [{
            'name': '港交所行情',
            'group': 0,
            'enable': 0,
            'dir': 0,
            'recursive': 0,
            'path': 'C:\HGInfo\HGHQ.DBF',
            'filter_by_fn': '',
            'event_trigger': 0,
            'time_check': 0,
            'checksum_func': 'block',
            'scan': 200,
            'compress': 4,
            'filter_by_ft': '0|0',
            'work_time': '00-00-00|23-59-59',
            'play': 0,},],
            'recv_files': [{
            'name': '港交所行情',
            'path': '',
            'timeout': 0,
            'chk_tm_am': '09-00-00|11-30-00',
            'chk_tm_pm': '13-00-00|15-30-00',
            'record': 0,
            'group': 1,
            'enable': 0,
            'guard': 0,
            'watch': 0,},],
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        group = Group(a)
        r = group.modifyNodeGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'modifyNodeGroup', body)

    def testDeleteNodeGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        group = Group(a)
        r = group.deleteNodeGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'deleteNodeGroup', body)

    def testCreateBlockGroup(self):
        a = Auth(username, pwd)
        body = {
            'block_name': 'yyy',
            'block_desc': 'xxx',
            'block_prior': 1,
        }
        
        group = Group(a)
        r = group.createBlockGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'createBlockGroup', body)

    def testListBlockGroup(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
            'limit': 1,
            'page': 1,
        }
        
        group = Group(a)
        r = group.listBlockGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'listBlockGroup', body)

    def testDescribeBlockGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        group = Group(a)
        r = group.describeBlockGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'describeBlockGroup', body)

    def testModifyBlockGroup(self):
        a = Auth(username, pwd)
        body = {
            'random_str': '',
            'block_name': 'yyy',
            'block_desc': 'xxx',
            'block_prior': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        group = Group(a)
        r = group.modifyBlockGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'modifyBlockGroup', body)

    def testDeleteBlockGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        group = Group(a)
        r = group.deleteBlockGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Group', 'deleteBlockGroup', body)


if __name__ == '__main__':
    unittest.main()
