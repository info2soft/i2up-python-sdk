
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
# from info2soft import bigDataBackup as Backup
from info2soft.bigdata.v20220622.Backup import Backup
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
    
                
class BackupTestCase(unittest.TestCase):

    def testCreateBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'bigdata_backup': {
            'rule_name': '',
            'rule_uuid': '',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'bk_path': [],
            'baked_paths': [],
            'data_type': '',
            'cred_switch': 1,
            'cred_uuid': '',
            'auth_user': '',
            'auth_key': '',
            'mirr_file_check': 0,
            'mirr_sync_flag': 1,
            'bkup_one_time': 0,
            'bkup_policy': 2,
            'bkup_schedule': [{
            'sched_day': 5,
            'sched_time': '22:48',
            'sched_every': 2,
            'limit': 16,
            'backup_type': 0,
            'policys': '每天22:00自动执行',
            'backup_type_show': '全备',
            'running_time': '22:00',},],
            'random_str': '11111111-1111-1111-1111-111111111111',},
        }
        
        backup = Backup(a)
        r = backup.createBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'createBigdataBackup', body)

    def testListBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'limit': 10,
            'page': 1,
            'search_value': '',
            'type': 0,
        }
        
        backup = Backup(a)
        r = backup.listBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listBigdataBackup', body)

    def testListBigdataBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        backup = Backup(a)
        r = backup.listBigdataBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listBigdataBackupStatus', body)

    def testDescribeBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        backup = Backup(a)
        r = backup.describeBigdataBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'describeBigdataBackup', body)

    def testStartBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'uuids': [
                '22D03E06-94D0-5E2C-336E-4BEEC2D28EC4',
            ],
        }

        backup = Backup(a)
        r = backup.startBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'startBigdataBackup', body)

    def testStopBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'uuids': [
                '22D03E06-94D0-5E2C-336E-4BEEC2D28EC4',
            ],
        }

        backup = Backup(a)
        r = backup.stopBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'stopBigdataBackup', body)

    def testStartImmediatelyBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start_immediately',
            'uuids': [
                '22D03E06-94D0-5E2C-336E-4BEEC2D28EC4',
            ],
        }

        backup = Backup(a)
        r = backup.startImmediatelyBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'startImmediatelyBigdataBackup', body)

    def testDeleteBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'del_policy': 0,
        }
        
        backup = Backup(a)
        r = backup.deleteBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'deleteBigdataBackup', body)

if __name__ == '__main__':
    unittest.main()
