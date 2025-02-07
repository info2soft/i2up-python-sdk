
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import StoragePool
from info2soft.resource.v20250123.StoragePool import StoragePool
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


class StoragePoolTestCase(unittest.TestCase):

    def testAvailablePoolMemberList(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '',
            'pool_type': 'BlockStorage',
            'storage_conf_ip': '',
            'os_user': '',
            'os_pwd': '',
            'pool_uuid': '',
            'storage_conf_user': '',
            'storage_conf_password': '',
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.availablePoolMemberList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'availablePoolMemberList', body)

    def testCreateStoragePool(self):
        a = Auth(username, pwd)
        body = {
            'pool_name': '',
            'pool_type': '',
            'ip': '',
            'disk_list': [{
            'name': '',
            'size': '',
            'type': '',},],
            'description': '',
            'data_addr': '',
            'storage_conf_ip': '',
            'compress': 0,
            'dedup': 0,
            'fc_as_target': 0,
            'wwpn_info': [],
            'tape_uuid': '',
            'physical_name': '',
            'node_uuid': '',
            'bind_lic_list': [],
            'os_user': '',
            'os_pwd': '',
            'monitor_settings': {
            'warn_sw': 0,
            'usage_threshold': 80,},
            'storage_conf_user': '',
            'storage_conf_password': '',
            'dev_id': '',
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.createStoragePool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'createStoragePool', body)

    def testModifyStoragePool(self):
        a = Auth(username, pwd)
        body = {
            'pool_name': '',
            'pool_type': '',
            'ip': '',
            'disk_list': [{
            'name': '',
            'size': '',
            'type': '',},],
            'random_str': '',
            'description': '',
            'data_addr': '',
            'compress': 0,
            'dedup': 0,
            'fc_as_target': 0,
            'wwpn_info': [],
            'tape_uuid': '',
            'physical_name': '',
            'node_uuid': '',
            'os_user': '',
            'os_pwd': '',
            'monitor_settings': {
            'warn_sw': '',
            'usage_threshold': '',},
            'storage_conf_user': '',
            'storage_conf_password': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        storagePool = StoragePool(a)
        r = storagePool.modifyStoragePool(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'modifyStoragePool', body)

    def testStoragePoolList(self):
        a = Auth(username, pwd)
        body = {
            'page': '',
            'limit': '',
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.storagePoolList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'storagePoolList', body)

    def testDescribeStoragePool(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        storagePool = StoragePool(a)
        r = storagePool.describeStoragePool(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'describeStoragePool', body)

    def testDeleteStoragePool(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuids': [],
            'force': 1,
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.deleteStoragePool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'deleteStoragePool', body)

    def testListStoragePoolStatus(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuids': [],
            'force_refresh': '',
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.listStoragePoolStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'listStoragePoolStatus', body)

    def testListHbaInfo(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
            'os_user': '',
            'os_pwd': '',
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.listHbaInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'listHbaInfo', body)

    def testDeleteFcTarget(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuid': '',
            'wwpn': '',
            'force': 1,
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.deleteFcTarget(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'deleteFcTarget', body)

    def testResetStoragePool(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuids': [],
            'operate': '',
            'add_disk_list': [{
            'name': '/dev/sdb',
            'size': 2000398934016,
            'type': 'disk',},],
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.resetStoragePool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'resetStoragePool', body)

    def testExtendStoragePool(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuids': [],
            'operate': '',
            'add_disk_list': [{
            'name': '/dev/sdb',
            'size': 2000398934016,
            'type': 'disk',},],
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.extendStoragePool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'extendStoragePool', body)

    def testRenewKeyStoragePool(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuids': [],
            'operate': '',
            'add_disk_list': [{
            'name': '/dev/sdb',
            'size': 2000398934016,
            'type': 'disk',},],
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.renewKeyStoragePool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'renewKeyStoragePool', body)

    def testStoragePoolLoadPools(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.storagePoolLoadPools(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'storagePoolLoadPools', body)

    def testStoragePoolBatchImport(self):
        a = Auth(username, pwd)
        body = {
            'pool_list': [{
            'pool_name': '',
            'pool_type': '',
            'ip': '',
            'disk_list': [{
            'name': '',
            'size': '',
            'type': '',},],
            'description': '',
            'data_addr': '',
            'storage_conf_ip': '',
            'compress': 0,
            'dedup': 0,
            'fc_as_target': 0,
            'wwpn_info': [],
            'tape_uuid': '',
            'physical_name': '',
            'node_uuid': '',
            'os_user': '',
            'os_pwd': '',},],
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.storagePoolBatchImport(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'storagePoolBatchImport', body)

    def testStoragePoolUpdateConfig(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuid': '',
        }
        
        
        storagePool = StoragePool(a)
        r = storagePool.storagePoolUpdateConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'StoragePool', 'storagePoolUpdateConfig', body)


if __name__ == '__main__':
    unittest.main()
