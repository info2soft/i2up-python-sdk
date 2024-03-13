
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import AppSystem
from info2soft.resource.v20240228.AppSystem import AppSystem
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


class AppSystemTestCase(unittest.TestCase):

    def testSecDirList(self):
        a = Auth(username, pwd)
        body = {
        }
        
        appSystem = AppSystem(a)
        r = appSystem.secDirList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'secDirList', body)

    def testCreateSecDir(self):
        a = Auth(username, pwd)
        body = {
            'dir_name': '',
            'pid': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.createSecDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createSecDir', body)

    def testModifySecDir(self):
        a = Auth(username, pwd)
        body = {
            'dir_name': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.modifySecDir(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifySecDir', body)

    def testDeleteSecDir(self):
        a = Auth(username, pwd)
        body = {
            'dir_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.deleteSecDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteSecDir', body)

    def testAppSystemList(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'limit': 1,
            'page': 1,
            'search_field': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.appSystemList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'appSystemList', body)

    def testAppSystemMembersList(self):
        a = Auth(username, pwd)
        body = {
            'rule_type': 1,
            'name': '',
            'os_type': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.appSystemMembersList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'appSystemMembersList', body)

    def testDescribeAppSystem(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.describeAppSystem(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeAppSystem', body)

    def testCreateAppSystem(self):
        a = Auth(username, pwd)
        body = {
            'dir_uuid': '73412DAD-A7A6-4605-A9FF-081495C8800B',
            'sys_name': '应用系统name',
            'level_cfg': [{
            'day': [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',],
            'periods': [{
            'level': 0,
            'start_time': '10:10',
            'end_time': '12:20',},],},],
            'node_uuids': [
            'EA52A961-9883-66FE-188B-D7266AD9594B',
            '09EEA553-C3B8-0D7A-4797-F7A7E2D4FAE1',],
            'vm_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.createAppSystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createAppSystem', body)

    def testModifyAppSystem(self):
        a = Auth(username, pwd)
        body = {
            'dir_uuid': '',
            'sys_name': '',
            'level_cfg': [{
            'day': [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',],
            'periods': [{
            'level': 1,
            'start_time': '10:10',
            'end_time': '12:20',},],},],
            'random_str': '',
            'node_uuids': [
            'EF4825D6-7FB3-7961-6271-5E5B2603414D',],
            'vm_uuids': [
            'EF4825D6-7FB3-7961-6271-5E5B2603414D',],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.modifyAppSystem(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifyAppSystem', body)

    def testDeleteAppSystem(self):
        a = Auth(username, pwd)
        body = {
            'sys_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.deleteAppSystem(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteAppSystem', body)

    def testGetVmList(self):
        a = Auth(username, pwd)
        body = {
        }
        
        appSystem = AppSystem(a)
        r = appSystem.getVmList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'getVmList', body)

    def testGetMembersList(self):
        a = Auth(username, pwd)
        body = {
            'sys_uuid': '',
            'page': 1,
            'limit': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.getMembersList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'getMembersList', body)

    def testRecoveryList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
            'type': 1,
            'search_field': '',
            'search_value': '',
            'wk_status_filter': '',
            'tgt_status_filter': '',
            'failback_status_filter': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.recoveryList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'recoveryList', body)

    def testRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.recoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'recoveryStatus', body)

    def testBatchTaskList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1
        }
        
        appSystem = AppSystem(a)
        r = appSystem.batchTaskList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'batchTaskList', body)

    def testBatchTaskStatus(self):
        a = Auth(username, pwd)
        body = {
            'batch_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.batchTaskStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'batchTaskStatus', body)

    def testStartBatchTask(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'batch_uuid': '',
            'delete_tgtvm': '',
            'del_policy': '',
        }

        appSystem = AppSystem(a)
        r = appSystem.startBatchTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'startBatchTask', body)

    def testStopBatchTask(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'batch_uuid': '',
            'delete_tgtvm': '',
            'del_policy': '',
        }

        appSystem = AppSystem(a)
        r = appSystem.stopBatchTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'stopBatchTask', body)

    def testDeleteBatchTask(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'batch_uuid': '',
            'delete_tgtvm': '',
            'del_policy': '',
        }

        appSystem = AppSystem(a)
        r = appSystem.deleteBatchTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteBatchTask', body)

    def testResourceView(self):
        a = Auth(username, pwd)
        body = {
        }
        
        appSystem = AppSystem(a)
        r = appSystem.resourceView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'resourceView', body)

    def testListBackupCenter(self):
        a = Auth(username, pwd)
        body = {
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listBackupCenter(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listBackupCenter', body)

    def testGetBackupCenterInfo(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.getBackupCenterInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'getBackupCenterInfo', body)

    def testListHosts(self):
        a = Auth(username, pwd)
        body = {
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listHosts(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listHosts', body)

    def testResourceProtectionCoverage(self):
        a = Auth(username, pwd)
        body = {
            'level_a': 1,
            'level_b': 1,
            'level_c': 1,
            'vp_uuid': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.resourceProtectionCoverage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'resourceProtectionCoverage', body)

    def testTaskView(self):
        a = Auth(username, pwd)
        body = {
        }
        
        appSystem = AppSystem(a)
        r = appSystem.taskView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'taskView', body)

    def testListStatisticsReport(self):
        a = Auth(username, pwd)
        body = {
            'start_time': '',
            'end_time': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listStatisticsReport(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listStatisticsReport', body)

    def testAutoRegisterNode(self):
        a = Auth(username, pwd)
        body = {
            'node_name': '',
            'os_type': 1,
            'os_user': '',
            'os_pwd': '',
            'cc_ip': '',
            'config_addr': '',
            'root': '',
            'disk_limit': 1,
            'mem_limit': 1,
            'disk_free_space_limit': 1,
            'uuid': '',
            'vm_uuid': '',
            'config_port': 1,
            'vp_uuid': '',
            'cache_path': '',
            'log_path': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.autoRegisterNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'autoRegisterNode', body)

    def testCreateFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'fsp_type': 21,
            'wk_uuid': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            }
        }
        
        appSystem = AppSystem(a)
        r = appSystem.createFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createFullMachineCopy', body)

    def testModifyFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'fsp_type': 21,
            'wk_uuid': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            'timeout': 0,
            'wk_path': [],
            'bk_path': [],
            'resource_settings': {
            'tgt_uuid': '',
            'new_dc': '',
            'new_host': '',
            'new_ds': '',
            'new_dc_mor': '',
            'vm_list': [{
            'disk_list': [{
            'boot_index': '',
            'file_name': '',
            'new_ds': '',
            'size': '',
            'is_ignored': '',
            'disk_name': '',
            'disk_path': '',
            'id': '',
            'disk_provision_type': 1,},],
            'vm_name': '',
            'new_vm_name': '',
            'custom_config': 1,
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'dynamic_mem': '',
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'auto_ip': '',
            'ip': '',
            'security_group_name': '',},],},],},
            'fsp_name': '',
            'bk_data_type': 21,
            'wk_data_type': 0,
            'auto_register': 1,
            'node_name': '',
            'random_str': '',},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.modifyFullMachineCopy(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifyFullMachineCopy', body)

    def testDeleteFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'force': 1,
            'del_policy': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.deleteFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteFullMachineCopy', body)

    def testDescribeFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.describeFullMachineCopy(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeFullMachineCopy', body)

    def testListFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'limit': 10,
            'page': 1,
            'search_value': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listFullMachineCopy', body)

    def testlistFullMachineCopyStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': '',
            'force_refresh': 0
        }

        appSystem = AppSystem(a)
        r = appSystem.listFullMachineCopyStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listFullMachineCopyStatus', body)

    def teststartFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': '',
            'operate': ''
        }

        appSystem = AppSystem(a)
        r = appSystem.startFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'startFullMachineCopy', body)

    def teststopFullMachineCopy(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': '',
            'operate': ''
        }

        appSystem = AppSystem(a)
        r = appSystem.stopFullMachineCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'stopFullMachineCopy', body)

    def testCreateAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_name': '',
            'wk_uuid': '',
            'vp_uuid': '',
            'biz_grp_list': [],
            'vm_name': '',
            'vm_ref': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            'wk_path': [],
            'bk_path': [],
            'excl_path': [],
            'mirr_file_check': 1,
            'mirr_sync_flag': 1,
            'mirr_open_type': 1,
            'mirr_sync_attr': 1,
            'encrypt_switch': 1,
            'secret_key': '',
            'compress': 1,
            'bkup_schedule': [{
            'sched_day': [],
            'sched_time': [],
            'sched_every': 1,
            'limit': '',
            'sched_gap_hour': 1,
            'sched_time_start': '',},],
            'band_width': '',
            'verify_settings': {
            'add_drill': 1,
            'auto': '',
            'drill_plat_uuid': '',
            'vm_list': [{
            'vm_name': '',
            'orch_vm_name': '',
            'scripts_type': 1,
            'scripts': '',
            'custom_config': 1,
            'orch_disks': [{
            'file_name': '',
            'size': '',
            'new_ds': '',
            'boot_index': '',
            'disk_name': '',
            'disk_path': '',
            'id': '',},],
            'orch_networks': [{
            'source_network_name': '',
            'network_name': '',
            'network_id': '',
            'subnet_name': '',
            'ip': '',
            'security_group_name': '',
            'mac_address': '',
            'keep_mac': '',},],
            'orch_cpu_num': '',
            'orch_cores_per_cpu_num': '',
            'orch_memory_mb': '',},],},
            'take_over_settings': {
            'disk_list': [{
            'file_name': '',
            'size': '',
            'new_ds': '',
            'boot_index': 1,},],
            'networks': [{
            'network_name': '',
            'network_id': '',
            'subnet_name': '',
            'auto_ip': '',
            'ip': '',
            'security_group_name': '',},],
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',},
            'oph_path': '',
            'oph_policy': 1,
            'thread_num': 1,
            'is_continue_policy': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.createAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createAppContinuity', body)

    def testModifyAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_name': '',
            'wk_uuid': '',
            'vp_uuid': '',
            'biz_grp_list': [],
            'vm_name': '',
            'vm_ref': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            'wk_path': [],
            'bk_path': [],
            'excl_path': [],
            'mirr_file_check': 1,
            'mirr_sync_flag': 1,
            'mirr_open_type': 1,
            'mirr_sync_attr': 1,
            'encrypt_switch': 1,
            'secret_key': '',
            'compress': 1,
            'bkup_schedule': [{
            'sched_day': [],
            'sched_time': [],
            'sched_every': 1,
            'limit': '',},],
            'band_width': '',
            'verify_settings': {
            'add_drill': 1,
            'auto': '',
            'drill_plat_uuid': '',
            'vm_list': [{
            'vm_name': '',
            'orch_vm_name': '',
            'scripts_type': 1,
            'scripts': '',
            'custom_config': 1,
            'orch_disks': [{
            'file_name': '',
            'size': '',
            'new_ds': '',
            'boot_index': '',
            'disk_name': '',
            'disk_path': '',
            'id': '',},],
            'orch_networks': [{
            'source_network_name': '',
            'network_name': '',
            'network_id': '',
            'subnet_name': '',
            'ip': '',
            'security_group_name': '',
            'mac_address': '',
            'keep_mac': '',},],
            'orch_cpu_num': '',
            'orch_cores_per_cpu_num': '',
            'orch_memory_mb': '',},],},
            'take_over_settings': {
            'disk_list': [{
            'file_name': '',
            'size': '',
            'new_ds': '',
            'boot_index': 1,},],
            'networks': [{
            'network_name': '',
            'network_id': '',
            'subnet_name': '',
            'auto_ip': '',
            'ip': '',
            'security_group_name': '',},],
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',},
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.modifyAppContinuity(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifyAppContinuity', body)

    def testDeleteAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'force': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.deleteAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteAppContinuity', body)

    def testDescribeAppContinuity(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.describeAppContinuity(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeAppContinuity', body)

    def testListAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listAppContinuity', body)

    def teststartAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }

        appSystem = AppSystem(a)
        r = appSystem.startAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'startAppContinuity', body)

    def teststopAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }

        appSystem = AppSystem(a)
        r = appSystem.stopAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'stopAppContinuity', body)

    def testsnapshotImmediatelyAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }

        appSystem = AppSystem(a)
        r = appSystem.snapshotImmediatelyAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'snapshotImmediatelyAppContinuity', body)

    def testsnapshotDeleteAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }

        appSystem = AppSystem(a)
        r = appSystem.snapshotDeleteAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'snapshotDeleteAppContinuity', body)

    def testfailoverAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }

        appSystem = AppSystem(a)
        r = appSystem.failoverAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'failoverAppContinuity', body)

    def testfailbackAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }

        appSystem = AppSystem(a)
        r = appSystem.failbackAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'failbackAppContinuity', body)

    def testmodifyScriptAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }

        appSystem = AppSystem(a)
        r = appSystem.modifyScriptAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifyScriptAppContinuity', body)

    def testlistAppContinuityStatus(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }

        appSystem = AppSystem(a)
        r = appSystem.listAppContinuityStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listAppContinuityStatus', body)

    def testCreateFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 0,
            'vp_uuid': '',
            'auto': 0,
            'vm_list': [{
            'new_vm_name': '',
            'vm_ref': '',
            'cpu': 1,
            'ver_sig': '',
            'core_per_sock': 1,
            'mem_mb': 1024,
            'scripts': '',
            'bk_uuid': '',
            'bk_path': '',
            'time': '',
            'original_rule_uuid': '',
            'scripts_type': 0,
            'os_type': 1,
            'wk_uuid': '',
            'src_uuid': '',
            'data_ip_uuid': '',
            'bk_type': 0,
            'bucket_': '',
            'sto_uuid': '',
            'bucket_path': '',
            'disk_list': [{
            'datastore': '',
            'new_ds': '',
            'is_ignored': 1,
            'size': '',
            'boot_index': 1,
            'disk_dir': '',
            'disk_name': '',
            'id': '',},],
            'networks': [{
            'source_network_name': '',
            'source_network_id': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'ip_address': '',
            'subnet_name': '',
            'auto_ip': 1,
            'ip': '',
            'security_group_name': '',},],
            'new_flavor_id': '',
            'vm_name': '',},],
            'quick_back': 1,
            'backup_type': 'i',
            'lan_free': 23,
            'del_bkup_data': 0,
            'automate': 0,
            'auto_shutdown': 1,
            'bkup_policy': 1,
            'bkup_schedule': {
            'sched_time_start': '0',
            'limit': 0,
            'sched_day': 6,
            'sched_every': 0,
            'sched_time': [],
            'sched_gap_min': 0,},
            'new_network_id': '',
            'new_network_name': '',
            'datastore': '',
            'hostname': '',
            'datacenter': '',
            'create_vm_type': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.createFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createFirstReplica', body)

    def testListFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listFirstReplica', body)

    def testDescribeFirstReplica(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.describeFirstReplica(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeFirstReplica', body)

    def testModifyFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 0,
            'vp_uuid': '',
            'auto': 0,
            'vm_list': [{
            'new_vm_name': '',
            'vm_ref': '',
            'cpu': 1,
            'ver_sig': '',
            'core_per_sock': 1,
            'mem_mb': 1024,
            'scripts': '',
            'bk_uuid': '',
            'bk_path': '',
            'time': '',
            'original_rule_uuid': '',
            'scripts_type': 0,
            'os_type': 1,
            'wk_uuid': '',
            'src_uuid': '',
            'data_ip_uuid': '',
            'bk_type': 0,
            'bucket_': '',
            'sto_uuid': '',
            'bucket_path': '',
            'disk_list': [{
            'datastore': '',
            'new_ds': '',
            'is_ignored': 1,
            'size': '',
            'boot_index': 1,
            'disk_dir': '',
            'disk_name': '',
            'id': '',},],
            'networks': [{
            'source_network_name': '',
            'source_network_id': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'ip_address': '',
            'subnet_name': '',
            'auto_ip': 1,
            'ip': '',
            'security_group_name': '',},],
            'new_flavor_id': '',
            'vm_name': '',},],
            'quick_back': 1,
            'backup_type': 'i',
            'lan_free': 23,
            'del_bkup_data': 0,
            'automate': 0,
            'auto_shutdown': 1,
            'bkup_policy': 1,
            'bkup_schedule': {
            'sched_time_start': '0',
            'limit': 0,
            'sched_day': 6,
            'sched_every': 0,
            'sched_time': [],
            'sched_gap_min': 0,},
            'new_network_id': '',
            'new_network_name': '',
            'datastore': '',
            'hostname': '',
            'datacenter': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.modifyFirstReplica(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifyFirstReplica', body)

    def testListFirstReplicaStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': 1,
            'force_refresh': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listFirstReplicaStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listFirstReplicaStatus', body)

    def teststartVmFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.startVmFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'startVmFirstReplica', body)

    def teststopVmFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
        }

        appSystem = AppSystem(a)
        r = appSystem.stopVmFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'stopVmFirstReplica', body)

    def testDeleteFirstReplica(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': '',
            'group_uuids': '',
            'delete_tgtvm': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.deleteFirstReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteFirstReplica', body)

    def testCreateSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'fsp_type': 22,
            'wk_uuid': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            'timeout': 0,
            'wk_path': [],
            'bk_path': [],
            'resource_settings': {
            'tgt_uuid': '',
            'new_dc': '',
            'new_host': '',
            'new_ds': '',
            'new_dc_mor': '',
            'vm_list': [{
            'disk_list': [{
            'boot_index': '',
            'file_name': '',
            'new_ds': '',
            'size': '',
            'is_ignored': '',
            'disk_name': '',
            'disk_path': '',
            'id': '',
            'disk_provision_type': 1,},],
            'vm_name': '',
            'new_vm_name': '',
            'custom_config': 1,
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'dynamic_mem': '0',
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'auto_ip': '',
            'ip': '',
            'security_group_name': '',},],},],
            'create_vm_type': 1,},
            'fsp_name': '',
            'bk_data_type': 21,
            'wk_data_type': 0,
            'auto_register': 0,
            'node_name': '',},
        }
        
        appSystem = AppSystem(a)
        r = appSystem.createSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createSecondReplica', body)

    def testListSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listSecondReplica', body)

    def testDescribeSecondReplica(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.describeSecondReplica(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeSecondReplica', body)

    def testModifySecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
            'fsp_type': 22,
            'wk_uuid': '',
            'bk_uuid': '',
            'data_ip_uuid': '',
            'timeout': 0,
            'wk_path': [],
            'bk_path': [],
            'resource_settings': {
            'tgt_uuid': '',
            'new_dc': '',
            'new_host': '',
            'new_ds': '',
            'new_dc_mor': '',
            'vm_list': [{
            'disk_list': [{
            'boot_index': '',
            'file_name': '',
            'new_ds': '',
            'size': '',
            'is_ignored': '',
            'disk_name': '',
            'disk_path': '',
            'id': '',
            'disk_provision_type': 1,},],
            'vm_name': '',
            'new_vm_name': '',
            'custom_config': 1,
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',
            'dynamic_mem': '0',
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'auto_ip': '',
            'ip': '',
            'security_group_name': '',},],},],},
            'fsp_name': '',
            'bk_data_type': 21,
            'wk_data_type': 0,
            'auto_register': 0,
            'node_name': '',
            'node_lic_list': [],},
        }
        
        appSystem = AppSystem(a)
        r = appSystem.modifySecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifySecondReplica', body)

    def teststartVmSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'fsp_uuids': [],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.startVmSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'startVmSecondReplica', body)

    def teststopVmSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'fsp_uuids': [],
        }

        appSystem = AppSystem(a)
        r = appSystem.stopVmSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'stopVmSecondReplica', body)

    def teststopSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'fsp_uuids': [],
        }

        appSystem = AppSystem(a)
        r = appSystem.stopSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'stopSecondReplica', body)

    def teststartSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'fsp_uuids': [],
        }

        appSystem = AppSystem(a)
        r = appSystem.startSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'startSecondReplica', body)

    def testDeleteSecondReplica(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'del_policy': 1,
            'force': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.deleteSecondReplica(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteSecondReplica', body)

    def testCreateVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'wk_path': [],
            'bk_path': [],
            'auto_start': 1,
            'vp_uuid': '',
            'new_dc': '',
            'new_dc_mor': '',
            'new_host': '',
            'new_ds': '',
            'create_vm_type': 1,
            'vm_list': [{
            'vm_name': '',
            'cpu': 1,
            'core_per_sock': 1,
            'mem_mb': 1,
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'auto_ip': '',
            'ip': '',
            'security_group_name': '',
            'gateway': '',},],
            'dns': '',},],
            'vm_cnt': 1,
            'prefix': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.createVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'createVmCloneRule', body)

    def testListVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_field': '',
            'search_value': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listVmCloneRule', body)

    def testDescribeVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.describeVmCloneRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeVmCloneRule', body)

    def testDeleteVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': 1,
            'force': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.deleteVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'deleteVmCloneRule', body)

    def teststartVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'rules_uuid': 1,
            'operate': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.startVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'startVmCloneRule', body)

    def teststopVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'rules_uuid': 1,
            'operate': '',
        }

        appSystem = AppSystem(a)
        r = appSystem.stopVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'stopVmCloneRule', body)

    def testListVmCloneRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': 1,
            'force_refresh': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listVmCloneRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listVmCloneRuleStatus', body)

    def testListVmCloneVm(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listVmCloneVm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listVmCloneVm', body)

    def testModifyVmConfig(self):
        a = Auth(username, pwd)
        body = {
            'vm_name': '',
            'cpu': 1,
            'core_per_sock': 1,
            'mem_mb': 1,
            'dns': '',
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'auto_ip': '',
            'ip': '',
            'security_group_name': '',
            'gateway': '',},],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.modifyVmConfig(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'modifyVmConfig', body)

    def teststartVmVmCloneVm(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }
        
        appSystem = AppSystem(a)
        r = appSystem.startVmVmCloneVm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'startVmVmCloneVm', body)

    def teststopVmVmCloneVm(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': '',
        }

        appSystem = AppSystem(a)
        r = appSystem.stopVmVmCloneVm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'stopVmVmCloneVm', body)

    def testListVmCloneVmStatus(self):
        a = Auth(username, pwd)
        body = {
            'force_refresh': 1,
            'uuids': [
            'F0Bd1A0B-503F-D174-d298-eeF39aBAcfAe',
            'fFbfcBDC-fef1-38d8-0848-F5ECb2D34627',],
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listVmCloneVmStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listVmCloneVmStatus', body)

    def testDescribeVmCloneVm(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.describeVmCloneVm(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeVmCloneVm', body)

    def testListRuleVersion(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listRuleVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listRuleVersion', body)

    def testDescribeRuleVersionInfo(self):
        a = Auth(username, pwd)
        body = {
            'id': 1,
        }
        
        appSystem = AppSystem(a)
        r = appSystem.describeRuleVersionInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeRuleVersionInfo', body)

    def testListRecycleBin(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1
        }
        
        appSystem = AppSystem(a)
        r = appSystem.listRecycleBin(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'listRecycleBin', body)

    def testDescribeRecycleBin(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        appSystem = AppSystem(a)
        r = appSystem.describeRecycleBin(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppSystem', 'describeRecycleBin', body)


if __name__ == '__main__':
    unittest.main()
