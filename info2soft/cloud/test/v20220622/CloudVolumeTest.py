
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
sys.path.append(r'/Users/chengl/Desktop/sdk/python-sdk/')

import unittest
# from info2soft import CloudVolume
from info2soft.cloud.v20220622.CloudVolume import CloudVolume
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
    
                
class CloudVolumeTestCase(unittest.TestCase):
    def testListZone(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }
        
        cloudVolume = CloudVolume(a)
        r = cloudVolume.listZone(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudVolume', 'listZone', body)

    def testCreateVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_name': '',
            'cloud_uuid': '',
            'volume_size': '',
            'volume_type': '',
            'server_zone': '',
            'image_ref': '',
        }
        
        cloudVolume = CloudVolume(a)
        r = cloudVolume.createVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudVolume', 'createVolume', body)

    def testDeleteVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        cloudVolume = CloudVolume(a)
        r = cloudVolume.deleteVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudVolume', 'deleteVolume', body)

    def testModifyVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuids': [],
            'ecs_id': '',
            'attach_point': '',
        }
        
        cloudVolume = CloudVolume(a)
        r = cloudVolume.modifyVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudVolume', 'modifyVolume', body)

    def testDetachVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuids': [],
        }
        
        cloudVolume = CloudVolume(a)
        r = cloudVolume.detachVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudVolume', 'detachVolume', body)

    def testListVolume(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'page': 1,
            'limit': 1,
        }
        
        cloudVolume = CloudVolume(a)
        r = cloudVolume.listVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudVolume', 'listVolume', body)

    def testListVolumeStatus(self):
        a = Auth(username, pwd)
        body = {
        }
        
        cloudVolume = CloudVolume(a)
        r = cloudVolume.listVolumeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudVolume', 'listVolumeStatus', body)

    def testListImage(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }
        
        cloudVolume = CloudVolume(a)
        r = cloudVolume.listImage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudVolume', 'listImage', body)

    def testListVolumeEcs(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '501C1AD2-9BE0-D9EF-E860-0F2A10448076',
        }
        
        cloudVolume = CloudVolume(a)
        r = cloudVolume.listVolumeEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudVolume', 'listVolumeEcs', body)

if __name__ == '__main__':
    unittest.main()
