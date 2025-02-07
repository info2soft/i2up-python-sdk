
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import AppHighAvailability
from info2soft.ha.v20250123.AppHighAvailability import AppHighAvailability
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


class AppHighAvailabilityTestCase(unittest.TestCase):

    def testListNicInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': [
            'B8566905-411E-B2CD-A742-77B1346D8E84',
            '67E33CDB-D75B-15B3-367D-50C764F5A26F',],
            'master_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.listNicInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'listNicInfo', body)

    def testDescribeHAScriptPath(self):
        a = Auth(username, pwd)
        body = {
            'master_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.describeHAScriptPath(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'describeHAScriptPath', body)

    def testDescribeVolumeInfo(self):
        a = Auth(username, pwd)
        body = {
            'master_uuid': '',
            'slave_uuid': '',
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.describeVolumeInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'describeVolumeInfo', body)

    def testHaVerifyName(self):
        a = Auth(username, pwd)
        body = {
            'ha_name': 'testfdsa',
            'ha_type': '0',
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.haVerifyName(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'haVerifyName', body)

    def testCreateHA(self):
        a = Auth(username, pwd)
        body = {
            'heartbeat': [{
            'interval': 2,
            'maxfail': 5,
            'protocol': 'tcp',
            'ifconfig': [{
            'uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'netif': '{AB1E4EFF-14FE-441E-8A1F-EE59BDA12D6F}',
            'ip': '192.168.72.75',
            'label': '',},{
            'uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'netif': '{5C3A44A0-EF11-4705-A9A3-2F3ACEED4798}',
            'ip': '192.168.72.82',
            'label': '',},],
            'port': 26850,},],
            'sync_data': [{
            'back_rule': 0,
            'need_rep_status': 1,
            'create_start': 0,
            'wait_cache': 1,
            'rule_relation': [{
            'rep_name': 'sdk_ha-N3_72.75-N4_72.76',
            'autostart_rep': 0,
            'path': [
            'E:\\test\\',],
            'uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'append_name': 0,},{
            'rep_name': 'sdk_ha-N3_72.75-N4_72.76',
            'autostart_rep': 0,
            'path': [
            'E:\\test\\',],
            'uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'append_name': 0,},],
            'excludes': [],},],
            'arbitration': {
            'radio': 1,
            'node': [{
            'arbit_protocol': 'TCP',
            'arbit_addr': '192.168.72.82',
            'arbit_port': 26868,},],
            'disk': {
            'path': '',},},
            'master_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'ha_name': 'sdk_ha',
            'res_switch': [{
            'script': {
            'after_failover_arr': [{
            'node_uuid': '',
            'script_uuid': '',},],
            'before_failover': '',
            'before_switch_arr': [{
            'node_uuid': '',
            'script_uuid': '',},],
            'after_switch': '',
            'switch_timeout': '',
            'after_failover': '',
            'before_switch': '',},
            'vip': {
            'top': 0,
            'ip': '192.168.72.82',
            'ifconfig': [{
            'uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'netif': '{AB1E4EFF-14FE-441E-8A1F-EE59BDA12D6F}',
            'label': 'Ethernet0',},{
            'uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'netif': '{5C3A44A0-EF11-4705-A9A3-2F3ACEED4798}',
            'label': 'Ethernet0',},],
            'mask': '255.255.255.0',
            'del': 0,
            'seq_execute': 1,
            'try_number': 1,},
            'type': 'ip',
            'disk': {
            'mnt_name': '',
            'try_time': '',
            'disk_info': {
            'master_node': {
            'mnt_name': '',
            'disk_name': '',
            'label': '',
            'flags': '',},
            'sub_node': {
            'mnt_name': '',
            'disk_name': '',
            'label': '',
            'flags': '',},
            'size': '',
            'uuid': '',
            'fs_type': '',
            'offset': '',
            'os_type': '',
            'disk_id': '',},},
            'virtualdisk': {
            'vp_type': '',
            'sub_node_uuid': '',
            'master_node_uuid': '',
            'disk_info': [{
            'is_switch': '',
            'vir_uuid': '',
            'mount_point': '',
            'part_list': {
            'uuid': '',
            'is_mount': '',},},],
            'vp_uuid': '',},},],
            'switch_type': 1,
            'monitor': [{
            'threshold': 90,
            'interval': 2,
            'name': '',
            'script': '',
            'access_method': '',
            'type': 'cpu',
            'great': '',
            'useid': '',
            'maxfail': 5,
            'action': 'warn',
            'residual': 1,
            'role': 'master',
            'path': '',
            'monitor_file': '',},],
            'node_priority': [{
            'uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'priority': 'high',},{
            'uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'priority': 'high',},],
            'ctrl_switch': 0,
            'dynamic_node': '',
            'cluster_id': '',
            'service_label': 1,
            'key_file_path': [],
            'switch_sync_data': 1,
            'cron_expression': '',
            'local_takeover': '',
            'force_switch_center': '',
            'reboot_takeover': 0,
            'ha_type': 1,
            'band_width': '',
            'sys_uuid': '',
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.createHA(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'createHA', body)

    def testModifyHA(self):
        a = Auth(username, pwd)
        body = {
            'sync_data': {
            'create_start': 1,
            'rule_relation': [{
            'rep_name': '',
            'path': [],
            'append_name': 1,
            'autostart_rep': 1,
            'uuid': '',},{
            'rep_name': '',
            'path': [],
            'append_name': 1,
            'autostart_rep': 1,
            'uuid': '',},],
            'wait_cache': 1,
            'need_rep_status': 1,
            'back_rule': 1,
            'excludes': [],},
            'monitor': [{
            'great': '',
            'interval': 1,
            'type': '',
            'useid': '',
            'script': '',
            'residual': 1,
            'threshold': 1,
            'action': '',
            'role': '',
            'monitor_file': '',
            'path': '',
            'name': '',
            'access_method': '',
            'maxfail': 1,},],
            'ha_name': '',
            'heartbeat': [{
            'interval': 1,
            'maxfail': 1,
            'port': 1,
            'ifconfig': [{
            'uuid': '',
            'netif': 1,
            'ip': '',
            'label': '',},{
            'uuid': '',
            'netif': 1,
            'ip': '',
            'label': '',},],
            'protocol': '',},],
            'node_priority': [{
            'uuid': '',
            'priority': '',},],
            'master_uuid': '',
            'arbitration': {
            'node': {
            'arbit_port': 1,
            'arbit_addr': '',
            'arbit_protocol': '',},
            'disk': {},
            'radio': 1,},
            'res_switch': [{
            'type': '',
            'script': {
            'before_failover': '',
            'after_failover': '',
            'before_switch': '',
            'after_switch': '',
            'switch_timeout': '20',},
            'vip': {
            'mask': '',
            'ip': '',
            'ifconfig': [{
            'uuid': '',
            'label': '',
            'netif': '',},{
            'uuid': '',
            'label': '',
            'netif': '',},],
            'top': 1,
            'del': 1,},},],
            'auto_switch': 1,
            'ha_uuid': '',
            'reboot_takeover': 0,
            'sys_uuid': '',
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.modifyHA(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'modifyHA', body)

    def testDescribeHA(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.describeHA(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'describeHA', body)

    def testListHA(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'search_value': '',
            'page': 1,
            'limit': 10,
            'type': False,
            'status': '',
            'where_args': {
            'take_over_status': 1,},
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.listHA(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'listHA', body)

    def testListHAStatus(self):
        a = Auth(username, pwd)
        body = {
            'ha_uuid': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.listHAStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'listHAStatus', body)

    def testStartHA(self):
        a = Auth(username, pwd)
        body = {
            'ha_uuid': [],
            'node_uuid': '',
            'type': '',
            'ha_name': '',
            'force': 0,
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.startHA(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'startHA', body)

    def testStopHA(self):
        a = Auth(username, pwd)
        body = {
            'ha_uuid': [],
            'node_uuid': '',
            'type': '',
            'ha_name': '',
            'force': 0,
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.stopHA(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'stopHA', body)

    def testForceSwitchHA(self):
        a = Auth(username, pwd)
        body = {
            'ha_uuid': [],
            'node_uuid': '',
            'type': '',
            'ha_name': '',
            'force': 0,
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.forceSwitchHA(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'forceSwitchHA', body)

    def testDeleteHA(self):
        a = Auth(username, pwd)
        body = {
            'uuid': [
            '11111111-1111-1111-1111-111111111111',],
            'force': 1,
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.deleteHA(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'deleteHA', body)

    def testListStageOptions(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.listStageOptions(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'listStageOptions', body)

    def testCreateHAGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_name': '111',
            'error_confirm': 1,
            'switch_confirm': 1,
            'ha_rules': [
            'B95DB026-AEDF-737A-0442-B5134660D204',
            '128C2F7D-0795-41F3-1274-3FBAA2449BAD',
            '214E0B0C-6BFA-B1D7-1AFC-C11E3B5874C0',
            '2FD74EEE-CFDB-FB01-8E11-B6560B6D20F8',],
            'stage': {
            'step_1': {
            'ha_rule': [
            'B95DB026-AEDF-737A-0442-B5134660D204',
            '128C2F7D-0795-41F3-1274-3FBAA2449BAD',],
            'failover_serial': 1,
            'failback_serial': -1,
            'haList': [{
            'ha_name': 'tst',
            'ha_uuid': 'B95DB026-AEDF-737A-0442-B5134660D204',},{
            'ha_name': 'test4',
            'ha_uuid': '128C2F7D-0795-41F3-1274-3FBAA2449BAD',},],},
            'step_2': {
            'ha_rule': [
            '214E0B0C-6BFA-B1D7-1AFC-C11E3B5874C0',
            '2FD74EEE-CFDB-FB01-8E11-B6560B6D20F8',],
            'failover_serial': 2,
            'failback_serial': -2,
            'haList': [{
            'ha_name': 'test3',
            'ha_uuid': '214E0B0C-6BFA-B1D7-1AFC-C11E3B5874C0',
            'disabled': True,},{
            'ha_name': 'test2',
            'ha_uuid': '2FD74EEE-CFDB-FB01-8E11-B6560B6D20F8',
            'disabled': True,},],},},
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.createHAGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'createHAGroup', body)

    def testListHAGroup(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_field': 'group_name',
            'search_value': '',
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.listHAGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'listHAGroup', body)

    def testDeleteHAGroup(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'CFCEDC75-F48E-22B0-8A67-DE1FCA51C4C7',],
        }
        
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.deleteHAGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'deleteHAGroup', body)

    def testModifyHAGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': 'CFCEDC75-F48E-22B0-8A67-DE1FCA51C4C7',
            'group_name': '111',
            'error_confirm': 1,
            'switch_confirm': 1,
            'ha_rules': [
            'B95DB026-AEDF-737A-0442-B5134660D204',
            '128C2F7D-0795-41F3-1274-3FBAA2449BAD',],
            'stage': {
            'step_1': {
            'ha_rule': [
            'B95DB026-AEDF-737A-0442-B5134660D204',
            '128C2F7D-0795-41F3-1274-3FBAA2449BAD',],
            'failover_serial': 1,
            'failback_serial': -1,
            'haList': [{
            'ha_name': 'tst',
            'ha_uuid': 'B95DB026-AEDF-737A-0442-B5134660D204',},{
            'ha_name': 'test4',
            'ha_uuid': '128C2F7D-0795-41F3-1274-3FBAA2449BAD',},],},},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.modifyHAGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'modifyHAGroup', body)

    def testDescribeHAGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.describeHAGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'describeHAGroup', body)

    def testForceSwitchHAGroup(self):
        a = Auth(username, pwd)
        body = {
            'ha_uuids': [
            'B95DB026-AEDF-737A-0442-B5134660D204',
            '128C2F7D-0795-41F3-1274-3FBAA2449BAD',],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.forceSwitchHAGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'forceSwitchHAGroup', body)

    def testListHASwitchTaskStatus(self):
        a = Auth(username, pwd)
        body = {
            'task_uuid': 'F696DC12-6727-B799-93D4-8B2213086F5A',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.listHASwitchTaskStatus(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'listHASwitchTaskStatus', body)

    def testResumeHAGroupSwitch(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'resume',
            'task_uuid': 'F696DC12-6727-B799-93D4-8B2213086F5A',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.resumeHAGroupSwitch(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'resumeHAGroupSwitch', body)

    def testPauseHAGroupSwitch(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'resume',
            'task_uuid': 'F696DC12-6727-B799-93D4-8B2213086F5A',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        appHighAvailability = AppHighAvailability(a)
        r = appHighAvailability.pauseHAGroupSwitch(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'AppHighAvailability', 'pauseHAGroupSwitch', body)


if __name__ == '__main__':
    unittest.main()
