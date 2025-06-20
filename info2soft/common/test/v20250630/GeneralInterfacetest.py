
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import GeneralInterface
from info2soft.common.v20250630.GeneralInterface import GeneralInterface
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


class GeneralInterfaceTestCase(unittest.TestCase):
    def setUp(self):
        """在每个测试方法运行前执行"""
        self.original_cwd = os.getcwd()
        # 获取当前测试文件的目录
        test_dir = os.path.dirname(os.path.abspath(__file__))
        # 切换工作目录到测试文件所在的目录
        os.chdir(test_dir)

    def tearDown(self):
        """在每个测试方法运行后执行"""
        # 恢复原始工作目录，避免影响其他测试
        os.chdir(self.original_cwd)

    def testDescribeVersion(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.describeVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'describeVersion', body)

    def testLatestVersion(self):
        a = Auth(username, pwd)
        body = {
            'plat': 'example_plat',
            'kernel_version': '',
            'kernel_module_name': '',
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.latestVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'latestVersion', body)

    def testListVersionHistory(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listVersionHistory(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listVersionHistory', body)

    def testNodeConnectTest(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
            'port': '',
            'type': 'node',
            'node_uuids': [],
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.nodeConnectTest(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'nodeConnectTest', body)

    def testUpMonitorOverall(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.upMonitorOverall(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'upMonitorOverall', body)

    def testOverall(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.overall(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'overall', body)

    def testSysadmin(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.sysadmin(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'sysadmin', body)

    def testStatusOverall(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.statusOverall(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'statusOverall', body)

    def testStatusStreamOverall(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.statusStreamOverall(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'statusStreamOverall', body)

    def testListOverallLogs(self):
        a = Auth(username, pwd)
        body = {
            'get_all': 0,
            'limit': 1,
            'days': '',
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listOverallLogs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listOverallLogs', body)

    def testListOverallResourceSta(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listOverallResourceSta(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listOverallResourceSta', body)

    def testListOverallRealTimeCopy(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listOverallRealTimeCopy(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listOverallRealTimeCopy', body)

    def testListOverallHa(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listOverallHa(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listOverallHa', body)

    def testListOverallCdm(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listOverallCdm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listOverallCdm', body)

    def testListOverallFspMv(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listOverallFspMv(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listOverallFspMv', body)

    def testNodeRepSummary(self):
        a = Auth(username, pwd)
        body = {
            'summary': '',
            'cache': '',
            'rep_rule': '',
            'filter': '',
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.nodeRepSummary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'nodeRepSummary', body)

    def testListVpRuleStat(self):
        a = Auth(username, pwd)
        body = {
            'type': 'VP_PT',
            'wk_uuid': 'AC7A5A1F-5BB1-41D6-E075-1648ADC5C60B',
            'mode': 'month',
            'up_uuids': [],
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listVpRuleStat(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listVpRuleStat', body)

    def testListSchedule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listSchedule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listSchedule', body)

    def testGetDashboardHotColdData(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.getDashboardHotColdData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'getDashboardHotColdData', body)

    def testGetDashboardStatOverall(self):
        a = Auth(username, pwd)
        body = {
            'statistics_days': 1,
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.getDashboardStatOverall(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'getDashboardStatOverall', body)

    def testUpdateDashboardPlate(self):
        a = Auth(username, pwd)
        body = {
            'plate_info': [{
            'name': '',
            'display': 1,},],
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.updateDashboardPlate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'updateDashboardPlate', body)

    def testGetDashboardPlate(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.getDashboardPlate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'getDashboardPlate', body)

    def testCreateColumnExt(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
            'list_col': {
            'wk_ip': {
            'display': '1',
            'width': '100',},
            'bk_ip': {
            'display': '1',},
            'cdp_switch': {
            'display': '1',},
            'name': {
            'display': 1,
            'width': 80,},},
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.createColumnExt(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'createColumnExt', body)

    def testDescribeColumnext(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.describeColumnext(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'describeColumnext', body)

    def testExportRules(self):
        a = Auth(username, pwd)
        body = {
            'suffix': 'csv',
            'type': 'rep_backup',
            'sub_type': '0',
            'where_args': {
            'timing_type': '',
            'raw_uuid': '',},
            'uuids': [],
            'for_import': 0,
            'filter_uuid': '',
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.exportRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'exportRules', body)

    def testImportRules(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
            'file': '',
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.importRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'importRules', body)

    def testListStatisticsReport(self):
        a = Auth(username, pwd)
        body = {
            'start_time': '',
            'end_time': '',
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listStatisticsReport(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listStatisticsReport', body)

    def testCsrSign(self):
        a = Auth(username, pwd)
        body = {
            'csr_file': '''-----BEGIN CERTIFICATE REQUEST-----
MIID7jCCAlYCAQAwgagxCzAJBgNVBAYTAkNOMREwDwYDVQQIDAhTaGFuZ2hhaTEU
MBIGA1UEBwwLR2xhc3RvbmJ1cnkxHjAcBgNVBAoMFUluZm9ybWF0aW9uMiBTb2Z0
d2FyZTEcMBoGA1UECwwTSTJzb2Z0IERldmVsb3AgVGVhbTEMMAoGA1UEAwwDZGV2
MSQwIgYJKoZIhvcNAQkBFhVzdXBwb3J0QGluZm8yc29mdC5jb20wggGiMA0GCSqG
SIb3DQEBAQUAA4IBjwAwggGKAoIBgQDXfZ9/Kxgwyaa9OyYbxbFzn8D4C35PlvyA
XwW7tRrYr9BVfO2k9ZmSb2rVIokhmC69ZSYtpeQkmX8hEdNDraDs+Ikvia5nj96K
MfbVuepfOKEXhVGaLGaXZ/FAlIcobYTTk57KF7k51leSStqc3IC8V+hKfwaMH651
qFXIUZAC/+WZxZU43hedr2+HyDlatkLqluzWAeZLzAYzaad/7sW9MDP9sPQ8Gp1o
J4ib4bDqIP1CtC6ud6A47zjKai1wVfMsZIL2m8AjW39LQQmEx34tDfiv5UKAPOt4
/Oy7x5XlFN5KJNSMnAN+z+Hd6F08jcIUxyMQ8F1rriVS+XlE5ZzM8a93sH80IH2U
odMSkxwy3e6Jm1hgz60+K0Q3KZX3xeH48G7SqVa8iHVsmaqa0BpGEAII73ANDIVr
JFAdQa44AX/080YeUdwZG82ArlCesrE90K7qXu1HEGc9XA2fixYWNbZIuVUxMl2Q
+TEtYTMuREfU4wLvOWWzIcc/JrF5vwkCAwEAAaAAMA0GCSqGSIb3DQEBDAUAA4IB
gQBPnbOV9BuAtEkmVOXO7tu/ZBFc6WbcRAesCb9N+M4Z+JoFwFZBsUTQdrpuIsPQ
SJk6FDB4DyALQ0C0kbnUUczeSTYOc0/tpfarc1cTHU9CYit73UW6Ww/vT1eLB5H1
6vV3b3mRklIPE9dKLYG8lVOGuiKatjL41CI1TdUd+ZuYolCuxcJBBCamMdTCjl3m
cnTDOgPZr9LdWgfYXUpLfZg12+4AyQ1tztPouX6Ux+TMGG7vpV+SzhQmywohwCiv
V/V83RoKbR2IClnaRGnzUg77/KSrP7c1JBmRXNPusos1Yt9qecuoBE3Ky0t7px2k
PTIS4vnLtICCpPHGtsxVHq9ylcu6uSz/ZPGgA0xmzXeilELLvoAzYW+S41qds3XV
UyJ+NLO7M4scciU5zMemBdSbKNbbi4DfofMg15Lc6ljDz2llFhpMdDLOVmbzohkg
SzxWfxCZU7I3oSHr9/WmHxZiDGdzgJKv0WnmIxv0CEfeauzj+tn4vzy/CnutQwY2
K+M=
-----END CERTIFICATE REQUEST-----
''',
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.csrSign(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'csrSign', body)

    def testListCerts(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listCerts(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listCerts', body)

    def testDownloadCa(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.downloadCa(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'downloadCa', body)

    def testListRpcTask(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listRpcTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listRpcTask', body)

    def testListCronTask(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.listCronTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listCronTask', body)

    def testDeleteCronTask(self):
        a = Auth(username, pwd)
        body = {
            'ids': [],
        }
        
        
        generalInterface = GeneralInterface(a)
        r = generalInterface.deleteCronTask(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'deleteCronTask', body)


if __name__ == '__main__':
    unittest.main()
