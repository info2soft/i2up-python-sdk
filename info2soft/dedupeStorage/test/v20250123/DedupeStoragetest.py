
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import DedupeStorage
from info2soft.dedupeStorage.v20250123.DedupeStorage import DedupeStorage
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


class DedupeStorageTestCase(unittest.TestCase):

    def testCreateDedupeStorage(self):
        a = Auth(username, pwd)
        body = {
            'sto_name': '',
            'bk_uuid': '',
            'data_addr': '',
            'meta_server_port': 1,
            'fp_server_port': 1,
            'block_server_port': 1,
            'hash_path': '',
            'block_path': '',
            'recycle_strategy': {
            'day': '',
            'every': 1,
            'time': '00:00',},
            'description': '',
            'sto_type': 1,
            'dto_sto_uuid': '',
            'bucket_uuid': '',
            'meta_server_type': 1,
        }
        
        
        dedupeStorage = DedupeStorage(a)
        r = dedupeStorage.createDedupeStorage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DedupeStorage', 'createDedupeStorage', body)

    def testModifyDedupeStorage(self):
        a = Auth(username, pwd)
        body = {
            'sto_name': '',
            'bk_uuid': '',
            'data_addr': '',
            'meta_server_port': 1,
            'fp_server_port': 1,
            'block_server_port': 1,
            'hash_path': '',
            'block_path': '',
            'recycle_strategy': {
            'day': '',
            'every': 1,
            'time': '00:00',},
            'description': '',
            'random_str': '',
            'sto_uuid': '',
            'sto_type': 1,
            'dto_sto_uuid': '',
            'bucket_uuid': '',
            'meta_server_type': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dedupeStorage = DedupeStorage(a)
        r = dedupeStorage.modifyDedupeStorage(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DedupeStorage', 'modifyDedupeStorage', body)

    def testDeleteDedupeStorage(self):
        a = Auth(username, pwd)
        body = {
            'sto_uuids': [],
            'force': 1,
        }
        
        
        dedupeStorage = DedupeStorage(a)
        r = dedupeStorage.deleteDedupeStorage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DedupeStorage', 'deleteDedupeStorage', body)

    def testListDedupeStorage(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'status': '',
            'search_field': '',
            'search_value': '',
        }
        
        
        dedupeStorage = DedupeStorage(a)
        r = dedupeStorage.listDedupeStorage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DedupeStorage', 'listDedupeStorage', body)

    def testDescribeDedupeStorage(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dedupeStorage = DedupeStorage(a)
        r = dedupeStorage.describeDedupeStorage(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DedupeStorage', 'describeDedupeStorage', body)

    def testListDedupeStorageStatus(self):
        a = Auth(username, pwd)
        body = {
            'sto_uuids': [],
            'force_refresh': 0,
        }
        
        
        dedupeStorage = DedupeStorage(a)
        r = dedupeStorage.listDedupeStorageStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DedupeStorage', 'listDedupeStorageStatus', body)

    def testRecoverSpaceDedupeStorage(self):
        a = Auth(username, pwd)
        body = {
            'sto_uuids': [],
            'operate': '',
        }
        
        
        dedupeStorage = DedupeStorage(a)
        r = dedupeStorage.recoverSpaceDedupeStorage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DedupeStorage', 'recoverSpaceDedupeStorage', body)

    def testListBkSvrUsedPorts(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
        }
        
        
        dedupeStorage = DedupeStorage(a)
        r = dedupeStorage.listBkSvrUsedPorts(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DedupeStorage', 'listBkSvrUsedPorts', body)


if __name__ == '__main__':
    unittest.main()
