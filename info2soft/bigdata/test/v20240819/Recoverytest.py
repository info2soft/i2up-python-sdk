
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Recovery
from info2soft.bigdata.v20240819.Recovery import Recovery
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


class RecoveryTestCase(unittest.TestCase):

    def testListBackupHistory(self):
        a = Auth(username, pwd)
        body = {
            'bk_path': [],
            'bk_node_uuid': '',
            'bk_rule_uuid': '',
            'cluster_config_path': '',
            'obs_settings': {
            'sto_uuid': '',
            'bucket': '',},
            'bk_type': '',
        }
        
        
        recovery = Recovery(a)
        r = recovery.listBackupHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'listBackupHistory', body)

    def testCreateBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'bigdata_recovery': {
            'rule_name': '',
            'rule_uuid': '',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'bk_path': '备份数据目录',
            'baked_paths': '要恢复的目录',
            'rc_data_path': '目标平台目录',
            'rc_point': '还原时间点',
            'data_type': '',
            'cred_switch': '',
            'cred_uuid': '',
            'auth_user': '',
            'auth_key': '',
            'mirr_file_check': '0',
            'mirr_sync_flag': '',
            'sel_db': [],
            'sel_tbl': [],
            'hive_bktype': 1,
            'rc_path_policy': '',
            'platform_uuid': '',
            'sel_part': [],
            'approver_uuid': '',
            'band_width': '',},
            'obs_settings': {
            'sto_uuid': '',
            'bucket': '',
            'bucket_path': '',},
        }
        
        
        recovery = Recovery(a)
        r = recovery.createBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'createBigdataRecovery', body)

    def testDescribeBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        recovery = Recovery(a)
        r = recovery.describeBigdataRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'describeBigdataRecovery', body)

    def testDeleteBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
            'force': 1,
        }
        
        
        recovery = Recovery(a)
        r = recovery.deleteBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'deleteBigdataRecovery', body)

    def testListBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'limit': 10,
            'page': 1,
            'search_value': '',
            'type': 0,
        }
        
        
        recovery = Recovery(a)
        r = recovery.listBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'listBigdataRecovery', body)

    def testListBigdataRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force_refresh': 1,
        }
        
        
        recovery = Recovery(a)
        r = recovery.listBigdataRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'listBigdataRecoveryStatus', body)

    def testStartBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
        }
        
        
        recovery = Recovery(a)
        r = recovery.startBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'startBigdataRecovery', body)

    def testStopBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
        }
        
        
        recovery = Recovery(a)
        r = recovery.stopBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'stopBigdataRecovery', body)

    def testPauseBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
        }
        
        
        recovery = Recovery(a)
        r = recovery.pauseBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'pauseBigdataRecovery', body)

    def testResumeBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
        }
        
        
        recovery = Recovery(a)
        r = recovery.resumeBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'resumeBigdataRecovery', body)

    def testGetBigdataRecoveryPartitionInfoDetail(self):
        a = Auth(username, pwd)
        body = {
            'cluster_config_path': '',
            'back_path': '',
            'rec_time': '',
            'table_name': '',
            'obs_settings': {
            'sto_uuid': '',
            'bucket_name': '',
            'bucket_path': '',},
            'bk_type': '',
            'bk_uuid': '',
            'partition_name': '',
        }
        
        
        recovery = Recovery(a)
        r = recovery.getBigdataRecoveryPartitionInfoDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'getBigdataRecoveryPartitionInfoDetail', body)


if __name__ == '__main__':
    unittest.main()
