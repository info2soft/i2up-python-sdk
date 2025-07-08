
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import RepBackup
from info2soft.rep.v20250630.RepBackup import RepBackup
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


class RepBackupTestCase(unittest.TestCase):
    def setUp(self):
        """在每个测试方法运行前执行"""
        self.original_cwd = os.getcwd()
        # 获取当前测试文件的目录
        test_dir = os.path.dirname(os.path.abspath(__file__))
        # 切换工作目录到测试文件所在的目录
        os.chdir(test_dir)

    def tearDown(self):
        """在每个测试方法运行后执行"""
        # 恢复原始工作目录，避免影响其他测试
        os.chdir(self.original_cwd)

    def testListRepBackupCdpZfs(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.listRepBackupCdpZfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'listRepBackupCdpZfs', body)

    def testRepBackupVerifyDevice(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'dir_name': '',
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.repBackupVerifyDevice(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'repBackupVerifyDevice', body)

    def testGetRepBackupCdpSnapNum(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
            'cdp_zfs_pool': '',
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.getRepBackupCdpSnapNum(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'getRepBackupCdpSnapNum', body)

    def testCreateRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'rep_backup': {
            'mirr_sync_attr': 1,
            'cdp_path': 'E:\\test3\\',
            'oph_path': 'E:\\test4\\',
            'secret_key': '',
            'rep_name': 'rep_backup',
            'snapshot_policy': 0,
            'bk_path_policy': 1,
            'cdp_process_time': '05:07:28',
            'mirr_open_type': 0,
            'compress': 0,
            'cdp_switch': 1,
            'snapshot_start': 1546913351,
            'cdp_baseline_format': 0,
            'cdp_bl_bkup_switch': 0,
            'encrypt_switch': 0,
            'auto_start': 1,
            'disk_limit': '0',
            'wk_path': [
            'E:\\test\\',],
            'band_width': '',
            'snapshot_limit': 24,
            'mirr_sync_flag': 0,
            'bk_path': [
            'E:\\test2\\',],
            'wk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'mirr_file_check': 0,
            'cdp_bl_sched_switch': 1,
            'del_policy': 1,
            'cmp_switch': 0,
            'rep_type': 0,
            'snapshot_interval': 1,
            'file_type_filter_switch': 0,
            'snapshot_switch': 1,
            'file_type_filter': '',
            'cdp_param': '3,30,0',
            'oph_policy': 2,
            'mirr_skip': '0',
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'cdp_bl_sched': '2|1|0|5',
            'excl_path': [],
            'mirr_sched': '',
            'bkup_one_time': 1515568566,
            'mirr_sched_switch': 0,
            'cdp_snap_on': 0,
            'cdp_snap_interval': 30,
            'cdp_snap_count': 240,
            'ct_name_type': 0,
            'ct_name_str1': '',
            'ct_name_str2': '',
            'ct_name_str3': '',
            'ct_name_str4': '',
            'cmp_file_check': 0,
            'cmp_schedule': [{
            'sched_every': 1,
            'sched_time': [
            '11:15',],
            'sched_day': [
            '26',],},],
            'thread_num': '0',
            'cdp_zfs_pool': '',
            'cdp_data_inc_switch': 0,
            'cdp_data_inc': 0,
            'cdp_data_inc_flag': '',
            'latency_threshold': 1,
            'mscs_autostart': 1,
            'mir_detect_script': '',
            'mscs_group': {},
            'filter_delete': 0,
            'cmp_limit': 1,
            'data_ip_uuid': 'B8166905-411E-B2CD-A742-77B1346D8E84',
            'bk_file_crypt': 0,
            'mir_detect_src_script': '',
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'traversing_sync': 1,
            'encrypt': 1,
            'compress_switch': 1,
            'rep_uuid': 'B8166905-411E-B2CD-A742-77B1346D8E84',
            'cdp_path_switch': 1,
            'pool_uuid': '',
            'buf_in_bk': 1,
            'rep_oph_policy': 0,
            'rep_oph_path': '',
            'rep_oph_switch': 1,
            'network_type': 1,
            'channel_uuid': '',
            'cmp_type': 1,
            'mirr_hash_type': 1,
            'black_box_on': '',
            'cdp_inc_on': '',
            'cdp_inc_interval': '',
            'black_box_addr': '10.226.13.109:8012',
            'black_box_read_node_uuid': '',
            'black_box_read_pool_uuid': '',
            'black_box_read_interval': 1,
            'save_local_disk': 1,
            'black_download_method': 1,
            'mirror_type': 1,
            'mirror_wk_path': [],
            'mirror_bk_path': [],
            'oph_keep_days': 0,},
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.createRepBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'createRepBackup', body)

    def testDescribeRepBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        repBackup = RepBackup(a)
        r = repBackup.describeRepBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'describeRepBackup', body)

    def testModifyRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'rep_backup': {
            'cdp_param': '',
            'rep_type': 0,
            'bkup_one_time': 1515568566,
            'snapshot_switch': 0,
            'cdp_baseline_format': '',
            'mirr_sync_flag': '0',
            'mirr_open_type': '0',
            'auto_start': '1',
            'snapshot_policy': '0',
            'cdp_bl_sched_switch': 0,
            'snapshot_interval': '0',
            'bk_path': 'D:\\DataTest2\\',
            'snapshot_start': 1515568566,
            'random_str': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
            'cdp_path': '',
            'file_type_filter_switch': 0,
            'cmp_schedule': {
            'sched_time': '02:44',
            'sched_day': 7,
            'sched_every': 2,},
            'snapshot_limit': '24',
            'cmp_switch': 0,
            'oph_path': '',
            'secret_key': '',
            'excl_path': [],
            'schedule': '',
            'policy_interval': 1,
            'cdp_switch': '',
            'wk_uuid': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
            'policy_operation': 1,
            'wk_path': 'D:\\DataTest\\',
            'mirr_skip': '0',
            'policy_limit': 1,
            'cdp_bl_sched': '',
            'del_policy': '1',
            'mirr_sched': '3*03:00-14:00,2*02:00-15:00',
            'encrypt_switch': '0',
            'band_width': '3*03:00-14:00*2m,2*02:00-15:00*80m',
            'compress': '0',
            'mirr_sync_attr': '1',
            'policy_start': 1,
            'cdp_process_time': '',
            'bk_path_policy': '0',
            'cdp_bl_bkup_switch': 0,
            'file_type_filter': '',
            'disk_limit': '0',
            'oph_policy': '0',
            'mirr_file_check': '0',
            'cmp_file_check': 0,
            'mirr_sched_switch': 0,
            'thread_num': '0',
            'cdp_data_inc': 1,
            'cdp_data_inc_switch': 1,
            'cdp_data_inc_flag': '',
            'mscs_autostart': 1,
            'mir_detect_script': '',
            'filter_delete': 0,
            'batch_adv_switch': 1,
            'batch_encrypt_switch': 1,
            'batch_mirr_switch': '',
            'batch_switch': 1,
            'batch_cdp_switch': '',
            'batch_cmp_switch': '',
            'cmp_limit': 1,
            'data_ip_uuid': 'B8166905-411E-B2CD-A742-77B1346D8E84',
            'compress_switch': 1,
            'cmp_type': 1,
            'rep_cmp_uuid': '',},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        repBackup = RepBackup(a)
        r = repBackup.modifyRepBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'modifyRepBackup', body)

    def testDeleteRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force': 1,
            'del_policy': 0,
            'recycle': 0,
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.deleteRepBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'deleteRepBackup', body)

    def testStartRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rep_uuids': [],
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.startRepBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'startRepBackup', body)

    def testStopRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rep_uuids': [],
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.stopRepBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'stopRepBackup', body)

    def testStartSyncRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rep_uuids': [],
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.startSyncRepBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'startSyncRepBackup', body)

    def testStopSyncRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rep_uuids': [],
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.stopSyncRepBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'stopSyncRepBackup', body)

    def testListRepBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [
            '11111111-1111-1111-1111-111111111111',
            '11111111-1111-1111-1111-111111111112',],
            'force_refresh': 1,
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.listRepBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'listRepBackupStatus', body)

    def testListRepBackupSyncStatus(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuid': '',
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.listRepBackupSyncStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'listRepBackupSyncStatus', body)

    def testListRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'limit': 15,
            'type': 1,
            'page': 1,
            'search_field': '',
            'status': '',
            'where_args': {
            'rule_uuid': 'xxxxx',
            'status': 'replication',},
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.listRepBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'listRepBackup', body)

    def testListRepBackupBaseLine(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'rep_uuid': '',
            'rc_method': 0,
            'data_path': '',
            'bk_uuid': '',
            'cdp_time_zone': '',
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.listRepBackupBaseLine(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'listRepBackupBaseLine', body)

    def testDeleteRepBackupBaseline(self):
        a = Auth(username, pwd)
        body = {
            'cdp_time_list': '2017-11-17 17:24:14',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        repBackup = RepBackup(a)
        r = repBackup.deleteRepBackupBaseline(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'deleteRepBackupBaseline', body)

    def testListRepBackupOrphan(self):
        a = Auth(username, pwd)
        body = {
            'path': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        repBackup = RepBackup(a)
        r = repBackup.listRepBackupOrphan(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'listRepBackupOrphan', body)

    def testDeleteRepBackupOrphan(self):
        a = Auth(username, pwd)
        body = {
            'path': '/',
            'orphan_list': [
            '',],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        repBackup = RepBackup(a)
        r = repBackup.deleteRepBackupOrphan(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'deleteRepBackupOrphan', body)

    def testDownloadRepBackupOrphan(self):
        a = Auth(username, pwd)
        body = {
            'orphan': '',
            'path': '/',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        repBackup = RepBackup(a)
        r = repBackup.downloadRepBackupOrphan(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'downloadRepBackupOrphan', body)

    def testListRepBackupSnapshot(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'rc_method': '',
            'rep_uuid': '',
            'bk_uuid': '',
            'data_path': '',
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.listRepBackupSnapshot(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'listRepBackupSnapshot', body)

    def testDeleteRepBackupSnapshot(self):
        a = Auth(username, pwd)
        body = {
            'snapshot_names': [],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        repBackup = RepBackup(a)
        r = repBackup.deleteRepBackupSnapshot(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'deleteRepBackupSnapshot', body)

    def testCreateRepBackupSnapshot(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        repBackup = RepBackup(a)
        r = repBackup.createRepBackupSnapshot(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'createRepBackupSnapshot', body)

    def testListRepBackupMscsGroup(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.listRepBackupMscsGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'listRepBackupMscsGroup', body)

    def testBatchCreateRepBackup(self):
        a = Auth(username, pwd)
        body = {
            'base_info_list': {
            'mirr_sync_attr': '1',
            'cdp_path': 'E: est3/',
            'oph_path': 'E: est4/',
            'secret_key': '',
            'rep_prefix': 'bk_',
            'snapshot_policy': '0',
            'bk_path_policy': '1',
            'cdp_process_time': '05:07:28',
            'mirr_open_type': '0',
            'compress': '0',
            'cdp_switch': '1',
            'snapshot_start': 1546913351,
            'cdp_baseline_format': '0',
            'cdp_bl_bkup_switch': 0,
            'encrypt_switch': '0',
            'auto_start': '1',
            'disk_limit': '0',
            'band_width': '',
            'snapshot_limit': '24',
            'mirr_sync_flag': '0',
            'mirr_file_check': '0',
            'cdp_bl_sched_switch': 1,
            'del_policy': '1',
            'cmp_switch': 0,
            'rep_type': 0,
            'snapshot_interval': '1',
            'file_type_filter_switch': 0,
            'snapshot_switch': 1,
            'file_type_filter': '',
            'cdp_param': '3,30,0',
            'oph_policy': '2',
            'mirr_skip': '0',
            'cdp_bl_sched': '2|1|0|5',
            'mirr_sched': '',
            'bkup_one_time': 1515568566,
            'mirr_sched_switch': 0,
            'cdp_snap_on': 0,
            'cdp_snap_interval': 30,
            'cdp_snap_count': 240,
            'ct_name_type': 0,
            'ct_name_str1': '',
            'ct_name_str2': '',
            'ct_name_str3': '',
            'ct_name_str4': '',
            'cmp_file_check': 0,
            'cmp_schedule': [{
            'sched_every': 1,
            'sched_time': [
            '20:50',],
            'sched_day': [
            '17',],},],
            'thread_num': '0',
            'cdp_zfs_pool': '',
            'cdp_data_inc_switch': 0,
            'cdp_data_inc': 0,
            'cdp_data_inc_flag': '',
            'latency_threshold': 1,
            'mscs_autostart': 1,
            'mir_detect_script': '',
            'mscs_group': {},
            'rep_sufix': '',
            'variable_type': 'node',
            'batch_name': '',
            'compress_switch': 0,
            'cmp_type': 1,
            'cmp_limit': 1,
            'buf_in_bk': 1,},
            'rep_backup': [{
            'wk_uuid': '',
            'bk_uuid': '',
            'wk_path': [],
            'bk_path': [],
            'excl_path': [],},],
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.batchCreateRepBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'batchCreateRepBackup', body)

    def testCheckBkPath(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
            'bk_path': [],
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.checkBkPath(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'checkBkPath', body)

    def testChkRules(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
            'bk_uuid': '',
            'bk_path': [],
            'chk_list': [
            'bk_path',
            'rules',
            'wk_path',],
            'has_reverse': 1,
            'rep_type': 1,
            'wk_path': [],
        }
        
        
        repBackup = RepBackup(a)
        r = repBackup.chkRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'chkRules', body)


if __name__ == '__main__':
    unittest.main()
