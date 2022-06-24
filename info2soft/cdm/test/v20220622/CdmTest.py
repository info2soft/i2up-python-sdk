
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
# from info2soft import Cdm
from info2soft.cdm.v20220622.Cdm import Cdm
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
    
                
class CdmTestCase(unittest.TestCase):

    def testCreateVpDrill(self):
        a = Auth(username, pwd)
        body = {
            'vm_name': '测试5',
            'vm_ref': 'vm-10811',
            'limit': 3,
            'sched_day': [
            '1',
            '2',
            '3',],
            'sched_time': [
            '00:00',],
            'sched_every': 0,
            'bkup_type': 0,
            'rule_name': '',
            'rule_type': 0,
            'vp_uuid': '',
            'auto': 0,
            'vm_list': [{
            'vm_name': '',
            'new_vm_name': '',
            'bk_uuid': '',
            'time': '',
            'original_rule_uuid': '',
            'scripts': '',
            'bk_path': '',
            'scripts_type': 1,
            'os_type': 1,
            'wk_uuid': '',
            'src_uuid': '',
            'data_ip_uuid': '',
            'ver_sig': '',
            'os_ip': '',},],
            'backup_type': 'i',
            'del_bkup_data': 0,
            'automate': 0,
            'auto_shutdown': 1,
        }

        cdm = Cdm(a)
        r = cdm.createVpDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'createVpDrill', body)

    def testDescribeVpDrillGroup(self):
        a = Auth(username, pwd)
        body = {
        }

        cdm = Cdm(a)
        r = cdm.describeVpDrillGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'describeVpDrillGroup', body)

    def testDescribeVpDrill(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cdm = Cdm(a)
        r = cdm.describeVpDrill(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'describeVpDrill', body)

    def testDeleteCdmDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'group_uuids': [],
            'delete_tgtvm': 0,
        }

        cdm = Cdm(a)
        r = cdm.deleteCdmDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'deleteCdmDrill', body)

    def testListCdmDrillStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }

        cdm = Cdm(a)
        r = cdm.listCdmDrillStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listCdmDrillStatus', body)

    def testStopCdmDrill(self):
        a = Auth(username, pwd)
        body = {
            'msg': '',
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'group_uuids': [],
            'status': '',
        }

        cdm = Cdm(a)
        r = cdm.stopCdmDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'stopCdmDrill', body)

    def testStartCdmDrill(self):
        a = Auth(username, pwd)
        body = {
            'msg': '',
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'group_uuids': [],
            'status': '',
        }

        cdm = Cdm(a)
        r = cdm.startCdmDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'startCdmDrill', body)

    def testSetStatusCdmDrill(self):
        a = Auth(username, pwd)
        body = {
            'msg': '',
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'group_uuids': [],
            'status': '',
        }

        cdm = Cdm(a)
        r = cdm.setStatusCdmDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'setStatusCdmDrill', body)

    def testQueryGroupVmStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'group_uuid': '',
        }

        cdm = Cdm(a)
        r = cdm.queryGroupVmStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'queryGroupVmStatus', body)

    def testCreateCdm(self):
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
            'sched_day': 26,
            'sched_time': '02:20',
            'sched_every': 2,
            'limit': 39,
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
            'cdp_switch': 1,
            'cdp_snapshot_days': 1,
            'cdp_snapshot_execute_interval': 1,},
            'vp_uuid': '',
            'storage_uuid': '',
            'data_ip_uuid': '',
            'oracle_dbagent_param': {
            'oracle_sid': '',
            'sql_plus_path': '',
            'username': '',
            'password': '',
            'port': 1,
            'table_space': [],
            'timeout': 1,},
            'mysql_dbagent_param': {
            'mysql_path': '',
            'username': '',
            'password': '',
            'port': 1,
            'database_name': [],
            'timeout': 1,},
            'sqlserver_dbagent_param': {
            'timeout': 1,
            'enable': 0,},
            'database_type': '0',
            'database_switch': 0,
            'auto': '',
            'orch_vm_name': '',
            'scripts_type': '',
            'scripts': '',
            'start_type': 0,
            'custom_dbagent_param': {
            'pre_snapshot_script': '',
            'post_snapshot_script': '',},},
        }

        cdm = Cdm(a)
        r = cdm.createCdm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'createCdm', body)

    def testDescribeCdm(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cdm = Cdm(a)
        r = cdm.describeCdm(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'describeCdm', body)

    def testModifyCdm(self):
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
            'sched_day': 28,
            'sched_time': '15:08',
            'sched_every': 2,
            'limit': 60,
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
            'cdp_snapshot_execute_interval': 1,},
            'vp_uuid': '',
            'storage_uuid': '',
            'data_ip_uuid': '',
            'oracle_dbagent_param': {
            'oracle_sid': '',
            'sql_plus_path': '',
            'username': '',
            'password': '',
            'port': 1,
            'table_space': [],
            'timeout': 1,},
            'mysql_dbagent_param': {
            'mysql_path': '',
            'username': '',
            'password': '',
            'port': 1,
            'database_name': [],
            'timeout': 1,},
            'sqlserver_dbagent_param': {
            'timeout': 1,
            'enable': 0,},
            'database_type': '0',
            'database_switch': 0,
            'auto': '',
            'orch_vm_name': '',
            'scripts_type': '',
            'scripts': '',
            'start_type': 0,},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cdm = Cdm(a)
        r = cdm.modifyCdm(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'modifyCdm', body)

    def testListCdm(self):
        a = Auth(username, pwd)
        body = {
            'type': 3,
            'limit': 10,
            'page': 1,
            'where_args': [],
        }

        cdm = Cdm(a)
        r = cdm.listCdm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listCdm', body)

    def testListCdmStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }

        cdm = Cdm(a)
        r = cdm.listCdmStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listCdmStatus', body)

    def testGetByWk(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
        }

        cdm = Cdm(a)
        r = cdm.getByWk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getByWk', body)

    def testGetPointList(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
            'path': '',
            'type': '',
            'suffix': '',
            'page': 1,
            'limit': 1,
            'rule_uuid': '',
            'search_key': '',
            'search_value': '2',
            'start': 1,
            'end': 1,
            'order': '',
        }

        cdm = Cdm(a)
        r = cdm.getPointList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getPointList', body)

    def testGetNetworkList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'type': '',
            'storage_id': '',
        }

        cdm = Cdm(a)
        r = cdm.getNetworkList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getNetworkList', body)

    def testDescribeFfomount(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cdm = Cdm(a)
        r = cdm.describeFfomount(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'describeFfomount', body)

    def testGetNodeList(self):
        a = Auth(username, pwd)
        body = {
            'path': '',
            'type': '',
            'bk_uuid': '',
        }

        cdm = Cdm(a)
        r = cdm.getNodeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getNodeList', body)

    def testGetResourceList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'search_field': '',
            'search_value': '',
        }

        cdm = Cdm(a)
        r = cdm.getResourceList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getResourceList', body)

    def testGetHostStorageList(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }

        cdm = Cdm(a)
        r = cdm.getHostStorageList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getHostStorageList', body)

    def testGetVmInfo(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'bk_uuid': '',
            'vm_ref': '',
        }

        cdm = Cdm(a)
        r = cdm.getVmInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getVmInfo', body)

    def testCreateCdmRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_recovery': {
                'dst_path': '',
                'monitor_type': 0,
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
                'bak_wk_uuid': '',
                'bak_wk_address': '',
                'vp_uuid': '',
                'storage_uuid': '',
                'bak_wk_name': '',
                'vm_name': '',
                'vm_ref': '',
                'compress_switch': 1,
                'compress': 1,
                'encrypt_switch': 1,
                'encrypt': '',
                'secret_key': '', },
        }

        cdm = Cdm(a)
        r = cdm.createCdmRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'createCdmRecovery', body)

    def testOperateCdmRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
        }

        cdm = Cdm(a)
        r = cdm.operateCdmRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'operateCdmRecovery', body)

    def testListCdmRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
        }

        cdm = Cdm(a)
        r = cdm.listCdmRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listCdmRecoveryStatus', body)

    def testListCdmRecovery(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'page': 1,
            'limit': 10
        }

        cdm = Cdm(a)
        r = cdm.listCdmRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listCdmRecovery', body)

    def testTakeOverDrillList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1
        }
        
        cdm = Cdm(a)
        r = cdm.takeOverDrillList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'takeOverDrillList', body)

    def testCreateTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'vm_name': '',
            'rule_type': 1,
            'wk_uuid': '',
            'bk_version': '',
            'vm_cpu_core': '',
            'vm_mem': '',
            'vm_network': {
            'cards': [{
            'mac': '',
            'gateway': [],
            'dns': {
            'domain': '',
            'servers': [],},
            'cidr': [],
            'network_id': '',
            'network_name': '',},],
            'dns': {
            'domain': '',
            'servers': '',},},
            'bk_uuid': '',
            'vm_disks': [{
            'path': '',
            'size': '',
            'interface': '',
            'isBoot': '',},],
            'bios_type': '',
            'vp_uuid': '',
            'timezone': '',
            'storage_uuid': '',
            'bk_path': '',
            'os_version': '',
            'fsp_uuid': '',
            'by_type': 1,
            'wk_address': '',
            'wk_name': '',
            'has_virtio': 'false',
            'has_virtio_scsi': 'false',
            'has_net_kvm': 'false',
            'network_switch': 0,
            'restore_info': {},
        }
        
        cdm = Cdm(a)
        r = cdm.createTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'createTakeOverDrill', body)

    def testDeleteTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force': 1,
            'del_policy': 0,
        }
        
        cdm = Cdm(a)
        r = cdm.deleteTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'deleteTakeOverDrill', body)

    def testDescribeTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cdm = Cdm(a)
        r = cdm.describeTakeOverDrill(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'describeTakeOverDrill', body)

    def testGetVmStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
            '0E807AD3-DD1E-9224-2B9B-E713CF258467',
            '1A807AD3-DD1E-9224-2B9B-E713CF258467',],
        }

        cdm = Cdm(a)
        r = cdm.getVmStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'getVmStatus', body)

    def testStartTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
            'type': '',
        }

        cdm = Cdm(a)
        r = cdm.startTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'startTakeOverDrill', body)

    def testStopTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
            'type': '',
        }

        cdm = Cdm(a)
        r = cdm.stopTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'stopTakeOverDrill', body)

    def testOpenConsoleTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
            'type': '',
        }

        cdm = Cdm(a)
        r = cdm.openConsoleTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'openConsoleTakeOverDrill', body)

    def testCreateFfoMount(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'bk_version': '',
            'os_version': '',
            'storage_uuid': '',
            'mount_name': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'vm_disks': [{
            'path': '',
            'size': '',
            'interface': '',
            'isBoot': '',},],
            'protocol': '',
            'fsp_uuid': '',
            'acl': '',
            'by_type': '',
            'wk_address': '',
            'wk_name': '',
            'client_uuid': '',
            'specify_client': 0,
        }
        
        cdm = Cdm(a)
        r = cdm.createFfoMount(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'createFfoMount', body)

    def testModifyFfoMount(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'bk_version': '',
            'os_version': '',
            'storage_uuid': '',
            'mount_name': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'vm_disks': [{
            'path': '',
            'size': '',
            'interface': '',
            'isBoot': '',},],
            'protocol': '',
            'acl': '',
            'random_str': '',
            'fsp_uuid': '',
            'specify_client': 1,
            'client_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cdm = Cdm(a)
        r = cdm.modifyFfoMount(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'modifyFfoMount', body)

    def testFfoMountList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'search_field': 'mount_name',
            'search_value': 'mount_name',
        }
        
        cdm = Cdm(a)
        r = cdm.ffoMountList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'ffoMountList', body)

    def testListFfoMountStatus(self):
        a = Auth(username, pwd)
        body = {
            'mount_uuids': [],
        }
        
        cdm = Cdm(a)
        r = cdm.listFfoMountStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listFfoMountStatus', body)

    def testDeleteFfoMount(self):
        a = Auth(username, pwd)
        body = {
            'mount_uuids': [],
        }

        cdm = Cdm(a)
        r = cdm.deleteFfoMount(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'deleteFfoMount', body)

    def testVerifyOracleArchiveMode(self):
        a = Auth(username, pwd)
        body = {
            'username': '',
            'password': '',
            'sqlplus_path': '',
            'sid': '',
            'timeout': '',
            'port': '',
            'wk_uuid': '',
            'bk_uuid': '',
        }

        cdm = Cdm(a)
        r = cdm.verifyOracleArchiveMode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'verifyOracleArchiveMode', body)

    def testAutoDrillCdmRule(self):
        a = Auth(username, pwd)
        body = {
        }
        
        cdm = Cdm(a)
        r = cdm.autoDrillCdmRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'autoDrillCdmRule', body)

    def testVerifyDuplicateCdmCoopyRule(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
        }
        
        cdm = Cdm(a)
        r = cdm.verifyDuplicateCdmCoopyRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'verifyDuplicateCdmCoopyRule', body)

    def testCreateCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'old_bk_uuid': '',
            'old_platform_uuid': '',
            'old_storage_uuid': '',
            'rule_uuids': [],
            'proxy_uuid': '',
            'new_bk_uuid': '',
            'new_platform_uuid': '',
            'data_addr': '',
            'new_storage_uuid': '',
            'bkup_policy': '',
            'bkup_one_time': '',
            'bkup_schedule': {
            'sched_gap_min': '60',
            'sched_time': [
                "00:00:00"
            ],
            'sched_day': [
                "1"
            ],
            'sched_time_end': '23:59',
            'limit': '5',
            'sched_time_start': '00:00',
            'sched_every': '0'},
            'compress_switch': '',
            'encrypt_switch': '',
            'band_width': '',
            'rule_uuid': '',
            'rule_name': '',
        }
        
        cdm = Cdm(a)
        r = cdm.createCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'createCdmRemoteCoopy', body)

    def testListCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'search_args': '',
            'search_value': '',
        }
        
        cdm = Cdm(a)
        r = cdm.listCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listCdmRemoteCoopy', body)

    def testListCdmRemoteCoopyStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': '',
        }
        
        cdm = Cdm(a)
        r = cdm.listCdmRemoteCoopyStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listCdmRemoteCoopyStatus', body)

    def testDeleteCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
            'del_policy': '',
            'rule_uuids': [],
        }
        
        cdm = Cdm(a)
        r = cdm.deleteCdmRemoteCoopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'deleteCdmRemoteCoopy', body)

    def testDescribeCdmRemoteCoopy(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cdm = Cdm(a)
        r = cdm.describeCdmRemoteCoopy(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'describeCdmRemoteCoopy', body)

    def testVerifyCdmCapacity(self):
        a = Auth(username, pwd)
        body = {
            'disk_space': 1,
            'storage_uuid': '',
            'old_bk_uuid': '',
            'new_bk_uuid': '',
        }
        
        cdm = Cdm(a)
        r = cdm.verifyCdmCapacity(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'verifyCdmCapacity', body)

    def testListCdmRemoteCoopyLicense(self):
        a = Auth(username, pwd)
        body = {
            'old_bk_uuid': '',
            'new_bk_uuid': '',
        }
        
        cdm = Cdm(a)
        r = cdm.listCdmRemoteCoopyLicense(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listCdmRemoteCoopyLicense', body)


if __name__ == '__main__':
    unittest.main()
