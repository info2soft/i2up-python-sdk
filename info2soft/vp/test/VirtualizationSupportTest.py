# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.vp.v20181227.VirtualizationSupport import VirtualizationSupport
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
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.createVp(body)
        print(r[0])

    def testDescribeVp(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.describeVp(body)
        print(r[0])

    def testModifyVp(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.modifyVp(body)
        print(r[0])

    def testListVp(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVp(body)
        print(r[0])

    def testListVpStatus(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpStatus(body)
        print(r[0])

    def testDeleteVp(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.deleteVp(body)
        print(r[0])

    def testListVM(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVM(body)
        print(r[0])

    def testDescribeVpAttribute(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.describeVpAttribute(body)
        print(r[0])

    def testListBakVer(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listBakVer(body)
        print(r[0])

    def testListBakVerInfo(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listBakVerInfo(body)
        print(r[0])

    def testListDatastoreFile(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listDatastoreFile(body)
        print(r[0])

    def testListDatacenter(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listDatacenter(body)
        print(r[0])

    def testListDatacenterHost(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listDatacenterHost(body)
        print(r[0])

    def testListDatastore(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listDatastore(body)
        print(r[0])

    def testListDatastoreInfo(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listDatastoreInfo(body)
        print(r[0])

    def testCreateVpBackup(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.createVpBackup(body)
        print(r[0])

    def testModifyVpBackup(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.modifyVpBackup(body)
        print(r[0])

    def testDescribeVpBackup(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.describeVpBackup(body)
        print(r[0])

    def testDescribeVpBackupGroup(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.describeVpBackupGroup(body)
        print(r[0])

    def testListVpBackup(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpBackup(body)
        print(r[0])

    def testListVpBackupGroup(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpBackupGroup(body)
        print(r[0])

    def testListVpBackupStatus(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpBackupStatus(body)
        print(r[0])

    def testStartVpBackup(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.startVpBackup(body)
        print(r[0])

    def testDeleteVpBackup(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.deleteVpBackup(body)
        print(r[0])

    def testCreateVpRecovery(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.createVpRecovery(body)
        print(r[0])

    def testDescribeVpRecoveryGroup(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.describeVpRecoveryGroup(body)
        print(r[0])

    def testListVpRecovery(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpRecovery(body)
        print(r[0])

    def testListVpRecoveryStatus(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpRecoveryStatus(body)
        print(r[0])

    def testStartVpRecovery(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.startVpRecovery(body)
        print(r[0])

    def testDeleteVpRecovery(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.deleteVpRecovery(body)
        print(r[0])

    def testCreateVpMove(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.createVpMove(body)
        print(r[0])

    def testDescribeVpMove(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.describeVpMove(body)
        print(r[0])

    def testModifyVpMove(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.modifyVpMove(body)
        print(r[0])

    def testListVpMove(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpMove(body)
        print(r[0])

    def testListVpMoveStatus(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpMoveStatus(body)
        print(r[0])

    def testStopVpMove(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.stopVpMove(body)
        print(r[0])

    def testDeleteVpMove(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.deleteVpMove(body)
        print(r[0])

    def testCreateVpRep(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.createVpRep(body)
        print(r[0])

    def testDescribeVpRep(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.describeVpRep(body)
        print(r[0])

    def testModifyVpRep(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.modifyVpRep(body)
        print(r[0])

    def testListVpRep(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpRep(body)
        print(r[0])

    def testListVpRepStatus(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpRepStatus(body)
        print(r[0])

    def testStopVpRep(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.stopVpRep(body)
        print(r[0])

    def testDeleteVpRep(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.deleteVpRep(body)
        print(r[0])

    def testListVpRepPointList(self):
        a = Auth(username, pwd)
        virtualizationSupport = VirtualizationSupport(a)
        body = {}
        r = virtualizationSupport.listVpRepPointList(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()
