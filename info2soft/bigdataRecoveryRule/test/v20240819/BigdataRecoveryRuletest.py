
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import BigdataRecoveryRule
from info2soft.bigdataRecoveryRule.v20240819.BigdataRecoveryRule import BigdataRecoveryRule
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


class BigdataRecoveryRuleTestCase(unittest.TestCase):

    def testListBigdataRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'filter_by_biz_grp': 1,
            'status': '',
            'where_args': {
            'rule_uuid': '',},
            'like_args': {
            'rule_name': '',},
        }
        
        
        bigdataRecoveryRule = BigdataRecoveryRule(a)
        r = bigdataRecoveryRule.listBigdataRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataRecoveryRule', 'listBigdataRecoveryRule', body)

    def testCreateBigdataRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'data_type': 1,
            'biz_grp_list': [],
            'auto_start': 1,
            'start_time': 1,
            'priority': 90000,
            'bk_set_uuid': '',
            'rc_mode': 1,
            'platform_uuid': '',
            'rc_path_policy': 1,
            'backup_chain_policy': 1,
            'bk_path': [],
            'wk_path': [],
            'mirr_file_check': 1,
            'mirr_sync_flag': 1,
            'oph_policy': 1,
            'sel_db': [],
            'sel_tbl': [],
            'sel_part': [],
            'hive_bk_type': '',
            'band_width': '',
        }
        
        
        bigdataRecoveryRule = BigdataRecoveryRule(a)
        r = bigdataRecoveryRule.createBigdataRecoveryRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataRecoveryRule', 'createBigdataRecoveryRule', body)

    def testModifyBigdataRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'data_type': 1,
            'biz_grp_list': [],
            'auto_start': 1,
            'start_time': 1,
            'priority': 90000,
            'bk_set_uuid': '',
            'rc_mode': 1,
            'platform_uuid': '',
            'rc_path_policy': 1,
            'backup_chain_policy': 1,
            'bk_path': [],
            'wk_path': [],
            'mirr_file_check': 1,
            'mirr_sync_flag': 1,
            'oph_policy': 1,
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bigdataRecoveryRule = BigdataRecoveryRule(a)
        r = bigdataRecoveryRule.modifyBigdataRecoveryRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataRecoveryRule', 'modifyBigdataRecoveryRule', body)

    def testDescribeBigdataRecoveryRule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        bigdataRecoveryRule = BigdataRecoveryRule(a)
        r = bigdataRecoveryRule.describeBigdataRecoveryRule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataRecoveryRule', 'describeBigdataRecoveryRule', body)

    def testListBigdataRecoveryRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': '',
        }
        
        
        bigdataRecoveryRule = BigdataRecoveryRule(a)
        r = bigdataRecoveryRule.listBigdataRecoveryRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigdataRecoveryRule', 'listBigdataRecoveryRuleStatus', body)


if __name__ == '__main__':
    unittest.main()
