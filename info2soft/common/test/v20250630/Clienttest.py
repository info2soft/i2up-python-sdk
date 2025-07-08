
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Client
from info2soft.common.v20250630.Client import Client
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


class ClientTestCase(unittest.TestCase):
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

    def testListRestRpcCcip(self):
        a = Auth(username, pwd)
        body = {
            'method': '',
            'uuid': '',
            'cc_uuid': '',
        }
        
        
        client = Client(a)
        r = client.listRestRpcCcip(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'listRestRpcCcip', body)

    def testUpdateTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'slot_barcode': '',
            'slot_flag': '',
            'pool_name': '',
            'last_write': '',
            'move_times': 1,
            'slot_expiretime': '',
            'slot_index': 1,
            'slot_mtype': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'status': 1,
            'write_protected': 1,
        }
        
        
        client = Client(a)
        r = client.updateTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'updateTapeMedia', body)

    def testRegisterNodeFromNode(self):
        a = Auth(username, pwd)
        body = {
            'node_name': '',
            'os_type': 1,
            'os_user': '',
            'i2id': '',
            'cc_ip': '',
            'config_addr': '',
            'root': '',
            'disk_limit': '',
            'mem_limit': '',
            'disk_free_space_limit': '',
            'log_path': '',
            'cache_path': '',
            'data_addr': '',
        }
        
        
        client = Client(a)
        r = client.registerNodeFromNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'registerNodeFromNode', body)

    def testUpdateSlaveNode(self):
        a = Auth(username, pwd)
        body = {
            'config': '',
            'cc_uuid': '',
            'aes_key': '',
            'aes_iv': '',
        }
        
        
        client = Client(a)
        r = client.updateSlaveNode(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'updateSlaveNode', body)

    def testAddRestRpcresult(self):
        a = Auth(username, pwd)
        body = {
            'type': 'result',
            'code': 1,
            'ip': '',
            'cc_uuid': '',
        }
        
        
        client = Client(a)
        r = client.addRestRpcresult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'addRestRpcresult', body)

    def testAddRestRpcHa(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'failed_node_uuid': '',
            'new_node_uuid': '',
            'cc_uuid': '',
        }
        
        
        client = Client(a)
        r = client.addRestRpcHa(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'addRestRpcHa', body)

    def testAddRestRpcCluster(self):
        a = Auth(username, pwd)
        body = {
            'cluster_uuid': '',
            'center_node_ip': '',
        }
        
        
        client = Client(a)
        r = client.addRestRpcCluster(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'addRestRpcCluster', body)

    def testCreateCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '65DA3916-AF53-CE70-0B47-A142414AA140',
            'result_uuid': '25DA3916-AF13-CE70-0B47-B142414AA142',
            'result': {
            'code': '0',
            'time': '10',
            'files': '100',
            'bytes': '1111111',
            'missing': '2',
            'diff': '48',
            'equal': '50',
            'erro': '',},
            'result_type': 'rep',
            'cc_uuid': '',
        }
        
        
        client = Client(a)
        r = client.createCompareResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'createCompareResult', body)

    def testUploadCompareDiffDetail(self):
        a = Auth(username, pwd)
        body = {
            'files': [],
            'missing_files': [
            'file',
            'file',],
            'diff_files': [],
            'uuid': '',
            'cc_uuid': '',
            'is_new': 0,
        }
        
        
        client = Client(a)
        r = client.uploadCompareDiffDetail(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'uploadCompareDiffDetail', body)

    def testCollectCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'code': '',
            'time': '1632453814-1632453816',
            'files': '',
            'bytes': '',
            'missing': '',
            'diff': '',
            'erro': '',
            'equal': '',
            'task_uuid': '',
            'cc_uuid': '',
            'send_bytes': '',
        }
        
        
        client = Client(a)
        r = client.collectCompareResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'collectCompareResult', body)

    def testModifyEcs(self):
        a = Auth(username, pwd)
        body = {
            'restored_uuid': '',
            'ecs_id': '',
            'code': 1,
        }
        
        
        client = Client(a)
        r = client.modifyEcs(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'modifyEcs', body)

    def testGetVirtualPlatforms(self):
        a = Auth(username, pwd)
        body = {
            'npsvr_uuid': '',
            'cc_uuid': '',
        }
        
        
        client = Client(a)
        r = client.getVirtualPlatforms(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'getVirtualPlatforms', body)

    def testGetVirtualPlatformRules(self):
        a = Auth(username, pwd)
        body = {
            'vp_uuids': [
            '3C334EF3',
            '3C334EF3',],
            'config_addr': [{
            '': '',},],
            'cc_uuid': '',
        }
        
        
        client = Client(a)
        r = client.getVirtualPlatformRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'getVirtualPlatformRules', body)

    def testGetDtoStorageList(self):
        a = Auth(username, pwd)
        body = {
            'cc_uuid': '',
        }
        
        
        client = Client(a)
        r = client.getDtoStorageList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'getDtoStorageList', body)

    def testGetAllActiveRules(self):
        a = Auth(username, pwd)
        body = {
            'cc_uuid': '',
            'rule_uuids': [],
        }
        
        
        client = Client(a)
        r = client.getAllActiveRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'getAllActiveRules', body)

    def testUploadHdfsCompareResult(self):
        a = Auth(username, pwd)
        body = {
            'cc_uuid': '',
            'policy_uuid': '',
            'session_uuid': '',
            'comparison_results': [{
            'diff_name': '',
            'diff_name_type': '',
            'result': '',
            'existence_state': '',},],
            'statistical_result': {
            'start_time': '',
            'end_time': '',
            'comparison_count': '',
            'difference_count': '',},
            'comparison_detail_results': [{
            'diff_name': '',
            'comparison_term': '',
            'source': '',
            'destination': '',},],
        }
        
        
        client = Client(a)
        r = client.uploadHdfsCompareResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'uploadHdfsCompareResult', body)

    def testCfsNodeMove(self):
        a = Auth(username, pwd)
        body = {
            'cfs_uuid': '',
            'fs_id': '',
            'src_server_id': '',
            'dst_server_id': '',
        }
        
        
        client = Client(a)
        r = client.cfsNodeMove(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'cfsNodeMove', body)

    def testCfsStopRule(self):
        a = Auth(username, pwd)
        body = {
            'cfs_uuid': '',
            'fs_id': '',
            'src_server_id': '',
            'dst_server_id': '',
        }
        
        
        client = Client(a)
        r = client.cfsStopRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'cfsStopRule', body)

    def testListSlotTapeName(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        client = Client(a)
        r = client.listSlotTapeName(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Client', 'listSlotTapeName', body)


if __name__ == '__main__':
    unittest.main()
