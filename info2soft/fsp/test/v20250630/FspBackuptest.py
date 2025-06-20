
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import FspBackup
from info2soft.fsp.v20250630.FspBackup import FspBackup
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


class FspBackupTestCase(unittest.TestCase):
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

    def testListFspBackupNic(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'bk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.listFspBackupNic(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspBackupNic', body)

    def testListFspBackupDir(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'fsp_uuid': '',
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.listFspBackupDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspBackupDir', body)

    def testVerifyFspBackupCoopySpace(self):
        a = Auth(username, pwd)
        body = {
            'bk_path': [
            'fsp_bk',],
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
            'excl_path': [
            '/cgroup/',
            '/dev/',
            '/etc/X11/xorg.conf/',
            '/etc/init.d/i2node/',
            '/etc/rc.d/init.d/i2node/',
            '/etc/sdata/',
            '/lost+found/',
            '/media/',
            '/mnt/',
            '/proc/',
            '/run/',
            '/selinux/',
            '/sys/',
            '/tmp/',
            '/usr/local/sdata/',
            '/var/i2/',
            '/var/i2data/',
            '/var/lock/',
            '/var/run/vmblock-fuse/',],
            'wk_path': [
            '/',],
            'storage_left_size': '',
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspBackupCoopySpace(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspBackupCoopySpace', body)

    def testVerifyFspBackupLicense(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspBackupLicense(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspBackupLicense', body)

    def testVerifyFspBackupOldRule(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'bk_path': [
            '/fsp_bk/',],
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspBackupOldRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspBackupOldRule', body)

    def testVerifyFspBackupOsVersion(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspBackupOsVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspBackupOsVersion', body)

    def testListFspBackupDriverInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.listFspBackupDriverInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspBackupDriverInfo', body)

    def testCreateFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'secret_key': '',
            'band_width': '',
            'mirr_open_type': '0',
            'service_uuid': '',
            'mirr_sync_flag': '0',
            'excl_path': [
            '/cgroup/',
            '/dev/',
            '/etc/X11/xorg.conf/',
            '/etc/init.d/i2node/',
            '/etc/rc.d/init.d/i2node/',
            '/etc/sdata/',
            '/lost+found/',
            '/media/',
            '/mnt/',
            '/proc/',
            '/run/',
            '/selinux/',
            '/sys/',
            '/tmp/',
            '/usr/local/sdata/',
            '/var/i2/',
            '/var/i2data/',
            '/var/lock/',
            '/var/run/vmblock-fuse/',],
            'bkup_one_time': 0,
            'encrypt_switch': '0',
            'mirr_sync_attr': '1',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'wk_data_type': 1,
            'bk_path': [
            '/fsp_bk/',],
            'sync_item': '/',
            'bkup_policy': 2,
            'mirr_file_check': '0',
            'compress': '0',
            'monitor_type': 0,
            'failover': 0,
            'wk_path': [
            '/',],
            'fsp_name': 'test',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
            'fsp_wk_shut_flag': '2',
            'bk_data_type': 1,
            'bkup_schedule': [{
            'sched_day': 25,
            'sched_time': '13:38',
            'sched_every': 2,
            'limit': 6,
            'backup_type': 0,
            'policys': '"每天22:00自动执行"',
            'backup_type_show': '"全备"',
            'running_time': '"22:00"',},],
            'fsp_type': 3,
            'random_str': '11111111-1111-1111-1111-111111111111',
            'del_policy': 1,
            'timeout': 1,
            'cbt_switch': 1,
            'threshold_vaild_byte': '',
            'advanced_policy': {
            'bk_cdp': 1,
            'execute_interval': 1,
            'cdp_detail': 1,
            'cdp_daily': 1,
            'cdp_param': '',
            'cdp_switch': 1,
            'cdp_snapshot_days': 1,
            'cdp_snapshot_execute_interval': 1,
            'cdp_keep_data': 1,},
            'vp_uuid': '',
            'storage_uuid': '',
            'verify_settings': {
            'vm_list': [{
            'vm_name': '新建虚拟机1',
            'orch_vm_name': '新建虚拟机1_20200612100700',
            'scripts_type': '',
            'scripts': '',
            'orch_disks': [{
            'is_ignored': '',
            'disk_name': '',
            'disk_path': '',
            'new_ds': '',
            'id': '',
            'boot_index': '',
            'file_name': '',
            'size': '',},],
            'orch_networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'ip': '',
            'security_group_name': '',},],
            'orch_cpu_num': '',
            'orch_cores_per_cpu_num': '',
            'orch_memory_mb': '',
            'custom_config': 1,},],
            'drill_plat_uuid': '',
            'auto': '',
            'add_drill': '',
            'hostname': '',
            'create_vm_type': '1',},
            'resource_settings': {
            'new_host': '',
            'new_ds': '',
            'new_dc_mor': '',
            'new_dc': '',
            'tgt_uuid': '',
            'network_name': '',
            'vm_list': [{
            'vm_name': '',
            'new_vm_name': '',
            'custom_config': '',
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'ip': '',
            'security_group_name': '',
            'auto_ip': False,
            'gateway': '',
            'is_defroute': False,},],
            'disk_list': [{
            'is_ignored': '',
            'disk_name': '',
            'disk_path': '',
            'new_ds': '',
            'id': '',
            'boot_index': '',
            'file_name': '',
            'size': '',
            'disk_provision_type': 1,},],
            'dynamic_mem': '',
            'new_vm_hostname': '',},],
            'network_id': '',
            'bk_uuid': '',
            'bk_path': [],
            'create_vm_type': 1,},
            'data_ip_uuid': '',
            'bk_file_crypt': 0,
            'bk_crypt_type': 1,
            'bk_crypt_key': '',
            'encrypt': 0,
            'thread_num': 1,
            'start_type': 0,
            'src_dedupe_switch': 1,
            'oph_policy': 0,
            'dedupe_uuid': '',
            'dedupe_secret_key': '',
            'database_switch': 0,
            'database_type': 0,
            'oracle_dbagent_param': {
            'oracle_sid': '',
            'sql_plus_path': '',
            'username': '',
            'password': '',
            'port': '',
            'table_space': '',
            'timeout': '',},
            'mysql_dbagent_param': {
            'mysql_path': '',
            'username': '',
            'password': '',
            'port': '',
            'database_name': '',
            'timeout': '',},
            'sqlserver_dbagent_param': {
            'timeout': '',
            'enable': '',},
            'custom_dbagent_param': {
            'pre_snapshot_script': '',
            'post_snapshot_script': '',},
            'bk_storage': 1,
            'pool_uuid': '',
            'in_failover_switch': 0,
            'in_failover_settings': {
            'virtual_cidr': '',
            'virtuai_gateway': '',
            'virtual_ip': '',
            'virtual_port': 1,
            'virtual_data_ip': '',
            'oph_policy': 0,
            'rc_dir': [],
            'data_path': [],
            'excl_dir': [],},
            'proxy_uuid': '',
            'obs_settings': {
            'sto_uuid': '',
            'bucket_name': '',
            'bucket_path': '',},
            'del_shared_dir_switch': 1,},
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.createFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'createFspBackup', body)

    def testModifyFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'secret_key': '',
            'band_width': '3*03:00-14:00*2m',
            'mirr_open_type': '0',
            'service_uuid': '',
            'mirr_sync_flag': '0',
            'excl_path': '["/cgroup/","/dev/","/etc/X11/xorg.conf/","/etc/init.d/i2node/","/etc/rc.d/init.d/i2node/","/etc/sdata/","/lost+found/","/media/","/mnt/","/proc/","/run/","/selinux/","/sys/","/tmp/","/usr/local/sdata/","/var/i2/","/var/i2data/","/var/lock/","/var/run/vmblock-fuse/"],',
            'bkup_one_time': 1515568566,
            'encrypt_switch': '0',
            'bk_type': 0,
            'mirr_sync_attr': '1',
            'bk_uuid': 'C11FE572-5207-3359-DB85-001E95F5F185',
            'wk_data_type': 1,
            'bk_path': '["/FSPback0107/"],',
            'sync_item': '/',
            'bkup_policy': 0,
            'net_mapping_type': '2',
            'snapshot_policy': '0',
            'mirr_file_check': '0',
            'snapshot_interval': '0',
            'compress': '0',
            'monitor_type': 0,
            'failover': '0',
            'wk_path': '["/","/boot/"],',
            'snapshot_limit': '24',
            'snapshot_switch': 0,
            'fsp_name': 'rrrrr',
            'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
            'fsp_wk_shut_flag': '2',
            'bk_data_type': 0,
            'bkup_schedule': [{
            'sched_day': 22,
            'sched_time': '01:06',
            'sched_every': 2,
            'limit': 29,
            'backup_type': 1,
            'backup_type_show': '"全备"',
            'running_time': '"22:00"',
            'policys': '"每天22:00自动执行"',},],
            'fsp_type': 1,
            'random_str': '11111111-1111-1111-1111-111111111111',
            'timeout': 1,
            'cbt_switch': 1,
            'threshold_vaild_byte': 1,
            'advanced_policy': {
            'bk_cdp': 1,
            'execute_interval': 1,
            'cdp_detail': 1,
            'cdp_daily': 1,
            'cdp_switch': 1,
            'cdp_param': '',
            'cdp_keep_data': 1,},
            'data_ip_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
            'thread_num': 1,
            'in_failover_switch': 1,
            'in_failover_settings': {
            'virtual_cidr': '',
            'virtuai_gateway': '',
            'virtual_ip': '',
            'virtual_port': 1,
            'virtual_data_ip': '',
            'oph_policy': 1,
            'data_path': [],
            'rc_dir': [],
            'excl_dir': [],},},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fspBackup = FspBackup(a)
        r = fspBackup.modifyFspBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'modifyFspBackup', body)

    def testDescribeFspBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fspBackup = FspBackup(a)
        r = fspBackup.describeFspBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'describeFspBackup', body)

    def testDeleteFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'del_policy': 1,
            'force': 1,
            'recycle': 0,
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.deleteFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'deleteFspBackup', body)

    def testListFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'type': 3,
            'limit': 10,
            'page': 1,
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.listFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspBackup', body)

    def testStartFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'bk_type': '',
            'continue_last_backup': 0,
            'stop_later': '',
            'op_code': '',
            'snap_point': '',
            'power_on': 1,
            'in_failover_settings': {
            'virtual_cidr': '',
            'virtuai_gateway': '',
            'virtual_ip': '',
            'virtual_port': 1,
            'virtual_data_ip': '',
            'oph_policy': 1,
            'data_path': [],
            'rc_dir': [],
            'excl_dir': [],},
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.startFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'startFspBackup', body)

    def testStopFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'bk_type': '',
            'continue_last_backup': 0,
            'stop_later': '',
            'op_code': '',
            'snap_point': '',
            'power_on': 1,
            'in_failover_settings': {
            'virtual_cidr': '',
            'virtuai_gateway': '',
            'virtual_ip': '',
            'virtual_port': 1,
            'virtual_data_ip': '',
            'oph_policy': 1,
            'data_path': [],
            'rc_dir': [],
            'excl_dir': [],},
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.stopFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'stopFspBackup', body)

    def testFinishFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'bk_type': '',
            'continue_last_backup': 0,
            'stop_later': '',
            'op_code': '',
            'snap_point': '',
            'power_on': 1,
            'in_failover_settings': {
            'virtual_cidr': '',
            'virtuai_gateway': '',
            'virtual_ip': '',
            'virtual_port': 1,
            'virtual_data_ip': '',
            'oph_policy': 1,
            'data_path': [],
            'rc_dir': [],
            'excl_dir': [],},
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.finishFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'finishFspBackup', body)

    def testFailoverFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'bk_type': '',
            'continue_last_backup': 0,
            'stop_later': '',
            'op_code': '',
            'snap_point': '',
            'power_on': 1,
            'in_failover_settings': {
            'virtual_cidr': '',
            'virtuai_gateway': '',
            'virtual_ip': '',
            'virtual_port': 1,
            'virtual_data_ip': '',
            'oph_policy': 1,
            'data_path': [],
            'rc_dir': [],
            'excl_dir': [],},
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.failoverFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'failoverFspBackup', body)

    def testFailbackFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'bk_type': '',
            'continue_last_backup': 0,
            'stop_later': '',
            'op_code': '',
            'snap_point': '',
            'power_on': 1,
            'in_failover_settings': {
            'virtual_cidr': '',
            'virtuai_gateway': '',
            'virtual_ip': '',
            'virtual_port': 1,
            'virtual_data_ip': '',
            'oph_policy': 1,
            'data_path': [],
            'rc_dir': [],
            'excl_dir': [],},
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.failbackFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'failbackFspBackup', body)

    def testListFspBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.listFspBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspBackupStatus', body)

    def testBatchCreateFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'base_info_list': {
            'secret_key': '',
            'band_width': '',
            'mirr_open_type': '0',
            'service_uuid': '',
            'mirr_sync_flag': '0',
            'bkup_one_time': 0,
            'encrypt_switch': '0',
            'mirr_sync_attr': '1',
            'wk_data_type': 1,
            'sync_item': '/',
            'bkup_policy': 2,
            'mirr_file_check': '0',
            'compress': '0',
            'monitor_type': 0,
            'failover': '0',
            'fsp_wk_shut_flag': '2',
            'bk_data_type': 1,
            'bkup_schedule': [{
            'sched_day': 7,
            'sched_time': '21:57',
            'sched_every': 2,
            'limit': 37,
            'backup_type': 0,
            'policys': '"每天22:00自动执行"',
            'backup_type_show': '"全备"',
            'running_time': '"22:00"',},],
            'fsp_type': 3,
            'del_policy': 1,
            'timeout': 1,
            'cbt_switch': 1,
            'threshold_vaild_byte': '',
            'advanced_policy': {
            'bk_cdp': 1,
            'execute_interval': 1,
            'cdp_detail': 1,
            'cdp_daily': 1,
            'cdp_param': '',
            'cdp_switch': 1,},
            'tgt_uuid': '',
            'new_dc': '',
            'new_dc_mor': '',
            'new_host': '',
            'new_ds': '',
            'network_name': '',
            'network_id': '',
            'create_vm_type': 1,},
            'common_params': {
            'batch_name': '',
            'rep_prefix': '',
            'rep_sufix': '',
            'variable_type': 1,},
            'node_list': [{
            'bk_uuid': '',
            'excl_path': [],
            'bk_path': [],
            'wk_uuid': '',
            'wk_path': [],
            'vm_name': '',
            'new_vm_name': '',
            'custom_config': 1,
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'dynamic_mem': '',
            'add_drill': 1,
            'auto': 1,
            'orch_vm_name': '',
            'scripts_type': '',
            'scripts': '',
            'os_type': 1,
            'new_vm_hostname': '',},],
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.batchCreateFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'batchCreateFspBackup', body)

    def testVerifyEnvironment(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
            'bk_uuid': '',
            'wk_path': '',
            'cbt_switch': 0,
            'task_type': 1,
        }
        
        
        fspBackup = FspBackup(a)
        r = fspBackup.verifyEnvironment(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyEnvironment', body)


if __name__ == '__main__':
    unittest.main()
