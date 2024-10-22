
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import CdmRule
from info2soft.cdm.v20240819.CdmRule import CdmRule
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


class CdmRuleTestCase(unittest.TestCase):

    def testTakeOverDrillList(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'where_args': [{
            'wk_uuid': 'BC92C981-D637-AC10-7CB0-450504DF8A3C',
            'bk_uuid': 'BC92C981-D637-AC10-7CB0-450504DF8A3C',},],
        }
        
        
        cdmRule = CdmRule(a)
        r = cdmRule.takeOverDrillList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRule', 'takeOverDrillList', body)

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
            'start_switch': 0,
            'vpc_settings': [{
            'work_vpc_id': '',
            'work_network_id': '',
            'work_security_group_id': '',
            'work_ipaddr': '',
            'vpc_id': '',},],
        }
        
        
        cdmRule = CdmRule(a)
        r = cdmRule.createTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRule', 'createTakeOverDrill', body)

    def testDeleteTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force': 1,
            'del_policy': 0,
        }
        
        
        cdmRule = CdmRule(a)
        r = cdmRule.deleteTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRule', 'deleteTakeOverDrill', body)

    def testDescribeTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cdmRule = CdmRule(a)
        r = cdmRule.describeTakeOverDrill(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRule', 'describeTakeOverDrill', body)

    def testGetVmStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
            '0E807AD3-DD1E-9224-2B9B-E713CF258467',
            '1A807AD3-DD1E-9224-2B9B-E713CF258467',],
            'force_refresh': 1,
        }
        
        
        cdmRule = CdmRule(a)
        r = cdmRule.getVmStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRule', 'getVmStatus', body)

    def testStartTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
            'type': '',
        }
        
        
        cdmRule = CdmRule(a)
        r = cdmRule.startTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRule', 'startTakeOverDrill', body)

    def testStopTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
            'type': '',
        }
        
        
        cdmRule = CdmRule(a)
        r = cdmRule.stopTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRule', 'stopTakeOverDrill', body)

    def testOpenConsoleTakeOverDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'operate': '',
            'type': '',
        }
        
        
        cdmRule = CdmRule(a)
        r = cdmRule.openConsoleTakeOverDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRule', 'openConsoleTakeOverDrill', body)


if __name__ == '__main__':
    unittest.main()
