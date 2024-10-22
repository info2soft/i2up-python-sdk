
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Drill
from info2soft.cdm.v20240819.Drill import Drill
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


class DrillTestCase(unittest.TestCase):

    def testCreateCdmDrill(self):
        a = Auth(username, pwd)
        body = {
            'vm_name': '测试5',
            'vm_ref': 'vm-10811',
            'limit': 3,
            'sched_day': [
            '1',
            '2',
            '3',],
            'sched_time': [
            '00:00',],
            'sched_every': 0,
            'bkup_type': 0,
            'rule_name': '',
            'rule_type': 0,
            'vp_uuid': '',
            'auto': 0,
            'vm_list': [{
            'vm_name': '',
            'new_vm_name': '',
            'bk_uuid': '',
            'time': '',
            'original_rule_uuid': '',
            'scripts': '',
            'bk_path': '',
            'scripts_type': 1,
            'os_type': 1,
            'wk_uuid': '',
            'src_uuid': '',
            'data_ip_uuid': '',
            'ver_sig': '',
            'os_ip': '',},],
            'backup_type': 'i',
            'del_bkup_data': 0,
            'automate': 0,
            'auto_shutdown': 1,
        }
        
        
        drill = Drill(a)
        r = drill.createCdmDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Drill', 'createCdmDrill', body)

    def testDescribeCdmDrill(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        drill = Drill(a)
        r = drill.describeCdmDrill(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Drill', 'describeCdmDrill', body)

    def testDescribeCdmDrillGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        drill = Drill(a)
        r = drill.describeCdmDrillGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Drill', 'describeCdmDrillGroup', body)

    def testDeleteCdmDrill(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'group_uuids': [],
            'delete_tgtvm': 0,
        }
        
        
        drill = Drill(a)
        r = drill.deleteCdmDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Drill', 'deleteCdmDrill', body)

    def testStopCdmDrill(self):
        a = Auth(username, pwd)
        body = {
            'msg': '',
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'group_uuids': [],
            'status': '',
        }
        
        
        drill = Drill(a)
        r = drill.stopCdmDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Drill', 'stopCdmDrill', body)

    def testStartCdmDrill(self):
        a = Auth(username, pwd)
        body = {
            'msg': '',
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'group_uuids': [],
            'status': '',
        }
        
        
        drill = Drill(a)
        r = drill.startCdmDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Drill', 'startCdmDrill', body)

    def testSetStatusCdmDrill(self):
        a = Auth(username, pwd)
        body = {
            'msg': '',
            'operate': '',
            'rule_uuids': '[C6335F62-2565-1957-4BB9-587F2FF46B00]',
            'group_uuids': [],
            'status': '',
        }
        
        
        drill = Drill(a)
        r = drill.setStatusCdmDrill(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Drill', 'setStatusCdmDrill', body)

    def testListCdmDrillStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        
        drill = Drill(a)
        r = drill.listCdmDrillStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Drill', 'listCdmDrillStatus', body)

    def testQueryGroupVmStatus(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'group_uuid': '',
        }
        
        
        drill = Drill(a)
        r = drill.queryGroupVmStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Drill', 'queryGroupVmStatus', body)


if __name__ == '__main__':
    unittest.main()
