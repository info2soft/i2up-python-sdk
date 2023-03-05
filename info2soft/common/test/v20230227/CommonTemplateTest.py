# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.common.v20230227.CommonTemplate import CommonTemplate
# from info2soft.common.v20200722.CommonTemplate import CommonTemplate
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


class CommonTemplateTestCase(unittest.TestCase):

    def testCreateCommonTemplate(self):
        a = Auth(username, pwd)
        body = {
            'common_template': {
                'template_name': '',
                'template_type': 1,
                'template_text': '', },
        }

        commonTemplate = CommonTemplate(a)
        r = commonTemplate.createCommonTemplate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CommonTemplate', 'createCommonTemplate', body)

    def testDescribeCommonTemplate(self):
        a = Auth(username, pwd)
        body = {
            'template_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        commonTemplate = CommonTemplate(a)
        r = commonTemplate.describeCommonTemplate(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CommonTemplate', 'describeCommonTemplate', body)

    def testModifyCommonTemplate(self):
        a = Auth(username, pwd)
        body = {
            'common_template': {
                'template_name': '',
                'template_type': 1,
                'template_text': '', },
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        commonTemplate = CommonTemplate(a)
        r = commonTemplate.modifyCommonTemplate(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CommonTemplate', 'modifyCommonTemplate', body)

    def testDeleteCommonTemplate(self):
        a = Auth(username, pwd)
        body = {
            'template_uuid': [],
        }

        commonTemplate = CommonTemplate(a)
        r = commonTemplate.deleteCommonTemplate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CommonTemplate', 'deleteCommonTemplate', body)

    def testListCommonTemplate(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 1,
            'search_field': '',
            'search_value': '',
        }

        commonTemplate = CommonTemplate(a)
        r = commonTemplate.listCommonTemplate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CommonTemplate', 'listCommonTemplate', body)


if __name__ == '__main__':
    unittest.main()
