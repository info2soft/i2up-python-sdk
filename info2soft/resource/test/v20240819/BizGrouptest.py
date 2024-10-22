
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import BizGroup
from info2soft.resource.v20240819.BizGroup import BizGroup
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
pwd = 'Info@123'


class BizGroupTestCase(unittest.TestCase):

    def testCreateBizGroup(self):
        a = Auth(username, pwd)
        body = {
            'biz_grp': {
            'grp_name': '',
            'type': 1,
            'subtype': 1,
            'comment': '',},
        }
        
        
        bizGroup = BizGroup(a)
        r = bizGroup.createBizGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BizGroup', 'createBizGroup', body)

    def testModifyBizGroup(self):
        a = Auth(username, pwd)
        body = {
            'biz_grp': {
            'comment': '123',
            'grp_name': 'grp_name',
            'type': 3,
            'subtype': 10,},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bizGroup = BizGroup(a)
        r = bizGroup.modifyBizGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BizGroup', 'modifyBizGroup', body)

    def testDescribeBizGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bizGroup = BizGroup(a)
        r = bizGroup.describeBizGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BizGroup', 'describeBizGroup', body)

    def testDeleteBizGroup(self):
        a = Auth(username, pwd)
        body = {
            'grp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        
        bizGroup = BizGroup(a)
        r = bizGroup.deleteBizGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BizGroup', 'deleteBizGroup', body)

    def testListBizGroup(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'search_field': '',
            'search_value': '',
            'direction': '',
            'order_by': '',
            'page': 1,
            'filter': [{
            'key': '',
            'operator': '',
            'value': '',},],
            'filter_and_or': 1,
            'where_args': {
            'type': '',},
        }
        
        
        bizGroup = BizGroup(a)
        r = bizGroup.listBizGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BizGroup', 'listBizGroup', body)

    def testUpdateBizGroupBind(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            '67E33CDB-D75B-15B3-367D-50C764F5A26F',],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bizGroup = BizGroup(a)
        r = bizGroup.updateBizGroupBind(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BizGroup', 'updateBizGroupBind', body)

    def testListBizGroupBind(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bizGroup = BizGroup(a)
        r = bizGroup.listBizGroupBind(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BizGroup', 'listBizGroupBind', body)

    def testListBizGroupResource(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
            'subtype': 0,
            'uuid': '',
            'group_uuid': '',
            'name': '',
            'wk_uuid': '',
            'bk_uuid': '',
        }
        
        
        bizGroup = BizGroup(a)
        r = bizGroup.listBizGroupResource(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BizGroup', 'listBizGroupResource', body)


if __name__ == '__main__':
    unittest.main()
