
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.v20181227.Monitor import Monitor
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
    
                
class MonitorTestCase(unittest.TestCase):

    def testListDriversInfo(self):
        a = Auth(username, pwd)
        monitor = Monitor(a)
        body = {}
        r = monitor.listDriversInfo(body)
        print(r[0])

    def testListPhyInfo(self):
        a = Auth(username, pwd)
        monitor = Monitor(a)
        body = {}
        r = monitor.listPhyInfo(body)
        print(r[0])

    def testListChartConfig(self):
        a = Auth(username, pwd)
        monitor = Monitor(a)
        body = {}
        r = monitor.listChartConfig(body)
        print(r[0])

    def testSetChartConfig(self):
        a = Auth(username, pwd)
        monitor = Monitor(a)
        body = {}
        r = monitor.setChartConfig(body)
        print(r[0])

    def testListChartData(self):
        a = Auth(username, pwd)
        monitor = Monitor(a)
        body = {}
        r = monitor.listChartData(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
