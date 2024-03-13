# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.common.v20240228.BigScreen import BigScreen
# from info2soft.common.v20200722.BigScreen import BigScreen
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


class BigScreenTestCase(unittest.TestCase):

    def testCreateBigScreen(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'rule_type': 0,
            'config': {},
            'comment': '',
            'logo_name': 'I2Infomation2',
        }

        bigScreen = BigScreen(a)
        r = bigScreen.createBigScreen(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'createBigScreen', body)

    def testModifyBigScreen(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'comment': '',
            'logo_name': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        bigScreen = BigScreen(a)
        r = bigScreen.modifyBigScreen(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'modifyBigScreen', body)

    def testDescribeBigScreen(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        bigScreen = BigScreen(a)
        r = bigScreen.describeBigScreen(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'describeBigScreen', body)

    def testListBigScreen(self):
        a = Auth(username, pwd)
        body = {
            'rule_type': 1,
            'rule_name': '',
        }

        bigScreen = BigScreen(a)
        r = bigScreen.listBigScreen(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'listBigScreen', body)

    def testDeleteBigScreen(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }

        bigScreen = BigScreen(a)
        r = bigScreen.deleteBigScreen(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'deleteBigScreen', body)

    def testUploadBigScreenLogo(self):
        a = Auth(username, pwd)
        body = {
            'logo_file': '',
            'logo_name': '',
        }

        bigScreen = BigScreen(a)
        r = bigScreen.uploadBigScreenLogo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'uploadBigScreenLogo', body)

    def testDeleteBigScreenLogo(self):
        a = Auth(username, pwd)
        body = {
            'logo_name': '',
        }

        bigScreen = BigScreen(a)
        r = bigScreen.deleteBigScreenLogo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'deleteBigScreenLogo', body)

    def testListBigScreenLogo(self):
        a = Auth(username, pwd)
        body = {
        }

        bigScreen = BigScreen(a)
        r = bigScreen.listBigScreenLogo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'listBigScreenLogo', body)

    def testConfigBigScreen(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
            'rule_uuid': '',
            'config': [{
                'mod_type': 'data_stat',
                'title': [],
                'location': 1,
                'graph_num': 4,
                'scroll_limit': 20,
                'rule_uuids': [],
                'node_uuids': [],
                'db_uuids': [],
                'warn_limit': 1,
                'node_group_uuids': [],
                'warn_modules': [],
                'stat_days': 1,
                'stat_modules': [],
                'vp_uuids': [],
                'display': '', }, {
                'mod_type': 'data_stat',
                'title': [],
                'location': 1,
                'graph_num': 4,
                'scroll_limit': 20,
                'rule_uuids': [],
                'node_uuids': [],
                'db_uuids': [],
                'warn_limit': 1,
                'node_group_uuids': [],
                'warn_modules': [],
                'stat_days': 1,
                'stat_modules': [],
                'vp_uuids': [],
                'display': '', }, ],
        }

        bigScreen = BigScreen(a)
        r = bigScreen.configBigScreen(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'configBigScreen', body)

    def testDescribeBigScreenConfig(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'type': 1,
        }

        bigScreen = BigScreen(a)
        r = bigScreen.describeBigScreenConfig(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'describeBigScreenConfig', body)

    def testClearBigScreenStatData(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }

        bigScreen = BigScreen(a)
        r = bigScreen.clearBigScreenStatData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'clearBigScreenStatData', body)

    def testListBigScreenStatRules(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'mod_type': '',
            'type': '',
        }

        bigScreen = BigScreen(a)
        r = bigScreen.listBigScreenStatRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'listBigScreenStatRules', body)

    def testDescribeBigScreenStat(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'mod_type': '',
        }

        bigScreen = BigScreen(a)
        r = bigScreen.describeBigScreenStat(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'describeBigScreenStat', body)

    def testListBigScreenGraph(self):
        a = Auth(username, pwd)
        body = {
            'mod_type': '',
            'rule_uuid': '',
            'rule_uuids': [],
        }

        bigScreen = BigScreen(a)
        r = bigScreen.listBigScreenGraph(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'BigScreen', 'listBigScreenGraph', body)


if __name__ == '__main__':
    unittest.main()
