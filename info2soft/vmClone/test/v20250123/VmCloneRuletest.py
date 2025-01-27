
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import VmCloneRule
from info2soft.vmClone.v20250123.VmCloneRule import VmCloneRule
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


class VmCloneRuleTestCase(unittest.TestCase):

    def testCreateVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'wk_path': [],
            'bk_path': [],
            'auto_start': 1,
            'vp_uuid': '',
            'new_dc': '',
            'new_dc_mor': '',
            'new_host': '',
            'new_ds': '',
            'create_vm_type': 1,
            'vm_list': [{
            'vm_name': '',
            'cpu': 1,
            'core_per_sock': 1,
            'mem_mb': 1,
            'networks': [{
            'source_network_name': '',
            'mac_address': '',
            'keep_mac': '',
            'network_id': '',
            'network_name': '',
            'subnet_name': '',
            'auto_ip': False,
            'ip': '',
            'security_group_name': '',
            'gateway': '',},],
            'dns': '',
            'vm_hostname': '',},],
            'vm_cnt': 1,
            'prefix': '',
            'bkup_one_time': 1,
            'bkup_policy': 1,
        }
        
        
        vmCloneRule = VmCloneRule(a)
        r = vmCloneRule.createVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneRule', 'createVmCloneRule', body)

    def testListVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'search_field': '',
            'search_value': '',
        }
        
        
        vmCloneRule = VmCloneRule(a)
        r = vmCloneRule.listVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneRule', 'listVmCloneRule', body)

    def testDescribeVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        vmCloneRule = VmCloneRule(a)
        r = vmCloneRule.describeVmCloneRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneRule', 'describeVmCloneRule', body)

    def testDeleteVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': 1,
            'force': 1,
        }
        
        
        vmCloneRule = VmCloneRule(a)
        r = vmCloneRule.deleteVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneRule', 'deleteVmCloneRule', body)

    def testStartVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'rules_uuid': 1,
            'operate': '',
        }
        
        
        vmCloneRule = VmCloneRule(a)
        r = vmCloneRule.startVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneRule', 'startVmCloneRule', body)

    def testStopVmCloneRule(self):
        a = Auth(username, pwd)
        body = {
            'rules_uuid': 1,
            'operate': '',
        }
        
        
        vmCloneRule = VmCloneRule(a)
        r = vmCloneRule.stopVmCloneRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneRule', 'stopVmCloneRule', body)

    def testListVmCloneRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': 1,
            'force_refresh': '',
        }
        
        
        vmCloneRule = VmCloneRule(a)
        r = vmCloneRule.listVmCloneRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VmCloneRule', 'listVmCloneRuleStatus', body)


if __name__ == '__main__':
    unittest.main()
