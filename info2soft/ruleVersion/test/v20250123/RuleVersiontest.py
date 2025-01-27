
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import RuleVersion
from info2soft.ruleVersion.v20250123.RuleVersion import RuleVersion
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


class RuleVersionTestCase(unittest.TestCase):

    def testListRuleVersion(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'where_args': {
            'uuid': '',
            'type': '',},
            'like_args': {
            'sys_name': '',
            'protect_name': '',},
        }
        
        
        ruleVersion = RuleVersion(a)
        r = ruleVersion.listRuleVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleVersion', 'listRuleVersion', body)

    def testDescribeRuleVersionInfo(self):
        a = Auth(username, pwd)
        body = {
            'id': 1,
        }
        
        
        ruleVersion = RuleVersion(a)
        r = ruleVersion.describeRuleVersionInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleVersion', 'describeRuleVersionInfo', body)

    def testSetMainRuleVersion(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'ids': [],
        }
        
        
        ruleVersion = RuleVersion(a)
        r = ruleVersion.setMainRuleVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RuleVersion', 'setMainRuleVersion', body)


if __name__ == '__main__':
    unittest.main()
