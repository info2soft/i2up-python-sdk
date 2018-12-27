
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
        body = {"uuid": "53486DB1-A6C0-8E01-6917-0A9AF96FAD37&_=0.6100473644312074","rep_backup":{"rep_uuid":"53486DB1-A6C0-8E01-6917-0A9AF96FAD37&_=0.6100473644312074","rep_name":"123","ruleUnit":"","secret_key":"","bk_path_policy":"1","rep_mode":0,"cdp_path":"","wk_uuid":"F1BB0688-95BD-7CC1-C811-56B4EDCC76F1","bk_uuid":"9746B067-FCA5-944E-788B-1C805213F795","file_type_filter":"","policy_interval":"","mirr_file_check":"0","mirr_sync_flag":"0","mirr_open_type":"0","mirr_sync_attr":"1","encrypt_switch":"0","snapshot_switch":0,"cdp_snap_on":"0","cdp_snap_interval":30,"cdp_snap_count":240,"snapshot_interval":"1","snapshot_limit":"24","snapshot_policy":"0","snapshot_start":"","compress":"0","oph_policy":"0","oph_path":"","del_policy":"0","file_type_filter_switch":0,"wk_node_name":"linux-25.11","bk_node_name":"linux-25.12(L)","cdp_switch":"0","cdp_detail_copy":3,"cdp_daily_copy":30,"cdp_process_time":"04:33:34","cdp_baseline_format":"0","cdp_bl_bkup_switch":0,"cdp_bl_sched_switch":0,"band_width":"","cdp_bl_sched":"","wk_path":["/.autofsck","/.autorelabel"],"bk_path":["/1011rep/"],"excl_path":[],"bkup_one_time": None,"auto_start":"1","rep_type":0,"mirr_sched":"","mirr_sched_switch":0,"cmp_file_check":0,"cmp_schedule":[],"cmp_switch":0,"biz_grp_list":[],"mirr_skip":"0","thread_num":"0","ct_name_type":0,"ct_name_str1":"","ct_name_str2":"","cdp_param":"32,30,0"}}
        print(body["uuid"])
        r = repBackup.modifyRepBackup(body)
        print(r[0])

    def testDeleteRepBackup(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
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
        body = {}
        r = repBackup.listRepBackupStatus(body)
        print(r[0])

    def testListRepBackup(self):
        a = Auth(username, pwd)
        repBackup = RepBackup(a)
        body = {}
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
