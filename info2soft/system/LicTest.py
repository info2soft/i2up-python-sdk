
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.system.v20181227.Lic import Lic
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
    
                
class LicTestCase(unittest.TestCase):

    def testDescribeActivateInfo(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.describeActivateInfo(body)
        print(r[0])

    def testDownloadLicInfo(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.downloadLicInfo(body)
        print(r[0])

    def testDescribeLicCcHwCode(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.describeLicCcHwCode(body)
        print(r[0])

    def testDescribeLicObjHwCode(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.describeLicObjHwCode(body)
        print(r[0])

    def testActivateLicAll(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.activateLicAll(body)
        print(r[0])

    def testCreateLic(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.createLic(body)
        print(r[0])

    def testUpdateLic(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.updateLic(body)
        print(r[0])

    def testUpdateBatchLic(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.updateBatchLic(body)
        print(r[0])

    def testDescribeLic(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {
            'uuid': '6847CBD7-DEB2-9D08-A35F-ED907803CAD8'
        }
        r = lic.describeLic(body)
        print(r[0])

    def testListLic(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.listLic(body)
        print(r[0])

    def testDeleteLic(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.deleteLic(body)
        print(r[0])

    def testListLicObjBind(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.listLicObjBind(body)
        print(r[0])

    def testListLicBind(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.listLicBind(body)
        print(r[0])

    def testUpdateLicBind(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.updateLicBind(body)
        print(r[0])

    def testListLicObj(self):
        a = Auth(username, pwd)
        lic = Lic(a)
        body = {}
        r = lic.listLicObj(body)
        print(r[0])


if __name__ == '__main__':
    unittest.main()  
