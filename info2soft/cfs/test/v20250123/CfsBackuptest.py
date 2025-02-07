
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import CfsBackup
from info2soft.cfs.v20250123.CfsBackup import CfsBackup
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


class CfsBackupTestCase(unittest.TestCase):

    def testCreateCfsBackup(self):
        a = Auth(username, pwd)
        body = {
            'cfs_backup': {
            'mirr_sync_attr': 1,
            'oph_path': 'E:\\test4\\',
            'rep_name': 'rep_backup',
            'bk_path_policy': 1,
            'mirr_open_type': 0,
            'compress': 0,
            'encrypt_switch': 0,
            'auto_start': 1,
            'wk_path': [
            'E:\\test\\',],
            'band_width': '',
            'mirr_sync_flag': 0,
            'bk_path': [
            'E:\\test2\\',],
            'wk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'mirr_file_check': 0,
            'rep_type': 0,
            'file_type_filter_switch': 0,
            'file_type_filter': '',
            'oph_policy': 2,
            'mirr_skip': 0,
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'excl_path': [],
            'mirr_sched': '',
            'bkup_one_time': 1515568566,
            'mirr_sched_switch': 0,
            'ct_name_type': 0,
            'ct_name_str1': '',
            'ct_name_str2': '',
            'ct_name_str3': '',
            'ct_name_str4': '',
            'thread_num': 0,
            'latency_threshold': 1,
            'mir_detect_script': '',
            'data_ip_uuid': 'B8166905-411E-B2CD-A742-77B1346D8E84',
            'bk_file_crypt': 0,
            'mir_detect_src_script': '',
            'traversing_sync': 1,
            'encrypt': 1,
            'compress_switch': 1,
            'rep_uuid': 'B8166905-411E-B2CD-A742-77B1346D8E84',
            'buf_in_bk': 1,
            'rep_oph_policy': 0,
            'rep_oph_path': '',
            'rep_oph_switch': 1,
            'src_cfs_uuid': '',
            'tgt_cfs_uuid': '',
            'src_filesystem_id': '',
            'tgt_filesystem_id': '',
            'proxy_uuid': '',
            'mirr_hash_type': 1,
            'src_zone_id': '',
            'tgt_zone_id': '',},
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.createCfsBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'createCfsBackup', body)

    def testModifyCfsBackup(self):
        a = Auth(username, pwd)
        body = {
            'cfs_backup': {
            'mirr_sync_attr': 1,
            'oph_path': 'E:\\test4\\',
            'rep_name': 'rep_backup',
            'bk_path_policy': 1,
            'mirr_open_type': 0,
            'compress': 0,
            'encrypt_switch': 0,
            'auto_start': 1,
            'wk_path': [
            'E:\\test\\',],
            'band_width': '',
            'mirr_sync_flag': 0,
            'bk_path': [
            'E:\\test2\\',],
            'wk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'mirr_file_check': 0,
            'rep_type': 0,
            'file_type_filter_switch': 0,
            'file_type_filter': '',
            'oph_policy': 2,
            'mirr_skip': '0',
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'excl_path': [],
            'mirr_sched': '',
            'bkup_one_time': 1515568566,
            'mirr_sched_switch': 0,
            'ct_name_type': 0,
            'ct_name_str1': '',
            'ct_name_str2': '',
            'ct_name_str3': '',
            'ct_name_str4': '',
            'thread_num': 0,
            'latency_threshold': 1,
            'mir_detect_script': '',
            'data_ip_uuid': 'B8166905-411E-B2CD-A742-77B1346D8E84',
            'bk_file_crypt': 0,
            'mir_detect_src_script': '',
            'traversing_sync': 1,
            'encrypt': 1,
            'compress_switch': 1,
            'rep_uuid': 'B8166905-411E-B2CD-A742-77B1346D8E84',
            'buf_in_bk': 1,
            'rep_oph_policy': 0,
            'rep_oph_path': '',
            'rep_oph_switch': 1,
            'src_cfs_uuid': '',
            'tgt_cfs_uuid': '',
            'src_filesystem_id': '',
            'tgt_filesystem_id': '',
            'proxy_uuid': '',
            'mirr_hash_type': 1,
            'random_str': '',
            'src_zone_id': '',
            'tgt_zone_id': '',},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.modifyCfsBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'modifyCfsBackup', body)

    def testDescribeCfsBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.describeCfsBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'describeCfsBackup', body)

    def testListCfsBackup(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_field': '',
            'where_args': {
            'status': 'NO_MOVE',},
            'search_value': '',
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.listCfsBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'listCfsBackup', body)

    def testDeleteCfsBackup(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'force': 1,
            'del_policy': 1,
            'recycle': 1,
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.deleteCfsBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'deleteCfsBackup', body)

    def testStartCfsBackup(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.startCfsBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'startCfsBackup', body)

    def testStopCfsBackup(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.stopCfsBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'stopCfsBackup', body)

    def testStartSyncCfsBackup(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.startSyncCfsBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'startSyncCfsBackup', body)

    def testStopSyncCfsBackup(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.stopSyncCfsBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'stopSyncCfsBackup', body)

    def testMoveCfsBackup(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.moveCfsBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'moveCfsBackup', body)

    def testListCfsBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'force_refresh': '',
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.listCfsBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'listCfsBackupStatus', body)

    def testListCfsBackupSyncStatus(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuid': [],
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.listCfsBackupSyncStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'listCfsBackupSyncStatus', body)

    def testGetWatingMoveNumber(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.getWatingMoveNumber(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'getWatingMoveNumber', body)

    def testListCfsBackupHistory(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuid': '',
        }
        
        
        cfsBackup = CfsBackup(a)
        r = cfsBackup.listCfsBackupHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CfsBackup', 'listCfsBackupHistory', body)


if __name__ == '__main__':
    unittest.main()
