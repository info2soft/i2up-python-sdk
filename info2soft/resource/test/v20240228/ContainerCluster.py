
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import ContainerCluster
from info2soft.resource.v20240228.ContainerCluster import ContainerCluster
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


class ContainerClusterTestCase(unittest.TestCase):

    def testCreateBackupDestination(self):
        a = Auth(username, pwd)
        body = {
            'name': '',
            'sto_uuid': '',
            's3_real_address': 1,
            'bucket': '',
            'region': '',
            'check_sto_address': 1,
            'sto_address_cert': '',
            'cls_uuid': '',
            'copy_switch': 1,
            'src_uuid': '',
            'src_cls_uuid': '',
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.createBackupDestination(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'createBackupDestination', body)

    def testListBackupDestination(self):
        a = Auth(username, pwd)
        body = {
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.listBackupDestination(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'listBackupDestination', body)

    def testDescibeBackupDestination(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        containerCluster = ContainerCluster(a)
        r = containerCluster.descibeBackupDestination(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'descibeBackupDestination', body)

    def testModifyBackupDestination(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'name': '',
            'sto_uuid': '',
            'random_str': '',
            's3_real_address': 1,
            'bucket': '',
            'region': '',
            'check_sto_address': 1,
            'sto_address_cert': '',
            'cls_uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        containerCluster = ContainerCluster(a)
        r = containerCluster.modifyBackupDestination(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'modifyBackupDestination', body)

    def testDeleteBackupDestination(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.deleteBackupDestination(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'deleteBackupDestination', body)

    def testListBackupDestinationStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '',
            'force_refresh': '',
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.listBackupDestinationStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'listBackupDestinationStatus', body)

    def testListContainerClusterInfo(self):
        a = Auth(username, pwd)
        body = {
            'cls_config': {},
            'username': '',
            'password': '',
            'component_namespace': '',
            'net_type': '',
            'cls_uuid': '',
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.listContainerClusterInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'listContainerClusterInfo', body)

    def testSyncContainerClusterInfo(self):
        a = Auth(username, pwd)
        body = {
            'cls_uuid': '',
            'type': '',
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.syncContainerClusterInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'syncContainerClusterInfo', body)

    def testListContainerClusterResource(self):
        a = Auth(username, pwd)
        body = {
            'cls_uuid': '',
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.listContainerClusterResource(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'listContainerClusterResource', body)

    def testListContainerClsNamespace(self):
        a = Auth(username, pwd)
        body = {
            'cls_uuid': '58ECEEB7-D4FC-4746-A507-AA3BBC98EFD1',
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.listContainerClsNamespace(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'listContainerClsNamespace', body)

    def testContainerClusterMonitoringOverview(self):
        a = Auth(username, pwd)
        body = {
            'cls_uuid': '',
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.containerClusterMonitoringOverview(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'containerClusterMonitoringOverview', body)

    def testContainerClusterMonitoringNode(self):
        a = Auth(username, pwd)
        body = {
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.containerClusterMonitoringNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'containerClusterMonitoringNode', body)

    def testCreateContainerCluster(self):
        a = Auth(username, pwd)
        body = {
            'cls_name': '',
            'cls_config': '',
            'component_settings': {
            'cls_component_config': {
            'cpu_limit': 1,
            'cpu_request': 1,
            'mem_limit': 1,
            'mem_request': 1,},
            'pv_component_config': {
            'cpu_limit': 1,
            'cpu_request': 1,
            'mem_limit': 1,
            'mem_request': 1,},},
            'component_version': '',
            'cls_version': '',
            'cls_type': 1,
            'component_namespace': '',
            'os_user': '',
            'os_pwd': '',
            'net_type': '',
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.createContainerCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'createContainerCluster', body)

    def testListContainerCluster(self):
        a = Auth(username, pwd)
        body = {
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.listContainerCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'listContainerCluster', body)

    def testDescribeContainerCluster(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        containerCluster = ContainerCluster(a)
        r = containerCluster.describeContainerCluster(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'describeContainerCluster', body)

    def testModifyContainerCluster(self):
        a = Auth(username, pwd)
        body = {
            'cls_name': '',
            'cls_config': {},
            'component_settings': {
            'cls_component_config': {
            'cpu_limit': 1,
            'cpu_request': 1,
            'mem_limit': 1,
            'mem_request': 1,},
            'pv_component_config': {
            'cpu_limit': 1,
            'cpu_request': 1,
            'mem_limit': 1,
            'mem_request': 1,},},
            'component_version': '',
            'current_context': '',
            'cls_version': '',
            'authorization_info': '',
            'random_str': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        containerCluster = ContainerCluster(a)
        r = containerCluster.modifyContainerCluster(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'modifyContainerCluster', body)

    def testDeleteContainerCluster(self):
        a = Auth(username, pwd)
        body = {
            'cls_uuids': [],
            'force': 1,
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.deleteContainerCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'deleteContainerCluster', body)

    def testCreateCallbackSettings(self):
        a = Auth(username, pwd)
        body = {
            'name': '',
            'type': 1,
            'cls_uuid': '',
            'pod': '',
            'before_backup': [{
            'cmd': '',
            'container': '',
            'error_handling': '',
            'timeout': '',},],
            'after_backup': [{
            'cmd': '',
            'container': '',
            'error_handling': '',
            'timeout': '',},],
            'init_container': [{
            'name': '',
            'mirror': '',
            'cmd': '',
            'volume': '',},],
            'recovery_callback': [{
            'container': '',
            'cmd': '',
            'error_handling': '',
            'exec_timeout': 1,
            'wait_timeout': 1,},],
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.createCallbackSettings(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'createCallbackSettings', body)

    def testListCallbackSettings(self):
        a = Auth(username, pwd)
        body = {
            'where_args[type]': 1,
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.listCallbackSettings(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'listCallbackSettings', body)

    def testDescribeCallbackSettings(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        containerCluster = ContainerCluster(a)
        r = containerCluster.describeCallbackSettings(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'describeCallbackSettings', body)

    def testModifyCallbackSettings(self):
        a = Auth(username, pwd)
        body = {
            'name': '',
            'type': 1,
            'cls_uuid': '',
            'pod': '',
            'uuid': 'E8CdEd75-71ea-AC5E-7E19-ABC24D4B2cfb',
            'user_uuid': 'E679EF73-5288-E3C4-9608-B33B47416B87',
            'username': 'admin',
            'random_uuid': 'E679EF73-5288-E3C4-9608-B33B47416B87',
            'before_backup': [{
            'cmd': '',
            'container': '',
            'error_handling': '',
            'timeout': '',},],
            'after_backup': [{
            'cmd': '',
            'container': '',
            'error_handling': '',
            'timeout': '',},],
            'init_container': [{
            'name': '',
            'mirror': '',
            'cmd': '',
            'volume': '',},],
            'recovery_callback': [{
            'container': '',
            'cmd': '',
            'error_handling': '',
            'exec_timeout': 1,
            'wait_timeout': 1,},],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        containerCluster = ContainerCluster(a)
        r = containerCluster.modifyCallbackSettings(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'modifyCallbackSettings', body)

    def testDeleteCallbackSettings(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.deleteCallbackSettings(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'deleteCallbackSettings', body)

    def testVerifyCallbackSettingsPod(self):
        a = Auth(username, pwd)
        body = {
            'cls_uuid': '',
            'pod': '',
        }
        
        containerCluster = ContainerCluster(a)
        r = containerCluster.verifyCallbackSettingsPod(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'ContainerCluster', 'verifyCallbackSettingsPod', body)


if __name__ == '__main__':
    unittest.main()
