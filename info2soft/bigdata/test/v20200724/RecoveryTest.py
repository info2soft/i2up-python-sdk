
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
from info2soft import bigDataRecovery as Recovery
# from info2soft.bigdata.v20200722.Recovery import Recovery
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
pwd = '123qwe-='
    
                
class BackupTestCase(unittest.TestCase):
    def testListBackupHistory(self):
        a = Auth(username, pwd)
        body = {
            'bk_path': [],
            'bk_node_uuid': '',
            'bk_rule_uuid': '',
        }
        
        bigDataRecovery = Recovery(a)
        r = bigDataRecovery.listBackupHistory(body)
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
            'mirr_sync_flag': '',},
        }
        
        bigDataRecovery = Recovery(a)
        r = bigDataRecovery.createBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'createBigdataRecovery', body)

    def testDescribeBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        bigDataRecovery = Recovery(a)
        r = bigDataRecovery.describeBigdataRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'describeBigdataRecovery', body)

    def testDeleteBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        
        bigDataRecovery = Recovery(a)
        r = bigDataRecovery.deleteBigdataRecovery(body)
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
        
        bigDataRecovery = Recovery(a)
        r = bigDataRecovery.listBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'listBigdataRecovery', body)

    def testListBigdataRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        bigDataRecovery = Recovery(a)
        r = bigDataRecovery.listBigdataRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'listBigdataRecoveryStatus', body)

    def testStartBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'uuids': [
                '22D03E06-94D0-5E2C-336E-4BEEC2D28EC4',
            ],
        }

        bigDataRecovery = Recovery(a)
        r = bigDataRecovery.startBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'startBigdataRecovery', body)

    def testStopBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'uuids': [
                '22D03E06-94D0-5E2C-336E-4BEEC2D28EC4',
            ],
        }

        bigDataRecovery = Recovery(a)
        r = bigDataRecovery.stopBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'stopBigdataRecovery', body)

    def testAuthBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
            'auth_key': '',
            'auth_name': '',
            'cred_uuid': '',
            'bk_uuid': '',
        }
        
        bigDataRecovery = Recovery(a)
        r = bigDataRecovery.authBigdataPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Recovery', 'authBigdataPlatform', body)

    def testListBigdataHiveTable(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '74e8C03A-5bAe-69Fe-2825-4E4DBF57D89F',
            'table_name': '',
            'limit': '',
            'page': '',
            'db_name': '',
            'cluster_config_path': '',
        }

        recovery = Recovery(a)
        r = recovery.listBigdataHiveTable(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listBigdataHiveTable', body)

    def testListAllBigdataHiveDatabase(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '62bbEE07-eEe8-EffF-d9cf-8ac9d7edcED1',
            'cluster_config_path': '',
        }

        recovery = Recovery(a)
        r = recovery.listAllBigdataHiveDatabase(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listAllBigdataHiveDatabase', body)


if __name__ == '__main__':
    unittest.main()
