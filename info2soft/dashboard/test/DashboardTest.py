
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

    def testDescribeVpRuleRate(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.describeVpRuleRate(body)
        print(r[0])

    def testDescribeVmProtectRate(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.describeVmProtectRate(body)
        print(r[0])

    def testRepBackup(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.repBackup(body)
        print(r[0])

    def testNode(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.node(body)
        print(r[0])

    def testHa(self):
        a = Auth(username, pwd)
        dashboard = Dashboard(a)
        body = {}
        r = dashboard.ha(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
