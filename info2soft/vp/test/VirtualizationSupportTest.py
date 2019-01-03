# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.dashboard.v20181227.Dashboard import Dashboard
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


class DashboardTestCase(unittest.TestCase):

    def testCreateVp(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.createVp(body)
        print(r[0])

    def testDescribeVp(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.describeVp(body)
        print(r[0])

    def testModifyVp(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.modifyVp(body)
        print(r[0])

    def testListVp(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVp(body)
        print(r[0])

    def testListVpStatus(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVpStatus(body)
        print(r[0])

    def testDeleteVp(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.deleteVp(body)
        print(r[0])

    def testListVM(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVM(body)
        print(r[0])

    def testVp(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.vp(body)
        print(r[0])

    def testListBakVer(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listBakVer(body)
        print(r[0])

    def testVp(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.vp(body)
        print(r[0])

    def testVp(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.vp(body)
        print(r[0])

    def testListDatacenter(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listDatacenter(body)
        print(r[0])

    def testListDatacenterHost(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listDatacenterHost(body)
        print(r[0])

    def testListDatastore(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listDatastore(body)
        print(r[0])

    def testListDatastoreInfo(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listDatastoreInfo(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.tempFuncName(body)
        print(r[0])

    def testCreateVpBackup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.createVpBackup(body)
        print(r[0])

    def testModifyVpBackup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.modifyVpBackup(body)
        print(r[0])

    def testDescribeVpBackup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.describeVpBackup(body)
        print(r[0])

    def testDescribeVpBackupGroup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.describeVpBackupGroup(body)
        print(r[0])

    def testListVpBackup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVpBackup(body)
        print(r[0])

    def testListVpBackupGroup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVpBackupGroup(body)
        print(r[0])

    def testListVpBackupStatus(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVpBackupStatus(body)
        print(r[0])

    def testStartVpBackup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.startVpBackup(body)
        print(r[0])

    def testDeleteVpBackup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.deleteVpBackup(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.tempFuncName(body)
        print(r[0])

    def testCreateVpRecovery(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.createVpRecovery(body)
        print(r[0])

    def testDescribeVpRecoveryGroup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.describeVpRecoveryGroup(body)
        print(r[0])

    def testListVpRecovery(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVpRecovery(body)
        print(r[0])

    def testListVpRecoveryStatus(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVpRecoveryStatus(body)
        print(r[0])

    def testStartVpRecovery(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.startVpRecovery(body)
        print(r[0])

    def testDeleteVpRecovery(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.deleteVpRecovery(body)
        print(r[0])

    def testTempFuncName(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.tempFuncName(body)
        print(r[0])

    def testCreateVpMove(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.createVpMove(body)
        print(r[0])

    def testDescribeVpMove(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.describeVpMove(body)
        print(r[0])

    def testModifyVpMove(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.modifyVpMove(body)
        print(r[0])

    def testListVpMove(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVpMove(body)
        print(r[0])

    def testListVpMoveStatus(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVpMoveStatus(body)
        print(r[0])

    def testStopVpMove(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.stopVpMove(body)
        print(r[0])

    def testDeleteVpMove(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.deleteVpMove(body)
        print(r[0])

    def testListVpRepPointList(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.listVpRepPointList(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()
