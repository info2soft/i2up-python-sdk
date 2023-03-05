
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.nas.v20230227.NAS import NAS
# from info2soft.nas.v20200722.NAS import NAS
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


class NASTestCase(unittest.TestCase):

    def testCreateNAS(self):
        a = Auth(username, pwd)
        body = {
            'compress': 0,
            'secret_key': '',
            'wk_list': [{
            'wk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'wk_path': 'E:/nas/',},],
            'type': 0,
            'sync_path': '',
            'encrypt_switch': 0,
            'band_width': '',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'bk_path': 'E:/t/',
            'sync_uuid': '',
            'nas_name': 'test2',
            'cmp_schedule': [],
            'cmp_file_check': 0,
            'cmp_switch': 0,
            'file_type_filter_switch': 1,
            'file_type_filter': '',
            'thread_num': 1,
            'mirr_sync_attr': 1,
            'cmp_sync_file': 1,
            'runtime_range': '12345*09:00-18:00,06*10:00-14:00',
            'runtime_switch': 1,
            'filter_delete': 0,
            'cmp_limit': '',
            'data_ip_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'sync_data_ip_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'oph_path': 'E:/test4/',
            'oph_policy': 0,
            'dir_type_filter': '',
            'dir_type_filter_switch': 1,
            'bk_path_policy': 1,
            'bk_file_crypt': 0,
            'encrypt': 0,
            'compress_switch': 0,
            'nas_type': 1,
            'traversing_sync': 1,
        }
        
        nAS = NAS(a)
        r = nAS.createNAS(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NAS', 'createNAS', body)

    def testDescribeNASGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        nAS = NAS(a)
        r = nAS.describeNASGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NAS', 'describeNASGroup', body)

    def testModifyNAS(self):
        a = Auth(username, pwd)
        body = {
            'random_str': '11111111-1111-1111-1111-111111111111',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        nAS = NAS(a)
        r = nAS.modifyNAS(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NAS', 'modifyNAS', body)

    def testListNAS(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
        }
        
        nAS = NAS(a)
        r = nAS.listNAS(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NAS', 'listNAS', body)

    def testListNASStatus(self):
        a = Auth(username, pwd)
        body = {
            'nas_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        nAS = NAS(a)
        r = nAS.listNASStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NAS', 'listNASStatus', body)

    def testStartNAS(self):
        a = Auth(username, pwd)
        body = {
            'nas_uuids': [
            '-111100003333',],
            'operate': 'start',
        }
        
        nAS = NAS(a)
        r = nAS.startNAS(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NAS', 'startNAS', body)

    def testDeleteNAS(self):
        a = Auth(username, pwd)
        body = {
            'nas_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force': 1,
        }
        
        nAS = NAS(a)
        r = nAS.deleteNAS(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'NAS', 'deleteNAS', body)


if __name__ == '__main__':
    unittest.main()
