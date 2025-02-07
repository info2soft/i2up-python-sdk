
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import CloudBackup
from info2soft.cloud.v20250123.CloudBackup import CloudBackup
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


class CloudBackupTestCase(unittest.TestCase):

    def testListDevice(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.listDevice(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listDevice', body)

    def testListIdleDevice(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.listIdleDevice(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listIdleDevice', body)

    def testCreateBackup(self):
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
            'failover': '0',
            'wk_path': [
            '/',],
            'fsp_name': 'test',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
            'fsp_wk_shut_flag': '2',
            'bk_data_type': 1,
            'bkup_schedule': [{
            'sched_day': 9,
            'sched_time': '16:48',
            'sched_every': 2,
            'limit': 6,
            'backup_type': 0,
            'policys': '"每天22:00自动执行"',
            'backup_type_show': '"全备"',
            'running_time': '"22:00"',},],
            'fsp_type': 6,
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
            'data_ip_uuid': '',
            'database_switch': 1,
            'database_type': 1,
            'oracle_dbagent_param': {
            'oracle_sid': '',
            'sql_plus_path': '',
            'username': '',
            'password': '',
            'port': '',
            'table_space': '',
            'timeout': '',},
            'sqlserver_dbagent_param': {
            'timeout': '',
            'enable': '0',},
            'custom_dbagent_param': {
            'pre_snapshot_script': '',
            'post_snapshot_script': '',},
            'bk_volume': [],
            'disk_billing_type': 1,
            'order_cycle_unit': 1,
            'order_cycle': 1,
            'disk_type': '',},
        }
        
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.createBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createBackup', body)

    def testModifyBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.modifyBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'modifyBackup', body)

    def testDeleteCloudBackup(self):
        a = Auth(username, pwd)
        body = {
            'force': 1,
            'rule_uuids': [],
        }
        
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.deleteCloudBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'deleteCloudBackup', body)

    def testListBackup(self):
        a = Auth(username, pwd)
        body = {
            'status': '',
        }
        
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.listBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listBackup', body)

    def testStartBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bkup_type': '',
            'stop_later': '',
        }
        
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.startBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'startBackup', body)

    def testStopBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bkup_type': '',
            'stop_later': '',
        }
        
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.stopBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'stopBackup', body)

    def testStartImmediatelyBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'bkup_type': '',
            'stop_later': '',
        }
        
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.startImmediatelyBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'startImmediatelyBackup', body)

    def testDescribeBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.describeBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'describeBackup', body)

    def testVerifySourceVirtioDriver(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
        }
        
        
        cloudBackup = CloudBackup(a)
        r = cloudBackup.verifySourceVirtioDriver(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'verifySourceVirtioDriver', body)


if __name__ == '__main__':
    unittest.main()
