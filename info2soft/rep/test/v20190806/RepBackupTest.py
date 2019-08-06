# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.rep.v20181227.RepBackup import RepBackup
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


class RepBackupTestCase(unittest.TestCase):

    def testListRepBackupCdpZfs(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
        }
        repBackup = RepBackup(a)
        r = repBackup.listRepBackupCdpZfs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'RepBackup', 'listRepBackupCdpZfs', body)


if __name__ == '__main__':
    unittest.main()
