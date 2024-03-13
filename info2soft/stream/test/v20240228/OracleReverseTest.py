
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import OracleReverse
from info2soft.stream.v20240228.OracleReverse import OracleReverse
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


class OracleReverseTestCase(unittest.TestCase):

    def testCreateReverse(self):
        a = Auth(username, pwd)
        body = {
            'reverse_name': '',
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'start_scn': 123,
            'rowid_thd': 5,
            'row_map_mode': '"rowid"',
        }
        
        oracleReverse = OracleReverse(a)
        r = oracleReverse.createReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleReverse', 'createReverse', body)


if __name__ == '__main__':
    unittest.main()
