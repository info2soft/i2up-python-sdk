# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.timing.v20181227.TimingRecovery import TimingRecovery
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


class TimingBackupTestCase(unittest.TestCase):

    def testListTimingRecoveryDb(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': 'B8566905-411E-B2CD-A742-77B1346D8E84',
            'rc_data_path': 'E:\\mssqlBK\\ts-11111111-1111-1111-1111-111111111111\\',
        }
        timingRecovery = TimingRecovery(a)
        r = timingRecovery.listTimingRecoveryDb(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TimingBackup', 'listTimingRecoveryDb', body)


if __name__ == '__main__':
    unittest.main()
