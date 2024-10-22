
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import StorageUnit
from info2soft.resource.v20240819.StorageUnit import StorageUnit
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


class StorageUnitTestCase(unittest.TestCase):

    def testGetStorageUnitBkCapacity(self):
        a = Auth(username, pwd)
        body = {
            'disk_pool_uuid': '',
            'export_path': '',
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.getStorageUnitBkCapacity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'getStorageUnitBkCapacity', body)

    def testGetStorageUnitDrivers(self):
        a = Auth(username, pwd)
        body = {
            'library_uuid': '',
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.getStorageUnitDrivers(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'getStorageUnitDrivers', body)

    def testCreateStorageUnit(self):
        a = Auth(username, pwd)
        body = {
            'unit_name': '',
            'unit_type': 1,
            'bk_uuid': '',
            'data_ip_uuid': '',
            'storage_path': '',
            'max_concurrent': 1,
            'high_water_mark': 1,
            'low_water_mark': 1,
            'auto_expand': 1,
            'library_uuid': '',
            'drivers_num': 1,
            'rootfs': 1,
            'pool_uuid': '',
            'fs_uuid': '',
            'biz_grp_list': '',
            'access_limit': 1,
            'bucket_uuid': '',
            'sto_uuid': '',
            'disk_pool_uuid': '',
            'default_tape_pool_uuid': '',
            'retention': '',
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.createStorageUnit(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'createStorageUnit', body)

    def testModifyStorageUnit(self):
        a = Auth(username, pwd)
        body = {
            'unit_name': '',
            'unit_type': '',
            'bk_uuid': '',
            'data_addr': '',
            'storage_path': '',
            'max_concurrent': 1,
            'fragment_switch': 1,
            'fragment_size': 1,
            'high_water_mark': 1,
            'low_water_mark': 1,
            'auto_expand': 1,
            'library_uuid': '',
            'drivers_num': 1,
            'rootfs': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        storageUnit = StorageUnit(a)
        r = storageUnit.modifyStorageUnit(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'modifyStorageUnit', body)

    def testDescribeStorageUnit(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        storageUnit = StorageUnit(a)
        r = storageUnit.describeStorageUnit(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'describeStorageUnit', body)

    def testListStorageUnit(self):
        a = Auth(username, pwd)
        body = {
            'where_args': [{
            'unit_type': '',
            'unit_name': '',
            'unit_uuid': '',},],
            'like_args': [{
            'bk_node_name': '',},],
            'filter_by_biz_grp': '',
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.listStorageUnit(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'listStorageUnit', body)

    def testDeleteStorageUnit(self):
        a = Auth(username, pwd)
        body = {
            'unit_uuids': [],
            'force': 1,
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.deleteStorageUnit(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'deleteStorageUnit', body)

    def testListStorageUnitStatus(self):
        a = Auth(username, pwd)
        body = {
            'unit_uuids': [],
            'force_refresh': 1,
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.listStorageUnitStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'listStorageUnitStatus', body)

    def testChkStorageUnitRules(self):
        a = Auth(username, pwd)
        body = {
            'disk_pool_uuid': '',
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.chkStorageUnitRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'chkStorageUnitRules', body)

    def testCreateStorageUnitGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_name': '',
            'group_type': 1,
            'unit_list': [],
            'policy': 1,
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.createStorageUnitGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'createStorageUnitGroup', body)

    def testModifyStorageUnitGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_name': '',
            'group_type': '',
            'unit_list': [],
            'policy': 1,
            'group_uuid': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        storageUnit = StorageUnit(a)
        r = storageUnit.modifyStorageUnitGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'modifyStorageUnitGroup', body)

    def testDescribeStorageUnitGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        storageUnit = StorageUnit(a)
        r = storageUnit.describeStorageUnitGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'describeStorageUnitGroup', body)

    def testListStorageUnitGroup(self):
        a = Auth(username, pwd)
        body = {
            'where_args': [{
            'group_type': 1,},],
            'like_args': [{
            'group_name': '',
            'unit_name': '',},],
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.listStorageUnitGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'listStorageUnitGroup', body)

    def testDeleteStorageUnitGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuids': [],
            'force': 1,
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.deleteStorageUnitGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'deleteStorageUnitGroup', body)

    def testGetStorageUnitAvailableConcurrent(self):
        a = Auth(username, pwd)
        body = {
            'disk_pool_uuid': '',
        }
        
        
        storageUnit = StorageUnit(a)
        r = storageUnit.getStorageUnitAvailableConcurrent(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StorageUnit', 'getStorageUnitAvailableConcurrent', body)


if __name__ == '__main__':
    unittest.main()
