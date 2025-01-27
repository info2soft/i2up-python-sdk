
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Backup
from info2soft.bigdata.v20250123.Backup import Backup
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


class BackupTestCase(unittest.TestCase):

    def testCreateBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'bigdata_backup': {
            'rule_name': '',
            'rule_uuid': '',
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
            'sched_day': 23,
            'sched_time': '01:37',
            'sched_every': 2,
            'limit': 60,
            'backup_type': 0,
            'policys': '每天22:00自动执行',
            'backup_type_show': '全备',
            'running_time': '22:00',},],
            'random_str': '11111111-1111-1111-1111-111111111111',
            'tape_uuid': 'E8566905-411E-B2CD-A742-77B1346D8E84',
            'archive_pen': 0,
            'library_sn': 'SYZZY_A',
            'sel_tbl': [],
            'sel_db': [],
            'hive_bktype': 1,
            'filter_type': 1,
            'filter_files': '',
            'exclude_paths': '',
            'band_width': '',
            'pre_backup_script': '',
            'post_backup_script': '',
            'script_timeout': 1,
            'tape_pool_uuid': '',
            'tape_pool_name': '',
            'tape_name': '',
            'tape_reserve': 1,
            'platform_uuid': '',
            'sel_part': [],
            'rule_type': '',
            'schedule_uuid': '',
            'scan_path': '',
            'schedule': {
            'type': '',
            'interval': '',
            'unit': '',
            'run_time': '12:00',},
            'scan_schedule': {
            'sched_every': '',
            'sched_day': '',
            'sched_time': '',},
            'approver_uuid': '',},
            'obs_settings': {
            'sto_uuid': '',
            'bucket_name': '',
            'bucket_path': '',},
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
            'force_refresh': 1,
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
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bk_type': 1,
        }
        
        
        backup = Backup(a)
        r = backup.startBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'startBigdataBackup', body)

    def testStopBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bk_type': 1,
        }
        
        
        backup = Backup(a)
        r = backup.stopBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'stopBigdataBackup', body)

    def testStartImmediatelyBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bk_type': 1,
        }
        
        
        backup = Backup(a)
        r = backup.startImmediatelyBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'startImmediatelyBigdataBackup', body)

    def testEnableBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bk_type': 1,
        }
        
        
        backup = Backup(a)
        r = backup.enableBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'enableBigdataBackup', body)

    def testDisableBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bk_type': 1,
        }
        
        
        backup = Backup(a)
        r = backup.disableBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'disableBigdataBackup', body)

    def testPauseBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bk_type': 1,
        }
        
        
        backup = Backup(a)
        r = backup.pauseBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'pauseBigdataBackup', body)

    def testResumeBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bk_type': 1,
        }
        
        
        backup = Backup(a)
        r = backup.resumeBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'resumeBigdataBackup', body)

    def testDeleteBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'del_policy': 0,
            'force': 1,
        }
        
        
        backup = Backup(a)
        r = backup.deleteBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'deleteBigdataBackup', body)

    def testListBigdataBackupTableDdl(self):
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
            'rec_time': '',
            'table_name': '',
        }
        
        
        backup = Backup(a)
        r = backup.listBigdataBackupTableDdl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listBigdataBackupTableDdl', body)

    def testAuthBigdataPlatform(self):
        a = Auth(username, pwd)
        body = {
            'auth_key': '',
            'auth_name': '',
            'cred_uuid': '',
            'bk_uuid': '',
        }
        
        
        backup = Backup(a)
        r = backup.authBigdataPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'authBigdataPlatform', body)

    def testListBigdataHiveTable(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '9E2e888B-9afC-DebB-2557-D1B4DE6FAf3D',
            'table_name': '',
            'limit': '',
            'page': '',
            'db_name': '',
            'cluster_config_path': '',
            'platform_uuid': '',
        }
        
        
        backup = Backup(a)
        r = backup.listBigdataHiveTable(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listBigdataHiveTable', body)

    def testListAllBigdataHiveDatabase(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'D2ffB1Fe-2251-Da34-BEB5-7ED7dc4Bf52b',
            'cluster_config_path': '',
            'platform_uuid': '',
        }
        
        
        backup = Backup(a)
        r = backup.listAllBigdataHiveDatabase(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listAllBigdataHiveDatabase', body)

    def testGetBigdataBackupPartitions(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
            'db_name': '',
            'table_name': '',
            'limit': '',
            'page': '',
            'platform_uuid': '',
        }
        
        
        backup = Backup(a)
        r = backup.getBigdataBackupPartitions(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'getBigdataBackupPartitions', body)

    def testImportBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'file': '',
        }
        
        
        backup = Backup(a)
        r = backup.importBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'importBigdataBackup', body)


if __name__ == '__main__':
    unittest.main()
