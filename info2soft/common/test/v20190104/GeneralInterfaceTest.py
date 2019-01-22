
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

    def testDescribeVersion(self):
        a = Auth(username, pwd)
        generalInterface = GeneralInterface(a)
        r = generalInterface.describeVersion()
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'describeVersion', None)

    def testUpdateDatabase(self):
        a = Auth(username, pwd)
        generalInterface = GeneralInterface(a)
        r = generalInterface.updateDatabase()
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'updateDatabase', None)

    def testListStatistics(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'end': 1848122966,
            'name': 'c',
            'limit': 10,
            'start': 1548122966,
            'status': '',
            'type': '',
            'result': 0,
            'group_uuid': '',
            'uuid': '',
        }
        generalInterface = GeneralInterface(a)
        r = generalInterface.listStatistics(body)
        print(r[0])
        # assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'listStatistics', body)

    def testDescribeStatistics(self):
        a = Auth(username, pwd)
        body = {
            'id': '2'
        }
        generalInterface = GeneralInterface(a)
        r = generalInterface.describeStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'describeStatistics', body)

    def testReadStatistics(self):
        a = Auth(username, pwd)
        body = {
            'type': 'I2VP_BK',
        }
        generalInterface = GeneralInterface(a)
        r = generalInterface.readStatistics(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'readStatistics', body)

    def testOverall(self):
        a = Auth(username, pwd)
        generalInterface = GeneralInterface(a)
        r = generalInterface.overall()
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'GeneralInterface', 'overall', None)


if __name__ == '__main__':
    unittest.main()  
