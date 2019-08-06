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

    def testUpdateDataAgentVp(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'update_data_agent',
            'vp_uuids': ['11111111-1111-1111-1111-111111111111'],
        }
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.updateDataAgentVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'updateDataAgentVp', body)

    def testDescribeVpFileRecoveryVmIp(self):
        a = Auth(username, pwd)
        body = {
            'recovery_uuid': '',
        }
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpFileRecoveryVmIp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpFileRecoveryVmIp', body)

    def testVpFileRecoveryLivecdPartition(self):
        a = Auth(username, pwd)
        body = {
            'recovery_uuid': 'A2D048Cd-54F1-4CD9-D58D-dCC811fEe3D8',
            'bk_ip': '',
        }
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.vpFileRecoveryLivecdPartition(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'vpFileRecoveryLivecdPartition', body)

    def testCreateVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
            'wk_ip': '',
            'os_user': '',
            'os_pwd': '',
            'wk_port': 26888,
            'wk_path': [],
            'is_override': 0,
            'rule_name': '',
            'recovery_uuid': '',
            'bk_path': [],
            'bk_ip': '',
            'is_remote': 1,
        }
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.createVpFileRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVpFileRecovery', body)

    def testDescribeVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpFileRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpFileRecovery', body)

    def testListVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpFileRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpFileRecovery', body)

    def testListVpFileRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111'],
        }
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpFileRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpFileRecoveryStatus', body)

    def testDeleteVpFileRecovery(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': ['11111111-1111-1111-1111-111111111111'],
        }
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.deleteVpFileRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVpFileRecovery', body)


if __name__ == '__main__':
    unittest.main()
