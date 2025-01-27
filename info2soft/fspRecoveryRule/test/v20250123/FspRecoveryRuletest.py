
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import FspRecoveryRule
from info2soft.fspRecoveryRule.v20250123.FspRecoveryRule import FspRecoveryRule
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


class FspRecoveryRuleTestCase(unittest.TestCase):

    def testCreateFspRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 1,
            'auto_start': 1,
            'priority': 1,
            'bk_set_uuid': '',
            'backup_chain_policy': 1,
            'wk_uuid': '',
            'wk_path': [],
            'bk_path': [],
            'bios_convert': 1,
            'bios_type': 1,
            'driver_url': '',
            'compress_switch': 1,
            'compress': 1,
            'encrypt_switch': 1,
            'encrypt': 1,
            'start_time': 1,
            'net_mapping': [{
            'bk_nic': {
            'name': '',
            'type': '',
            'ip': '',
            'dns': '',
            'gw': '',},
            'wk_nic': {
            'name': 'Ethernet0',},},],
            'net_mapping_type': 1,
            'dst_path': '',
            'excl_path': [],
            'rc_path_policy': 1,
            'wk_path_list': [],
            'rc_type': 1,
        }
        
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.createFspRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'createFspRecoveryRule', body)

    def testListFspRecoveryRules(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'filter_by_biz_grp': 1,
            'status': '',
            'where_args': {
            'rule_uuid': '',},
            'like_args': {
            'bk_set_id': '',
            'src_node_name': '',
            'rule_name': '',
            'wk_node_name': '',},
        }
        
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.listFspRecoveryRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'listFspRecoveryRules', body)

    def testListFspRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.listFspRecoveryRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'listFspRecoveryRule', body)

    def testDeleteFspRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force': 1,
        }
        
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.deleteFspRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'deleteFspRecoveryRule', body)

    def testModifyFspRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_uuid': '',
            'rule_type': '',
            'random_str': '',
            'create_time': '',
            'auto_start': 1,
            'priority': 1,
            'bk_set_uuid': '',
            'backup_chain_policy': 1,
            'wk_uuid': '',
            'wk_path': '',
            'bk_path': '',
            'bios_convert': 1,
            'bios_type': 1,
            'driver_url': '',
            'compress_switch': 1,
            'compress': 1,
            'encrypt_switch': 1,
            'encrypt': 1,
            'start_time': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.modifyFspRecoveryRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'modifyFspRecoveryRule', body)

    def testStartFspRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
        }
        
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.startFspRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'startFspRecoveryRule', body)

    def testStopFspRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
        }
        
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.stopFspRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'stopFspRecoveryRule', body)

    def testRebootFspRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuids': [],
        }
        
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.rebootFspRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'rebootFspRecoveryRule', body)

    def testListFspRecoveryRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.listFspRecoveryRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'listFspRecoveryRuleStatus', body)

    def testGetFspRecoveryRuleBiosType(self):
        a = Auth(username, pwd)
        body = {
            'device_list': [],
            'node_uuid': '',
        }
        
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.getFspRecoveryRuleBiosType(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'getFspRecoveryRuleBiosType', body)

    def testListFspRecoveryRuleDriverListUrl(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        fspRecoveryRule = FspRecoveryRule(a)
        r = fspRecoveryRule.listFspRecoveryRuleDriverListUrl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'FspRecoveryRule', 'listFspRecoveryRuleDriverListUrl', body)


if __name__ == '__main__':
    unittest.main()
