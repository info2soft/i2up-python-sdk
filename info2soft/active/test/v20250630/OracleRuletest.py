
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import OracleRule
from info2soft.active.v20250630.OracleRule import OracleRule
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


class OracleRuleTestCase(unittest.TestCase):
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

    def testListSyncRules(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': 'rule_name',
            'search_value': '',
            'group_uuid': '',
            'where_args': {
            'status': '',
            'src_db_name': '',
            'tgt_db_name': '',
            'db_ip': '',
            'username': '',
            'node_ip': '',
            'rule_name': '',
            'start_before': 1,
            'start_after': 1,},
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listSyncRules(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listSyncRules', body)

    def testCreateOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_name': 'ctt->ctt',
            'src_db_uuid': ' 6C4AEF37-6496-6DCD-E085-DD640001E4EC',
            'tgt_db_uuid': ' 1C5F3C4B-7333-9518-7349-9712BC9ED664',
            'tgt_type': 'oracle',
            'db_user_map': {
            'CTT': 'CTT',},
            'row_map_mode': 'rowid',
            'map_type': 'user',
            'table_map': [{
            'dst_table': 'a',
            'dst_user': 'b',
            'src_table': 'c',
            'src_user': 'd',
            'column': [{
            'dst_column': 'e',
            'src_column': 'f',},],
            'key': 'LopezWilsonTaylor',
            'split_dst_table': [{
            'condition': '',
            'dst_table': '',
            'dst_user': '',},],},],
            'dbmap_topic': '',
            'sync_mode': 1,
            'start_scn': '',
            'full_sync_settings': {
            'keep_exist_table': 0,
            'keep_table': 0,
            'load_thd': 1,
            'ld_dir_opt': 0,
            'his_thread': 1,
            'try_split_part_table': 0,
            'concurrent_table': [
            'hello.world',],
            'dump_thd': 1,
            'clean_user_before_dump': 0,
            'existing_table': 'drop_to_recycle',
            'sync_mode': 0,
            'start_scn': '',
            'full_sync_custom_cfg': [{
            'key': '',
            'value': '',},],},
            'full_sync_obj_filter': {
            'full_sync_obj_data': [
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'DATABASE LINK',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'INDEX',
            'VIEW',
            'FUNCTION',],},
            'filter_table_settings': {
            'exclude_table': [{
            'user': '',
            'table': '',},],
            'exclude_tab_with_column': [],
            'exclude_tab_with_column_switch': 1,},
            'etl_settings': {
            'etl_table': [{
            'oprType': 'IRP',
            'table': '',
            'user': '',
            'process': 'SKIP',
            'addInfo': '',},],},
            'start_rule_now': 0,
            'storage_settings': {
            'src_max_mem': 512,
            'src_max_disk': 5000,
            'txn_max_mem': 10000,
            'tf_max_size': 100,
            'tgt_extern_table': '',
            'max_ld_mem': '',
            'keep_incre_time': '',},
            'table_space_map': {
            'tgt_table_space': '',
            'table_mapping_way': 'ptop',
            'table_path_map': {
            'ddd': 'sss',
            'ddd1': 'sss1',},
            'table_space_name': {
            'qq': 'ss',},},
            'other_settings': {
            'keep_dyn_data': 0,
            'dyn_thread': 1,
            'dly_constraint_load': 0,
            'zip_level': 0,
            'ddl_cv': 0,
            'keep_bad_act': 0,
            'keep_usr_pwd': 1,
            'convert_urp_of_key': 0,
            'ignore_foreign_key': 0,
            'table_delay_load': [],
            'merge_track': '',
            'fill_lob_column': '',
            'keep_seq_sync': '',
            'gen_txn': '',
            'encrypt_switch': 1,
            'encrypt_type': 1,
            'encrypt_key': '',
            'table_change_info': 1,
            'message_format': '',
            'json_format': '',
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',
            'jointing': {
            'table': '',
            'op': 'append',
            'content': [],},
            'enable_truncate_frequence': 1,
            'target_add_columns': [{
            'schema': '',
            'table': '',
            'column': '',
            'function': '',
            'dataType': '',
            'opType': '',},],
            'initrans': 1,
            'redo_read_thread': 1,
            'virtual_key_settings': {
            'auto_switch': 1,
            'manual_switch': 1,
            'auto_col_name': '',
            'auto_separate': '',
            'manual_columns': [{
            'user': '',
            'tab': '',
            'col': '',
            'composite_col': '',
            'separator': '',},],},},
            'bw_settings': {
            'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'biz_grp_list': [],
            'kafka_time_out': '12000',
            'part_load_balance': 'by_table',
            'kafka_message_encoding': 'UTF-8',
            'kafka': [{
            'binary_code': 'hex',},],
            'dml_track': [{
            'enable': False,
            'keep_deleted_row': False,
            'date_column': '',
            'time_column': '',
            'date_time_column': '',
            'op_column': '',
            'opv_insert': '',
            'opv_update': '',
            'opv_update_key': '',
            'opv_delete': '',
            'audit': False,
            'audit_prefix': '',
            'audit_appendix': '',
            'identity_column': 'AUTO_INCR',
            'load_date_column': '',
            'load_time_column': '',
            'load_date_time_column': '',
            'change_table_structure': False,
            'date_time_column_unique': False,
            'load_date_time_column_unique': False,},],
            'error_handling': {
            'load_err_set': 'continue',
            'drp': 'ignore',
            'irp': 'irpafterdel',
            'urp': 'toirp',
            'report_failed_dml': 1,
            'info': '',},
            'save_json_text': False,
            'include_tab_with_column': [{
            'user': '',
            'target': '',
            'column': '',},],
            'include_tab_with_column_switch': 1,
            'full_map_switch': 1,
            'map_type_list': [],
            'encrypt_switch': '',
            'encrypt': '',
            'secret_key': '',
            'compress_switch': '',
            'compress': '',
            'src_db_auth_uuid': '',
            'tgt_db_auth_uuid': '',
            'comment': '',
            'incre_sync': 1,
            'encrypt_column_switch': 1,
            'encrypt_column_method': 1,
            'encrypt_column_key': 1,
            'encrypt_columns': [{
            'user': '',
            'table': '',
            'column': '',},],
            'incre_cmp_switch': 1,
            'incre_cmp_db_uuid': '',
            'incre_cmp_db_type': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.createOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'createOracleRule', body)

    def testCreateBatchOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'row_map_mode': 'rowid',
            'map_type': 'user',
            'table_map': [],
            'dbmap_topic': '',
            'sync_mode': 1,
            'start_scn': '',
            'full_sync_settings': {
            'dump_thd': 1,
            'clean_user_before_dump': 0,
            'existing_table': 'drop_to_recycle',
            'sync_mode': 0,
            'start_scn': '',
            'keep_exist_table': 0,
            'keep_table': 0,
            'load_thd': 1,
            'ld_dir_opt': 0,
            'his_thread': 1,
            'try_split_part_table': 0,
            'concurrent_table': [
            'hello.world',],},
            'full_sync_obj_filter': {
            'full_sync_obj_data': [
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'DATABASE LINK',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'INDEX',
            'VIEW',
            'FUNCTION',],},
            'filter_table_settings': {
            'exclude_table': [
            'hh.ww',],},
            'etl_settings': {
            'etl_table': [{
            'oprType': 'IRP',
            'table': '',
            'user': '',
            'process': 'SKIP',
            'addInfo': '',},],},
            'start_rule_now': 0,
            'storage_settings': {
            'src_max_mem': 512,
            'src_max_disk': 5000,
            'txn_max_mem': 10000,
            'tf_max_size': 100,
            'tgt_extern_table': '',
            'max_ld_mem': '',},
            'table_space_map': {
            'tgt_table_space': '',
            'table_mapping_way': 'ptop',
            'table_path_map': {
            'ddd': 'sss',
            'ddd1': 'sss1',},
            'table_space_name': {
            'qq': 'ss',},},
            'other_settings': {
            'gen_txn': '',
            'table_delay_load': [],
            'keep_dyn_data': 0,
            'dyn_thread': 1,
            'dly_constraint_load': 0,
            'zip_level': 0,
            'ddl_cv': 0,
            'keep_bad_act': 0,
            'keep_usr_pwd': 1,
            'convert_urp_of_key': 0,
            'ignore_foreign_key': 0,
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',
            'table_change_info': 1,
            'jointing': {
            'table': '',
            'op': 'append',
            'content': [],},
            'encrypt_switch': 1,
            'encrypt_type': 1,
            'encrypt_key': '',
            'merge_track': '',
            'message_format': '',
            'json_format': '',
            'fill_lob_column': '',
            'keep_seq_sync': '',
            'enable_truncate_frequence': 1,},
            'bw_settings': {
            'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'biz_grp_list': [],
            'save_json_text': False,
            'error_handling': {
            'load_err_set': 'continue',
            'drp': 'ignore',
            'irp': 'irpafterdel',
            'urp': 'toirp',
            'report_failed_dml': 1,},
            'part_load_balanceby_table': '',
            'kafka_time_out': 'qo&JY5ZTgVVjZ4NzOBOuLddsrwPe11xbCE^*0yjo6op!m)B#stAi1]T1)!UGjubwadQ8lV34GLskNcOWqgAL5d$[pQpW)B29FuJSg0dWpSQ4$uq)c2GtEny8PihwgyGdI$h@7^HlMh)GKsWD39!pw1FWJ0((0F7Sy@$Xev9k[v99@hCFyWU*oWVy40TI7iyANckXrg7JsMzjd@[G@zJ5j#WRh$glW9)c%!uUw1(o!#zz3JTgm&q2548B[io]8meQM9*rj^hrjSbA#vt*HHQ^Om69(I!m&kP^$kXf9B6mG[z0K&Bv7SqUYky3^[Dc^l$&4Y*NZjCCo*2Gz)5Lf)(g%ER6Woq)ARPHe[0$O^^6qZMe@0nvxQ3OsFKR0MzXEuRCf]75%f95QtCOap5Gc]D[6HNe^I)sub$BnwUqHHqe1[tAGRyz*rDgez^#wwCn%7sYr6kIjFa6uHP%8l51x7p$]UnnJ[W&L0!ZcAh^zDTh@pR6Wl6lh&31PloxSO^iWFfp48C3rB7*OpuVHcctT%&ry6T$)o5uqVGQXGj3FD49gqWvCHWo&w[jZ4XCtx0RsB2p!TRRDdG4B)UwQyZYh%2ovuM21%XdpGsGTRTENrwyXQ%7vdlp6L(&DT9Wu*mI6(odctYrAH9vVe%]HHz*]NF98qLO9mJ@]bhnGUMOg58Vq)x2Oe%w1IoEp$W70j^0giNyn(3T9(g!xwbRtI4tdqlvqKSb1V3O#mseipjoH5bCB1t*BPx55FW1dwDtLAS]DLt*KLrQV4Cz%kzV^uts0wZ)LGMpV2L%uN*L%8Bo[P!TUP2Aq!LXh08D*f*Fr33MR5YD1LNB[#Z1Mg35Pxa8zoc9XNcmH5BoCCm3gAHfmXxo^IDV$6TpQWj]!jbe8r1[p)OnAxPBp$j9zUR8roA&AfEP!H92UWK[WhJQO#P1D@Fq3sIAlY@a^HBTLc[cseA94rZ(qY[u!q@(^NV8kV6on0z3H[&)iKRJeYUBZguAbPU403eL5$^S9wgSjxQ%zn#KggUeePaxblDv6^KPpk)0R77JXUo^RTninMwvSMvudHVohR^[bzOYDkszMhYJf134GnnK1!qybuf0G4i^Alz)seQXBzYzDIfs121rUKgEF0nEG!&xXzj0I*AT8Kz00SEirwzjkfXGfR3L0kxM8GT2#Myo8OJd1x@e%r7bO&gZeFGRR!CUZlrDK107gZwisM@&Buyax*2Yqk6Vw)STcFrkkRKZjrLVVkO#inQeoFsU3dPb!5%e&qY[YdM!!wmfqr8q*SlVGKiBi$v[mr4h$28JIfK[YQ$03tDvxei8QT^9SV^gWriqDQpmAh6b4j1wxUoGxW7&)(5^KE8Z[ym5&I&!7hZKnx6khW&xXbgew$571Zk*dgiEGJG3wRS@flqZ1jQZIUbqGpMuScubf6de5fKC0q2fVMk9U$uoFDSqAMec8ac90E^aKXFvxQM$sDScJ9rO8vC^ATMSF9RZ83TggY&^@x8@sw5bujfWz$41)@WpCbC!#rXMfEcIMUI!KC0(guqEhGICT(gPY#fNef98@Im$)poUNf3J9B&PbFCS(091)OAXHEtaSCIPKiHBlW$viS(FJ3OUvpDCU(It(f]H%4^uQZVrop#acwXZE5tE]!&Wzw%HBiuKLs^1a22(j^(VuppZ]5MOclTEJck67!IvuH9(tD8Fre)Q3l4e&&Xj%yDAZfTj&YeZXEMq^X3RN2pR0eVPaKVDiG!GfAQJboL$)qp5ZEU0^Ux^@omBmKy0C*pm4MgiM3HFyz$7nS]o7w%(6ZtV[9J&uIjwYqV94YBW4j@E6&Cge$rRTjSLL@hPM*!lJhiNVJ1hJIAWKQ&iR0%@s)NdmjAYjGG9Bd&ZKM[Wehc9acIuTMHk4BCUJJQt%qb8FQ[0u@H&@)DTMANKO)dB$d3GGu]Ft*H1n3yyWb^2v0N!5VT6YFIP544JUaee^gVQH@$A(%R@oZh@&xGU4!*DHJejrH$BA6WKltTCHuQcRO%&A^C8J!Dvs([ltZ26O8iDWRy!o(tOYbD5qlkY6FIVJPcEB8p]XSQ1P!vN)Y^U)g4]q8x5*GQ9o82m2C0#X1ukMZtIfNMT)J$4cWh$%Gg4cscy2Ql9yo2L!TXDeM@vqmiu9ODb(5GcADBXetshal&91kuS[7eO6nYuLZCDmL352)DK2jD*P4JG22B6pTgj[L$ye(dRmI61QR&5imswV4s5ccTfQqlYb#@7443Aw[ISn7qrCrBRiHXSwzSqc8ekrrW!fDkle3Yze!B(Uwu1H(uygV*z8e2%czU5rfXr9v%119SusjkO^RH[hrr]ZKJ*XBTmqbm9g$ii$qF]Ai@uoveW^!xjgPok4h4y6]S(O7yor#Fr9E@$xwJrDpkU!8lu#zbZ$RGIxXUsm8xHGg*4oOLwxlGeX%KCacb$lzd*A[elh5Z8(sS*W35iCBb*q9J8UG]oJee&aOhryUnmK*8X)[a164yKoEVvP54PNOwj1w)q^jUJTmFERhx5&sNN8^ajC2&!%G8xiFB0(OSeY#uezvneD#[wAA[HI22EcTRv598&SLSSydGVDb2BY0RArM&2SZlK1tFG0GtUrg8SYIn^rlN^DIOSCt)8^HjEyPnn&NF@j7Im2^4y#AqJGTpmxo5jjfFZz1Zs2rZlV8oMJH&h6V90du5IcNmGtseee$nY0gf$VLkdFhEI8A2W1J7rG7Dyr[KN[LITUCorKCs91H(J@C*uCBr@#@@Yx^llzo01%o7cbvU$#dt4(UtuHHt9yn%Xqh5HL*!VYcbdBIRdi9k0uVVhxYULqcAW4k$m2PZKl8YtcKiR]vV%tgSQqdd[R)w8]up(58LJC@SZ#DcOFJwiAjKrNiL[kcW@s)HiJL!f(V#6^[%0HW[ax2YT0BedEiCeqHKoKOZfxBIeZf**Uk$!Y&uxw6u&8fRnni#dRsI1Re&xKxY&A#x^4ag1V^[(bhs61cU^qSPE1f(5VYS[)NUtMwpErWyJFYmf1$w!1r0U]Xv2VN6nlQKd!(G9&p@7uiYqBRADo$ipF#t$giYIJqUIGYLmpil38Yf37CEW!3BtJCC0f$ehTVe(pe#$qBZT&uAP9&DSBf*HSthTZ(Q[pF#Sf7dgnI!b)bjBg!tFbmyem9SC@KiXk2JbbXT2yTb9SFGfsjr5I*vpxLl@@g15r@0Z[%8IhliL^0kXmM4moV7GkwXoT[X)oQ)W[MGla8v7SzK9U0vkD3yRruPUYcdIPz@&WOf%v!MI9Vro(*7@$c91cNA3CL^@2V&jMzwyls@TKzX8I$QW2R8iK1WULjVrye#[fwMY$1WjPXv(KdZdcQb0s0UNAU^DzUZZAL6r5)$KGiWhYGkR2Fdd#pFGQ^X9p%Am2qR$Z%r&sjAD3i*d)sbo7[DqMWoHfi0HFl!*Mq[!1(@vzZ%mHgVYwgBs8DLpjCLH%eb3s4@y!P]DbfWj6kqF5PdN@Snh(stZNg(3Yr8hbrH*#5vvo9j[Xx2sLWlBRxiE!(RTh7mWDWcXrrcdh!%2lffOatIlUGrK8*b8m1c!85XM!Pl15)xec5xk85x0YmTU[y8^^8]4ZQ4lK$V95#xU^33@w^D01B6oAgIBOoM&1HpxN92HhWXbDhhCp)&*wktOR2Bev!tqLe5EN9sB$7ojC0#@k3H7G&qX7QTXXuN9GkJU$afs(z2OMb[7CL)LQRn#LB&7kubLn[HjxMKUGf%PX0naz%s^C0DwU0sT6y1wfKV@8nV1yfRntt55FjrOIKm%Ev*Z1%nuMQ3AX9Ff@qKK#hnil^&a&*0GQ2*t[%2cnInM$TfR@Ym&p0@W(qu$vfcToDHBtoPgxK&hiO8cvvQ*11M#B7D%2OQ%SiHZZ[S$koGi2d[H*zSe[A4S8lfHTCOLGuZhRn5jiIXzix6BJjQFQ0c(^J@cVKZAlNUmiJ&S2NtmDH[Fr6K!@s2qrnheYPpXgX*#tk50IYXYL%vVyK8eMvPVqig2Rh(#nyAke*@1]DxbC1EiX49hRH&wGCD@Ij6IrMCXUrCN[)UB956xDp*4Av1jT1sXqF)2s*hL09Axd2x2%O3i#&bV8ooaDur7p!R6U4^vMI6ADqh@2Vv)i1QZ1[$v(kR$dxaK6ggjHN8!!i6nDZWUe1@zE#Vms(bhMl0))fdWq(CVKdYwnxSeBNvtXsN)aGq8CNE6fo7rMupP35t8(cKB2S^*7ThyBPmfp%7RGTBlT!%MTLL5%o7Hi9Y%aZo#T*f0M]0EKIrsBdSGELPcY$AzQyK2SsvEZqOHW3yf!uS*DmUR74fnhDxo$&PL$WuO8%Q8owItSOliD3wOK!u6@5ypkAc2d($M)veSUZMQQ1RYhHGUSl1mJZMSEIp&czSKc8WsFH9[5ZhWJQe0vt&6&B]rxg3)(b23C%k(UE$LUQG&ZqubNdkQX8vjYrkVh@Irp%z1$Fs1cg$*IQuDAt3cBxGcAKLzZHf7kD83gz5n*G5KH0dQV7%OtcLcrO&C2jyC@LI3BbP76PIp^86%Zdyq!o[pnrHJ%RwhIUS5s$gnO9dCNGQi!K[ihP0A$W@fGXm1E)]DY&x@j[iQM^cGpxc[VD9(l89A53FzU)*#mOuX1cVM81Axd@bA7de@AA]T#vMwb8*]!8jPEes(^ssSqe%sc(EwvOe9[q4AnH&6nIm9f81EYe#q[OMKHQlacoY8H6^AH7c1nosNLjhSyAf#ZN]8&hf1Uujg2$vNzwQVkj&[T0ueRN9czIRkbkAvFYGf*Q0i#NlUD6vZ5)yYKMUYolDLCHuF5K&hU4&vy7Zv%u7Nh[XT51Cp[yP89r[PIXsUu$@M3oP%ToYvvAHCbO0Mqdw4y!vSTEYg2)9%pPhc70K0*k@L$YZy4p@&tW0vRT268G(BoxeFDRrM4]tTgt0MZbvI#w(c!$MSLnF]AlER@8iC#aqO&0ygxte$5*L9H[vnscrNwW[u9rhh5GN^)^414P@nN)J[FHchCe#cWn91qLQDMli06GGH$k*!MPs@cO7#nmDs3$J*z[scyUCZ5lz5XYmHwiHse*0neCe0hpdcaTH6yrJgo28#KLVF05@wbgfSMY2xpRTdC!$KKLDWI(^SGuP5wQILBkBVdP%u@&3SxMkW*Lkl*e2BZZ[!i89XAdB0qNT)9SZHxA%XrUM(7FMn2Wo5i^6^[vWLrMFRGcDbnl$H0YIpwweJWYn31&]yUC8IFn@tzobemL6q2i&V*vZ3tb$]DUj%vtp1U&OKni9D$Fbg(DECJfkK2jK$fz1y6uI#X0xQzfQkIVd$ALimwhjTAzcQyGvNm@peHpv(XmepyyETZtzGHOZAx1)BYL3x&0v8dF2OhDJuJGThzqvd)E[Lgooi1BjSLHM2uhpzeiIC7%[Y!9[vvi6NoT1hVhZeK2Z6GB4k^&LkN$HnxMT[GoD[OKHY!$rqJlOFXX6Qx[p*QmDpNgAuNtdB1cVoz6f%vS91pJkl8HVVlw8gmc(7HM7!biB$0Q0zVLFpcVERSnp8T8XAdNWE1UmLgYQ9icqBU8W(CU)uh!VGI12BRBkB*(U*eo!8Wzt@@vI7EH7^g58qv#X79pNz4hjCp@D[U$okb9IO6!ZfykkQ*Y0E5^!1x]!%%gc4q&j%10d&Hu*kF98sgI5Mt2aKXiYAXwOKu1jjd3MO$PHLQCllQ3OGWVX]s&DpHuNfvMwCkYSGOiH@sHqV[ALfmG$MbxDy&(fWXAJv0!F9LChPwB9[!t2WDV#acH$%HOwJ$414Xc!%U!VLFgW%B7LHYlY@Tg(8[WqZxRAvz)705jDUyMK&%S1OM2hLZ*R#2D^F(bh$O^DpUS)lhGu5!Ir!f7TnoRZQXz(CgpX)Ko]TtP68nn1OZFQ&fM$I82fY#l@gttrJILYAZC7ASqzg5etc6K!G0Y6QPrzjgW(LBLQ1pxL0vj5eER6AsMqdRhQQQ$Ht4Q(MhjQ!1#jhEWLNil4V230$^J!QWGRv47fLHFQsPYv@I@tZvUE#DKq2SPNi!VQ(F36B^*iwf&[4lfYpJyCCnjky^hecp8$M@bwidUko4L@cPv^Tb4JGZz9dv$d!DMut7j9ZkdUx3(DPhS[^N]F@m2]6qxN2cvi(NdauPLjiP6WqmQCFC0Giwh#]^Nm(YuT!xOD39NtfPYLnwzg*#7JEXH3DuutK8NCht2E6(60GwXAsMl9ZlW%)ZAXpRNi8kjcWKH&lVTW)dP6tmMSxG[7ok6vS40Y&NACnR@7JY!TCo4XiCuc^Dy0i74EGfqg060Y^E^vNa96VhKT2#oeyTTpFhG]3dW^Ec4)@)2NvxGv&f5QVP3y95#)BLF)V%rmFlKmGE@2Rel0*vYQLG*eKysq@u0fx0jPf5JquHn#qJ9]O$JUPFr(pFS6tPzFbN5eGTB1F6qch7Dyvm%uOtOQ818hHEPxGnASTdd@ODNpjtW7A@GpV4xFID4C7DYGnoCCjN0KqH%Y0)pz@33iuE6GNvLd46H723nlGDw9AeI46q$ZWgW!peSbcqLVD4NbeVp#(7kVi1FtMw21[V$)RpPc[loX6BmftUQ@Rla11lw7QFiMG!8ZXJQrFRfdqqbZ%8%RJ7!4dOiZc6fqoOg5y[%ki7]whGM@B!#iOcJp%bR$UNw7839BXg0HJ33wyMPCbzX8x9nsIV1q$XN(cIqdL7(RvCrQdd5BY&7)q1lDsTsOQlLb8%Fnn1dj&cIP8PZ@JoIH#t@So[4]Lx&wwo2@yhix75hEXZWuB[c6G2o@ovOvsJpVc(u7k3ZQlK6$ja)1k(r@pq$DwS%N%IoTL4e#Y)VGF$yb]R7wm3ffDXtJPRo$hU#F[S4LX&H(Q[]KUkg3ovv&G7prsF%U4V!UZkFvBCKOO43lK*n@dP)$qhyr9Go0(UDmd1DxhMS!UauuU(^lX4qXba8QB9$qchMtpnLyG5ZP5&bj757blT$&S3G%PPCwm$)lvw7GDnlBLpkf2WRp)CwmhrAYyHvJOLWLZ1)zX!(dqt8k(xCTGe^MzsGBQ$KpKiS1XAJzojUgY#nvmCjVXcd&lX01UoR!LINhE3$k^f$1xvz1n&JHfr[gjs^Cx7rGyZyV7rSNzUrjdeAhl8d6dDQOcFnknc^L6f&L7WDtLn3RkV$!yj[mP6b*WJdzuqv84keST9F9g(wgMObe$8Y6JY46oNLIMBlQjv$CGUt8HQcxkn!sLTGXmYpquYSsXu(zDZRcoMxP3t&WYYBqPB3f0#Y8%nCXgTZE070vQmdBkcKW)pYFzCl(]rsz*Ks8XF)*BU#af5Jayecgp1s#5I0[M[cMX#Ebv^w%VN#[NfRSR7WwVQ7U7HFjktXHwyISB6[y6W0Gn%QYLQ@d!yrv*Z!IsxG^OQQ%DVb[71g3SY9idY@hp7MrBwMqFLvhyB&Cu6uZf$2MGfk8ZH*Q[ZFf$U0QIkvCU4duf0o@E)O@0R3F4aMh&*We8Dq[hwXmz6$IT@jR9h(RUpVb8^%D$JTXSW%vnl0#HPpz9K)bSJ5GDfr5Yihx0@4^Jr)7&tKle^%zZf&CB)c^N0FDcAlutS[ig8VrCS3)KGqfS#Sw4kmQ!EQ3N84H$LT#DKFt&UDw#v#!q6nUrAReOA1P*#D(purPA3&wZgDjfgnCwSzBuBlv*##KQlk5N(Fl!&(Bn[dvlKNP]tWQShkLEacGaWM)g[bXb1u$icb3qnQBsZR!BQAsF#^ugvL&!Uey8![2)WwlUsgS)9ObSs7FLr*DZnAEJtPt9xIl83@)kTyTzmx)ipEl&)$7@U#*$0brfu]gQVPTBgLhPT57Aq7@tPGpeieRxOq45G*OD!Yr3NLaZzMm24wH9P@J98$^yUDVgGxuc4&luMytIH)HJc)z@d^N(j3Yy]gxk5DYjDs6e6!4wXVj@&eJ5YQj4@SP*e(FCx89P71B72D[bIOSJpws0UvkJSmrbe1asf3JJ1C*D1GgAF(RWr^(H76]RkwbAbO9AfyE!&Y]v9QjBRtfXT^M(7[hLDMixHC1hxy&7ZNfCtwiKf)73VwAxAbySY6SK)n@Id2ySV3OR8gpztL)jJRwh#Zusx8ve5V*gNr9iWSsYv^F#zZ28UYRkAGqJXFWv9@l]jyh&k$81%ehlLtB9*hbk%nPg%xAlZeVekQVe^gSzj1Ye#BMIkomW]p&5D6OiNmq^yM5iKz&gTWvmmFgCIZ@P5H$Phjx^@FYr9hOGB8W5hv]TOIw4IwNsHkCsq89O%r$dT%lGjdMDdhu7)hHsYe@W&4%id4RGX7ZQmhIUQVFq@l&F^Z#wn*^f[m(gORpQfnPtBQAdQcV5Cs95nTk34l9Wb87zzUGQ2kz@Wr(8X2%0s152l*7!mkQrj$Q2yR5JCm4HRakC[WKY%D4ho[FIOjfnMaCotcv6SAftM!cclEKV*XTbQXqI7s@NIVmY2a6nYeW#dZROR1yRJ@CNm6W4*qL*wOJvwex8NO]!VH!8Z6J7s6(!FcNn1FOTbgh#y9ylU#nKAWfaw8sf5VEp[Klr6QpSQaiI(u&cwRG9QYDa(viD6IHplcS4Hmm$TAOihb)c9vj#4H[$*C$fd66Hgdw72zA5W6UU1!Cwonu(XRbBQHIV2S]Wvy4vJiwR8$#gihT7qz2JhB)^eZm@nH*bc5yuBMqAZJ0T7)PZ33L82vrfRVdCRu&873!GHhwV9Rm5AHW!6hxaWnorOk3$z$werYt6lSj*rI[@T[DFi62G!qR]iplt)6NkxG7%KGq0X26lRs$[gzf3L*jw*(&rmPTj@%YOoUavv1s^emxHmebMQZuFvK6%9ebKjBpjJr@68Mzdmx[c^ps9V)^o!PE]W3#6qX&kfjV(ES&3[ZtnXtS@fXyig@%RBn3VV2&WQDYVnA[p*Vk^I$tx[BifEDj]DAJK[R2$qMRZrXAjCwi)&j5HY([!6b7XitzoCE90Gq&EOp4M&EZNLAFsg$e#LSn68w%MpRX%Xc565V^IQXgoJ@BIAN2VTp#!8Hy0#PO$LId&tucSfhb)E^3meZypyOhTB9bzZY8ns@Xsxi4AeY55M@DzbWGR(3FJRG]d$t9wP6zrC9IJKt7AwWlUhCPQ2vFFQ%@orFzDiOT4JUs5Dc16CUD41GCQdSAJkr2M4YzG8kEfC*eVSz8BMX4FalQ6h7hul9EPAkk7yvlP5YfnehX@IveGDUZ5p2R0M([EcxNDP*43N9JDvCg^@d6zHj&ee@aY5mjN$2r8C#Zv8kd!U08#VIG1DsM#%Q2sKnrDumE#Jk]EZ!(ki9E)cX)R$g]CDmq5$Ezk)L5sQX2CF$UT^3&gaUu!p^lLo^NM4ZDVgx2t1y)D4PdC)&*HCRWg45BCwRrN$mURr1O&%z(J#sB^iJ#[6dKf]O@z2EXjUbb*CEeb1zQJ*ND%PG5H]1avlTlet2a)vXng37zD[*s3UlvJ3JYR!HrjwAGC*o0CBpLi(3]qQNlwF%s&2FwykHeh&wVX(PsAHv@Zbyu5(p4#@SyRP!0&JFHBte@Bc]^o8kHp[GUE*a8gu8A[Hj6vkvE&fhgooX8^I70p1gvUEP[%cP6uY3z*a%#i*D*!s$g4el&fNc#m1E^M8Xw(d[o3D5IOWd6jig3!ZCcBpc7(iSmwj*Akt%Z[#)X4xCkYP@)&@Y7r3jIq351q$YbT@cnwulD*Oi%HTTxKMYlAmxX1vu^q0By1MH#Mh%0aWvxU0&1fV76oKW[0o3J2QCGtt9P3G6slefm6ppW8&COkSEhyC4ygi6%S&kVhx*md@7G&[x7[ExI2$OG(1(UL!ZKIEOvxChM#scl)92dX]RhiLosjdaB2&AJO5o)E6EC88Kp^9LjjTDv4MUyUKcwDVkBVBj6IilnQPLb$HA[3ABGH@r[J9KGxFISPw3OBX#v!5X4Ykj@lGct%pB6ywDURPxRI!J9wVOW$ndA5zOBdrXnOOPCGwi%oLjBuMJMdZhVanj!wJEwFIs64eO^gd4U6&h]v!tEGrylyj^mwc4N#qTRrM*WkfqdC23pv%SbVZ(bG(KgESqvRQGWHGk9HTmLLz54&fJ]NUp1bGQnHwEYUE6dAcWKSO5q83gWZo$D&A&XWg2iGcYP20[nk1d6#UJcR7]sX%q6NMhRnEPZ2msIQYwbXVl9VGs46ZtUo&4Hw3XIvv3tnNZOororKRcYS8Ng%@@kI^buDcG66m$dwQ$67zGrXtQADChKgi%p2PJ&dzHb^D4f$OE9[TZ!VbRxQaI%Wf8cHv98cVMjOvcw9TzUYuBkl2&&LzG(gGR1tD%H4*yw^D&A4RG[jzxVFzrwXxGEAj!Z3Z9sGz!Z)bE&k%6j24PKjCGd#9eAx&w*Nzm%8!64E@vHmy3kZ)@sAI7sB08olm%L^FVpjJOx#5Inw)3POH)35*NodT1g959[@fqx1qFXF5iU4W4@3drXqTaP6fV9%AjOFcnYrukZ8nMRbYF54*GpKmh7Mzdy4eQsuEQ*sO#C&hJp#S0hK)PL$SSSfoaA8$uVT411f8Is6o$2Ow72H)2PBYv6zuxC@7!iJl%uisjjkFAgs74fVVInrDWOUSwmRClwo$Ho1ZtxK70DzYDIgOyVjSyXh!N2zxFigE5Q%[PN2AW#P%ZaJikMTdxWKzY$tk(d&#LSGe*UB*L8eX*fdrpptP$m2cUDMkCXs6!7vgY^r)O#pvrJAmO23B9$PdWEH*a3(UJ()7ObcI(0WyXaVK28f8lFqpv9hn87j)8gH6NJGimDhIK&pYptJ%ekLzRU4oZ%!E16pgUrlT[net)j*!6s19WAr6RDpmeFpYi2JSsQXN1rD5f^d4]bPn4jPZFtD9(*6&U1MSUkp!@0Q*PJTCuu[ad)vbG3fWoK6d6jkXbg%7NZHtNZWM^hm0k1Fn$UPs6Fj%Pi6X1sx5hT$nU7ZzuC]&IPBC^*^HJ6dJ%v*aVxOpKWL@90(wbTFzbi!ceJtbIfWI&YuMp8d06]Ys[WF)QI()i0GcdPhc@BIq1P&e2^%3p^VAEw&I[DkJ9(ToT^!Xw30K04S[qB)Yr(GgH07K@bo9[W]PtCMIFq482YKaBshlF2aOO[QHC(t0cgJo4QF*$$bMH%iQsjkIVXRqe7cvfDS[v#sjNI64QmZ(Ex^VXfDvuydi#Fc)3x9cpxZuqMrHYA&6I)7pA@8kArYj4kCjgNe76!tfXyzkhFa2(DTE65QRDNEC^HpFKdqMB7uwSTmqvrB6*HQru[chuZ(9vpxM!uNrkHNXwYRSwd8O8%ik3X(%7xl#kjClAHD*EmE^L7kWncO[M4VsWy#WQUo4FS$M*IOT7Vf96O^WrByeGZA#%1x3Vi9lvDKqgjY6w!o$PpzdRra4%(QQ2xP%l42uRw&D2BNh(9AANS$x6Kw(DlGZSq87f3Cmqdu)c$mhY6eo3qft8yt]MkO5H6U*cskeU9NDGu%4ll1XZ$Kx1G@FZ3*5UTKr[K7DDD%sqoV*M#DXrkP[t9$piC())N]lWv28vyyupdzW4Qlx8@CcBW&lRQM[8NvyBB@JSCp!EkzPeq4Ey8lq&gTJysBmJDY)ZT&70R3mrQ$9dMYlKTYbvFgClRW#bgV3OACieUM4QeAHCMED8A1RI[OWFELU&7RNDD1hUEl)MEulynpO#SR!3uLooo*B%vGc@KvUzT1**AF8@WbYwOPVBbU7H$AXv%9NWx9QKC5vLLI(pTt1e168sF7eTCp)D@6rho0$beUebvsV7U2nB(qvlXUJv6g$gW7)Q3OY%TypoxyX0bE%c[b4D08WIrUUtr(e8vVdg&%$8bsg[mu)Fy#R9#a8wLDe$*&)mRha00Kcm%r*mpLI5!D9aDhJg)57)AnL5cBSuodP2xKPJO2wRWmxUcv%ytFP#&F3q!uduOahZPn9c^qAOP)GSEeTB&E!MNYcO8#b[n(e)dX6Q(b7H%bDTu8hlu4S2$hsHw5MJ0FOh1DE(jH9lo#I@O5r[!ot&L^AeUAZK*TX&I3[C]xFq3f7L!jbj4cVTZSty9Ar)mYBKvok$cBUAeHPZ))*tno8Kr%b&syww1tANNcyVok%W^%C8HNQdEWroysU0!nzC&eCV*OO6c75(IbcJc^B7gkrA^OldG*bS5teWWpHCpyRb$0C%7H3QQSUlc$',
            'kafka_message_encodingUTF-8': '',
            'kafka': [{
            'binary_codehex': '',},],
            'dml_track': [{
            'op_column': '',
            'opv_insert': '',
            'opv_update': '',
            'opv_update_key': '',
            'opv_delete': '',
            'audit': False,
            'audit_prefix': '',
            'audit_appendix': '',
            'identity_column': 'AUTO_INCR',
            'load_date_column': '',
            'load_time_column': '',
            'load_date_time_column': '',
            'enable': False,
            'keep_deleted_row': False,
            'date_column': '',
            'time_column': '',
            'date_time_column': '',},],
            'prefix': 'temp',
            'db_list': [{
            'src_db_uuid': ' 6C4AEF37-6496-6DCD-E085-DD640001E4EC',
            'tgt_db_uuid': '',},],
            'db_user_map': {
            'CTT': 'CTT',},
            'tgt_type': '',
            'maintenance': 1,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.createBatchOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'createBatchOracleRule', body)

    def testModifyOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'row_map_mode': 'rowid',
            'map_type': 'user',
            'table_map': [],
            'dbmap_topic': 'test1',
            'sync_mode': 1,
            'start_scn': '1',
            'full_sync_settings': {
            'keep_exist_table': 0,
            'keep_table': 0,
            'load_mode': 'direct',
            'ld_dir_opt': 0,
            'his_thread': 1,
            'try_split_part_table': 0,
            'concurrent_table': [
            'hello.world',],
            'dump_thd': 1,
            'clean_user_before_dump': 1,
            'existing_table': 's',
            'sync_mode': 1,
            'start_scn': '1',
            'load_thd': 1,},
            'full_sync_obj_filter': {
            'full_sync_obj_data': [
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'DATABASE LINK',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'INDEX',
            'VIEW',
            'FUNCTION',],},
            'filter_table_settings': {
            'exclude_table': [
            'hh.ww',],},
            'etl_settings': {
            'etl_table': [{
            'oprType': 'IRP',
            'table': '1',
            'user': 'user',
            'process': 'SKIP',
            'addInfo': '1',},],},
            'start_rule_now': 0,
            'storage_settings': {
            'src_max_mem': 512,
            'src_max_disk': 5000,
            'txn_max_mem': 10000,
            'tf_max_size': 100,
            'tgt_extern_table': '1',
            'max_ld_mem': '1',},
            'error_handling': {
            'load_err_set': 'continue',
            'drp': 'ignore',
            'irp': 'irpafterdel',
            'urp': 'toirp',
            'report_failed_dml': 1,},
            'table_space_map': {
            'tgt_table_space': '1',
            'table_mapping_way': 'ptop',
            'table_path_map': {
            'ddd': 'sss',
            'ddd1': 'sss1',},
            'table_space_name': {
            'qq': 'ss',},},
            'other_settings': {
            'keep_dyn_data': 0,
            'dyn_thread': 1,
            'dly_constraint_load': 0,
            'zip_level': 0,
            'ddl_cv': 0,
            'keep_bad_act': 0,
            'keep_usr_pwd': 1,
            'convert_urp_of_key': 0,
            'ignore_foreign_key': 0,
            'table_delay_load': [{
            'table': '',
            'user': '',},],
            'keep_seq_sync': '1',
            'gen_txn': '1',
            'merge_track': '',
            'fill_lob_colum': '',
            'sync_lob': 1,
            'table_change_info': 1,
            'message_format': '',
            'json_format': '',
            'run_time': '',
            'enable_truncate_frequence': 1,},
            'bw_settings': {
            'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'biz_grp_list': [],
            'part_load_balance': '12',
            'kafka_time_out': '12000',
            'rule_name': 'ctt->ctt',
            'src_db_uuid': ' 6C4AEF37-6496-6DCD-E085-DD640001E4EC',
            'tgt_db_uuid': '  1C5F3C4B-7333-9518-7349-9712BC9ED664',
            'tgt_type': 'oracle',
            'db_user_map': {
            'CTT': 'CTT',},
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'kafka': [{
            'binary_code': 'base64',},],
            'dml_track': [{
            'enable': True,
            'urp': 1,
            'drp': 1,
            'tmcol': '1',
            'delcol': '1',},],
            'save_json_text': False,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.modifyOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'modifyOracleRule', body)

    def testModifyOracleRuleBatch(self):
        a = Auth(username, pwd)
        body = {
            'kafka': [{
            'binary_code': 'base64',},],
            'dml_track': [{
            'enable': True,
            'urp': 1,
            'drp': 1,
            'tmcol': '1',
            'delcol': '1',},],
            'save_json_text': False,
            'row_map_mode': 'rowid',
            'map_type': 'user',
            'table_map': [],
            'dbmap_topic': 'test1',
            'sync_mode': 1,
            'start_scn': '1',
            'full_sync_settings': {
            'dump_thd': 1,
            'clean_user_before_dump': 1,
            'existing_table': 's',
            'sync_mode': 1,
            'start_scn': '1',
            'load_thd': 1,
            'keep_exist_table': 0,
            'keep_table': 0,
            'load_mode': 'direct',
            'ld_dir_opt': 0,
            'his_thread': 1,
            'try_split_part_table': 0,
            'concurrent_table': [
            'hello.world',],},
            'full_sync_obj_filter': {
            'full_sync_obj_data': [
            'PROCEDURE',
            'PACKAGE',
            'PACKAGE BODY',
            'DATABASE LINK',
            'OLD JOB',
            'JOB',
            'PRIVS',
            'CONSTRAINT',
            'JAVA RESOURCE',
            'JAVA SOURCE',],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'INDEX',
            'VIEW',
            'FUNCTION',],},
            'filter_table_settings': {
            'exclude_table': [
            'hh.ww',],},
            'etl_settings': {
            'etl_table': [{
            'oprType': 'IRP',
            'table': '1',
            'user': 'user',
            'process': 'SKIP',
            'addInfo': '1',},],},
            'start_rule_now': 0,
            'storage_settings': {
            'max_ld_mem': '1',
            'src_max_mem': 512,
            'src_max_disk': 5000,
            'txn_max_mem': 10000,
            'tf_max_size': 100,
            'tgt_extern_table': '1',},
            'error_handling': {
            'report_failed_dml': 1,
            'load_err_set': 'continue',
            'drp': 'ignore',
            'irp': 'irpafterdel',
            'urp': 'toirp',},
            'table_space_map': {
            'tgt_table_space': '1',
            'table_mapping_way': 'ptop',
            'table_path_map': {
            'ddd': 'sss',
            'ddd1': 'sss1',},
            'table_space_name': {
            'qq': 'ss',},},
            'other_settings': {
            'table_delay_load': [{
            'table': '',
            'user': '',},],
            'keep_seq_sync': '1',
            'gen_txn': '1',
            'merge_track': '',
            'fill_lob_colum': '',
            'run_time': '',
            'sync_lob': 1,
            'keep_dyn_data': 0,
            'dyn_thread': 1,
            'dly_constraint_load': 0,
            'zip_level': 0,
            'ddl_cv': 0,
            'keep_bad_act': 0,
            'keep_usr_pwd': 1,
            'convert_urp_of_key': 0,
            'ignore_foreign_key': 0,
            'table_change_info': 1,
            'message_format': '',
            'json_format': '',
            'enable_truncate_frequence': '',},
            'bw_settings': {
            'bw_limit': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',},
            'biz_grp_list': [],
            'part_load_balance': '12',
            'kafka_time_out': '12000',
            'tgt_type': 'oracle',
            'db_user_map': {
            'CTT': 'CTT',},
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'rule_uuids': [],
            'batch_basic_settings': 0,
            'batch_full_sync_settings': 0,
            'batch_incre_sync_settings': 0,
            'batch_advanced_settings': 0,
            'batch_full_sync_obj_filter': 0,
            'batch_inc_sync_ddl_filter': 0,
            'batch_encrypt_compress': 0,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.modifyOracleRuleBatch(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'modifyOracleRuleBatch', body)

    def testDeleteOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [
            'DBED8CDE-435D-7865-76FE-149AA54AC7F7',],
            'type': '',
            'force': False,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteOracleRule', body)

    def testDescribeSyncRules(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeSyncRules(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeSyncRules', body)

    def testResumeOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'rule_uuid': '158Fb736-e99c-865E-3532-8e2F31d3aB5a',
            'scn': '1',
            'all': 1,
            'rule_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.resumeOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'resumeOracleRule', body)

    def testStopOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'rule_uuid': 'ABDB53E3-EACC-97e2-f7EA-eA806b01e2bD',
            'scn': '1',
            'all': 1,
            'rule_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.stopOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'stopOracleRule', body)

    def testRestartOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'rule_uuid': 'Fef6e6ED-14E4-8E11-9343-cAccD5DeF8A4',
            'scn': '1',
            'all': 1,
            'rule_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.restartOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'restartOracleRule', body)

    def testStartAnalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'rule_uuid': 'CC0Ea734-36F4-aECB-d1Dc-96556FdB2Cd6',
            'scn': '1',
            'all': 1,
            'rule_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.startAnalysisOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'startAnalysisOracleRule', body)

    def testStopAnalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'rule_uuid': '51E3a95D-bb22-E3Ed-DE1b-9ee0e316226C',
            'scn': '1',
            'all': 1,
            'rule_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.stopAnalysisOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'stopAnalysisOracleRule', body)

    def testResetAnalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'rule_uuid': '1a04cFeF-9B69-d3Eb-A3E4-0de5D49c2750',
            'scn': '1',
            'all': 1,
            'rule_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.resetAnalysisOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'resetAnalysisOracleRule', body)

    def testStopAndStopanalysisOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'rule_uuid': '35bAF59B-1Ba7-BEED-8aBf-61d7d2cbCaFD',
            'scn': '1',
            'all': 1,
            'rule_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.stopAndStopanalysisOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'stopAndStopanalysisOracleRule', body)

    def testDuplicateOracleRule(self):
        a = Auth(username, pwd)
        body = {
            'operate': 'restart',
            'rule_uuid': 'CEb8D6CD-4CAe-59Da-3bEa-DCEdBB787574',
            'scn': '1',
            'all': 1,
            'rule_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.duplicateOracleRule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'duplicateOracleRule', body)

    def testListSyncRulesStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listSyncRulesStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listSyncRulesStatus', body)

    def testDescribeRuleTableFix(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'tab': [
            'I2.table',],
            'fix_relation': 0,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeRuleTableFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeRuleTableFix', body)

    def testDescribeRuleGetScn(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '51c7D7E6-082F-3bDD-CB3D-Abc6BDE6dA1a',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeRuleGetScn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeRuleGetScn', body)

    def testGetRpcScn(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.getRpcScn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'getRpcScn', body)

    def testGetRevertRpcScn(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.getRevertRpcScn(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'getRevertRpcScn', body)

    def testDiffFix(self):
        a = Auth(username, pwd)
        body = {
            'start': '',
            'uuid': '',
            'tab': [
            'srcuser.srctable',],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.diffFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'diffFix', body)

    def testCreateTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_name': 'ctt->ctt',
            'src_db_uuids': [
            '4CA773F4-36E3-A091-122C-ACDFB2112C21',],
            'tgt_db_uuids': [
            '4CA773F4-36E3-A091-122C-ACDFB2112C22',],
            'cmp_type': 'user',
            'db_user_map': '{"CTT":"CTT"}',
            'filter_table': [
            'i2.test',],
            'db_tb_map': '{"ctt:ctt"}',
            'dump_thd': 1,
            'rule_uuid': 'C5BcC4f8-e6bE-B57B-a5f9-dcaACa9Ee143',
            'polices': '"0|00:00',
            'policy_type': 'one_time',
            'concurrent_table': [
            'hh.ww',],
            'try_split_part_table': 0,
            'one_time': '2019-05-27 16:07:08',
            'repair': 0,
            'fix_related': 0,
            'config': {
            'one_task': '',
            'tab_cmp_fiter': [{
            'user': '',
            'table': '',
            'condition': '',},],
            'start_rule_now': 1,},
            'report_msg': 0,
            'map_type_list': [],
            'include_tab_with_column': [{
            'user': '',
            'table': '',
            'column': '',},],
            'full_map_switch': 1,
            'incre_cmp_switch': 1,
            'incre_cmp_db_uuid': '',
            'incre_cmp_db_type': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.createTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'createTbCmp', body)

    def testDescribeTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '6c2C12Bc-aBbF-252c-BC9e-964bF54EFBCE',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeTbCmp(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeTbCmp', body)

    def testDeleteTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'f6d22dBe-fCF2-be88-f199-85f21C77111E',
            'force': False,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteTbCmp', body)

    def testListTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listTbCmp', body)

    def testListTbCmpStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': 'BACFAeAe-CBBb-167E-DD21-A8cD3B116A62',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listTbCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listTbCmpStatus', body)

    def testStopTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_uuids': '71ED7de7-8F28-B2a7-7e37-2fceA58feA6E',
            'operate': '',
            'tb_cmp_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.stopTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'stopTbCmp', body)

    def testRestartTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_uuids': 'FE3eAcBf-44Fd-A8F3-77Ae-837B663bDA11',
            'operate': '',
            'tb_cmp_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.restartTbCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'restartTbCmp', body)

    def testCmpStopTime(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_uuids': '494D79BF-7293-Ccf3-fDcE-cFB17eB7Cd42',
            'operate': '',
            'tb_cmp_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.cmpStopTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'cmpStopTime', body)

    def testCmpResumeTime(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_uuids': 'fCD666fe-59f2-bCd2-f93E-48E8a2FdF47c',
            'operate': '',
            'tb_cmp_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.cmpResumeTime(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'cmpResumeTime', body)

    def testCmpImmediate(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_uuids': 'a1C3A35E-eaCE-9dB9-dCF7-3c980f76Fa66',
            'operate': '',
            'tb_cmp_name': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.cmpImmediate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'cmpImmediate', body)

    def testListTbCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'limit': 1,
            'offset': 1,
            'result': 0,
            'before': 1,
            'after': 160000,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listTbCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listTbCmpResultTimeList', body)

    def testDescribeTbCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'time_list': '36EE7911-fdeC-46Cf-6FeE-cC79DE4DdD17',
            'uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeTbCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeTbCmpResultTimeList', body)

    def testDescribeTbCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': 'f097CF26-67b6-75Fc-e4Cf-BfDABfFCDFdc',
            'start_time': '',
            'flag': 0,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeTbCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeTbCmpResult', body)

    def testDescribeTbCmpErrorMsg(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': '1994e0B3-be0D-c288-c9B7-dD8aC9a4873C',
            'start_time': '',
            'name': '',
            'owner': 'admin',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeTbCmpErrorMsg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeTbCmpErrorMsg', body)

    def testDescribeTbCmpCmpDesc(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
            'uuid': 'a69Ad4Fe-2c3f-FC5A-a98D-1dAAC75E7A74',
            'start_time': '',
            'name': '',
            'owner': 'admin',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeTbCmpCmpDesc(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeTbCmpCmpDesc', body)

    def testDescribeTbCmpCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeTbCmpCmpResult(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeTbCmpCmpResult', body)

    def testDescribeTbCmpStart(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeTbCmpStart(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeTbCmpStart', body)

    def testDeleteTbCmpOracle(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '195A1DF9-C8C4-4AAd-b93b-dF7bCEcCb9ca',
            'force': False,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteTbCmpOracle(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteTbCmpOracle', body)

    def testStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.status(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'status', body)

    def testListObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': 'test',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listObjCmp', body)

    def testCreateObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'obj_cmp_name': 'test',
            'src_db_uuid': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuid': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'cal_table_recoders': 1,
            'cmp_type': 'user',
            'rule_uuid': '751A03F5-C97D-645B-82B2-316A5D198528',
            'db_user_map': {'src_user':'dst_user'},
            'policies': '',
            'policy_type': 'periodic',
            'one_time': '2019-05-27 16:07:08',
            'repair': 1,
            'config': {
            'one_task': 'immediate',},
            'obj_filter': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.createObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'createObjCmp', body)

    def testDeleteObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force': False,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteObjCmp', body)

    def testDescribeObjCmp(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeObjCmp(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeObjCmp', body)

    def testStopObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.stopObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'stopObjCmp', body)

    def testRestartObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.restartObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'restartObjCmp', body)

    def testCmpStopTimeObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.cmpStopTimeObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'cmpStopTimeObjCmp', body)

    def testCmpResumeTimeObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.cmpResumeTimeObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'cmpResumeTimeObjCmp', body)

    def testCmpImmediateObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'obj_cmp_uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.cmpImmediateObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'cmpImmediateObjCmp', body)

    def testListObjCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '3bBB822F-FEAe-f4B9-2e4B-A86DfbceAd44',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listObjCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listObjCmpResultTimeList', body)

    def testDescribeObjCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '19Aace3b-EBbA-9047-38AA-87458cceBEEA',
            'start_time': '',
            'limit': 1,
            'offset': '',
            'search_value': '',
            'BackLackOnly': 0,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeObjCmpResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeObjCmpResult', body)

    def testListObjCmpStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listObjCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listObjCmpStatus', body)

    def testDescribeObjCmpResultTimeList(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'd2eD4671-78cA-BcAe-84dB-28918F1cBA33',
            'time_list': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeObjCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeObjCmpResultTimeList', body)

    def testListObjCmpCmpInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 10,
            'search_value': '',
            'usr': 'I2',
            'filed': '',
            'uuid': '',
            'start_time': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listObjCmpCmpInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listObjCmpCmpInfo', body)

    def testDeleteOracleObjCmp(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            '11111111-1111-1111-1111-111111111111',],
            'force': False,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteOracleObjCmp(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteOracleObjCmp', body)

    def testCreateObjFix(self):
        a = Auth(username, pwd)
        body = {
            'obj_fix_name': 'test',
            'src_db_uuid': '4CA773F4-36E3-A091-122C-ACDFB2112C21',
            'tgt_db_uuid': '40405FD3-DB86-DC8A-81C9-C137B6FDECE5',
            'obj_map': [{
            'type': 'owner.name',},{
            'type': 'owner.name',},],
            'obj_fix_uuid': 'AaEfC6ee-DDd6-3e7F-9B7B-68764ACF671F',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.createObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'createObjFix', body)

    def testDescribeObjFix(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'D1eBbb9B-CCb7-eB21-1af6-e2D7A8Cf3b92',
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeObjFix(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeObjFix', body)

    def testDeleteObjFix(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '9cADC147-8e6E-7B4c-dD3A-D7EF8AAD896D',
            'force': False,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteObjFix', body)

    def testListObjFix(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listObjFix', body)

    def testRestartObjFix(self):
        a = Auth(username, pwd)
        body = {
            'obj_fix_uuids': [],
            'operate': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.restartObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'restartObjFix', body)

    def testStopObjFix(self):
        a = Auth(username, pwd)
        body = {
            'obj_fix_uuids': [],
            'operate': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.stopObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'stopObjFix', body)

    def testDescribeObjFixResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '69C9faAD-712F-29d8-dCb5-25bbe2431bA8',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeObjFixResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeObjFixResult', body)

    def testListObjFixStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listObjFixStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listObjFixStatus', body)

    def testListBkTakeoveNetworkCard(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listBkTakeoveNetworkCard(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listBkTakeoveNetworkCard', body)

    def testCreateBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '1d3efaA3-A481-1eDE-A47A-FF9BD3FfF4dF',
            'type': 1,
            'enable_trgjob': 1,
            'enable_alter_seq': 1,
            'start_val': 10,
            'enable_attachip': 0,
            'net_adapter': '',
            'ip': '',
            'disable_trgjob': 1,
            'dettach_ip': 1,
            'script_content': '',
            'execute_script': 1,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.createBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'createBkTakeover', body)

    def testDescribeBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeBkTakeover(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeBkTakeover', body)

    def testDeleteBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '680FFCA9-86De-b9aA-4DC8-Ded5B5CFDb6C',
            'force': False,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteBkTakeover', body)

    def testDescribeBkTakeoverResult(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuid': '3d418992-E8Ca-1261-366c-bB0fAAb25e94',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeBkTakeoverResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeBkTakeoverResult', body)

    def testStopBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuids': '99E3954b-F856-F9FF-f702-AfE4EAd90AF5',
            'operate': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.stopBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'stopBkTakeover', body)

    def testRestartBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuids': '7AFada71-369a-EFe2-091d-f0d7CEf3C3C4',
            'operate': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.restartBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'restartBkTakeover', body)

    def testListBkTakeoverStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listBkTakeoverStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listBkTakeoverStatus', body)

    def testListBkTakeover(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listBkTakeover(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listBkTakeover', body)

    def testCreateReverse(self):
        a = Auth(username, pwd)
        body = {
            'reverse_name': '',
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'start_scn': 123,
            'rowid_thd': 5,
            'row_map_mode': '"rowid"',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.createReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'createReverse', body)

    def testDeleteReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
            'force': False,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteReverse', body)

    def testDescribeReverse(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '8e76E87f-c1f8-6EF4-BbeE-edFAcd8fDef4',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeReverse', body)

    def testListReverse(self):
        a = Auth(username, pwd)
        body = {
            'page': 1,
            'limit': 10,
            'search_field': '',
            'search_value': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listReverse', body)

    def testListReverseStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': '7BAB745f-fEe5-34B6-0db6-fcddCA209ddA',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listReverseStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listReverseStatus', body)

    def testStopReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '4B44D84A-c66f-eCf3-865E-6FF3CBDB62e2',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.stopReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'stopReverse', body)

    def testRestartReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '83DC8d28-bd45-75Ea-7cfE-BDE453866D9a',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.restartReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'restartReverse', body)

    def testDescribeSingleReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '72Cb8921-eBdf-cF3A-484A-63cD82834F12',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeSingleReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeSingleReverse', body)

    def testSwitchActiveRuleMaintenance(self):
        a = Auth(username, pwd)
        body = {
            'maintenance_switch': 1,
            'uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.switchActiveRuleMaintenance(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'switchActiveRuleMaintenance', body)

    def testSyncRuleCommonOperate(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'uuids': 'a06F844D-b8be-1d6A-4DFe-beE4c2FbCD66',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.syncRuleCommonOperate(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'syncRuleCommonOperate', body)

    def testListSyncRulesGeneralStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [
            'aBbda191-Cc3B-AdFB-0E13-95a71C5Bb4E5',
            'F2CFC09e-7aAf-778F-6804-DD12d8E7B59D',],
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listSyncRulesGeneralStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listSyncRulesGeneralStatus', body)

    def testDescribeSyncRulesLoadInfo(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeSyncRulesLoadInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeSyncRulesLoadInfo', body)

    def testDescribeSyncRulesMrtg(self):
        a = Auth(username, pwd)
        body = {
            'set_time': 1,
            'type': '',
            'interval': '时间间隔',
            'set_time_init': '',
            'rule_uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeSyncRulesMrtg(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeSyncRulesMrtg', body)

    def testListRuleLog(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'query_type': 1,
            'limit': 10,
            'date_start': '1989-03-15',
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'search_content': 'test',
            'date_end': '2022-08-20',
            'type': -1,
            'module_type': -1,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listRuleLog(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listRuleLog', body)

    def testListRuleSyncTable(self):
        a = Auth(username, pwd)
        body = {
            'row_uuid': 'FeeaB056-AAEa-AA0c-5F5e-8EbFFE9E29D9',
            'limit': 15,
            'offset': 1,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listRuleSyncTable(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listRuleSyncTable', body)

    def testDescribeSyncRulesHasSync(self):
        a = Auth(username, pwd)
        body = {
            'offset': '0',
            'limit': 10,
            'row_uuid': '32D8838C-eeeE-fA61-AcA9-74536ce6C1fB',
            'search': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeSyncRulesHasSync(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeSyncRulesHasSync', body)

    def testDescribeSyncRulesObjInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': 'f525BE36-87eB-7A5e-4C05-b9BF2BFd11DE',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
            'obj_type': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeSyncRulesObjInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeSyncRulesObjInfo', body)

    def testDescribeSyncRulesFailObj(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': '46Bd2F38-C6C5-09EB-DeA9-Be46D66A5Fbb',
            'search': '',
            'type': 1,
            'stage': 1,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeSyncRulesFailObj(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeSyncRulesFailObj', body)

    def testListKafkaOffsetInfo(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': 'Bf2B1a3D-F104-354A-A86d-D9e136cd5d18',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listKafkaOffsetInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listKafkaOffsetInfo', body)

    def testDescribeSyncRulesIncreDdl(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': '10',
            'rule_uuid': 'cE1dccA7-D44b-aAfE-56cC-CBE09A5af1f4',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeSyncRulesIncreDdl(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeSyncRulesIncreDdl', body)

    def testListRuleIncreDml(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': '10',
            'rule_uuid': '12caE6F7-4B3c-A7a0-73dA-4C1b33b0bb56',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listRuleIncreDml(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listRuleIncreDml', body)

    def testDescribeExtractSyncRulesObjInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': '5e0bE149-FCbe-59DD-d4C1-fCA909eB785A',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
            'obj_type': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeExtractSyncRulesObjInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeExtractSyncRulesObjInfo', body)

    def testDescribeLoadSyncRulesObjInfo(self):
        a = Auth(username, pwd)
        body = {
            'offset': 0,
            'limit': 10,
            'rule_uuid': '1e15dbFb-8BEE-f7Eb-1EfD-740F3FeC29eD',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
            'obj_type': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeLoadSyncRulesObjInfo(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeLoadSyncRulesObjInfo', body)

    def testDescribeSyncRulesDML(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': '10',
            'usr': '',
            'rule_uuid': '68615d9c-65Bf-A8A7-ebD3-b4BBfD0dcABE',
            'sort_order': 'asc',
            'search': '',
            'sort': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeSyncRulesDML(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeSyncRulesDML', body)

    def testDeleteSyncRulesDML(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'type': 0,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteSyncRulesDML(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteSyncRulesDML', body)

    def testIncreDmlFixAll(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.increDmlFixAll(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'increDmlFixAll', body)

    def testDescribeRuleZStructure(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': 'Fd8A0EeE-d8Dc-1D23-B8EB-28cfef73e7eD',
            'level': '',
            'type': '',
            'tab_name': '',
            'type_value': '',
            'auth_uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeRuleZStructure(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeRuleZStructure', body)

    def testDescribeRuleDbCheck(self):
        a = Auth(username, pwd)
        body = {
            'src_db_uuid': '',
            'dst_db_uuid': '',
            'full_map_switch': 1,
            'map_type': '',
            'tab_map': [],
            'map_type_list': [],
            'isCreateTable': 1,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeRuleDbCheck(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeRuleDbCheck', body)

    def testDeleteIncreDML(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '',
            'opr_type': 'ddl',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.deleteIncreDML(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'deleteIncreDML', body)

    def testDescribeRuleSelectUser(self):
        a = Auth(username, pwd)
        body = {
            'db_uuid': '8E892cdB-C661-5cF4-7fCe-a669f74034A3',
            'list_db': 1,
            'db_name': '',
            'auth_uuid': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeRuleSelectUser(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeRuleSelectUser', body)

    def testListIncreDmlExtract(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '72D3FAE9-0498-B536-9Ac7-AAF3fecAEFf4',
            'offset': 1,
            'limit': 1,
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listIncreDmlExtract(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listIncreDmlExtract', body)

    def testListIncreDmlLoad(self):
        a = Auth(username, pwd)
        body = {
            'offset': 1,
            'limit': 1,
            'rule_uuid': '55e2BfD7-3c6f-D4ec-cCBB-7bb974Bb5b0F',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listIncreDmlLoad(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listIncreDmlLoad', body)

    def testListExtractHeatMap(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'top': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listExtractHeatMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listExtractHeatMap', body)

    def testListLoadHeatMap(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuid': '',
            'top': '',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listLoadHeatMap(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listLoadHeatMap', body)


if __name__ == '__main__':
    unittest.main()
