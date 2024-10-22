
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import VirtualizationSupport
from info2soft.resource.v20240819.VirtualizationSupport import VirtualizationSupport
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


class VirtualizationSupportTestCase(unittest.TestCase):

    def testCreateVp(self):
        a = Auth(username, pwd)
        body = {
            'comment': '',
            'os_pwd': '12345678',
            'os_usr': 'root',
            'vp_addr': '192.168.88.107',
            'vp_name': 'test',
            'vp_type': 0,
            'biz_grp_list': [],
            'use_credential': 0,
            'cred_uuid': '',
            'is_drill': 1,
            'drill_config': {
            'proxy_name': '',
            'proxy_ip': '',
            'proxy_mask': '',
            'proxy_gw': '',
            'new_hostname': '',
            'new_ds': '',
            'new_dc': '',
            'new_dcmor': '',
            'network_name': '',
            'network_id': '',
            'rpc_port': '',
            'orch_vm_network_name': '',
            'orch_vm_network_id': '',
            'system_uuid': '',
            'subnet_name': '',
            'security_group_name': '',
            'orch_vm_subnet_name': '',
            'orch_security_group_name': '',
            'subnet_cidr': '',
            'location': '',
            'location_name': '',},
            'is_backup_center': 1,
            'maintenance': 0,
            'data_transmission_port': 902,
            'is_ssl': 1,
            'monitor_storage_switch': 1,
            'monitor_storages': [{
            'name': '',
            'storage_id': '',},],
            'monitor_storage_threshold': 1,
            'npsvr_uuid': '',
            'connect_port': 443,
            'region': '',
            'authurl': '',
            'register_type': '',
            'iam_user': '',
            'user_domain_id': '',
            'project_id': '',
            'mfa_switch': 1,
            'access_key': '',
            'secret_access_key': '',
            'user_domain_name': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.createVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createVp', body)

    def testModifyVp(self):
        a = Auth(username, pwd)
        body = {
            'comment': '',
            'os_pwd': '12345678',
            'os_usr': 'root',
            'vp_addr': '192.168.88.107',
            'vp_name': 'test',
            'vp_type': 0,
            'biz_grp_list': [],
            'use_credential': 0,
            'cred_uuid': '',
            'is_drill': 1,
            'drill_config': {
            'proxy_name': '',
            'proxy_ip': '',
            'proxy_mask': '',
            'proxy_gw': '',
            'new_hostname': '',
            'new_ds': '',
            'new_dc': '',
            'new_dcmor': '',
            'network_name': '',
            'network_id': '',
            'rpc_port': '',
            'orch_vm_network_name': '',
            'orch_vm_network_id': '',
            'system_uuid': '',
            'subnet_name': '',
            'security_group_name': '',
            'orch_vm_subnet_name': '',
            'orch_security_group_name': '',
            'subnet_cidr': '',
            'location': '',
            'location_name': '',},
            'is_backup_center': 1,
            'maintenance': 0,
            'data_transmission_port': 902,
            'is_ssl': 1,
            'monitor_storage_switch': 1,
            'monitor_storages': [{
            'name': '',
            'storage_id': '',},],
            'monitor_storage_threshold': 1,
            'npsvr_uuid': '',
            'connect_port': 443,
            'region': '',
            'authurl': '',
            'register_type': '',
            'iam_user': '',
            'user_domain_id': '',
            'project_id': '',
            'mfa_switch': 1,
            'access_key': '',
            'secret_access_key': '',
            'user_domain_name': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.modifyVp(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'modifyVp', body)

    def testListVp(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'status': '',
            'filter_by_biz_grp': 1,
            'where_args': {
            'vp_type': '',
            'vp_uuid': '',},
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVp', body)

    def testDescribeVp(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVp(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVp', body)

    def testListVpStatus(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpStatus', body)

    def testUpdateDataAgentVp(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'update_data_agent',
            'vp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'switch': 0,
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.updateDataAgentVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'updateDataAgentVp', body)

    def testDeleteVp(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuids': [
            '11111111-1111-1111-1111-111111111111',],
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.deleteVp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'deleteVp', body)

    def testListVM(self):
        a = Auth(username, pwd)
        body = {
            'type': '',
            'id': '',
            'view_type': '',
            'search_name': '',
            'force_rpc': '',
            'show_vm': '',
            'project_id': '',
            'region_id': '',
            'vm_uuid': '',
            'vm_ref': '',
            'has_backup_set': 1,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVM(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVM', body)

    def testListVmNoHierarchy(self):
        a = Auth(username, pwd)
        body = {
            'search_name': '',
            'force_rpc': '',
            'vm_uuid': '',
            'vm_ref': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVmNoHierarchy(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVmNoHierarchy', body)

    def testGetVmInfo(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'vm_id': '',
            'region_id': '',
            'project_id': '',
            'vm_name': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.getVmInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'getVmInfo', body)

    def testDescribeVpAttribute(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeVpAttribute(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeVpAttribute', body)

    def testListBakVer(self):
        a = Auth(username, pwd)
        body = {
            'bk_path': 'H:\\vp_bk5\\test2_BAK_vm-11880_192.168.88.22\\',
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'rule_uuid': '',
            'sto_uuid': '',
            'bucket': '',
            'bucket_path': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listBakVer(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listBakVer', body)

    def testListBakVerInfo(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '67E33CDB-D75B-15B3-367D-50C764F5A26F',
            'bk_path': 'H:\\vp_bk5\\testRC1_BAK_99_192.168.85.139',
            'ver_sig': 'A59DB76E-E33D-4E22-BB08-59723B1FC539',
            'group_uuid': '',
            'time': '2019-01-07_13-10-45',
            'bucket': '',
            'sto_uuid': '',
            'bucket_path': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listBakVerInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listBakVerInfo', body)

    def testListDatastoreFile(self):
        a = Auth(username, pwd)
        body = {
            'dir_file': '/',
            'ds_name': 'datastore107（1）',
            'dc_name': 'ha-datacenter',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listDatastoreFile(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatastoreFile', body)

    def testListDatacenter(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listDatacenter(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatacenter', body)

    def testListDatacenterHost(self):
        a = Auth(username, pwd)
        body = {
            'dc_name': 'ha-datacenter',
            'dc_mor': 'ha-datacenter',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listDatacenterHost(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatacenterHost', body)

    def testListResourcePool(self):
        a = Auth(username, pwd)
        body = {
            'id': '',
            'type': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listResourcePool(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listResourcePool', body)

    def testListDatastore(self):
        a = Auth(username, pwd)
        body = {
            'host_name': 'dev-esxi.6.6.6',
            'path': '/',
            'scope': '',
            'dc_name': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listDatastore(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatastore', body)

    def testListDatastoreInfo(self):
        a = Auth(username, pwd)
        body = {
            'ds_name': 'datastore107（1）',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listDatastoreInfo(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatastoreInfo', body)

    def testCreateDatastore(self):
        a = Auth(username, pwd)
        body = {
            'host_name': 'dev-esxi.6.6.6',
            'path': 'C:\\abc\\',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.createDatastore(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'createDatastore', body)

    def testListDatastoreDir(self):
        a = Auth(username, pwd)
        body = {
            'host_name': '',
            'scope': '',
            'is_fusion_storage': 0,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listDatastoreDir(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDatastoreDir', body)

    def testListVmDisk(self):
        a = Auth(username, pwd)
        body = {
            'vm_ref': 'vm-1376',
            'region_id': '',
            'project_id': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVmDisk(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVmDisk', body)

    def testListNetwork(self):
        a = Auth(username, pwd)
        body = {
            'host_name': '',
            'dc_name': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listNetwork(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listNetwork', body)

    def testDrilConfigInfo(self):
        a = Auth(username, pwd)
        body = {
            'vp_addr': '',
            'vp_type': '',
            'use_credential': '',
            'cred_uuid': '',
            'os_usr': '',
            'os_pwd': '',
            'npsvr_uuid': '',
            'vp_uuid': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.drilConfigInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'drilConfigInfo', body)

    def testDl(self):
        a = Auth(username, pwd)
        body = {
            'type': 'vm_ip_csv',
            'vp_uuid': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.dl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'dl', body)

    def testImportVmIpMapping(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.importVmIpMapping(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'importVmIpMapping', body)

    def testListNetworkInfo(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'vm_ids': [],
            'region_id': '',
            'project_id': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listNetworkInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listNetworkInfo', body)

    def testDescribeOsVersion(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'os_versions': [],
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeOsVersion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeOsVersion', body)

    def testListSecurityGroup(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'dc_name': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listSecurityGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listSecurityGroup', body)

    def testListPhysicalInterface(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'resource_pool_id': '',
            'host_name': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listPhysicalInterface(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listPhysicalInterface', body)

    def testTgtVmStatusInfo(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.tgtVmStatusInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'tgtVmStatusInfo', body)

    def testArcherVmConsole(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.archerVmConsole(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'archerVmConsole', body)
    def testListVmStatus(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'vm_uuids': [],
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVmStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVmStatus', body)

    def testListPlatformStorage(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': 'FC151595-EB90-86F5-B659-CA787753CA5D',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listPlatformStorage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listPlatformStorage', body)

    def testPlatformAuthorize(self):
        a = Auth(username, pwd)
        body = {
            'vp_storage': [{
            'uuid': 'FC151595-EB90-86F5-B659-CA787753CA5D',
            'enabled': 0,
            'capacity': '10',},],
            'vp_uuid': 'DC151595-EB90-86F5-B659-CA787751CA5D',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.platformAuthorize(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'platformAuthorize', body)

    def testListVpStorage(self):
        a = Auth(username, pwd)
        body = {
            'where_args': {
            'enabled': '1',},
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpStorage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpStorage', body)

    def testListBakVerByIp(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid': '',
            'bk_path': '',
            'npsvr_uuid': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listBakVerByIp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listBakVerByIp', body)

    def testListBakVerInfoByIp(self):
        a = Auth(username, pwd)
        body = {
            'time': '',
            'ver_sig': '',
            'bk_uuid': '',
            'bk_path': '',
            'npsvr_uuid': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listBakVerInfoByIp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listBakVerInfoByIp', body)

    def testTestNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '5765E77A-C658-9AF1-83D0-1897B8A5850E',
            'cred_uuid': '4165E77A-C658-9AF1-83D0-1897B8A5850E',
            'trans_type': 'FTP',
            'vp_uuid': '6765E77A-C658-9AF1-83D0-1897B8A5850E',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.testNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'testNode', body)

    def testGetTargetVmInfo(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'group_uuid': '',
            'rule_type': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.getTargetVmInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'getTargetVmInfo', body)

    def testListDiskType(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'region_id': '',
            'project_id': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listDiskType(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listDiskType', body)

    def testDiscoveryVm(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'match_policy': {
            'vm_name': [{
            'type': '',
            'value': '',},],
            'location': [{
            'type': '',
            'value': '',},],
            'folder': [{
            'type': '',
            'value': '',},],},
            'project_id': '',
            'region_id': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.discoveryVm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'discoveryVm', body)

    def testListPools(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listPools(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listPools', body)

    def testListPoolHosts(self):
        a = Auth(username, pwd)
        body = {
            'pool_id': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listPoolHosts(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listPoolHosts', body)

    def testListAioClusters(self):
        a = Auth(username, pwd)
        body = {
            'region_id': '',
            'datecenter_id': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listAioClusters(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listAioClusters', body)

    def testListAioHosts(self):
        a = Auth(username, pwd)
        body = {
            'cluster_id': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listAioHosts(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listAioHosts', body)

    def testListAioPools(self):
        a = Auth(username, pwd)
        body = {
            'host_id': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listAioPools(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listAioPools', body)

    def testDescribeAioHostCapability(self):
        a = Auth(username, pwd)
        body = {
            'host_id': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.describeAioHostCapability(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'describeAioHostCapability', body)

    def testListScpHosts(self):
        a = Auth(username, pwd)
        body = {
            'resource_pool_id': '',
            'datastore_name': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listScpHosts(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listScpHosts', body)

    def testListVmPagination(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
            'vp_uuid': '',
            'view_type': '',
            'type': '',
            'id': '',
            'search_name': '',
            'protected': 1,
            'force_rpc': 1,
            'region_id': '',
            'project_id': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVmPagination(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVmPagination', body)

    def testExportVmList(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'view_type': '',
            'type': '',
            'id': '',
            'search_name': '',
            'protected': 1,
            'force_rpc': 1,
            'suffix': '',
            'vm_refs': [],
            'region_id': '',
            'project_id': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.exportVmList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'exportVmList', body)

    def testListVpc(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpc(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpc', body)

    def testListVpcSubnets(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
            'vpc_id': '',
        }
        
        
        virtualizationSupport = VirtualizationSupport(a)
        r = virtualizationSupport.listVpcSubnets(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'VirtualizationSupport', 'listVpcSubnets', body)


if __name__ == '__main__':
    unittest.main()
