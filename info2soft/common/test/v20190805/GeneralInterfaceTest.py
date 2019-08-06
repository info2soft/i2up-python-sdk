
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.GeneralInterface import GeneralInterface
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
    
                
class GeneralInterfaceTestCase(unittest.TestCase):

    def testListStatisticsChart(self):
        a = Auth(username, pwd)
        body = {
            'start': 1,
            'src_type': '0',
            'end': 2,
            'type': 'I2BAK_BK',
        }
        generalInterface = GeneralInterface(a)
        r = generalInterface.listStatisticsChart(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listStatisticsChart', body)

    def testUpMonitorOverall(self):
        a = Auth(username, pwd)
        body = {
        }
        generalInterface = GeneralInterface(a)
        r = generalInterface.upMonitorOverall(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'upMonitorOverall', body)


if __name__ == '__main__':
    unittest.main()  
