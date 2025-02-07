
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import CdmRecovery
from info2soft.cdm.v20250123.CdmRecovery import CdmRecovery
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


class CdmRecoveryTestCase(unittest.TestCase):

    def testCreateCdmRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_recovery': {
            'dst_path': '',
            'monitor_type': 0,
            'net_mapping': [{
            'bk_nic': {
            'type': '0',
            'name': 'Ethernet0',
            'ip': '192.168.72.74/255.255.240.0',},
            'wk_nic': {
            'name': 'Ethernet0',
            'type': '0',
            'ip': '192.168.72.73/255.255.240.0',},},],
            'wk_uuid': '42614852-BB62-1EF7-FED0-D2354BF3149D',
            'mirr_sync_attr': '1',
            'bk_path': [
            '/fsp_bk/192.168.71.77_26821/20190111113656/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/bin/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/boot/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/etc/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/lib/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/lib64/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/root/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/sbin/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/usr/bin/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/usr/lib/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/usr/lib64/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/usr/libexec/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/usr/local/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/usr/sbin/',
            '/fsp_bk/192.168.71.77_26821/20190111113656/var/lib/nfs/',],
            'band_width': '',
            'fsp_name': 'testRC',
            'bk_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'net_mapping_type': '2',
            'mirr_open_type': '0',
            'restore_point': '20190111113656',
            'mirr_file_check': '0',
            'service_uuid': '',
            'excl_path': [],
            'wk_path': [
            '/',
            '/I2FFO/bin/',
            '/I2FFO/boot/',
            '/I2FFO/etc/',
            '/I2FFO/lib/',
            '/I2FFO/lib64/',
            '/I2FFO/root/',
            '/I2FFO/sbin/',
            '/I2FFO/usr/bin/',
            '/I2FFO/usr/lib/',
            '/I2FFO/usr/lib64/',
            '/I2FFO/usr/libexec/',
            '/I2FFO/usr/local/',
            '/I2FFO/usr/sbin/',
            '/I2FFO/var/lib/nfs/',],
            'mirr_sync_flag': '0',
            'fsp_wk_shut_flag': '2',
            'sync_item': '/',
            'failover': '0',
            'fsp_type': '5',
            'random_str': '11111111-1111-1111-1111-111111111111',
            'data_ip_uuid': 'F85DFEC0-149E-373D-0B9E-3DA9A5C43940',
            'by_type': '',
            'bak_wk_uuid': '',
            'bak_wk_address': '',
            'vp_uuid': '',
            'storage_uuid': '',
            'bak_wk_name': '',
            'vm_name': '',
            'vm_ref': '',
            'compress_switch': 1,
            'compress': 1,
            'encrypt_switch': 1,
            'encrypt': '',
            'secret_key': '',},
        }
        
        
        cdmRecovery = CdmRecovery(a)
        r = cdmRecovery.createCdmRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRecovery', 'createCdmRecovery', body)

    def testStartCdmRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'operate': '',
        }
        
        
        cdmRecovery = CdmRecovery(a)
        r = cdmRecovery.startCdmRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRecovery', 'startCdmRecovery', body)

    def testStopCdmRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'operate': '',
        }
        
        
        cdmRecovery = CdmRecovery(a)
        r = cdmRecovery.stopCdmRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRecovery', 'stopCdmRecovery', body)

    def testRecoveryCdmRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'operate': '',
        }
        
        
        cdmRecovery = CdmRecovery(a)
        r = cdmRecovery.recoveryCdmRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRecovery', 'recoveryCdmRecovery', body)

    def testRebootCdmRecovery(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [],
            'operate': '',
        }
        
        
        cdmRecovery = CdmRecovery(a)
        r = cdmRecovery.rebootCdmRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRecovery', 'rebootCdmRecovery', body)

    def testListCdmRecovery(self):
        a = Auth(username, pwd)
        body = {
            'search_value': '',
            'search_field': '',
            'page': 1,
            'limit': 10,
        }
        
        
        cdmRecovery = CdmRecovery(a)
        r = cdmRecovery.listCdmRecovery(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRecovery', 'listCdmRecovery', body)

    def testListCdmRecoveryStatus(self):
        a = Auth(username, pwd)
        body = {
            'fsp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        
        cdmRecovery = CdmRecovery(a)
        r = cdmRecovery.listCdmRecoveryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CdmRecovery', 'listCdmRecoveryStatus', body)


if __name__ == '__main__':
    unittest.main()
