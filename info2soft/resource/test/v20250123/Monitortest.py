
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Monitor
from info2soft.resource.v20250123.Monitor import Monitor
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


class MonitorTestCase(unittest.TestCase):

    def testListDriversInfo(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        monitor = Monitor(a)
        r = monitor.listDriversInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Monitor', 'listDriversInfo', body)

    def testListPhyInfo(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        monitor = Monitor(a)
        r = monitor.listPhyInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Monitor', 'listPhyInfo', body)

    def testListChartData(self):
        a = Auth(username, pwd)
        body = {
            'start_time': 1546272000,
            'last_time': 1548950400,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        monitor = Monitor(a)
        r = monitor.listChartData(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Monitor', 'listChartData', body)

    def testListChartConfig(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        monitor = Monitor(a)
        r = monitor.listChartConfig(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Monitor', 'listChartConfig', body)

    def testSetChartConfig(self):
        a = Auth(username, pwd)
        body = {
            'storage_io': 1,
            'nic_io': 0,
            'per_core': 1,
            'per_disk': 0,
            'net_in': 0,
            'net_out': 0,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        monitor = Monitor(a)
        r = monitor.setChartConfig(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Monitor', 'setChartConfig', body)

    def testListBkNodeOverall(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        monitor = Monitor(a)
        r = monitor.listBkNodeOverall(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Monitor', 'listBkNodeOverall', body)


if __name__ == '__main__':
    unittest.main()
