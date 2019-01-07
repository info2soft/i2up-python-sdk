# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.fsp.v20181227.FspBackup import FspBackup
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

    def testListFspBackupNic(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
            'bk_uuid': 'C11FE572-5207-3359-DB85-001E95F5F185',
        }
        fspBackup = FspBackup(a)
        r = fspBackup.listFspBackupNic(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspBackupNic', body)

    def testListFspBackupDir(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
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
            'bk_path': ['/FSPback0107/', ],
            'bk_uuid': 'C11FE572-5207-3359-DB85-001E95F5F185',
            'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
            'excl_path': ["/cgroup/", "/dev/", "/etc/X11/xorg.conf/", "/etc/init.d/i2node/", "/etc/rc.d/init.d/i2node/",
                          "/etc/sdata/", "/lost+found/", "/media/", "/mnt/", "/proc/", "/run/", "/selinux/", "/sys/",
                          "/tmp/", "/usr/local/sdata/", "/var/i2/", "/var/i2data/", "/var/lock/",
                          "/var/run/vmblock-fuse/"],
            'wk_path': ['/', '/boot/', ]
        }
        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspBackupCoopySpace(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspBackupCoopySpace', body)

    def testVerifyFspBackupLicense(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
        }
        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspBackupLicense(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspBackupLicense', body)

    def testVerifyFspBackupOldRule(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'C11FE572-5207-3359-DB85-001E95F5F185',
            'bk_path': ['/FSPback0107/'],
            'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
        }
        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspBackupOldRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspBackupOldRule', body)

    def testVerifyFspBackupOsVersion(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'C11FE572-5207-3359-DB85-001E95F5F185',
            'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
        }
        fspBackup = FspBackup(a)
        r = fspBackup.verifyFspBackupOsVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'verifyFspBackupOsVersion', body)

    def testCreateFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
                'secret_key': '',
                'band_width': '3*03:00-14:00*2m',
                'mirr_open_type': '0',
                'service_uuid': '',
                'mirr_sync_flag': '0',
                'excl_path': ["/cgroup/", "/dev/", "/etc/X11/xorg.conf/", "/etc/init.d/i2node/",
                              "/etc/rc.d/init.d/i2node/", "/etc/sdata/", "/lost+found/", "/media/", "/mnt/", "/proc/",
                              "/run/", "/selinux/", "/sys/", "/tmp/", "/usr/local/sdata/", "/var/i2/", "/var/i2data/",
                              "/var/lock/", "/var/run/vmblock-fuse/"],
                'bkup_one_time': 1515568566,
                'encrypt_switch': '0',
                'bk_type': 0,
                'mirr_sync_attr': '1',
                'bk_uuid': 'C11FE572-5207-3359-DB85-001E95F5F185',
                'wk_data_type': 1,
                'bk_path': ["/FSPback0107/"],
                'sync_item': '/',
                'bkup_policy': 0,
                'net_mapping_type': '2',
                'snapshot_policy': '0',
                'mirr_file_check': '0',
                'snapshot_interval': '0',
                'compress': '0',
                'monitor_type': 0,
                'failover': '2',
                'wk_path': ["/", "/boot/"],
                'snapshot_limit': '24',
                'snapshot_switch': 0,
                'fsp_name': 'LinuxBackup',
                'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
                'backup_type': 1,
                'fsp_wk_shut_flag': '2',
                'bk_data_type': 0,
                'bkup_schedule': [
                    {
                        'sched_time_end': '18:12',
                        'sched_day': 23,
                        'sched_gap_min': 61,
                        'sched_time': '11:31',
                        'sched_time_start': '04:10',
                        'sched_every': 2,
                        'limit': 9,
                    }
                ],
                'fsp_type': 1,
            },
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
                'fsp_uuid': '90534F82-221E-08FE-9B4F-AA1029A0CFF8',
                'secret_key': '',
                'band_width': '3*03:00-19:00*16m',
                'mirr_open_type': '0',
                'service_uuid': '',
                'mirr_sync_flag': '0',
                'excl_path': ["/cgroup/", "/dev/", "/etc/X11/xorg.conf/", "/etc/init.d/i2node/",
                              "/etc/rc.d/init.d/i2node/", "/etc/sdata/", "/lost+found/", "/media/", "/mnt/", "/proc/",
                              "/run/", "/selinux/", "/sys/", "/tmp/", "/usr/local/sdata/", "/var/i2/", "/var/i2data/",
                              "/var/lock/", "/var/run/vmblock-fuse/"],
                'bkup_one_time': 1515568566,
                'encrypt_switch': '0',
                'bk_type': 0,
                'mirr_sync_attr': '1',
                'bk_uuid': 'C11FE572-5207-3359-DB85-001E95F5F185',
                'wk_data_type': 1,
                'bk_path': ["/FSPback0107/"],
                'sync_item': '/',
                'bkup_policy': 0,
                'net_mapping_type': '2',
                'snapshot_policy': '0',
                'mirr_file_check': '0',
                'snapshot_interval': '0',
                'compress': '0',
                'monitor_type': 0,
                'failover': '2',
                'wk_path': ["/", "/boot/"],
                'snapshot_limit': '24',
                'snapshot_switch': 0,
                'fsp_name': 'LinuxBackup',
                'wk_uuid': 'CE77F3D6-A6E3-A385-CE66-712313B7DDE8',
                'backup_type': 1,
                'fsp_wk_shut_flag': '2',
                'bk_data_type': 0,
                'bkup_schedule': [
                    {
                        'sched_time_end': '18:50',
                        'sched_day': 22,
                        'sched_gap_min': 31,
                        'sched_time': '01:06',
                        'sched_time_start': '13:35',
                        'sched_every': 2,
                        'limit': 29,
                    }
                ],
                'fsp_type': 1
            }
        }
        fspBackup = FspBackup(a)
        r = fspBackup.modifyFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'modifyFspBackup', body)

    def testDescribeFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
                'fsp_uuid': '90534F82-221E-08FE-9B4F-AA1029A0CFF8',
            }
        }
        fspBackup = FspBackup(a)
        r = fspBackup.describeFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'describeFspBackup', body)

    def testDeleteFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': ['90534F82-221E-08FE-9B4F-AA1029A0CFF8'],
        }
        fspBackup = FspBackup(a)
        r = fspBackup.deleteFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'deleteFspBackup', body)

    def testListFspBackup(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
        }
        fspBackup = FspBackup(a)
        r = fspBackup.listFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspBackup', body)

    def testStartFspBackup(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {
            'operate': 'start',
            'fsp_uuids': ['90534F82-221E-08FE-9B4F-AA1029A0CFF8'],
        }
        r = fspBackup.startFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'startFspBackup', body)

    def testStopFspBackup(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {
            'operate': 'stop',
            'fsp_uuids': ['90534F82-221E-08FE-9B4F-AA1029A0CFF8'],
        }
        r = fspBackup.stopFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'stopFspBackup', body)

    def testFinishFspBackup(self):
        a = Auth(username, pwd)
        fspBackup = FspBackup(a)
        body = {
            'operate': 'finish',
            'fsp_uuids': ['90534F82-221E-08FE-9B4F-AA1029A0CFF8'],
        }
        r = fspBackup.finishFspBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'finishFspBackup', body)

    def testListFspBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': ['90534F82-221E-08FE-9B4F-AA1029A0CFF8'],
        }
        fspBackup = FspBackup(a)
        r = fspBackup.listFspBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspBackup', 'listFspBackupStatus', body)


if __name__ == '__main__':
    unittest.main()
