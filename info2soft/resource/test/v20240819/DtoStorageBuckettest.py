
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import DtoStorageBucket
from info2soft.resource.v20240819.DtoStorageBucket import DtoStorageBucket
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


class DtoStorageBucketTestCase(unittest.TestCase):

    def testCreateDtoStorageBucket(self):
        a = Auth(username, pwd)
        body = {
            'sto_uuid': '',
            'bucket_name': '',
            'quota_size': '',
        }
        
        
        dtoStorageBucket = DtoStorageBucket(a)
        r = dtoStorageBucket.createDtoStorageBucket(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoStorageBucket', 'createDtoStorageBucket', body)

    def testDescribeDtoStorageBucket(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        dtoStorageBucket = DtoStorageBucket(a)
        r = dtoStorageBucket.describeDtoStorageBucket(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoStorageBucket', 'describeDtoStorageBucket', body)

    def testListDtoStorageBucket(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'search_value': '',
            'search_field': '',
            'page': 10,
        }
        
        
        dtoStorageBucket = DtoStorageBucket(a)
        r = dtoStorageBucket.listDtoStorageBucket(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoStorageBucket', 'listDtoStorageBucket', body)

    def testDeleteDtoStorageBucket(self):
        a = Auth(username, pwd)
        body = {
            'bucket_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        
        dtoStorageBucket = DtoStorageBucket(a)
        r = dtoStorageBucket.deleteDtoStorageBucket(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoStorageBucket', 'deleteDtoStorageBucket', body)

    def testImportDtoStorageBucket(self):
        a = Auth(username, pwd)
        body = {
            'bucket_names': [],
            'sto_uuid': '',
        }
        
        
        dtoStorageBucket = DtoStorageBucket(a)
        r = dtoStorageBucket.importDtoStorageBucket(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'DtoStorageBucket', 'importDtoStorageBucket', body)


if __name__ == '__main__':
    unittest.main()
