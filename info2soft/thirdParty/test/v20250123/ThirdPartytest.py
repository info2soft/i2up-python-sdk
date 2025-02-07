
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import ThirdParty
from info2soft.thirdParty.v20250123.ThirdParty import ThirdParty
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


class ThirdPartyTestCase(unittest.TestCase):

    def testGetThirdPartiesUrl(self):
        a = Auth(username, pwd)
        body = {
            'key': '步图领机听分',
        }
        
        
        thirdParty = ThirdParty(a)
        r = thirdParty.getThirdPartiesUrl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ThirdParty', 'getThirdPartiesUrl', body)


if __name__ == '__main__':
    unittest.main()
