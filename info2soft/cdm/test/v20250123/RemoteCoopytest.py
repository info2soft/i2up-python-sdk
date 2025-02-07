
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import RemoteCoopy
from info2soft.cdm.v20250123.RemoteCoopy import RemoteCoopy
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


class RemoteCoopyTestCase(unittest.TestCase):

    def testVerifyDuplicateCdmCoopyRule(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.verifyDuplicateCdmCoopyRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'verifyDuplicateCdmCoopyRule', body)

    def testCreateCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'old_bk_uuid': '',
            'old_platform_uuid': '',
            'old_storage_uuid': '',
            'rule_uuids': [],
            'proxy_uuid': '',
            'new_bk_uuid': '',
            'new_platform_uuid': '',
            'data_addr': '',
            'new_storage_uuid': '',
            'bkup_policy': '',
            'bkup_one_time': '',
            'bkup_schedule': {
            'sched_gap_min': '60',
            'sched_time': '["00:00:00"]',
            'sched_day': '["1"]',
            'sched_time_end': '23:59',
            'limit': '5',
            'sched_time_start': '00:00',
            'sched_every': '0',},
            'compress_switch': '',
            'encrypt_switch': '',
            'band_width': '',
            'rule_uuid': '',
            'start_type': '',
            'prefix': '',
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.createCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'createCdmRemoteCoopy', body)

    def testListCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'search_args': '',
            'search_value': '',
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.listCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'listCdmRemoteCoopy', body)

    def testStartCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': '',
            'operate': '',
            'modify_original_rule_name': '',
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.startCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'startCdmRemoteCoopy', body)

    def testStopCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': '',
            'operate': '',
            'modify_original_rule_name': '',
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.stopCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'stopCdmRemoteCoopy', body)

    def testMigrateCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': '',
            'operate': '',
            'modify_original_rule_name': '',
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.migrateCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'migrateCdmRemoteCoopy', body)

    def testStartImmediatelyCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': '',
            'operate': '',
            'modify_original_rule_name': '',
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.startImmediatelyCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'startImmediatelyCdmRemoteCoopy', body)

    def testListCdmRemoteCoopyStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': '',
            'force_refresh': 1,
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.listCdmRemoteCoopyStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'listCdmRemoteCoopyStatus', body)

    def testDeleteCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'del_policy': '',
            'rule_uuids': [],
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.deleteCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'deleteCdmRemoteCoopy', body)

    def testDescribeCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.describeCdmRemoteCoopy(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'describeCdmRemoteCoopy', body)

    def testVerifyCdmCapacity(self):
        a = Auth(username, pwd)
        body = {
            'old_storage_uuid': '',
            'new_storage_uuid': '',
            'old_vp_uuid': '',
            'new_vp_uuid': '',
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.verifyCdmCapacity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'verifyCdmCapacity', body)

    def testListCdmRemoteCoopyLicense(self):
        a = Auth(username, pwd)
        body = {
            'old_storage_uuid': '',
            'new_storage_uuid': '',
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.listCdmRemoteCoopyLicense(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'listCdmRemoteCoopyLicense', body)

    def testVerifyCdmDirExist(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'storage_uuid': '',
            'wk_uuids': [],
            'bk_uuid': '',
        }
        
        
        remoteCoopy = RemoteCoopy(a)
        r = remoteCoopy.verifyCdmDirExist(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RemoteCoopy', 'verifyCdmDirExist', body)


if __name__ == '__main__':
    unittest.main()
