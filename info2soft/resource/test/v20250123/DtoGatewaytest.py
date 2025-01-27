
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import DtoGateway
from info2soft.resource.v20250123.DtoGateway import DtoGateway
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


class DtoGatewayTestCase(unittest.TestCase):

    def testCreateDtoGateway(self):
        a = Auth(username, pwd)
        body = {
            'gateway_name': '',
            'enable': 1,
            'http_port': 1,
            'https_port': 1,
            'domain': '',
            'comment': '',
            'region': [{
            'name': '',
            'type': 1,
            'path': '',},],
            'bk_uuid': '',
        }
        
        
        dtoGateway = DtoGateway(a)
        r = dtoGateway.createDtoGateway(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoGateway', 'createDtoGateway', body)

    def testModifyDtoGateway(self):
        a = Auth(username, pwd)
        body = {
            'gateway_name': '',
            'enable': 1,
            'http_port': '',
            'https_port': '',
            'domain': '',
            'comment': '',
            'region': [{
            'name': '',
            'type': 1,
            'path': '',
            'uuid': '',},],
            'bk_uuid': '',
            'gateway_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoGateway = DtoGateway(a)
        r = dtoGateway.modifyDtoGateway(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoGateway', 'modifyDtoGateway', body)

    def testDescribeDtoGateway(self):
        a = Auth(username, pwd)
        body = {
            'gateway_name': '',
            'enable': 1,
            'http_port': '',
            'https_port': '',
            'domain': '',
            'comment': '',
            'region': [{
            'name': '',
            'type': 1,
            'path': '',
            'uuid': '',},],
            'bk_uuid': '',
            'gateway_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoGateway = DtoGateway(a)
        r = dtoGateway.describeDtoGateway(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoGateway', 'describeDtoGateway', body)

    def testListDtoGateway(self):
        a = Auth(username, pwd)
        body = {
            'search_field': 'gateway_name',
            'search_value': '',
        }
        
        
        dtoGateway = DtoGateway(a)
        r = dtoGateway.listDtoGateway(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoGateway', 'listDtoGateway', body)

    def testDeleteDtoGateway(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': 1,
        }
        
        
        dtoGateway = DtoGateway(a)
        r = dtoGateway.deleteDtoGateway(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoGateway', 'deleteDtoGateway', body)

    def testResetDtoGatewayAccessKey(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        dtoGateway = DtoGateway(a)
        r = dtoGateway.resetDtoGatewayAccessKey(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoGateway', 'resetDtoGatewayAccessKey', body)

    def testListDtoGatewayRegions(self):
        a = Auth(username, pwd)
        body = {
            'gateway_uuid': '',
        }
        
        
        dtoGateway = DtoGateway(a)
        r = dtoGateway.listDtoGatewayRegions(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoGateway', 'listDtoGatewayRegions', body)

    def testGetDtoGatewayStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force_refresh': 1,
        }
        
        
        dtoGateway = DtoGateway(a)
        r = dtoGateway.getDtoGatewayStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoGateway', 'getDtoGatewayStatus', body)


if __name__ == '__main__':
    unittest.main()
