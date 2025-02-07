
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Tape
from info2soft.resource.v20250123.Tape import Tape
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


class TapeTestCase(unittest.TestCase):

    def testSanTapeLibraries(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuids': [],
        }
        
        
        tape = Tape(a)
        r = tape.sanTapeLibraries(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'sanTapeLibraries', body)

    def testListTapeLibraryDrivers(self):
        a = Auth(username, pwd)
        body = {
            'library_uuid': '',
            'library_sn': '',
            'bk_uuid_list': [],
        }
        
        
        tape = Tape(a)
        r = tape.listTapeLibraryDrivers(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapeLibraryDrivers', body)

    def testCreateTapeLibrary(self):
        a = Auth(username, pwd)
        body = {
            'library_name': '磁带库1',
            'comment': '说明',
            'bk_uuid_list': [
            'D42BF707-C971-EEA9-521F-BB0F3F7A92FC',],
            'library_list': [{
            'bk_uuid': 'D42BF707-C971-EEA9-521F-BB0F3F7A92FC',
            'library_sn': 'SYZZ_A',
            'library_vendor': 'STK',
            'library_product': 'L80',
            'library_revision': '0106',
            'drive_num': 1,
            'slot_num': 1,
            'dev_path': '/dev',
            'checked': False,},],
            'ctrl_host_uuid': '',
            'library_sn': '',
            'library_vendor': '',
            'library_product': '',
            'library_revision': '',
            'drive_num': '',
            'dev_path': '',
            'slot_num': '',
            'driver_info': [{
            'bk_uuid': '',
            'library_sn': '',
            'driver_list': [{
            'checked': '',
            'index': '',
            'barcode': '',
            'driver_sn': '',
            'dev_path': '',
            'status': '',
            'last_write': '',},],},],
            'robotic_arm_info': [],
            'slave': 1,
        }
        
        
        tape = Tape(a)
        r = tape.createTapeLibrary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'createTapeLibrary', body)

    def testListTapeLibrary(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        tape = Tape(a)
        r = tape.listTapeLibrary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapeLibrary', body)

    def testDescribeTapeLibrary(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        tape = Tape(a)
        r = tape.describeTapeLibrary(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'describeTapeLibrary', body)

    def testModifyTapeLibrary(self):
        a = Auth(username, pwd)
        body = {
            'library_name': '磁带库1',
            'library_uuid': '',
            'random_str': '',
            'comment': '说明',
            'bk_uuid_list': [
            'D42BF707-C971-EEA9-521F-BB0F3F7A92FC',],
            'library_list': [{
            'bk_uuidtrue': 'D42BF707-C971-EEA9-521F-BB0F3F7A92FC',
            'library_sn': 'SYZZ_A',
            'library_vendor': 'STK',
            'library_product': 'L80',
            'library_revision': '0106',
            'drive_num': 1,
            'slot_num': 1,
            'dev_path': '/dev',
            'checked': 1,},],
            'curl_host_uuid': '',
            'library_sn': '',
            'library_vendor': '',
            'library_product': '',
            'library_revision': '',
            'drive_num': '',
            'dev_path': '',
            'slot_num': '',
            'driver_info': [{
            'bk_uuid': '',
            'library_sn': '',
            'driver_list': {
            'checked': '',
            'index': '',
            'barcode': '',
            'driver_sn': '',
            'dev_path': '',
            'status': '',
            'last_write': '',},},],
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        tape = Tape(a)
        r = tape.modifyTapeLibrary(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'modifyTapeLibrary', body)

    def testDeleteTapeLibrary(self):
        a = Auth(username, pwd)
        body = {
            'library_uuids': [],
            'force': 1,
        }
        
        
        tape = Tape(a)
        r = tape.deleteTapeLibrary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'deleteTapeLibrary', body)

    def testRefreshTapeLibrarySlot(self):
        a = Auth(username, pwd)
        body = {
            'library_uuid': '',
            'refresh_type': 1,
        }
        
        
        tape = Tape(a)
        r = tape.refreshTapeLibrarySlot(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'refreshTapeLibrarySlot', body)

    def testListBusySlot(self):
        a = Auth(username, pwd)
        body = {
            'library_uuid': '',
        }
        
        
        tape = Tape(a)
        r = tape.listBusySlot(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listBusySlot', body)

    def testListBusyIeSlot(self):
        a = Auth(username, pwd)
        body = {
            'library_uuid': '',
        }
        
        
        tape = Tape(a)
        r = tape.listBusyIeSlot(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listBusyIeSlot', body)

    def testImportTapeLibrary(self):
        a = Auth(username, pwd)
        body = {
            'library_uuids': [],
            'operate': '',
            'list': [{
            'ieslot_barcode': '',
            'ieslot_index': '',},],
        }
        
        
        tape = Tape(a)
        r = tape.importTapeLibrary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'importTapeLibrary', body)

    def testListTapeLibraryStatus(self):
        a = Auth(username, pwd)
        body = {
            'library_uuids': [],
        }
        
        
        tape = Tape(a)
        r = tape.listTapeLibraryStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapeLibraryStatus', body)

    def testEnableTapeLibraryDrivers(self):
        a = Auth(username, pwd)
        body = {
            'library_uuid': '',
            'driver_index': '',
            'status': '',
            'dev_path': '',
            'driver_sn': '',
            'operate': '',
            'slot_index': '',
            'slot_flag': '',
            'barcode': '',
            'tape_uuid': '',
        }
        
        
        tape = Tape(a)
        r = tape.enableTapeLibraryDrivers(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'enableTapeLibraryDrivers', body)

    def testMoveTapeLibraryDrivers(self):
        a = Auth(username, pwd)
        body = {
            'library_uuid': '',
            'driver_index': '',
            'status': '',
            'dev_path': '',
            'driver_sn': '',
            'operate': '',
            'slot_index': '',
            'slot_flag': '',
            'barcode': '',
            'tape_uuid': '',
        }
        
        
        tape = Tape(a)
        r = tape.moveTapeLibraryDrivers(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'moveTapeLibraryDrivers', body)

    def testListTapePools(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        tape = Tape(a)
        r = tape.listTapePools(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapePools', body)

    def testCreateTapePool(self):
        a = Auth(username, pwd)
        body = {
            'pool_name': '',
            'comment': '',
            'note': '',
        }
        
        
        tape = Tape(a)
        r = tape.createTapePool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'createTapePool', body)

    def testUpdateTapePool(self):
        a = Auth(username, pwd)
        body = {
            'comment': '',
            'note': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        tape = Tape(a)
        r = tape.updateTapePool(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'updateTapePool', body)

    def testDeleteTapePool(self):
        a = Auth(username, pwd)
        body = {
            'pool_uuids': [],
        }
        
        
        tape = Tape(a)
        r = tape.deleteTapePool(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'deleteTapePool', body)

    def testFreezeTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'library_uuid': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'pool_name': '',},],
            'operate': '',
            'src_pool_name': '',
            'dst_pool_name': '',
            'freeze': '',
            'backupset_info': [{
            'copy_id': 1,
            'bk_set_id': '',
            'stage': 1,},],
            'erase_type': 1,
            'erase_mode': 1,
            'erase_times': 1,
            'drive_num': 1,
        }
        
        
        tape = Tape(a)
        r = tape.freezeTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'freezeTapeMedia', body)

    def testBrowseTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'library_uuid': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'pool_name': '',},],
            'operate': '',
            'src_pool_name': '',
            'dst_pool_name': '',
            'freeze': '',
            'backupset_info': [{
            'copy_id': 1,
            'bk_set_id': '',
            'stage': 1,},],
            'erase_type': 1,
            'erase_mode': 1,
            'erase_times': 1,
            'drive_num': 1,
        }
        
        
        tape = Tape(a)
        r = tape.browseTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'browseTapeMedia', body)

    def testRebuildTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'library_uuid': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'pool_name': '',},],
            'operate': '',
            'src_pool_name': '',
            'dst_pool_name': '',
            'freeze': '',
            'backupset_info': [{
            'copy_id': 1,
            'bk_set_id': '',
            'stage': 1,},],
            'erase_type': 1,
            'erase_mode': 1,
            'erase_times': 1,
            'drive_num': 1,
        }
        
        
        tape = Tape(a)
        r = tape.rebuildTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'rebuildTapeMedia', body)

    def testExportTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'library_uuid': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'pool_name': '',},],
            'operate': '',
            'src_pool_name': '',
            'dst_pool_name': '',
            'freeze': '',
            'backupset_info': [{
            'copy_id': 1,
            'bk_set_id': '',
            'stage': 1,},],
            'erase_type': 1,
            'erase_mode': 1,
            'erase_times': 1,
            'drive_num': 1,
        }
        
        
        tape = Tape(a)
        r = tape.exportTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'exportTapeMedia', body)

    def testMoveTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'library_uuid': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'pool_name': '',},],
            'operate': '',
            'src_pool_name': '',
            'dst_pool_name': '',
            'freeze': '',
            'backupset_info': [{
            'copy_id': 1,
            'bk_set_id': '',
            'stage': 1,},],
            'erase_type': 1,
            'erase_mode': 1,
            'erase_times': 1,
            'drive_num': 1,
        }
        
        
        tape = Tape(a)
        r = tape.moveTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'moveTapeMedia', body)

    def testRefreshTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'library_uuid': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'pool_name': '',},],
            'operate': '',
            'src_pool_name': '',
            'dst_pool_name': '',
            'freeze': '',
            'backupset_info': [{
            'copy_id': 1,
            'bk_set_id': '',
            'stage': 1,},],
            'erase_type': 1,
            'erase_mode': 1,
            'erase_times': 1,
            'drive_num': 1,
        }
        
        
        tape = Tape(a)
        r = tape.refreshTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'refreshTapeMedia', body)

    def testFormatTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'library_uuid': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'pool_name': '',},],
            'operate': '',
            'src_pool_name': '',
            'dst_pool_name': '',
            'freeze': '',
            'backupset_info': [{
            'copy_id': 1,
            'bk_set_id': '',
            'stage': 1,},],
            'erase_type': 1,
            'erase_mode': 1,
            'erase_times': 1,
            'drive_num': 1,
        }
        
        
        tape = Tape(a)
        r = tape.formatTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'formatTapeMedia', body)

    def testEraseTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'library_uuid': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'pool_name': '',},],
            'operate': '',
            'src_pool_name': '',
            'dst_pool_name': '',
            'freeze': '',
            'backupset_info': [{
            'copy_id': 1,
            'bk_set_id': '',
            'stage': 1,},],
            'erase_type': 1,
            'erase_mode': 1,
            'erase_times': 1,
            'drive_num': 1,
        }
        
        
        tape = Tape(a)
        r = tape.eraseTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'eraseTapeMedia', body)

    def testDeleteTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'list': [{
            'library_uuid': '',
            'slot_index': '',
            'slot_barcode': '',
            'slot_tapename': '',
            'slot_tapesequence': '',
            'pool_name': '',},],
            'operate': '',
            'src_pool_name': '',
            'dst_pool_name': '',
            'freeze': '',
            'backupset_info': [{
            'copy_id': 1,
            'bk_set_id': '',
            'stage': 1,},],
            'erase_type': 1,
            'erase_mode': 1,
            'erase_times': 1,
            'drive_num': 1,
        }
        
        
        tape = Tape(a)
        r = tape.deleteTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'deleteTapeMedia', body)

    def testListTapeMedia(self):
        a = Auth(username, pwd)
        body = {
            'type': 1,
            'flag': 1,
            'content_init': '',
            'where_args': {
            'library_uuid': '',
            'pool_name': '',
            'outbound': 1,
            'slot_tapename': '',
            'slot_flag': '',},
            'like_args': {
            'bk_rule_name': '',
            'slot_barcode': '',},
            'direction': '',
            'order_by': '',
        }
        
        
        tape = Tape(a)
        r = tape.listTapeMedia(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapeMedia', body)

    def testListTapeMediaBkData(self):
        a = Auth(username, pwd)
        body = {
            'slot_barcode': '',
            'limit': '',
            'page': '',
            'begin_time': '',
            'end_time': '',
            'check_rule': 1,
            'task_uuid': '',
        }
        
        
        tape = Tape(a)
        r = tape.listTapeMediaBkData(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapeMediaBkData', body)

    def testListTapeMediaBkFiles(self):
        a = Auth(username, pwd)
        body = {
            'slot_barcode': '',
            'bk_index': '',
            'bk_path': '',
            'limit': '',
            'page': '',
        }
        
        
        tape = Tape(a)
        r = tape.listTapeMediaBkFiles(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapeMediaBkFiles', body)

    def testListTapeMediaDetails(self):
        a = Auth(username, pwd)
        body = {
            'slot_barcode': '',
            'bk_index': '',
            'bk_path': '',
            'limit': 1,
            'page': 1,
        }
        
        
        tape = Tape(a)
        r = tape.listTapeMediaDetails(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapeMediaDetails', body)

    def testRefreshTapeLibrary(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuids': [],
        }
        
        
        tape = Tape(a)
        r = tape.refreshTapeLibrary(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'refreshTapeLibrary', body)

    def testListTapeLibraryRoboticArm(self):
        a = Auth(username, pwd)
        body = {
            'library_sn': '',
            'ctrl_host_uuid': '',
        }
        
        
        tape = Tape(a)
        r = tape.listTapeLibraryRoboticArm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapeLibraryRoboticArm', body)

    def testSetTapeLibraryFreezeNumber(self):
        a = Auth(username, pwd)
        body = {
            'medium_type': 1,
            'library_sn': '',
            'freeze_number': 1,
        }
        
        
        tape = Tape(a)
        r = tape.setTapeLibraryFreezeNumber(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'setTapeLibraryFreezeNumber', body)

    def testModifyTapeLibraryRoboticArm(self):
        a = Auth(username, pwd)
        body = {
            'ctrl_host_uuid': '',
            'library_sn': '',
            'robotic_arm_info': [{
            'dev_path': '\/dev\/sg11',
            'drive_num': 4,
            'library_product': 'L80',
            'library_revision': '0105',
            'library_sn': 'XYZZY_B',
            'library_vendor': 'STK',
            'slot_num': 40,
            'checked': True,
            'bk_uuid': '269C3D29-3131-4F21-9392-17F0A3CD9368',
            'bk_node_name': '192.168.31.31',
            'server_type': 0,},],
            'comment': '',
            'library_name': '',
            'save': 1,
        }
        
        
        tape = Tape(a)
        r = tape.modifyTapeLibraryRoboticArm(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'modifyTapeLibraryRoboticArm', body)

    def testListTapeLibraryBackupSvrDrivers(self):
        a = Auth(username, pwd)
        body = {
            'bk_uuid_list': [],
            'library_sn': '',
        }
        
        
        tape = Tape(a)
        r = tape.listTapeLibraryBackupSvrDrivers(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'listTapeLibraryBackupSvrDrivers', body)

    def testModifyTapeLibraryBackupSvr(self):
        a = Auth(username, pwd)
        body = {
            'library_sn': '',
            'bk_uuid_list': [],
            'driver_info': [{
            'bk_uuid': '',
            'bk_node_name': '',
            'driver_list': '',
            'library_sn': '',},],
        }
        
        
        tape = Tape(a)
        r = tape.modifyTapeLibraryBackupSvr(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'modifyTapeLibraryBackupSvr', body)

    def testModifyTapeLibraryDrivers(self):
        a = Auth(username, pwd)
        body = {
            'library_sn': '',
            'driver_info': [],
        }
        
        
        tape = Tape(a)
        r = tape.modifyTapeLibraryDrivers(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Tape', 'modifyTapeLibraryDrivers', body)


if __name__ == '__main__':
    unittest.main()
