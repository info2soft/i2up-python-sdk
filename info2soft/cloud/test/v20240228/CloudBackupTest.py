# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.cloud.v20240228.CloudBackup import CloudBackup
# from info2soft.cloud.v20200722.CloudBackup import CloudBackup
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


class CloudBackupTestCase(unittest.TestCase):

    def testListCloudPlatformRegion(self):
        a = Auth(username, pwd)
        body = {
            'cloud_type': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listCloudPlatformRegion(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listCloudPlatformRegion', body)

    def testRegisterCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'authurl': '',
            'os_user': '',
            'os_pwd': '',
            'user_domain_id': '',
            'cloud_name': '',
            'config_addr': '192.168.66.66',
            'register_type': '',
            'iam_user': '',
            'cloud_type': 1,
            'user_domain_name': '',
            'region': '',
            'vp_addr': '',
            'bind_lic_list': [],
            'maintenance': 0,
            'cc_ip_uuid': '',
            'access_key': '',
            'secret_access_key': '',
            'mfa_switch': 1,
            'connect_port': 5000,
            'project_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.registerCloudPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'registerCloudPlatform', body)

    def testModifyCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'os_user': '',
            'os_pwd': '',
            'user_domain_id': '',
            'register_type': '',
            'iam_user': '',
            'cloud_uuid': '',
            'bind_lic_list': '',
            'https://apiref.info2soft.com/repository/editor?id=28&itf=824': 0,
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.modifyCloudPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'modifyCloudPlatform', body)

    def testDeleteCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
            'force': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.deleteCloudPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'deleteCloudPlatform', body)

    def testListCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listCloudPlatform(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listCloudPlatform', body)

    def testListCloudPlatformStatus(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuids': [],
            'force_refresh': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listCloudPlatformStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listCloudPlatformStatus', body)

    def testDescribeCloudPlatform(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.describeCloudPlatform(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'describeCloudPlatform', body)

    def testSyncEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'region_id': '',
            'project_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.syncEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'syncEcs', body)

    def testSyncVolume(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.syncVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'syncVolume', body)

    def testListFlavor(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'server_zone': 'cn-east-2a',
            'region_id': '',
            'project_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listFlavor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listFlavor', body)

    def testListRelativeNode(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'cloud_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listRelativeNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listRelativeNode', body)

    def testSwitchMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'switch': 0,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.switchMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'switchMaintenance', body)

    def testListRegions(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listRegions(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listRegions', body)

    def testListProjects(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listProjects(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listProjects', body)

    def testListZone(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listZone(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listZone', body)

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

        cloudBackup = CloudBackup(a)
        r = cloudBackup.createVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createVolume', body)

    def testDeleteVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuids': [
                '11111111-1111-1111-1111-111111111111', ],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.deleteVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'deleteVolume', body)

    def testModifyVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuids': [],
            'ecs_id': '',
            'attach_point': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.modifyVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'modifyVolume', body)

    def testDetachVolume(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuids': [],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.detachVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'detachVolume', body)

    def testListVolume(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'page': 1,
            'limit': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listVolume(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listVolume', body)

    def testListVolumeStatus(self):
        a = Auth(username, pwd)
        body = {
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listVolumeStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listVolumeStatus', body)

    def testListImage(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listImage(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listImage', body)

    def testListVolumeEcs(self):
        a = Auth(username, pwd)
        body = {
            'volume_uuid': '501C1AD2-9BE0-D9EF-E860-0F2A10448076',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listVolumeEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listVolumeEcs', body)

    def testCreateEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'ecs_name': '',
            'flavorid': '',
            'volume_sys_id': '',
            'server_zone': '',
            'volume_data_ids': [],
            'wk_uuid': '',
            'rc_point': {
                'time': '',
                'disk_num': 1,
                'total_size': '',
                'list': [{
                    'id': '',
                    'size': '',
                    'boot_index': 1, }, ], },
            'from_backup': 0,
            'bind_public_ip': 1,
            'cloud_backup_uuid': '',
            'ecs_type': 1,
            'config': {
                'vpc': {
                    'id': '',
                    'name': '', },
                'subnet': [{
                    'id': '',
                    'name': '',
                    'network_id': 'b1e0f8fc-3be7-4539-b68e-ab7b7b69852c',
                    'ip': '', }, ],
                'security_group': {
                    'group_id': '',
                    'group_name': '',
                    'ingress': '',
                    'egress': '', },
                'subnet_type': 1,
                'band_width': 1,
                'cpu': '',
                'ram': '', },
            'disk_billing_type': 1,
            'order_cycle_unit': 1,
            'order_cycle': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.createEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createEcs', body)

    def testListVncConsole(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listVncConsole(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listVncConsole', body)

    def testListEcsStatus(self):
        a = Auth(username, pwd)
        body = {
            'ecs_ids': [],
            'force_refresh': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listEcsStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listEcsStatus', body)

    def testListEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'page': 1,
            'limit': 1,
            'type': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listEcs', body)

    def testDeleteEcs(self):
        a = Auth(username, pwd)
        body = {
            'ecs_ids': [],
            'complete_delete': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.deleteEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'deleteEcs', body)

    def testStartECS(self):
        a = Auth(username, pwd)
        body = {
            'ecs_ids': [],
            'operate': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.startECS(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'startECS', body)

    def testGetTakeoverECSInfo(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.getTakeoverECSInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'getTakeoverECSInfo', body)

    def testAttachPoint(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.attachPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'attachPoint', body)

    def testConfigRehearse(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup_uuid': '',
            'network_switch': 1
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.configRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'configRehearse', body)

    def testListRehearseGroup(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
            'cloud_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listRehearseGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listRehearseGroup', body)

    def testCreateRehearseGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'group_name': '',
            'ecs_ids': [
                '396c8bde-2d3a-4cad-87ea-8d1f81e2451c',
                'f3ca421d-9b6e-42b9-b911-36ebbeabb485', ],
            'group_content': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.createRehearseGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createRehearseGroup', body)

    def testDeleteRehearseGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuids': [
                'A14875A3-738E-3E5B-65D3-483CADE35E5D',
                'A14875A3-738E-3E5B-65D3-483CADE35E5D', ],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.deleteRehearseGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'deleteRehearseGroup', body)

    def testDescribeRehearseGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.describeRehearseGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'describeRehearseGroup', body)

    def testListDevice(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listDevice(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listDevice', body)

    def testListIdleDevice(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listIdleDevice(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listIdleDevice', body)

    def testCreateBackup(self):
        a = Auth(username, pwd)
        body = {
            'fsp_backup': {
                'secret_key': '',
                'band_width': '',
                'mirr_open_type': '0',
                'service_uuid': '',
                'mirr_sync_flag': '0',
                'sync_item': '/',
                'bkup_policy': 2,
                'mirr_file_check': '0',
                'compress': '0',
                'monitor_type': 0,
                'failover': '0',
                'disk_billing_type': 1,
                'order_cycle_unit': 1,
                'order_cycle': 1, },
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.createBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createBackup', body)

    def testModifyBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.modifyBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'modifyBackup', body)

    def testDeleteCloudBackup(self):
        a = Auth(username, pwd)
        body = {
            'force': 1,
            'rule_uuids': [],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.deleteCloudBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'deleteCloudBackup', body)

    def testListBackup(self):
        a = Auth(username, pwd)
        body = {
            'status': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listBackup', body)

    def testDescribeBackup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.describeBackup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'describeBackup', body)

    def testStopBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'stop',
            'fsp_uuids': ['22D03E06-94D0-5E2C-336E-4BEEC2D28EC4', '22D03E06-94D0-5E2C-336E-4BEEC2D28EC3']
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.stopBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'stopBackup', body)

    def testStartBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start',
            'fsp_uuids': ['22D03E06-94D0-5E2C-336E-4BEEC2D28EC4', '22D03E06-94D0-5E2C-336E-4BEEC2D28EC3']
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.startBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'startBackup', body)

    def testStartImmediatelyBackup(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'start_immediate',
            'fsp_uuids': ['22D03E06-94D0-5E2C-336E-4BEEC2D28EC4', '22D03E06-94D0-5E2C-336E-4BEEC2D28EC3']
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.startImmediatelyBackup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'startImmediatelyBackup', body)

    def testVerifySourceVirtioDriver(self):
        a = Auth(username, pwd)
        body = {
            'wk_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.verifySourceVirtioDriver(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'verifySourceVirtioDriver', body)

    def testDescribeEcs(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.describeEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'describeEcs', body)

    def testListHost(self):
        a = Auth(username, pwd)
        body = {
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listHost(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listHost', body)

    # def testListEcs(self):
    #     a = Auth(username, pwd)
    #     body = {
    #         'cloud_uuid': '',
    #         'page': 1,
    #         'limit': 1,
    #         'group_uuid': '',
    #     }
    #
    #     cloudBackup = CloudBackup(a)
    #     r = cloudBackup.listEcs(body)
    #     print(r[0])
    #     assert r[0]['ret'] == 200
    #     write(r[0], 'CloudBackup', 'listEcs', body)

    def testListRecoveryPoint(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup_uuid': '',
            'page': 1,
            'size': 1,
            'rc_point': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listRecoveryPoint(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listRecoveryPoint', body)

    def testListAvailabilityZone(self):
        a = Auth(username, pwd)
        body = {
            'ecs_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listAvailabilityZone(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listAvailabilityZone', body)

    # def testListFlavor(self):
    #     a = Auth(username, pwd)
    #     body = {
    #         'ecs_id': '',
    #         'region_id': '',
    #         'project_id': '',
    #     }
    #
    #     cloudBackup = CloudBackup(a)
    #     r = cloudBackup.listFlavor(body)
    #     print(r[0])
    #     assert r[0]['ret'] == 200
    #     write(r[0], 'CloudBackup', 'listFlavor', body)

    def testListVpc(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listVpc(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listVpc', body)

    def testListSubnet(self):
        a = Auth(username, pwd)
        body = {
            'vpc_id': '356c3295-afd0-4a09-8e6f-03620ef70854',
            'cloud_uuid': '',
            'region_id': '',
            'project_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listSubnet(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listSubnet', body)

    def testListSecureGroup(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'ecs_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listSecureGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listSecureGroup', body)

    def testCreateRehearse(self):
        a = Auth(username, pwd)
        body = {
            'cloud_backup_uuid': '',
            'network_switch': 1,
            'cpu': 1,
            'ram': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.createRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createRehearse', body)

    def testCreateBatchRehearse(self):
        a = Auth(username, pwd)
        body = {
            'rehearse_list': [],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.createBatchRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createBatchRehearse', body)

    def testListRehearse(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listRehearse', body)

    def testListRehearseStatus(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [
                'f1312ce5-7cb0-4e0c-a687-4ba4e5475e4c', ],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listRehearseStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listRehearseStatus', body)

    # def testListVncConsole(self):
    #     a = Auth(username, pwd)
    #     body = {
    #         'job_id': '',
    #         'ecs_id': '',
    #     }
    #
    #     cloudBackup = CloudBackup(a)
    #     r = cloudBackup.listVncConsole(body)
    #     print(r[0])
    #     assert r[0]['ret'] == 200
    #     write(r[0], 'CloudBackup', 'listVncConsole', body)

    def testEvacuateRehearse(self):
        a = Auth(username, pwd)
        body = {
            'job_id': '',
            'is_group': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.evacuateRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'evacuateRehearse', body)

    def testEvacuateBatchRehearse(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
            'is_group': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.evacuateBatchRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'evacuateBatchRehearse', body)

    def testListRehearseDetail(self):
        a = Auth(username, pwd)
        body = {
            'job_id': '',
            'type': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listRehearseDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listRehearseDetail', body)

    def testDescribeRehearse(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.describeRehearse(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'describeRehearse', body)

    def testDeleteRehearse(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.deleteRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'deleteRehearse', body)

    def testListEvacuatedRehearse(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'page': 1,
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listEvacuatedRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listEvacuatedRehearse', body)

    def testListNpsvrRehearseStatus(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.listNpsvrRehearseStatus(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listNpsvrRehearseStatus', body)

    def testListNpsvrRehearseProgress(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.listNpsvrRehearseProgress(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listNpsvrRehearseProgress', body)

    def testListNetwork(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '8E6FB8D2-F830-D67B-DA35-8E16F175053B',
            'network_conf': [{
                'vpc': {
                    'id': '356c3295-afd0-4a09-8e6f-03620ef70854',
                    'name': 'vpc-49a5,192.168.0.0/16', },
                'subnet': {
                    'id': '3509d824-1a5b-41e5-9570-4cf51440078f',
                    'name': 'subnet-1df4,192.168.64.0/24', }, }, ],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listNetwork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listNetwork', body)

    def testCreateNetwork(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.createNetwork(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createNetwork', body)

    def testListSubnetUsedIp(self):
        a = Auth(username, pwd)
        body = {
            'cloud_uuid': '',
            'subnet_id': '',
            'region_id': '',
            'project_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listSubnetUsedIp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listSubnetUsedIp', body)

    def testCreateGroup(self):
        a = Auth(username, pwd)
        body = {
            'group_uuid': '',
            'group_config': [],
            'rehearse_name': '',
            'cloud_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.createGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createGroup', body)

    def testListGroup(self):
        a = Auth(username, pwd)
        body = {
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listGroup', body)

    def testDescribeGroup(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        cloudBackup = CloudBackup(a)
        r = cloudBackup.describeGroup(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'describeGroup', body)

    def testDeleteGroup(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.deleteGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'deleteGroup', body)

    def testCreateEvacuateGroup(self):
        a = Auth(username, pwd)
        body = {
            'job_id': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.createEvacuateGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'createEvacuateGroup', body)

    def testListGroupStatus(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listGroupStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listGroupStatus', body)

    def testListEvacuatedGroup(self):
        a = Auth(username, pwd)
        body = {
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listEvacuatedGroup(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listEvacuatedGroup', body)

    def testListBatchRehearse(self):
        a = Auth(username, pwd)
        body = {
            'job_ids': [],
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.listBatchRehearse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'listBatchRehearse', body)

    def testDescribeFlavor(self):
        a = Auth(username, pwd)
        body = {
            'flavor_id': '',
            'server_zone': '',
            'cloud_uuid': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.describeFlavor(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'describeFlavor', body)

    def testBatchCreateEcs(self):
        a = Auth(username, pwd)
        body = {
            'prefix': '',
            'ecs_type': '',
        }

        cloudBackup = CloudBackup(a)
        r = cloudBackup.batchCreateEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'CloudBackup', 'batchCreateEcs', body)


if __name__ == '__main__':
    unittest.main()
