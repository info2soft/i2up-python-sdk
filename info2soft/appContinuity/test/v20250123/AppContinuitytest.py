
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import AppContinuity
from info2soft.appContinuity.v20250123.AppContinuity import AppContinuity
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


class AppContinuityTestCase(unittest.TestCase):

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
            'keep_mac': '',
            'gateway': '',
            'is_defroute': False,},],
            'orch_cpu_num': '',
            'orch_cores_per_cpu_num': '',
            'orch_memory_mb': '',},],
            'create_vm_type': 1,
            'hostname': '',},
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
            'auto_ip': False,
            'ip': '',
            'security_group_name': '',
            'gateway': '',
            'is_defroute': False,},],
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',},
            'oph_path': '',
            'oph_policy': 1,
            'thread_num': 1,
            'is_continue_policy': 1,
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.createAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'createAppContinuity', body)

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
            'keep_mac': '',
            'gateway': '',
            'is_defroute': False,},],
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
            'auto_ip': False,
            'ip': '',
            'security_group_name': '',
            'gateway': '',
            'is_defroute': False,},],
            'cpu': '',
            'core_per_sock': '',
            'mem_mb': '',},
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appContinuity = AppContinuity(a)
        r = appContinuity.modifyAppContinuity(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'modifyAppContinuity', body)

    def testDeleteAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'force': 1,
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.deleteAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'deleteAppContinuity', body)

    def testDescribeAppContinuity(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appContinuity = AppContinuity(a)
        r = appContinuity.describeAppContinuity(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'describeAppContinuity', body)

    def testListAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.listAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'listAppContinuity', body)

    def testStartAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
            'snap_name': '',
            'snap_point': '',
            'failover_script_uuid': '',
            'failback_script_uuid': '',
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.startAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'startAppContinuity', body)

    def testStopAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
            'snap_name': '',
            'snap_point': '',
            'failover_script_uuid': '',
            'failback_script_uuid': '',
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.stopAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'stopAppContinuity', body)

    def testMmediatelyAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
            'snap_name': '',
            'snap_point': '',
            'failover_script_uuid': '',
            'failback_script_uuid': '',
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.mmediatelyAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'mmediatelyAppContinuity', body)

    def testEleteAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
            'snap_name': '',
            'snap_point': '',
            'failover_script_uuid': '',
            'failback_script_uuid': '',
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.eleteAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'eleteAppContinuity', body)

    def testFailoverAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
            'snap_name': '',
            'snap_point': '',
            'failover_script_uuid': '',
            'failback_script_uuid': '',
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.failoverAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'failoverAppContinuity', body)

    def testFailbackAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
            'snap_name': '',
            'snap_point': '',
            'failover_script_uuid': '',
            'failback_script_uuid': '',
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.failbackAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'failbackAppContinuity', body)

    def testCriptAppContinuity(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'operate': '',
            'snap_name': '',
            'snap_point': '',
            'failover_script_uuid': '',
            'failback_script_uuid': '',
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.criptAppContinuity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'criptAppContinuity', body)

    def testListAppContinuityStatus(self):
        a = Auth(username, pwd)
        body = {
            'rep_uuids': [],
            'force_refresh': 0,
        }
        
        
        appContinuity = AppContinuity(a)
        r = appContinuity.listAppContinuityStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppContinuity', 'listAppContinuityStatus', body)


if __name__ == '__main__':
    unittest.main()
