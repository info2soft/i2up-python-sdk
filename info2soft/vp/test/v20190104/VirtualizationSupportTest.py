# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.vp.v20181227.VirtualizationSupport import VirtualizationSupport
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


class DashboardTestCase(unittest.TestCase):

    def testCreateVp(self):
        a = Auth(username, pwd)
        body = {
            'comment': '',
            'config_addr': '192.168.72.75',
            'config_port': 58083,
            'os_pwd': '12345678',
            'os_usr': 'root',
            'vp_addr': '192.168.88.107',
            'vp_name': 'test',
            'vp_type': 0,
            'bind_lic_list': [],
            'biz_grp_list': [],
        }
        vp = VirtualizationSupport(a)
        r = vp.createVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVp', body)

    def testDescribeVp(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111'
        }
        vp = VirtualizationSupport(a)
        r = vp.describeVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVp', body)

    def testModifyVp(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
            'comment': '',
            'config_addr': '192.168.72.75',
            'config_port': 58083,
            'os_pwd': '12345678',
            'os_usr': 'root',
            'vp_addr': '192.168.88.107',
            'vp_name': 'test1',
            'vp_type': 0,
            'bind_lic_list': [],
            'biz_grp_list': [],
            'random_str': '11111111-1111-1111-1111-111111111111',
        }
        vp = VirtualizationSupport(a)
        r = vp.modifyVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'modifyVp', body)

    def testListVp(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
            'page': 1,
            'limit': 10,
        }
        vp = VirtualizationSupport(a)
        r = vp.listVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVp', body)

    def testListVpStatus(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuids': ['11111111-1111-1111-1111-111111111111',],
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpStatus', body)

    def testDeleteVp(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuids': ['11111111-1111-1111-1111-111111111111',],
        }
        vp = VirtualizationSupport(a)
        r = vp.deleteVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVp', body)

    def testListVM(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
            'path': '/',
            'force_rpc': 0,
        }
        vp = VirtualizationSupport(a)
        r = vp.listVM(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVM', body)

    def testDescribeVpAttribute(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
        }
        vp = VirtualizationSupport(a)
        r = vp.describeVpAttribute(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpAttribute', body)

    def testListBakVer(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
            'bk_path': 'H:\\vp_bk5\\test2_BAK_vm-11880_192.168.88.22\\',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
        }
        vp = VirtualizationSupport(a)
        r = vp.listBakVer(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listBakVer', body)

    def testListBakVerInfo(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'bk_path': 'H:\\vp_bk5\\testRC1_BAK_99_192.168.85.139',
            'ver_sig': 'A59DB76E-E33D-4E22-BB08-59723B1FC539',
            'group_uuid': '',
            'time': '2019-01-07_13-10-45',
        }
        vp = VirtualizationSupport(a)
        r = vp.listBakVerInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listBakVerInfo', body)

    def testlistDatastoreFile(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
            'dir_file': '/',
            'ds_name': 'datastore107（1）',
            'dc_name': 'ha-datacenter',
        }
        vp = VirtualizationSupport(a)
        r = vp.listDatastoreFile(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatastoreFile', body)

    def testListDatacenter(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
        }
        vp = VirtualizationSupport(a)
        r = vp.listDatacenter(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatacenter', body)

    def testListDatacenterHost(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
            'dc_name': 'ha-datacenter',
            'dc_mor': 'ha-datacenter',
        }
        vp = VirtualizationSupport(a)
        r = vp.listDatacenterHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatacenterHost', body)

    def testListDatastore(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
            'host_name': 'dev-esxi.6.6.6',
        }
        vp = VirtualizationSupport(a)
        r = vp.listDatastore(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatastore', body)

    def testListDatastoreInfo(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '11111111-1111-1111-1111-111111111111',
            'ds_name': 'datastore107（1）',
        }
        vp = VirtualizationSupport(a)
        r = vp.listDatastoreInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatastoreInfo', body)

    def testCreateVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'del_bkup_data': 0,
            'quiet_snap': 0,
            'quick_back': 1,
            'vp_uuid': 'C6335F62-2565-1957-4BB9-587F2FF46B00',
            'bk_path': 'E:\\vp_bk5\\',
            'vm_list': [{
                'vm_name': '测试5',
                'vm_ref': 'vm-10811',
            }],
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'lan_free': 23,
            'rule_name': 'vp_bk cky',
            'bkup_policy': 0,
            'bkup_one_time': 1546831899,
            'bkup_schedule': [
                {
                    'limit': 3,
                    'sched_day': [
                        1,
                        2,
                        3, ],
                    'sched_time': ['00:00', ],
                    'sched_every': 0,
                    'bkup_type': 0,
                }],
            'biz_grp_list': [],
            'rule_type': 10,
            'band_width': '-1',
            'compress': 0,
            'mem_snap': 0,
        }
        vp = VirtualizationSupport(a)
        r = vp.createVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpBackup', body)

    def testModifyVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'del_bkup_data': 0,
            'quiet_snap': 0,
            'quick_back': 1,
            'vp_uuid': 'C6335F62-2565-1957-4BB9-587F2FF46B00',
            'bk_path': 'E:\\vp_bk5\\',
            'vm_list': [{
                'vm_name': '测试5',
                'vm_ref': 'vm-10811',
            }],
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'lan_free': 23,
            'rule_name': 'vp_bk cky',
            'bkup_policy': 0,
            'bkup_one_time': 1546831899,
            'bkup_schedule': [
                {
                    'limit': 3,
                    'sched_day': [
                        1,
                        2,
                        3, ],
                    'sched_time': ['00:00', ],
                    'sched_every': 0,
                    'bkup_type': 0,
                }],
            'biz_grp_list': [],
            'rule_type': 0,
            'band_width': '-1',
            'compress': 0,
            'mem_snap': 1,
            'rule_uuid': '11111111-1111-1111-1111-111111111111'
        }
        vp = VirtualizationSupport(a)
        r = vp.modifyVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'modifyVpBackup', body)

    def testDescribeVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '11111111-1111-1111-1111-111111111111'
        }
        vp = VirtualizationSupport(a)
        r = vp.describeVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpBackup', body)

    def testDescribeVpBackupGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '11111111-1111-1111-1111-111111111111'
        }
        vp = VirtualizationSupport(a)
        r = vp.describeVpBackupGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpBackupGroup', body)

    def testListVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'type': 0,
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpBackup', body)

    def testListVpBackupGroup(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'type': 0,
            'where_args[bk_path]': 'H:\\vp_bk5\\',
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpBackupGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpBackupGroup', body)

    def testListVpBackupStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111'],
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpBackupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpBackupStatus', body)

    def testStartVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
        }
        vp = VirtualizationSupport(a)
        r = vp.startVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'startVpBackup', body)

    def testStopVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
        }
        vp = VirtualizationSupport(a)
        r = vp.stopVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'stopVpBackup', body)

    def testDeleteVpBackup(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111',],
        }
        vp = VirtualizationSupport(a)
        r = vp.deleteVpBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpBackup', body)

    def testCreateVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'bk_path': 'H:\\vp_bk5\\testRC1_BAK_99_192.168.85.139',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'new_ds': 'datastore1',
            'vm_list': [
                {

                    'vm_cfg': {

                        'alt_name': '',
                        'anno': '',
                        'bk_path': 'H:\\vp_bk5\\testRC1_BAK_99_192.168.85.139\\',
                        'cdrom': '',
                        'chg_id': '52 19 10 74 e2 c2 b3 63-de 7a 2e d2 9d 40 91 bf/107',
                        'controller': '1,1000,100,3,0,3,noSharing,0',
                        'core_per_sock': '1',
                        'cpu': '1',
                        'dc': 'ha-datacenter',
                        'disk': '2,[datastore1] 测试5/proxy gateway1.vmdk,persistent,1,2048,2000,1000,0,52 19 10 74 e2 c2 b3 63-de 7a 2e d2 9d 40 91 bf/107,0,1',
                        'disk_count': '1',
                        'disk_list': ['proxy gateway1.vmdk', ],
                        'ds': 'datastore1',
                        'floppy': '',
                        'guest_os_id': 'rhel6_64Guest',
                        'hostname': 'localhost.localdomain',
                        'mem_mb': '1024',
                        'nic': '3,00:50:56:90:ff:ad,1,4000,100,7,1,VM Network;3,00:50:56:90:7b:51,1,4001,100,8,1,VM Network',
                        'nic_count': '2',
                        'storeMem': '0',
                        'time': '2019-01-07_13-10-45',
                        'valid_data': 4194304,
                        'ver_sig': 'A59DB76E-E33D-4E22-BB08-59723B1FC539',
                        'vm_name': '测试5',
                        'vm_ref': '99',
                        'vm_version': 'vmx-08',
                        'vp_uuid': '928B88A6-CDBA-6F55-ADCB-15A8A935C9C2',
                    },
                    'ver_sig': 'A59DB76E-E33D-4E22-BB08-59723B1FC539',
                    'vm_ref': '99',
                    'vm_name': '测试5',
                    'disk_list': [
                        {
                            'disk_name': 'proxy gateway1.vmdk',
                            'disk_path': '/',
                            'is_same': 1,
                            'new_ds': 'datastore1',
                        },
                    ],
                       }],
            'new_hostname': 'localhost.localdomain',
            'new_dc': 'ha-datacenter',
            'is_create': 0,
            'vp_uuid': '928B88A6-CDBA-6F55-ADCB-15A8A935C9C2',
            'new_ds_path': '/',
            'new_vp_uuid': '928B88A6-CDBA-6F55-ADCB-15A8A935C9C2',
            'rule_name': 'testRC cky',
            'lan_free': 23,
            'rule_type': 0,
            'automate': 0,
            'new_vm_name': '测试5',
            'new_dc_mor': 'ha-datacenter',
            'api_type': 'HostAgent',
            'biz_grp_list': [],
            'cpu': 1,
            'core_per_sock': 1,
            'mem_mb': 1024,
            'mac': '3,00:50:56:90:ff:ad,1,4000,100,7,1,VM Network;3,00:50:56:90:7b:51,1,4001,100,8,1,VM Network',
            'group_recovery': 0,
            'backup_rule_name': 'testRC1',
            'band_width': '-1',
        }
        vp = VirtualizationSupport(a)
        r = vp.createVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpRecovery', body)

    def testDescribeVpRecoveryGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '11111111-1111-1111-1111-111111111111'
        }
        vp = VirtualizationSupport(a)
        r = vp.describeVpRecoveryGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpRecoveryGroup', body)

    def testListVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'type': 0,
            'limit': 10,
            'page': 1,
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpRecovery', body)

    def testListVpRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111'],
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpRecoveryStatus', body)

    def testStartVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rule_uuids': '641A27BB-B4D1-F482-1FB8-E856898626DA',
            'rule_type': 0,
        }
        vp = VirtualizationSupport(a)
        r = vp.startVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'startVpRecovery', body)

    def testStopVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'rule_uuids': '641A27BB-B4D1-F482-1FB8-E856898626DA',
            'rule_type': 0,
        }
        vp = VirtualizationSupport(a)
        r = vp.stopVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'stopVpRecovery', body)

    def testClearFinishVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'clear_finish',
            'rule_uuids': '641A27BB-B4D1-F482-1FB8-E856898626DA',
            'rule_type': 0,
        }
        vp = VirtualizationSupport(a)
        r = vp.clearFinishVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'clearFinishVpRecovery', body)

    def testDeleteVpRecovery(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111'],
        }
        vp = VirtualizationSupport(a)
        r = vp.deleteVpRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpRecovery', body)

    def testCreateVpMove(self):
        a = Auth(username, pwd)
        body = {
            'new_ds': '103-数据盘',
            'support_cbt': 1,
            'tgt_uuid': '7F16E670-1A61-D565-6905-9C68B9520907',
            'del_bkup_swap': 0,
            'src_uuid': '7F16E670-1A61-D565-6905-9C68B9520907',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'automate': 0,
            'rule_name': 'testMove1 cky',
            'new_dc': 'i2test',
            'bk_path': 'H:\\vp_rep\\',
            'backup_type': 'i',
            'new_host': '192.168.88.103',
            'quiet_snap': 1,
            'bkup_schedule': {
                'sched_time_start': '0',
                'limit': 0,
                'sched_day': 19,
                'sched_every': 0,
                'sched_time': [],
                'sched_gap_min': 0,
            },
            'quick_back': 1,
            'del_bkup_data': 0,
            'lan_free': 23,
            'vm_list': [
                {

                    'vm_name': '新建虚拟机1',
                    'vm_ref': 'vm-11877',
                    'shd_name': '新建虚拟机1_move',
                    'overwrite': 0,
                }],
            'time_window': '',
            'new_dc_mor': 'datacenter-2',
            'bkup_policy': 0,
            'band_width': '-1',
            'rule_type': 1,
        }
        vp = VirtualizationSupport(a)
        r = vp.createVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpMove', body)

    def testDescribeVpMove(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '11111111-1111-1111-1111-111111111111'
        }
        vp = VirtualizationSupport(a)
        r = vp.describeVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpMove', body)

    def testModifyVpMove(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '11111111-1111-1111-1111-111111111111',
            'new_ds': '',
            'support_cbt': 1,
            'tgt_uuid': '',
            'del_bkup_swap': 1,
            'src_uuid': 'fa2eEdD2-AA4d-ecB3-2C1C-bA6099FEcCeF',
            'bk_uuid': '',
            'automate': 1,
            'rule_name': '',
            'new_dc': '',
            'bk_path': '',
            'backup_type': '',
            'new_host': '',
            'quiet_snap': 1,
            'bkup_schedule': [],
            'quick_back': 1,
            'del_bkup_data': 1,
            'lan_free': 1,
            'vm_list': [],
            'time_window': '',
            'new_dc_mor': '',
            'bkup_policy': 1,
        }
        vp = VirtualizationSupport(a)
        r = vp.modifyVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'modifyVpMove', body)

    def testListVpMove(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpMove', body)

    def testListVpMoveStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111',],
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpMoveStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpMoveStatus', body)

    def testStopVpMove(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'rule_uuids': '1C89A121-6B03-24B2-9273-D4B93C0687AD',
            'snap_point': '',
            'op_code': '',
        }
        vp = VirtualizationSupport(a)
        r = vp.stopVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'stopVpMove', body)

    def testStartVpMove(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rule_uuids': '1C89A121-6B03-24B2-9273-D4B93C0687AD',
            'snap_point': '',
            'op_code': '',
        }
        vp = VirtualizationSupport(a)
        r = vp.startVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'startVpMove', body)

    def testMoveVpMove(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rule_uuids': '1C89A121-6B03-24B2-9273-D4B93C0687AD',
            'snap_point': '',
            'op_code': '',
        }
        vp = VirtualizationSupport(a)
        r = vp.moveVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'moveVpMove', body)

    def testDeleteVpMove(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111'],
        }
        vp = VirtualizationSupport(a)
        r = vp.deleteVpMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpMove', body)

    def testListVpRepPointList(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '11111111-1111-1111-1111-111111111111',
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpRepPointList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpRepPointList', body)

    def testCreateVpRep(self):
        a = Auth(username, pwd)
        body = {
            'new_ds': '103-数据盘',
            'support_cbt': 1,
            'tgt_uuid': '7F16E670-1A61-D565-6905-9C68B9520907',
            'del_bkup_swap': 0,
            'src_uuid': '7F16E670-1A61-D565-6905-9C68B9520907',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'automate': 0,
            'rule_name': 'testMove1 cky',
            'new_dc': 'i2test',
            'bk_path': 'H:\\vp_rep\\',
            'backup_type': 'i',
            'new_host': '192.168.88.103',
            'quiet_snap': 1,
            'bkup_schedule': {
                'sched_time_start': '0',
                'limit': 0,
                'sched_day': 19,
                'sched_every': 0,
                'sched_time': [],
                'sched_gap_min': 0,
            },
            'quick_back': 1,
            'del_bkup_data': 0,
            'lan_free': 23,
            'vm_list': [
                {

                    'vm_name': '新建虚拟机1',
                    'vm_ref': 'vm-11877',
                    'shd_name': '新建虚拟机1_move',
                    'overwrite': 0,
                }],
            'time_window': '',
            'new_dc_mor': 'datacenter-2',
            'bkup_policy': 0,
            'band_width': '-1',
            'rule_type': 1,
        }
        vp = VirtualizationSupport(a)
        r = vp.createVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpRep', body)

    def testDescribeVpRep(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '11111111-1111-1111-1111-111111111111'
        }
        vp = VirtualizationSupport(a)
        r = vp.describeVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpRep', body)

    def testModifyVpRep(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '11111111-1111-1111-1111-111111111111',
            'new_ds': '',
            'support_cbt': 1,
            'tgt_uuid': '',
            'del_bkup_swap': 1,
            'src_uuid': 'fa2eEdD2-AA4d-ecB3-2C1C-bA6099FEcCeF',
            'bk_uuid': '',
            'automate': 1,
            'rule_name': '',
            'new_dc': '',
            'bk_path': '',
            'backup_type': '',
            'new_host': '',
            'quiet_snap': 1,
            'bkup_schedule': [],
            'quick_back': 1,
            'del_bkup_data': 1,
            'lan_free': 1,
            'vm_list': [],
            'time_window': '',
            'new_dc_mor': '',
            'bkup_policy': 1,
        }
        vp = VirtualizationSupport(a)
        r = vp.modifyVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'modifyVpRep', body)

    def testListVpRep(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpRep', body)

    def testListVpRepStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111',],
        }
        vp = VirtualizationSupport(a)
        r = vp.listVpRepStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpRepStatus', body)

    def testStopVpRep(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'rule_uuids': '1C89A121-6B03-24B2-9273-D4B93C0687AD',
            'snap_point': '',
            'op_code': '',
        }
        vp = VirtualizationSupport(a)
        r = vp.stopVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'stopVpRep', body)

    def testStartVpRep(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'rule_uuids': '1C89A121-6B03-24B2-9273-D4B93C0687AD',
            'snap_point': '',
            'op_code': '',
        }
        vp = VirtualizationSupport(a)
        r = vp.startVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'startVpRep', body)

    def testFailoverVpRep(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'failover',
            'rule_uuids': '1C89A121-6B03-24B2-9273-D4B93C0687AD',
            'snap_point': '',
            'op_code': '',
        }
        vp = VirtualizationSupport(a)
        r = vp.failoverVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'failoverVpRep', body)

    def testFailbackVpRep(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'failback',
            'rule_uuids': '1C89A121-6B03-24B2-9273-D4B93C0687AD',
            'snap_point': '',
            'op_code': '',
        }
        vp = VirtualizationSupport(a)
        r = vp.failbackVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'failbackVpRep', body)

    def testDeleteVpRep(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111'],
        }
        vp = VirtualizationSupport(a)
        r = vp.deleteVpRep(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpRep', body)


if __name__ == '__main__':
    unittest.main()
