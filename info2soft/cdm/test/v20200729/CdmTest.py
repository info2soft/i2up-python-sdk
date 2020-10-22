
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import Cdm
# from info2soft.cdm.v20200722.Cdm import Cdm
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
    
                
class CdmTestCase(unittest.TestCase):

    def testGetPointList(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
            'path': '',
            'type': '',
            'suffix': '',
            'page': 1,
            'limit': 1,
        }
        
        cdm = Cdm(a)
        r = cdm.getPointList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getPointList', body)

    def testGetResourceList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'search_field': '',
            'search_value': '',
        }
        
        cdm = Cdm(a)
        r = cdm.getResourceList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getResourceList', body)

    def testGetHostStorageList(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }
        
        cdm = Cdm(a)
        r = cdm.getHostStorageList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getHostStorageList', body)

    def testTakeOverDrillList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'where_args': {
            'wk_uuid': '',
            'bk_uuid': ''}
        }
        
        cdm = Cdm(a)
        r = cdm.takeOverDrillList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'takeOverDrillList', body)

    def testCreateTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'vm_name': '',
            'rule_type': 1,
            'wk_uuid': '',
            'bk_version': '',
            'vm_cpu_core': '',
            'vm_mem': '',
            'vm_network': {
            'cards': [{
            'ip': '',
            'mac': '',
            'mask': '',
            'gateway': '',
            'dns': {
            'domain': '',
            'servers': '',},},],
            'dns': {
            'domain': '',
            'servers': '',},},
            'bk_uuid': '',
            'vm_disks': [{
            'path': '',
            'size': '',
            'interface': '',
            'isBoot': '',},],
            'bios_type': '',
            'vp_uuid': '',
            'timezone': '',
            'storage_uuid': '',
            'bk_path': '',
            'os_version': '',
        }
        
        cdm = Cdm(a)
        r = cdm.createTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'createTakeOverDrill', body)

    def testDeleteTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        cdm = Cdm(a)
        r = cdm.deleteTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'deleteTakeOverDrill', body)

    def testDescribeTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cdm = Cdm(a)
        r = cdm.describeTakeOverDrill(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'describeTakeOverDrill', body)

    def testGetVmStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        cdm = Cdm(a)
        r = cdm.getVmStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getVmStatus', body)

    def testStartTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            "rule_uuids": [],
            "operate": "",
            "type": ""
        }
        
        cdm = Cdm(a)
        r = cdm.startTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'startTakeOverDrill', body)

    def testStopTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            "rule_uuids": [],
            "operate": "",
            "type": ""
        }

        cdm = Cdm(a)
        r = cdm.stopTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'stopTakeOverDrill', body)

    def testOpenConsoleTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            "rule_uuids": [],
            "operate": "",
            "type": ""
        }

        cdm = Cdm(a)
        r = cdm.openConsoleTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'openConsoleTakeOverDrill', body)


if __name__ == '__main__':
    unittest.main()
