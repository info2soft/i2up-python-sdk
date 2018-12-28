
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.rep.v20181227.RepBackup import RepBackup
from info2soft import Auth
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


class RepBackupTestCase(unittest.TestCase):

    def testCreateRepBackup(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {"rep_backup":{"rep_uuid":"","rep_name":"f123","ruleUnit":"","secret_key":"","bk_path_policy":"1","rep_mode":0,"cdp_path":"","wk_uuid":"F1BB0688-95BD-7CC1-C811-56B4EDCC76F1","bk_uuid":"9746B067-FCA5-944E-788B-1C805213F795","file_type_filter":"","policy_interval":"","mirr_file_check":"0","mirr_sync_flag":"0","mirr_open_type":"0","mirr_sync_attr":"1","encrypt_switch":"0","snapshot_switch":0,"cdp_snap_on":"0","cdp_snap_interval":30,"cdp_snap_count":240,"snapshot_interval":"1","snapshot_limit":"24","snapshot_policy":"0","snapshot_start":"","compress":"0","oph_policy":"0","oph_path":"","del_policy":"0","file_type_filter_switch":0,"wk_node_name":"linux-25.11","bk_node_name":"linux-25.12(L)","cdp_switch":"0","cdp_detail_copy":3,"cdp_daily_copy":30,"cdp_process_time":"04:33:34","cdp_baseline_format":"0","cdp_bl_bkup_switch":0,"cdp_bl_sched_switch":0,"band_width":"","cdp_bl_sched":"","wk_path":["/.autofsck","/.autorelabel"],"bk_path":["/1011rep/"],"excl_path":[],"bkup_one_time": None,"auto_start":"1","rep_type":0,"mirr_sched":"","mirr_sched_switch":0,"cmp_file_check":0,"cmp_schedule":[],"cmp_switch":0,"biz_grp_list":[],"mirr_skip":"0","thread_num":"0","ct_name_type":0,"ct_name_str1":"","ct_name_str2":"","cdp_param":"3,30,0"}}
        r = repBackup.createRepBackup(body)
        print(r[0])

    def testDescribeRepBackup(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.describeRepBackup(body)
        print(r[0])

    def testModifyRepBackup(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {"uuid": "F1479FED-B4DD-5063-AB92-6FA002C48198","rep_backup":{"rep_uuid":"F1479FED-B4DD-5063-AB92-6FA002C48198","rep_name":"f123","ruleUnit":"","secret_key":"","bk_path_policy":"1","rep_mode":0,"cdp_path":"","wk_uuid":"F1BB0688-95BD-7CC1-C811-56B4EDCC76F1","bk_uuid":"9746B067-FCA5-944E-788B-1C805213F795","file_type_filter":"","policy_interval":"","mirr_file_check":"1","mirr_sync_flag":"0","mirr_open_type":"0","mirr_sync_attr":"1","encrypt_switch":"1","snapshot_switch":0,"cdp_snap_on":"0","cdp_snap_interval":30,"cdp_snap_count":240,"snapshot_interval":"24","snapshot_limit":"2","snapshot_policy":"0","snapshot_start":1545995176,"compress":"0","oph_policy":"0","oph_path":"","del_policy":"0","file_type_filter_switch":0,"wk_node_name":"linux-25.11","bk_node_name":"linux-25.12(L)","cdp_switch":"0","cdp_detail_copy":3,"cdp_daily_copy":30,"cdp_process_time":"04:33:34","cdp_baseline_format":"0","cdp_bl_bkup_switch":0,"cdp_bl_sched_switch":0,"band_width":"","cdp_bl_sched":"","wk_path":["/.autofsck","/.autorelabel"],"bk_path":["/1011rep/"],"excl_path":[],"bkup_one_time":None,"auto_start":"1","rep_type":0,"mirr_sched":"","mirr_sched_switch":0,"cmp_file_check":0,"cmp_schedule":[],"cmp_switch":0,"biz_grp_list":[],"mirr_skip":"0","thread_num":"0","id":"33","bkup_policy":"2","bkup_schedule":None,"create_time":"1545896404","random_str":"2DC95D78-5FDE-46CA-6CCE-E4A81E48A8AC","uuid":"F1479FED-B4DD-5063-AB92-6FA002C48198","wk_ip":"192.168.25.11","wk_port":"26821","bk_ip":"192.168.25.12","bk_port":"26821","username":"admin","cdp_param":"3,30,0","disk_limit":"0","schedule":None,"user_uuid":"1BCFCAA3-E3C8-3E28-BDC5-BE36FDC2B5DC","group_uuid":None,"status":None,"sync_rep_uuid":None,"init_capacity":"0","bk_path_block":"0","ct_name_type":0,"ct_name_str1":"","ct_name_str2":"","ct_name_str3":None,"ct_name_str4":None,"is_from_ha":0,"biz_grp_name":[]}}
        print(body["uuid"])
        r = repBackup.modifyRepBackup(body)
        print(r[0])

    def testDeleteRepBackup(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {
            'rep_uuids': ['3B90032A-E6F5-7662-D1ED-F14090A25580']
        }
        r = repBackup.deleteRepBackup(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.tempFuncName(body)
        print(r[0])

    def testListRepBackupStatus(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {
            'rep_uuids': ['F1479FED-B4DD-5063-AB92-6FA002C48198', '53486DB1-A6C0-8E01-6917-0A9AF96FAD37']
        }
        r = repBackup.listRepBackupStatus(body)
        print(r[0])

    def testListRepBackup(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {
            'type': 0,
            'limit': 1,
            'page': 1
        }
        r = repBackup.listRepBackup(body)
        print(r[0])

    def testListRepBackupBaseLine(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.listRepBackupBaseLine(body)
        print(r[0])

    def testDeleteRepBackupBaseline(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.deleteRepBackupBaseline(body)
        print(r[0])

    def testListRepBackupOrphan(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.listRepBackupOrphan(body)
        print(r[0])

    def testDeleteRepBackupOrphan(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.deleteRepBackupOrphan(body)
        print(r[0])

    def testDownloadRepBackupOrphan(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.downloadRepBackupOrphan(body)
        print(r[0])

    def testListRepBackupSnapshot(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.listRepBackupSnapshot(body)
        print(r[0])

    def testCreateRepBackupSnapshot(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.createRepBackupSnapshot(body)
        print(r[0])

    def testDeleteRepBackupSnapshot(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.deleteRepBackupSnapshot(body)
        print(r[0])

    def testRepBackup(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
        r = repBackup.repBackup(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()
