# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.fsp.v20240228.FspBackup import FspBackup
# from info2soft.fsp.v20200722.FspBackup import FspBackup
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


class FspBackupTestCase(unittest.TestCase):

    def testListFspMoveNic(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspMoveNic(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspMoveNic', body)

    def testListFspMoveDir(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuid': '',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspMoveDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspMoveDir', body)

    def testVerifyFspMoveVolumeSpace(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'sync_item': '/',
            'wk_device_list': [{
                'name': '', }, ],
            'bk_device_list': [{
                'name': '', }, ],
            'is_block_move': 0,
            'pool_uuid': '',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspMoveVolumeSpace(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspMoveVolumeSpace', body)

    def testVerifyFspMoveLicense(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspMoveLicense(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspMoveLicense', body)

    def testVerifyFspMoveOldRule(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspMoveOldRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspMoveOldRule', body)

    def testVerifyFspMoveOsVersion(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
            'mode': 1,
        }

        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspMoveOsVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspMoveOsVersion', body)

    def testVerifyFspMoveEnvironment(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
            'bk_uuid': '',
            'wk_path': [{
                '': '', }, ],
            'bk_path': [{
                '': '', }, ],
        }

        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspMoveEnvironment(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspMoveEnvironment', body)

    def testListFspMoveDriverInfo(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspMoveDriverInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspMoveDriverInfo', body)

    def testCreateFspMove(self):
        a = Auth(username, pwd)
        body = {
            'fsp_move': {
                'fsp_name': 'testMove',
                'service_uuid': '',
                'monitor_type': 0,
                'bk_path': [
                    '/I2FFO/bin/',
                    '/I2FFO/boot/',
                    '/I2FFO/etc/',
                    '/I2FFO/lib/',
                    '/I2FFO/lib64/',
                    '/I2FFO/root/',
                    '/I2FFO/sbin/',
                    '/I2FFO/usr/bin/',
                    '/I2FFO/usr/lib/',
                    '/I2FFO/usr/lib64/',
                    '/I2FFO/usr/libexec/',
                    '/I2FFO/usr/local/',
                    '/I2FFO/usr/sbin/',
                    '/I2FFO/var/lib/nfs/', ],
                'compress': '0',
                'net_mapping': [{
                    'bk_nic': {
                        'name': 'Ethernet0',
                        'type': '0',
                        'ip': '192.168.72.74/255.255.240.0', },
                    'wk_nic': {
                        'name': 'Ethernet0',
                        'type': '0',
                        'ip': '192.168.72.73/255.255.240.0', }, }, ],
                'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
                'encrypt_switch': '0',
                'mirr_open_type': '0',
                'sync_item': '/',
                'mirr_sync_flag': '0',
                'net_mapping_type': '2',
                'mirr_sync_attr': '1',
                'band_width': '',
                'excl_path': [
                    '/etc/X11/xorg.conf/',
                    '/etc/init.d/i2node/',
                    '/etc/rc.d/init.d/i2node/',
                    '/etc/sdata/', ],
                'fsp_wk_shut_flag': '2',
                'secret_key': '',
                'wk_path': [
                    '/bin/',
                    '/boot/',
                    '/etc/',
                    '/lib/',
                    '/lib64/',
                    '/root/',
                    '/sbin/',
                    '/usr/bin/',
                    '/usr/lib/',
                    '/usr/lib64/',
                    '/usr/libexec/',
                    '/usr/local/',
                    '/usr/sbin/',
                    '/var/lib/nfs/', ],
                'mirr_file_check': '0',
                'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
                'failover': '0',
                'random_str': '11111111-1111-1111-1111-111111111111',
                'excl_driver': [
                    'inf1',
                    'inf2', ],
                'data_ip_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
                'wk_data_type': 1,
                'bk_file_crypt': 0,
                'encrypt': 0,
                'thread_num': 1,
                'fsp_type': 1,
                'auto_start': 1,
                'bkup_one_time': 1,
                'backup_type': '',
                'keep_hostname': 1, },
        }

        fspBackup = FspBackup(a)
        r = fspBackup.createFspMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'createFspMove', body)

    def testDescribeFspMove(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        fspBackup = FspBackup(a)
        r = fspBackup.describeFspMove(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'describeFspMove', body)

    def testModifyFspMove(self):
        a = Auth(username, pwd)
        body = {
            'fsp_move': {
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
                    '/var/run/vmblock-fuse/', ],
                'random_str': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
                'fsp_wk_shut_flag': '2',
                'monitor_type': 0,
                'mirr_sync_attr': '1',
                'net_mapping_type': '2',
                'mirr_sync_flag': '0',
                'mirr_file_check': '0',
                'sync_item': '/',
                'secret_key': '',
                'failover': '0',
                'fsp_name': 'changeName',
                'mirr_open_type': '0',
                'bk_uuid': 'C11FE572-5207-3359-DB85-001E95F5F185',
                'bk_path': [
                    '/',
                    '/I2FFO/bin/',
                    '/I2FFO/boot/',
                    '/I2FFO/etc/',
                    '/I2FFO/lib/',
                    '/I2FFO/lib64/',
                    '/I2FFO/root/',
                    '/I2FFO/sbin/',
                    '/I2FFO/usr/bin/',
                    '/I2FFO/usr/lib/',
                    '/I2FFO/usr/lib64/',
                    '/I2FFO/usr/libexec/',
                    '/I2FFO/usr/local/',
                    '/I2FFO/usr/sbin/',
                    '/I2FFO/var/lib/nfs/', ],
                'net_mapping': [{
                    'wk_nic': {
                        'ip': '192.168.72.73/255.255.240.0',
                        'type': '0',
                        'name': 'Ethernet0', },
                    'bk_nic': {
                        'type': '0',
                        'name': 'Ethernet0',
                        'ip': '192.168.72.74/255.255.240.0', }, }, ],
                'service_uuid': '',
                'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
                'compress': '0',
                'encrypt_switch': '0',
                'move_type': '0',
                'wk_path': [
                    '/',
                    '/bin/',
                    '/boot/',
                    '/etc/',
                    '/lib/',
                    '/lib64/',
                    '/root/',
                    '/sbin/',
                    '/usr/bin/',
                    '/usr/lib/',
                    '/usr/lib64/',
                    '/usr/libexec/',
                    '/usr/local/',
                    '/usr/sbin/',
                    '/var/lib/nfs/', ],
                'band_width': '3*03:00-14:00*2m',
                'excl_driver': [
                    'inf1',
                    'inf2', ],
                'data_ip_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
                'thread_num': 1, },
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        fspBackup = FspBackup(a)
        r = fspBackup.modifyFspMove(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'modifyFspMove', body)

    def testDeleteFspMove(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'force': 1,
        }

        fspBackup = FspBackup(a)
        r = fspBackup.deleteFspMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'deleteFspMove', body)

    def testListFspMove(self):
        a = Auth(username, pwd)
        body = {
            'search_field': '',
            'limit': 10,
            'page': 1,
            'search_value': '',
            'status': '',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspMove', body)

    def testStartFspMove(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'fsp_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'bk_type': '',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.startFspMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'startFspMove', body)

    def testListFspMoveStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'force_refresh': 1,
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspMoveStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspMoveStatus', body)

    def testBatchCreateFspMove(self):
        a = Auth(username, pwd)
        body = {
            'base_info_list': {
                'service_uuid': '',
                'monitor_type': 0,
                'compress': 0,
                'net_mapping': [{
                    'bk_nic': {
                        'name': 'Ethernet0',
                        'type': '0',
                        'ip': '192.168.72.74/255.255.240.0', },
                    'wk_nic': {
                        'name': 'Ethernet0',
                        'type': '0',
                        'ip': '192.168.72.73/255.255.240.0', }, }, ],
                'encrypt_switch': 0,
                'mirr_open_type': '0',
                'mirr_sync_flag': '0',
                'net_mapping_type': '2',
                'mirr_sync_attr': '1',
                'band_width': '',
                'fsp_wk_shut_flag': 2,
                'secret_key': '',
                'mirr_file_check': '0',
                'failover': 0,
                'excl_driver': [
                    'inf1',
                    'inf2', ],
                'compress_switch': 1,
                'encrypt': 1,
                'wk_data_type': 1,
                'auto_start': 1,
                'bkup_one_time': 1,
                'backup_type': '', },
            'common_params': {
                'batch_name': '',
                'rep_prefix': '',
                'rep_sufix': '',
                'variable_type': 0, },
            'node_list': [{
                'bk_uuid': '',
                'excl_path': [],
                'bk_path': [],
                'wk_uuid': '',
                'wk_path': [],
                'proxy_uuid': '',
                'data_ip_uuid': '',
                'sync_item': '/', }, ],
        }

        fspBackup = FspBackup(a)
        r = fspBackup.batchCreateFspMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'batchCreateFspMove', body)

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
                'fsp_bk', ],
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
                '/var/run/vmblock-fuse/', ],
            'wk_path': [
                '/', ],
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
                '/fsp_bk/', ],
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
                'bkup_one_time': 0,
                'encrypt_switch': '0',
                'mirr_sync_attr': '1',
                'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
                'wk_data_type': 1,
                'bk_path': [
                    '/fsp_bk/', ],
                'sync_item': '/',
                'bkup_policy': 2,
                'mirr_file_check': '0',
                'compress': '0',
                'monitor_type': 0,
                'failover': 0,
                'fsp_name': 'test',
                'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
                'fsp_wk_shut_flag': '2',
                'bk_data_type': 1,
                'fsp_type': 3,
                'random_str': '11111111-1111-1111-1111-111111111111',
                'del_policy': 1,
                'timeout': 1,
                'cbt_switch': 1,
                'threshold_vaild_byte': '',
                'storage_uuid': '',
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
                            'auto_ip': '', }, ],
                        'disk_list': [{
                            'is_ignored': '',
                            'disk_name': '',
                            'disk_path': '',
                            'new_ds': '',
                            'id': '',
                            'boot_index': '',
                            'file_name': '',
                            'size': '', }, ],
                        'dynamic_mem': '', }, ],
                    'network_id': '',
                    'bk_uuid': '',
                    'bk_path': [], },
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
                'bk_storage': 1,
                'pool_uuid': '', },
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
                    'cdp_param': '', },
                'data_ip_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
                'thread_num': 1, },
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
                '11111111-1111-1111-1111-111111111111', ],
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
                '11111111-1111-1111-1111-111111111111', ],
            'bk_type': '',
            'continue_last_backup': 0,
            'stop_later': '',
            'op_code': '',
            'snap_point': '',
            'power_on': 1,
        }

        fspBackup = FspBackup(a)
        r = fspBackup.startFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'startFspBackup', body)

    def testListFspBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
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
                    'cdp_switch': 1, },
                'tgt_uuid': '',
                'new_dc': '',
                'new_dc_mor': '',
                'new_host': '',
                'new_ds': '',
                'network_name': '',
                'network_id': '', },
            'common_params': {
                'batch_name': '',
                'rep_prefix': '',
                'rep_sufix': '',
                'variable_type': 1, },
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
                'os_type': 1, }, ],
        }

        fspBackup = FspBackup(a)
        r = fspBackup.batchCreateFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'batchCreateFspBackup', body)

    def testListFspRecoveryNic(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'dst_path': '/fsp_bk/192.168.71.77_26821/20190111113656/',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspRecoveryNic(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspRecoveryNic', body)

    def testListFspRecoveryDir(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'dst_path': '/fsp_bk/192.168.71.77_26821/20190111113656/',
            'fsp_uuid': '',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspRecoveryDir(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspRecoveryDir', body)

    def testListFspRecoveryPoint(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'rc_data_path': '/fsp_bk/192.168.71.77_26821/',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspRecoveryPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspRecoveryPoint', body)

    def testVerifyFspRecoveryVolumeSpace(self):
        a = Auth(username, pwd)
        body = {
            'sync_item': '/',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
            'dst_path': '/fsp_bk/192.168.71.77_26821/20190111113656/',
            'device_list': [{
                'name': '', }, ],
            'vmdk_list': [{
                'name': '', }, ],
            'fsp_type': '',
            'path': '',
            'type': '',
            'suffix': '',
            'restore_point': '',
            'vp_uuid': '',
            'vm_ref': '',
            'by_type': 0,
        }

        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspRecoveryVolumeSpace(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspRecoveryVolumeSpace', body)

    def testVerifyFspRecoveryLicense(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspRecoveryLicense(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspRecoveryLicense', body)

    def testVerifyFspRecoveryOldRule(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspRecoveryOldRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspRecoveryOldRule', body)

    def testVerifyFspRecoveryOsVersion(self):
        a = Auth(username, pwd)
        body = {
            'dst_path': '/fsp_bk/192.168.71.77_26821/20190111113656/',
            'wk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'bk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspRecoveryOsVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspRecoveryOsVersion', body)

    def testCreateFspRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_recovery': {
                'dst_path': '/fsp_bk/192.168.71.77_26821/20190111113656/',
                'encrypt_switch': '0',
                'net_mapping': [{
                    'bk_nic': {
                        'type': '0',
                        'name': 'Ethernet0',
                        'ip': '192.168.72.74/255.255.240.0', },
                    'wk_nic': {
                        'name': 'Ethernet0',
                        'type': '0',
                        'ip': '192.168.72.73/255.255.240.0', }, }, ],
                'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
                'mirr_sync_attr': '1',
                'secret_key': '',
                'bk_path': [
                    '/fsp_bk/192.168.71.77_26821/20190111113656/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/bin/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/boot/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/etc/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/lib/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/lib64/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/root/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/sbin/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/usr/bin/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/usr/lib/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/usr/lib64/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/usr/libexec/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/usr/local/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/usr/sbin/',
                    '/fsp_bk/192.168.71.77_26821/20190111113656/var/lib/nfs/', ],
                'band_width': '',
                'fsp_name': 'testRC',
                'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
                'net_mapping_type': '2',
                'mirr_open_type': '0',
                'restore_point': '20190111113656',
                'mirr_file_check': '0',
                'compress': '0',
                'service_uuid': '',
                'excl_path': [],
                'wk_path': [
                    '/',
                    '/I2FFO/bin/',
                    '/I2FFO/boot/',
                    '/I2FFO/etc/',
                    '/I2FFO/lib/',
                    '/I2FFO/lib64/',
                    '/I2FFO/root/',
                    '/I2FFO/sbin/',
                    '/I2FFO/usr/bin/',
                    '/I2FFO/usr/lib/',
                    '/I2FFO/usr/lib64/',
                    '/I2FFO/usr/libexec/',
                    '/I2FFO/usr/local/',
                    '/I2FFO/usr/sbin/',
                    '/I2FFO/var/lib/nfs/', ],
                'mirr_sync_flag': '0',
                'fsp_wk_shut_flag': '2',
                'sync_item': '/',
                'failover': '0',
                'fsp_type': '5',
                'random_str': '11111111-1111-1111-1111-111111111111',
                'data_ip_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
                'by_type': '',
                'bk_file_crypt': 1,
                'encrypt': 1,
                'thread_num': 1,
                'excl_driver': [
                    'inf1',
                    'inf2', ],
                'monitor_type': 1,
                'driver_url': '',
                'rc_method': '',
                'backup_task_uuid': '', },
        }

        fspBackup = FspBackup(a)
        r = fspBackup.createFspRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'createFspRecovery', body)

    def testModifyFspRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_recovery': {
                'restore_point': '20180724164452',
                'fsp_wk_shut_flag': '2',
                'excl_path': [],
                'secret_key': '',
                'band_width': '3*03:00-14:00*2m',
                'compress': '0',
                'wk_path': [],
                'net_mapping': [{
                    'wk_nic': {
                        'ip': '192.168.72.73/255.255.240.0',
                        'type': '0',
                        'name': 'Ethernet0', },
                    'bk_nic': {
                        'type': '0',
                        'ip': '192.168.72.74/255.255.240.0',
                        'name': 'Ethernet0', }, }, ],
                'service_uuid': '',
                'wk_uuid': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
                'net_mapping_type': '2',
                'bk_path': [],
                'fsp_name': 'rrrrr',
                'mirr_sync_flag': '0',
                'mirr_file_check': '0',
                'monitor_type': 0,
                'sync_item': 'C:',
                'mirr_sync_attr': '1',
                'random_str': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
                'dst_path': '???',
                'encrypt_switch': '0',
                'bk_uuid': '0DD4E727-70AB-62C6-BEB5-D012DFAE46E3',
                'mirr_open_type': '0',
                'failover': '0',
                'fsp_type': '',
                'data_ip_uuid': '',
                'thread_num': 1, },
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        fspBackup = FspBackup(a)
        r = fspBackup.modifyFspRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'modifyFspRecovery', body)

    def testDesribeFspRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        fspBackup = FspBackup(a)
        r = fspBackup.desribeFspRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'desribeFspRecovery', body)

    def testDeleteFspRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'force': 1,
        }

        fspBackup = FspBackup(a)
        r = fspBackup.deleteFspRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'deleteFspRecovery', body)

    def testListFspRecovery(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'page': 1,
            'limit': 10,
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspRecovery', body)

    def testStartFspRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'operate': 'start',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.startFspRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'startFspRecovery', body)

    def testListFspRecoveryDriverListUrl(self):
        a = Auth(username, pwd)
        body = {
        }

        fspBackup = FspBackup(a)
        r = fspBackup.listFspRecoveryDriverListUrl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspRecoveryDriverListUrl', body)

    def testGetFspMoveBiosType(self):
        a = Auth(username, pwd)
        body = {
            'device_list': [],
            'node_uuid': '',
        }

        fspBackup = FspBackup(a)
        r = fspBackup.getFspMoveBiosType(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'getFspMoveBiosType', body)


if __name__ == '__main__':
    unittest.main()
