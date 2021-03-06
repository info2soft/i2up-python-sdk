
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.common.Monitor import Monitor
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
    
                
class MonitorTestCase(unittest.TestCase):

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
