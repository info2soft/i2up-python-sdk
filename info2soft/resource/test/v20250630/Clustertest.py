
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Cluster
from info2soft.resource.v20250630.Cluster import Cluster
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


class ClusterTestCase(unittest.TestCase):
    def setUp(self):
        """在每个测试方法运行前执行"""
        self.original_cwd = os.getcwd()
        # 获取当前测试文件的目录
        test_dir = os.path.dirname(os.path.abspath(__file__))
        # 切换工作目录到测试文件所在的目录
        os.chdir(test_dir)

    def tearDown(self):
        """在每个测试方法运行后执行"""
        # 恢复原始工作目录，避免影响其他测试
        os.chdir(self.original_cwd)

    def testAuthCls(self):
        a = Auth(username, pwd)
        body = {
            'cls_is_local': 1,
            'os_pwd': 'info2soft_125',
            'os_user': 'i2test2018.com\administrator',
            'config_addr': '192.168.87.14',
            'config_port': 26821,
            'node_type': 3,
        }
        
        
        cluster = Cluster(a)
        r = cluster.authCls(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'authCls', body)

    def testVerifyClsNode(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': 'BD7D3EF7-2F75-E2BB-A2CB-CFE936CF1F6C',
            'cls_name': 'cluster-2018',
            'cls_node_name': 'cluster-node1',
            'node_type': 1,
        }
        
        
        cluster = Cluster(a)
        r = cluster.verifyClsNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'verifyClsNode', body)

    def testCreateCls(self):
        a = Auth(username, pwd)
        body = {
            'cls': {
            'comment': '',
            'cls_disk': [
            'E:\\',],
            'config_port': '26821',
            'cls_node': [{
            'host_name': '',
            'host_ip': '',
            'node_uuid': '',
            'node_name': '',
            'no_confidential': 1,
            'id': '',
            'address': '',
            'state_str': '',
            'health': False,
            'backup_script_uuid': '',
            'recovery_script_uuid': '',
            'role': '',
            'vc_name': '',
            'gcluster': False,
            'gcware': False,
            'host_port': '',
            'service_type': '',},],
            'node_type': 1,
            'cls_is_local': 1,
            'os_user': 'i2test2018.com\administrator',
            'config_addr': '192.168.74.25',
            'node_name': 'cls',
            'other_params': {
            'ora_home': '',
            'grid_home': '',
            'user': '',
            'roach_agent_port': 1,
            'roach_client_port': 1,
            'invasion': 1,
            'cn_ip': '',
            'cn_node_uuid': '',
            'ip': '',
            'port': 1,
            'password': '',
            'ob_username': '',
            'ob_password': '',
            'ob_ip': '',
            'ob_port': 1,
            'slave_uuid': '',
            'oss_ip': '',
            'oss_port': '',
            'tdsql_manage_user': '',
            'tdsql_db_user': '',
            'oss_user': '',
            'module_dir': '',
            'data_disk_dir': '',
            'log_disk_dir': '',
            'endpoint': '',
            'access_key': '',
            'secret_key': '',
            'project_id': '',
            'db_user': '',
            'db_password': '',
            'dba_user': '',
            'dba_password': '',
            'assist_node_uuids': [],
            'bin_path': '',
            'tiup_path': '',
            'tidb_name': '',
            'ob_role': 1,
            'deploy_user': '',
            'port_prefix': '',},
            'maintenance': 0,
            'iam_username': '',
            'iam_password': '',
            'iam_owning_account': '',
            'resource_set_name': '',
            'resource_set_id': '',
            'xbsa_ssl': 1,
            'root_cert': '',
            'user_cert': '',
            'user_private_key': '',
            'user_private_key_pwd': '',
            'business_addr': '',
            'management_addr': '',
            'biz_grp_list': [],
            'omm_ip': [],
            'omm_rdb_os_user': '',
            'omm_rdb_username': '',
            'omm_rdb_password': '',
            'dbagent_password': '',
            'data_manager_uuid': '',
            'tdsql_db_pwd': '',
            'oss_pwd': '',
            'dmcssm_uuid': '',
            'dm_user': '',
            'dm_home_path': '',
            'dmcssm_ini_path': '',
            'instance_info': '',
            'dmdsc_uuid': '',
            'application_type': '',
            'resource_type': '',
            'omm_rdb_login_path': '',
            'dbagent_username': '',
            'dbagent_login_path': '',
            'login_type': 1,
            'os_pwd': '',
            'is_single': 1,
            'db_instance_list': [{
            'instance_uuid': '',
            'instance_name': '',
            'node_uuid': '',
            'node_name': '',
            'hostname': '',
            'config_addr': '',},],},
        }
        
        
        cluster = Cluster(a)
        r = cluster.createCls(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'createCls', body)

    def testDescribeCls(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cluster = Cluster(a)
        r = cluster.describeCls(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'describeCls', body)

    def testClsNodeInfo(self):
        a = Auth(username, pwd)
        body = {
            'cls_ip': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.clsNodeInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'clsNodeInfo', body)

    def testModifyCls(self):
        a = Auth(username, pwd)
        body = {
            'cls': {
            'comment': '',
            'cls_disk': [
            'E:\\',],
            'config_port': '26821',
            'cls_node': [
            'BD7D3EF7-2F75-E2BB-A2CB-CFE936CF1F6C',],
            'node_type': 1,
            'cls_is_local': 1,
            'os_user': 'i2test2018.com\administrator',
            'config_addr': '192.168.74.25',
            'node_name': 'cls',
            'random_str': '11111111-1111-1111-1111-111111111111',
            'maintenance': 0,
            'other_params': {
            'ora_home': '',
            'grid_home': '',
            'user': '',},},
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        cluster = Cluster(a)
        r = cluster.modifyCls(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'modifyCls', body)

    def testListCls(self):
        a = Auth(username, pwd)
        body = {
            'limit': 1,
            'search_value': '',
            'search_field': '',
            'page': 1,
            'where_args': {
            'node_type': 1,
            'status': '',
            'is_single': 1,},
        }
        
        
        cluster = Cluster(a)
        r = cluster.listCls(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listCls', body)

    def testListClsStatus(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force_refresh': 1,
        }
        
        
        cluster = Cluster(a)
        r = cluster.listClsStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listClsStatus', body)

    def testDeleteCls(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force': 1,
        }
        
        
        cluster = Cluster(a)
        r = cluster.deleteCls(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'deleteCls', body)

    def testClsDetail(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'detail',
            'node_uuid': '11111111-1111-1111-1111-111111111111',
        }
        
        
        cluster = Cluster(a)
        r = cluster.clsDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'clsDetail', body)

    def testListRacStatus(self):
        a = Auth(username, pwd)
        body = {
            'node_uuids': [],
            'force_refresh': 1,
        }
        
        
        cluster = Cluster(a)
        r = cluster.listRacStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listRacStatus', body)

    def testGetGaussInfo(self):
        a = Auth(username, pwd)
        body = {
            'config_addr': '',
            'user': '',
            'config_port': '',
            'node_uuid': '',
            'invasion': '',
            'cn_ip': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.getGaussInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'getGaussInfo', body)

    def testSwitchMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'switch': 0,
        }
        
        
        cluster = Cluster(a)
        r = cluster.switchMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'switchMaintenance', body)

    def testListGaussHcsInstances(self):
        a = Auth(username, pwd)
        body = {
            'limit': '',
            'page': '',
            'where_args': [{
            'node_uuid': '',},],
            'search_field': 'node_name',
            'search_value': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.listGaussHcsInstances(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listGaussHcsInstances', body)

    def testListGaussHcsDefaultInstance(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'bk_set_uuid': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.listGaussHcsDefaultInstance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listGaussHcsDefaultInstance', body)

    def testListGaussTpopSolution(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        cluster = Cluster(a)
        r = cluster.listGaussTpopSolution(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listGaussTpopSolution', body)

    def testListGaussTpopDefaultInstance(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'os_type': '',
            'arch': '',
            'cpu': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.listGaussTpopDefaultInstance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listGaussTpopDefaultInstance', body)

    def testClsGoldenDBInfo(self):
        a = Auth(username, pwd)
        body = {
            'omm_ip': [],
            'omm_rdb_os_user': '',
            'omm_rdb_username': '',
            'omm_rdb_password': '',
            'dbagent_password': '',
            'data_manager_uuid': '',
            'login_type': 1,
            'dbagent_username': '',
            'omm_rdb_login_path': '',
            'dbagent_login_path': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.clsGoldenDBInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'clsGoldenDBInfo', body)

    def testClsMongoDBInfo(self):
        a = Auth(username, pwd)
        body = {
            'ip': '',
            'port': 1,
            'user': '',
            'password': '',
            'node_uuid': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.clsMongoDBInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'clsMongoDBInfo', body)

    def testClsTdsqlDBInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'oss_ip': '',
            'oss_port': '',
            'oss_user': '',
            'oss_pwd': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.clsTdsqlDBInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'clsTdsqlDBInfo', body)

    def testClsDorisInfo(self):
        a = Auth(username, pwd)
        body = {
            'user': '',
            'password': '',
            'ip': '',
            'port': 1,
            'bin_path': '',
            'data_manager_uuid': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.clsDorisInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'clsDorisInfo', body)

    def testTidbVerify(self):
        a = Auth(username, pwd)
        body = {
            'tidb_name': '',
            'tiup_path': '',
            'bin_path': '',
            'user': '',
            'password': '',
            'data_manager_uuid': '',
            'deploy_user': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.tidbVerify(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'tidbVerify', body)

    def testListRacInstances(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.listRacInstances(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'listRacInstances', body)

    def testGetTdsqlInstanceDefaultInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.getTdsqlInstanceDefaultInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'getTdsqlInstanceDefaultInfo', body)

    def testGetTdsqlInstanceDefaultMachineInfo(self):
        a = Auth(username, pwd)
        body = {
            'node_uuid': '',
            'machine': '',
        }
        
        
        cluster = Cluster(a)
        r = cluster.getTdsqlInstanceDefaultMachineInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Cluster', 'getTdsqlInstanceDefaultMachineInfo', body)


if __name__ == '__main__':
    unittest.main()
