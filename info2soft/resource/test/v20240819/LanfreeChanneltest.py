
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import LanfreeChannel
from info2soft.resource.v20240819.LanfreeChannel import LanfreeChannel
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


class LanfreeChannelTestCase(unittest.TestCase):

    def testCreateLanfreeChannel(self):
        a = Auth(username, pwd)
        body = {
            'channel_name': '',
            'channel_uuid': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'protocol': 1,
            'fc_target_wwpn': '',
            'fc_initiator_wwpn': '',
            'iscsi_initiator': '',
            'target_port': '',
            'data_ip_uuid': '',
            'sub_channel_num': 1,
        }
        
        
        lanfreeChannel = LanfreeChannel(a)
        r = lanfreeChannel.createLanfreeChannel(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LanfreeChannel', 'createLanfreeChannel', body)

    def testListLanfreeChannel(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        lanfreeChannel = LanfreeChannel(a)
        r = lanfreeChannel.listLanfreeChannel(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LanfreeChannel', 'listLanfreeChannel', body)

    def testDescribeLanfreeChannel(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        lanfreeChannel = LanfreeChannel(a)
        r = lanfreeChannel.describeLanfreeChannel(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LanfreeChannel', 'describeLanfreeChannel', body)

    def testModifyLanfreeChannel(self):
        a = Auth(username, pwd)
        body = {
            'channel_name': '',
            'channel_uuid': '',
            'wk_uuid': '',
            'bk_uuid': '',
            'protocol': 1,
            'fc_target_wwpn': '',
            'fc_initiator_wwpn': '',
            'random_str': '1CCDB5EB848C180F02814E96C2909202',
            'iscsi_initiator': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        lanfreeChannel = LanfreeChannel(a)
        r = lanfreeChannel.modifyLanfreeChannel(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LanfreeChannel', 'modifyLanfreeChannel', body)

    def testDeleteLanfreeChannel(self):
        a = Auth(username, pwd)
        body = {
            'channel_uuids': [],
            'force': 1,
        }
        
        
        lanfreeChannel = LanfreeChannel(a)
        r = lanfreeChannel.deleteLanfreeChannel(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LanfreeChannel', 'deleteLanfreeChannel', body)

    def testListLanfreeChannelStatus(self):
        a = Auth(username, pwd)
        body = {
            'channel_uuids': [],
            'force_refresh': 1,
        }
        
        
        lanfreeChannel = LanfreeChannel(a)
        r = lanfreeChannel.listLanfreeChannelStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LanfreeChannel', 'listLanfreeChannelStatus', body)

    def testListLanfreeChannelByWkBk(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuids': [],
            'unit_uuid': '',
            'bk_set_uuids': [],
            'bk_uuids': [],
            'unit_uuids': [],
        }
        
        
        lanfreeChannel = LanfreeChannel(a)
        r = lanfreeChannel.listLanfreeChannelByWkBk(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LanfreeChannel', 'listLanfreeChannelByWkBk', body)

    def testListLanfreeChannelInfo(self):
        a = Auth(username, pwd)
        body = {
            'channel_uuid': '',
        }
        
        
        lanfreeChannel = LanfreeChannel(a)
        r = lanfreeChannel.listLanfreeChannelInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'LanfreeChannel', 'listLanfreeChannelInfo', body)


if __name__ == '__main__':
    unittest.main()
