
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import TapeRecovery
from info2soft.tape.v20250123.TapeRecovery import TapeRecovery
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


class TapeRecoveryTestCase(unittest.TestCase):

    def testListTapeRecovery(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
        }
        
        
        tapeRecovery = TapeRecovery(a)
        r = tapeRecovery.listTapeRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeRecovery', 'listTapeRecovery', body)

    def testCreateTapeRecovery(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'library_sn': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'bk_index': '',
            'bk_path': '',
            'bk_files': [{
            'file_path_name': '',},],
            'rec_path': '',
            'rule_name': '',
            'recover_all': 0,
            'bk_data_type': 1,
            'pool_uuid': '',
            'volume_uuid': '',
            'tape_pool_uuid': '',
            'tape_uuid': '',
            'auto_start': 1,
            'appointment_time': 1664248414,
        }
        
        
        tapeRecovery = TapeRecovery(a)
        r = tapeRecovery.createTapeRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeRecovery', 'createTapeRecovery', body)

    def testDescribeTapeRecovery(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        tapeRecovery = TapeRecovery(a)
        r = tapeRecovery.describeTapeRecovery(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeRecovery', 'describeTapeRecovery', body)

    def testDeleteTapeRecovery(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        
        tapeRecovery = TapeRecovery(a)
        r = tapeRecovery.deleteTapeRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeRecovery', 'deleteTapeRecovery', body)

    def testListTapeRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'force_refresh': 1,
        }
        
        
        tapeRecovery = TapeRecovery(a)
        r = tapeRecovery.listTapeRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'TapeRecovery', 'listTapeRecoveryStatus', body)


if __name__ == '__main__':
    unittest.main()
