
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'E:/python-sdk')

import unittest
# from info2soft.dtrack.Dtrack import Dtrack
from info2soft.dtrack.v20220622.Dtrack import Dtrack
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


class DtrackTestCase(unittest.TestCase):

    def testListDtrackBackupDev(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listDtrackBackupDev(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackBackupDev', body)

    def testListDtrackBackupSystemInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listDtrackBackupSystemInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackBackupSystemInfo', body)

    def testVerifyDtrackBackupName(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'policy_name': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.verifyDtrackBackupName(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'verifyDtrackBackupName', body)

    def testCreateDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_name': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'config': {
            'source_disk_id': '',
            'mirror_file': '',
            'mirror_disk_path': '',
            'resolution': 1,
            'fs_analyze': 0,
            'scan_first': 0,
            'run_now': '0',
            'sync_type': 1,
            'schedule_config': '',
            'quiesce': 0,
            'snapshot': 0,
            'read_thread_count': 1,
            'send_thread_count': 1,
            'write_thread_count': 1,
            'mirror_fs_mountpoint': '',
            'source_disk_path': '',
            'track_length': 1,
            'job_history_start_time': '',
            'job_history_save_max_num': 1,
            'job_history_save_period': 1,
            'retry_times': 1,
            'retry_interval': 1,
            'compress': 1,
            'compress_method': '',
            'encryption': 1,
            'encryption_method': '',
            'mysql_db_array': [],
            'oracle_tablespace_array': [],
            'sqlserver_enable': 1,
            'max_snap_cnt': 1,
            'target_type': '',},
            'data_ip_uuid': '28C36A2E-230D-E66A-F0A6-A55C0134EA17',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.createDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'createDtrackBackup', body)

    def testModifyDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_name': '',
            'config': {
            'sync_type': 1,
            'schedule_config': '',
            'snapshot': 1,
            'quiesce': 1,
            'read_thread_count': 1,
            'send_thread_count': 1,
            'write_thread_count': 1,
            'job_history_start_time': '',
            'job_history_save_max_num': 1,
            'job_history_save_period': 1,
            'track_length': 1,
            'retry_times': 1,
            'retry_interval': 1,
            'compress': 1,
            'compress_method': '',
            'encryption': 1,
            'encryption_method': '',
            'mysql_db_array': [],
            'oracle_tablespace_array': [],
            'sqlserver_enable': 1,
            'max_snap_cnt': 1,},
            'wk_uuid': '',
            'bk_uuid': '',
            'random_str': '',
            'data_ip_uuid': '28C36A2E-230D-E66A-F0A6-A55C0134EA17',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.modifyDtrackBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'modifyDtrackBackup', body)

    def testDescribeDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.describeDtrackBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'describeDtrackBackup', body)

    def testListDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'bind_group_uuid':'',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackBackup', body)

    def testListDtrackBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuids': [],
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listDtrackBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackBackupStatus', body)

    def testDeleteDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'delete_mirror': 1,
            'policy_uuids': [],
            'force': 1,
        }
        
        dtrack = Dtrack(a)
        r = dtrack.deleteDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'deleteDtrackBackup', body)

    def testTakeSnapshotDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.takeSnapshotDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'takeSnapshotDtrackBackup', body)

    def testDeleteSnapshotDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }

        dtrack = Dtrack(a)
        r = dtrack.deleteSnapshotDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'deleteSnapshotDtrackBackup', body)

    def testTakeSnapshotCloneDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }

        dtrack = Dtrack(a)
        r = dtrack.takeSnapshotCloneDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'takeSnapshotCloneDtrackBackup', body)

    def testDeleteSnapshotCloneDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }

        dtrack = Dtrack(a)
        r = dtrack.deleteSnapshotCloneDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'deleteSnapshotCloneDtrackBackup', body)

    def testScanDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }

        dtrack = Dtrack(a)
        r = dtrack.scanDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'scanDtrackBackup', body)

    def testCancelScanDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }

        dtrack = Dtrack(a)
        r = dtrack.cancelScanDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'cancelScanDtrackBackup', body)

    def testSyncDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }

        dtrack = Dtrack(a)
        r = dtrack.syncDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'syncDtrackBackup', body)

    def testCancelSyncDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }

        dtrack = Dtrack(a)
        r = dtrack.cancelSyncDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'cancelSyncDtrackBackup', body)

    def testSuspendDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }

        dtrack = Dtrack(a)
        r = dtrack.suspendDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'suspendDtrackBackup', body)

    def testResumeDtrackBackup(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuid': '',
            'snapshot_name': '',
            'quiesce': 1,
            'fs_analyze': 0,
            'base_on_driver': 0,
            'sync_after_scan': 0,
            'reason': 128,
            'snapshot': 0,
            'operate': '',
            'force': 1,
            'snapshot_clone_name': '',
        }

        dtrack = Dtrack(a)
        r = dtrack.resumeDtrackBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'resumeDtrackBackup', body)

    def testAddDtrackBackupHistory(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
            'status': 1,
            'create_time': 1563257893,
            'end_time': 1563257893,
            'job_id': '',
            'reason': 1,
            'sync_option': {
            'analyze_fs': 0,
            'take_snapshot': 0,
            'quiesce': 0,},
            'scan_option': {
            'analyze_fs': 0,
            'base_on_driver': 1,
            'sync_after_scan': 1,},
            'sync_statistic': {
            'read_sector': 1,
            'send_sector': 1,
            'write_sector': 1,},
            'scan_statistic': {
            'local_scan_bit': 1,
            'remote_scan_bit': 1,
            'total_delta_bit': 1,
            'clean_bit': 1,},
            'Content-Type': 'application/json',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.addDtrackBackupHistory(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'addDtrackBackupHistory', body)

    def testListDtrackBackupHistory(self):
        a = Auth(username, pwd)
        body = {
            'start': 1,
            'end': 1,
            'page': 1,
            'limit': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.listDtrackBackupHistory(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackBackupHistory', body)

    def testListDtrackBackupSnap(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.listDtrackBackupSnap(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackBackupSnap', body)

    def testDtrackBackupCtlDrv(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'ctl_flag': 'INSTALL_DRIVER',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.dtrackBackupCtlDrv(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'dtrackBackupCtlDrv', body)

    def testDtrackBackupRebootSystem(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.dtrackBackupRebootSystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'dtrackBackupRebootSystem', body)

    def testDtrackBackupFeatureMatrix(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'type': 'tc',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.dtrackBackupFeatureMatrix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'dtrackBackupFeatureMatrix', body)

    def testDescribeDtrackNodeInitiatorName(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '',
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.describeDtrackNodeInitiatorName(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'describeDtrackNodeInitiatorName', body)

    def testDescribeDtrackNodeInitiatorStatus(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '',
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.describeDtrackNodeInitiatorStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'describeDtrackNodeInitiatorStatus', body)

    def testDescribeDtrackNodeInitiatorVersion(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'config_addr': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.describeDtrackNodeInitiatorVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'describeDtrackNodeInitiatorVersion', body)

    def testMysqlConf(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'username': '',
            'password': '',
            'timeout': 1,
            'port': 1,
            'mysql_path': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.mysqlConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'mysqlConf', body)

    def testListMysqlConf(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listMysqlConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listMysqlConf', body)

    def testListMysqlDb(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listMysqlDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listMysqlDb', body)

    def testOracleConf(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'username': '',
            'password': '',
            'timeout': 1,
            'port': 1,
            'sqlplus_path': '',
            'sid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.oracleConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'oracleConf', body)

    def testListOracleConf(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listOracleConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listOracleConf', body)

    def testListOracleDb(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listOracleDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listOracleDb', body)

    def testSqlserverConf(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'timeout': 1,
        }
        
        dtrack = Dtrack(a)
        r = dtrack.sqlserverConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'sqlserverConf', body)

    def testListSqlserverConf(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listSqlserverConf(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listSqlserverConf', body)

    def testListDtrackRecoveryTarget(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'address': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listDtrackRecoveryTarget(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackRecoveryTarget', body)

    def testDescribeDtrackRecoveryTargetDiscovered(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'address': '',
        }
        
        dtrack = Dtrack(a)
        r = dtrack.describeDtrackRecoveryTargetDiscovered(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'describeDtrackRecoveryTargetDiscovered', body)

    def testCreateDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
            'group_name': '',
            'config': {
                'sync_type': 1,
                'schedule_config': '',
                'snapshot': 1,
                'quiesce': 1,
                'retry_times': 1,
                'retry_interval': 1,
                'compress': 1,
                'compress_method': '',
                'encryption': 1,
                'encryption_method': '',
                'mysql_db_array': [],
                'oracle_tablespace_array': [],
                'sqlserver_enable': 1,
                'max_snap_cnt': 1, },
        }
        
        dtrack = Dtrack(a)
        r = dtrack.createDtrackGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'createDtrackGroup', body)

    def testModifyDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_name': '',
            'config': {
                'sync_type': 1,
                'schedule_config': '',
                'snapshot': 1,
                'quiesce': 1,
                'retry_times': 1,
                'retry_interval': 1,
                'compress': 1,
                'compress_method': '',
                'encryption': 1,
                'encryption_method': '',
                'mysql_db_array': [],
                'oracle_tablespace_array': [],
                'sqlserver_enable': 1,
                'max_snap_cnt': 1, },
            'wk_uuid': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.modifyDtrackGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'modifyDtrackGroup', body)

    def testDescribeDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.describeDtrackGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'describeDtrackGroup', body)

    def testListDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listDtrackGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackGroup', body)

    def testListDtrackGroupStatus(self):
        a = Auth(username, pwd)
        body = {
            'group_uuids': [],
        }
        
        dtrack = Dtrack(a)
        r = dtrack.listDtrackGroupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackGroupStatus', body)

    def testUpdateDtrackGroupBind(self):
        a = Auth(username, pwd)
        body = {
            'policy_uuids': [],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.updateDtrackGroupBind(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'updateDtrackGroupBind', body)

    def testUpdateDtrackBackupBind(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.updateDtrackBackupBind(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'updateDtrackBackupBind', body)

    def testDeleteDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuids': [],
        }
        
        dtrack = Dtrack(a)
        r = dtrack.deleteDtrackGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'deleteDtrackGroup', body)

    def testSuspendDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'operate': '',
            'fs_analyze': 1,
            'snapshot': 1,
            'quiesce': 1,
            'reason': 1,
            'snapshot_name': '',
            'force': 0,
        }
        
        dtrack = Dtrack(a)
        r = dtrack.suspendDtrackGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'suspendDtrackGroup', body)

    def testResumeDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'operate': '',
            'fs_analyze': 1,
            'snapshot': 1,
            'quiesce': 1,
            'reason': 1,
            'snapshot_name': '',
            'force': 0,
        }

        dtrack = Dtrack(a)
        r = dtrack.resumeDtrackGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'resumeDtrackGroup', body)

    def testSyncDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'operate': '',
            'fs_analyze': 1,
            'snapshot': 1,
            'quiesce': 1,
            'reason': 1,
            'snapshot_name': '',
            'force': 0,
        }

        dtrack = Dtrack(a)
        r = dtrack.syncDtrackGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'syncDtrackGroup', body)

    def testCancelSyncDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'operate': '',
            'fs_analyze': 1,
            'snapshot': 1,
            'quiesce': 1,
            'reason': 1,
            'snapshot_name': '',
            'force': 0,
        }

        dtrack = Dtrack(a)
        r = dtrack.cancelSyncDtrackGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'cancelSyncDtrackGroup', body)

    def testTakeSnapshotDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'operate': '',
            'fs_analyze': 1,
            'snapshot': 1,
            'quiesce': 1,
            'reason': 1,
            'snapshot_name': '',
            'force': 0,
        }

        dtrack = Dtrack(a)
        r = dtrack.takeSnapshotDtrackGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'takeSnapshotDtrackGroup', body)

    def testDeleteSnapshotDtrackGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'operate': '',
            'fs_analyze': 1,
            'snapshot': 1,
            'quiesce': 1,
            'reason': 1,
            'snapshot_name': '',
            'force': 0,
        }

        dtrack = Dtrack(a)
        r = dtrack.deleteSnapshotDtrackGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'deleteSnapshotDtrackGroup', body)

    def testListDtrackGroupSnap(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        dtrack = Dtrack(a)
        r = dtrack.listDtrackGroupSnap(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Dtrack', 'listDtrackGroupSnap', body)


if __name__ == '__main__':
    unittest.main()
