
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Summary
from info2soft.active.v20250123.Summary import Summary
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


class SummaryTestCase(unittest.TestCase):

    def testListSummaryView(self):
        a = Auth(username, pwd)
        body = {
            'src_db': '',
            'tgt_db': '',
            'status': '',
            'type': '',
            'rule_name': '',
        }
        
        
        summary = Summary(a)
        r = summary.listSummaryView(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Summary', 'listSummaryView', body)

    def testListSummary(self):
        a = Auth(username, pwd)
        body = {
            'status': [],
        }
        
        
        summary = Summary(a)
        r = summary.listSummary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Summary', 'listSummary', body)


if __name__ == '__main__':
    unittest.main()
