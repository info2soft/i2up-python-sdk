
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Cdm
from info2soft.cdm.v20240819.Cdm import Cdm
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


class CdmTestCase(unittest.TestCase):

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
            'sched_time': '01:36',
            'sched_every': 2,
            'limit': 8,
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
            'cdp_snapshot_execute_interval': 1,
            'cdp_keep_data': 1,},
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
            'sched_day': 4,
            'sched_time': '15:39',
            'sched_every': 2,
            'limit': 4,
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

    def testDeleteCdm(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'del_policy': 1,
            'force': 1,
            'recycle': 0,
        }
        
        
        cdm = Cdm(a)
        r = cdm.deleteCdm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'deleteCdm', body)

    def testListCdm(self):
        a = Auth(username, pwd)
        body = {
            'type': 3,
            'limit': 10,
            'page': 1,
            'where_args': [],
            'status': '',
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
            'force_refresh': 1,
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
            'vp_uuid': '',
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
            'restore_point': '',
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

    def testListDrillRestorePoint(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        cdm = Cdm(a)
        r = cdm.listDrillRestorePoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listDrillRestorePoint', body)

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

    def testCdmScriptPathCheck(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
            'file_dir': '',
        }
        
        
        cdm = Cdm(a)
        r = cdm.cdmScriptPathCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'cdmScriptPathCheck', body)

    def testListCdmDriverInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        cdm = Cdm(a)
        r = cdm.listCdmDriverInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cdm', 'listCdmDriverInfo', body)


if __name__ == '__main__':
    unittest.main()
