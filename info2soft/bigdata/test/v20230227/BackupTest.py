# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.bigdata.v20230227.Backup import Backup
# from info2soft.bigdata.v20200722.Backup import Backup
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
                    'sched_day': 9,
                    'sched_time': '18:35',
                    'sched_every': 2,
                    'limit': 4,
                    'backup_type': 0,
                    'policys': '每天22:00自动执行',
                    'backup_type_show': '全备',
                    'running_time': '22:00', }, ],
                'random_str': '11111111-1111-1111-1111-111111111111',
                'cluster_config_path': '',
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
                'tape_reserve': 1, },
            'obs_settings': {
                'sto_uuid': '',
                'bucket_name': '',
                'bucket_path': '', },
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

    def testDeleteBigdataBackup(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'del_policy': 0,
        }

        backup = Backup(a)
        r = backup.deleteBigdataBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'deleteBigdataBackup', body)

    def testListBackupHistory(self):
        a = Auth(username, pwd)
        body = {
            'bk_path': [],
            'bk_node_uuid': '',
            'bk_rule_uuid': '',
            'cluster_config_path': '',
            'obs_settings': {
                'sto_uuid': '',
                'bucket': '', },
            'bk_type': '',
        }

        backup = Backup(a)
        r = backup.listBackupHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listBackupHistory', body)

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
                'cluster_config_path': '',
                'sel_db': [],
                'sel_tbl': [],
                'hive_bktype': 1,
                'rc_path_policy': '', },
            'obs_settings': {
                'sto_uuid': '',
                'bucket': '',
                'bucket_path': '', },
        }

        backup = Backup(a)
        r = backup.createBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'createBigdataRecovery', body)

    def testDescribeBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        backup = Backup(a)
        r = backup.describeBigdataRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'describeBigdataRecovery', body)

    def testDeleteBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }

        backup = Backup(a)
        r = backup.deleteBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'deleteBigdataRecovery', body)

    def testListBigdataRecovery(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'limit': 10,
            'page': 1,
            'search_value': '',
            'type': 0,
        }

        backup = Backup(a)
        r = backup.listBigdataRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listBigdataRecovery', body)

    def testListBigdataRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force_refresh': 1,
        }

        backup = Backup(a)
        r = backup.listBigdataRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listBigdataRecoveryStatus', body)

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
            'bk_uuid': 'DBdfEB48-faf1-ddDA-8a2b-B70d77eadBb1',
            'table_name': '',
            'limit': '',
            'page': '',
            'db_name': '',
            'cluster_config_path': '',
        }

        backup = Backup(a)
        r = backup.listBigdataHiveTable(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listBigdataHiveTable', body)

    def testListAllBigdataHiveDatabase(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'bC55D1c9-f9fC-E9Ed-6d6E-5deD6AcCB1B9',
            'cluster_config_path': '',
        }

        backup = Backup(a)
        r = backup.listAllBigdataHiveDatabase(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'listAllBigdataHiveDatabase', body)

    def testGetTableInfoDetail(self):
        a = Auth(username, pwd)
        body = {
            'cluster_config_path': '',
            'back_path': '',
            'rec_time': '',
            'table_name': '',
            'obs_settings': {
                'sto_uuid': '',
                'bucket_name': '',
                'bucket_path': '', },
            'bk_type': '',
            'bk_uuid': '',
        }

        backup = Backup(a)
        r = backup.getTableInfoDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'getTableInfoDetail', body)

    def testTestClusterConnection(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
            'data_type': '',
            'cluster_config_path': '',
        }

        backup = Backup(a)
        r = backup.testClusterConnection(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Backup', 'testClusterConnection', body)


if __name__ == '__main__':
    unittest.main()
