
# -*- coding: utf-8 -*-
# flake8: noqa

import unittest
from info2soft.active.v20181227.Mask import Mask
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
    
                
class MaskTestCase(unittest.TestCase):

    def testListTypes(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        mask = Mask(a)
        r = mask.listTypes(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listTypes', body)

    def testCreateAlgo(self):
        a = Auth(username, pwd)
        body = {
            'ava_sens_type': 1,
            'parent_id': 1,
            'algo_name': '',
            'description': '',
            'params': '',
            'sort': '',
        }
        mask = Mask(a)
        r = mask.createAlgo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createAlgo', body)

    def testListAlgos(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        mask = Mask(a)
        r = mask.listAlgos(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listAlgos', body)

    def testListMaskRules(self):
        a = Auth(username, pwd)
        body = {
            'limit': 10,
            'page': 0,
        }
        mask = Mask(a)
        r = mask.listMaskRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listMaskRules', body)

    def testCreateMaskRules(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': '',
            'src_db_uuid': '',
            'tgt_db_uuid': '',
            'strate': [{
            'sens_map_id': 1,
            'mask_algo_id': 1,},],
            'load_thread': 9,
            'compress_level': 5,
        }
        mask = Mask(a)
        r = mask.createMaskRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createMaskRules', body)

    def testDeleteMaskRule(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        mask = Mask(a)
        r = mask.deleteMaskRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'deleteMaskRule', body)

    def testListMaskRuleStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        mask = Mask(a)
        r = mask.listMaskRuleStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listMaskRuleStatus', body)

    def testListMap(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }
        mask = Mask(a)
        r = mask.listMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listMap', body)

    def testCreateMap(self):
        a = Auth(username, pwd)
        body = {
            'map_name': '',
            'sens_type_id': '',
            'sens_column': [{
            'user': 'I2MASK',
            'table': 'MP',
            'column': 'MP',},],
        }
        mask = Mask(a)
        r = mask.createMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createMap', body)

    def testModifyMap(self):
        a = Auth(username, pwd)
        body = {
            'map_name': '',
            'sens_type_id': '',
            'sens_column': [{
            'user': 'I2MASK',
            'table': 'MP',
            'column': 'MP',},],
        }
        mask = Mask(a)
        r = mask.modifyMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'modifyMap', body)

    def testDeleteMap(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        mask = Mask(a)
        r = mask.deleteMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'deleteMap', body)

    def testDescriptMap(self):
        a = Auth(username, pwd)
        body = {
        }
        mask = Mask(a)
        r = mask.descriptMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'descriptMap', body)

    def testCreateDbMap(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '',
            'map_name': '',
        }
        mask = Mask(a)
        r = mask.createDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createDbMap', body)

    def testListDbMap(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        mask = Mask(a)
        r = mask.listDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listDbMap', body)

    def testDeleteDbMap(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        mask = Mask(a)
        r = mask.deleteDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'deleteDbMap', body)

    def testModifyDbMap(self):
        a = Auth(username, pwd)
        body = {
        }
        mask = Mask(a)
        r = mask.modifyDbMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'modifyDbMap', body)

    def testCreateSensCheck(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'src_db_uuid': '',
            'users': '',
            'tabs': '',
            'row': '',
            'min': '',
            'types': [{
            'type_id': 1,
            'type_arg': '',},],
        }
        mask = Mask(a)
        r = mask.createSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'createSensCheck', body)

    def testModifySensCheck(self):
        a = Auth(username, pwd)
        body = {
            'task_name': '',
            'src_db_uuid': '',
            'users': '',
            'tabs': '',
            'row': '',
            'min': '',
            'types': [{
            'type_id': 1,
            'type_arg': '',},],
        }
        mask = Mask(a)
        r = mask.modifySensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'modifySensCheck', body)

    def testDeleteSensCheck(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
        }
        mask = Mask(a)
        r = mask.deleteSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'deleteSensCheck', body)

    def testListSensCheck(self):
        a = Auth(username, pwd)
        body = {
            'page': 0,
            'limit': 10,
        }
        mask = Mask(a)
        r = mask.listSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'listSensCheck', body)

    def testDescriptSensCheck(self):
        a = Auth(username, pwd)
        body = {
        }
        mask = Mask(a)
        r = mask.descriptSensCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Mask', 'descriptSensCheck', body)


if __name__ == '__main__':
    unittest.main()
