
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import OracleRule
from info2soft.active.v20250123.OracleRule import OracleRule
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
            'key': 'GonzalezMartinezAllen',
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
            'kafka_time_out': 'p$yEhkdlg)5h7u[jI$l9tnfzPqEw!8UlLS*0anpICcaKPpPeq[JsQ9ey)INS[EziR5MGv$8!FlJm^CW[V(%vad%Qw3EAtNT%(2pFBcfRY#Vtl6JvBe#tO!qlvq1SW9ngOpWq[F48XBxi%5x9A0p@3tF[bjw@&Z(PR*OE1Ytkb@I7hGoMnXs@MqB*QJGtxD4[bre1%[Aoo8iYG&hNwEMBh$TioR4dndF8@y58pF%w39bh^A49(oXQ65&gb0Sm27vOm!qDq48XvFtp8r4UZ6xbakKS[N5W4yj3)88tST@RfG^i!nA1JI[CqVWY4fb4WRlJ!4S5UYis3z85ZlgExIm7G5kTC3Y[XnDn)#Jdte%G1M88^pUS7NXA2#YH]VGIUvscG7]h]8FPWkcF5BKgzIFKMg!@AlX#khX(LI6(Y2PhnRn)[3Ukg^45jx@cX(EixxX4)NBnnM[]wx&M#0iYf&Lv0I2V3Lg&II)$J]Q#Dc*rFrXmQ3w!yIHUfA*V(TGOJj%wN#9ehRZJ&3knPo4*%[ZqTz9ES259v!JaYwnWkiO1&nkcbmoabJSNZ9a0BDWjROTs6UEusLCTq#Iym[qdSFI]VT*v6zj6XDix[R9uoAKik2D2lA7hI6hSef8^FW7Y*SBPkJcZNW*h17pt8hIDKnCVRZ%&jWLV7Mj9pM[Khin[Nd#1dCF@AE9VGeU1gxAK(*CvzJ!H&XZPiNvgWReRct*xmAHXbV(y4*]&8l4TlyPgt^X0)yFPUlnUX2#6HwKMaMJLi%IphSMHiJq)qJjZ!myCm6*NQNYADIu5uOAtdPMm4!ddpG9bLkD[i^%afJ(Y]vRHRmIsLCCe3kU(YnW9vFt4tjEpQA[JFeTW7*y$UX$Rpdt^t6lbLVJ(iLoIaFBpcVUgtKWQ5DjdiLmN!LejNuLb8INvp!lvFv[QJIMaXwcy)0^7gitzB7yNpyETG&(R0hQ0UNu2OEuJl&DQsM]*NikbL3erSFj4EE5PdOxZRY#6Y18$I@h*VPsI^rBbRLZULTdOB7ytu1u6IVF)e!q3OSoBAZK7&Gp#nTp*FF6tNgGq&hJ)XSCLWKAM1ZiR[HIySrJ%XrW&Ju[ivV$5T#tyX[B4Ri%Mkyy@s24)1lN@v2didTbAp@L6ItQQ8r0PTcYiw0U2Br49AiPj6Edm0l!qHATF99q$UN5do2uTVZ5J&]^5BhPhm)]*JgI2&zz8#%(d1vh3ce^SyyAw6X7p#E4N&EwszE6B4OulYzL1vnKIdYL&F^ZXaUecpVGgW$cWr0NfnLOca2]e4qWX3n(0vbzSWfbocPej19^(&rGg!oL84jW)h8H8rL5#62*s&)rgXCsIrkA1m7vUcq@t1xbB]2hHn4s&NUt@bfR^%)9P#f$CNtRY9@]Fi$nH7LFkOHrX%([kYUaqG0zkn(m[t74Gr7^9z6d8*MkcGOYhE5SVdMKqs%jFx&LGkog^$dW1Pmemehim8cKZ7nk)q6)9c5Azp5*w8*vJrGZFROuzj)dFIZM)&fq*4de3i7utfGEkC2u!94tMjuVO5@es@SsPoQtGvq$SnHZm7Zw2*L*G6Y6k^vQu#cJ8(^R1KQrG8S^pR%iORNPUiutZ!5m460X4o(gO5%vJo[%P[zbpsEAi8U5qnq^qw)M#O%hFIraEgFi^jshV5eokNtQ03jjbKN@uk!Gb6HijyN!q5z*ZRJmZ0XbVdTDoqMZQXs@WrL4BEuUn2o7b0[dH)7[n3xSY0YmmGVCzxVZS8QqSKVFJVAoXCzrJ364[BSF^@kTnVQfzWCVQlx##IzziK%hC8xkL9tGq8eef4I$GLBqU%s15os540rrOZ^ZXwrTQjlQ7KQ9^Ek3G)CyXv^eH#7zWJ%N6dx)IyH6UrRGnf1@m1G&fVWRKtQAuZ&ec$lbO[R43*R&rd4A2KtXQf8jB55tdN]n7V6gDqO)H!Br#[E6&%(vLq6DMb9L0lVHYfN9[Qk6lzC#z5V(Wuc&zwSg1PB#UhO5BdygkvC(Jyo1zmT4o(O4c@aWgO1(eYLQZeOL&XhFAJp%AQU0zhGbPql&9mvZS[4Fv%BTUbOf8uxd[sunwpjVvYsNX5tid@ssGKQKu6B*PT%kwdhCEO@3ukrpDQNv6w(X)ypCW%EJAdFl2nRlSm1cX^K#5Y)Au!klm1ccV#sWA1$L5ARAGL4G^PSeKe8F0l@(q6[zNe%KA!DAC^Iov20!wuE6YWK]u^!jTGMxebkt9F@(dn2ZpoJ5tSv)pRNA1T!uOgy$7w(O$&8jFo&Qe0)hNCtUGVr4r^A2oXkx%1VnR^RSsOXm#ss(9KC18cDtBQ7tJli5GT6T6NQPkK#VSBNcQ$^LKcL2*ouT6C02!LrJkUpk@r)FrHdUR4J$Yzb^EoUnxORkQfYKrrc39lbuQ[$P0is5i2^uxtUe@8eQQlfHlZ9Yrx0(^jD2AJEIE2BZlbE)y[Z1iWM0(P(yq$Mql[k)Zq$11lIN9uq^eQyWbvcoJgm7pN4^7EMP(S^QW)7Q#ywQvrzex^VQvOlDvLNeH@5d5LypfM[R[7%u]Phm&ryxLqhz5[5whugDL#wHpnS05#0kIQQpawWnqN&2sEBuY]GcMKu[QzuQYHPdb#W!jyIn$3dT[NZNXkiL7YiHGXv61Bl)F3xA@WtKDb1GDBxU&&9[A#^8igUgARhoAf]ahK(uNUE%*vlIFJX#PNPLOtHc2)Cv^Qg8FFY$)hlRHq]6h(9lYJROlt[#n8%vW80XExSS*6R2wyY###k(g@93KBVLx3&[R&!YbtcGxld53m%@6n&B2bGmujx^T]4Enxn8(*8deLkhOYWS$FfW#$uR^rWcYvw%Qd(p6Ym4WBbfmklSDMlDcfL(@3ti73FPwy(8JqTloU!pdXT#k(gn&AUu(74XjOXuZOp(gARXS7@MPm49*LQst)jyT5ptIIdQLbProdhP*KhYCs7g@Sp&MFreXryBGhHMW9!(^qOdw%W#Q&p6^)60KLG9s2PdA(H)[!qcMkBOah12nAUC9I$y(TDAl8yQv2L$S&cSNvR@L&bJ0ekcCLurP&S6*vdDdMqCH!^41#]C2cwbBuf#h$(KcPOO^F6or4%4zoXiTG0Wsx3X&ms(SeJFStiZChL!D3Y5nY$7H)ewGlenUt%afz(pr12FkL%!p2v)5oAt!1j8[a[%R51Drh[L1pbj4kWa#hl)g*F!bWHcp(AVXlMDbfkgeG94R)jokdiAOXCJgYf2Ddf00kHyE5D)ZUm%80NWtxsbU3jUR7SyswKS*iyA#[8OQ(Lz7hTP*lVCpa4*gfsro9y)l)wK*Xj[b)ZW*Klb@$1eFeo4)EZ9ZNg&AzxFp*H6ILKSFf8UW)OlZtcNTVNiH#$ln*H7un)nHTY@yBCgWAALG&$(RQpUeSXh0is6Y(yzTig*JoYs9[boTlqiKoj&X[BGbS35ik^CVJyJ6&e5HDBAY@L^E%NTySZfVVscZOJCsFM([6J4OuIZ8GHnPRhRg^qkJEOCUIdTneh^zzgHG5f@Y6CWrio*m6TJAk43jS&sixrWK)D%OEo5F!8F@afcBYW(XcMk!ZDn7@ZGDVu&F6O]HmC$7&*nP#QdQC#Y0vuOoEZh#AcyMry*Iu87EJbtFIc$AO69QCW56uYQBNj&^uQR@eJFL)S*GW!fDQT*69KfO8xtiLzT0xJJh(e8qGLE!GDrbEIvhAjI@S9f3^9%^6)tD3(Fyqg)FlTS4YZtFg@3YM[pd4Ovj%tq%zxTEWy7kDMJvGkNtW!QaLHwwO&gnqc0hYYGdL35H8g4gWlt#F$sS@o070!I#m)HcwBe7UeGNBU9Yv25jAFw5sEwN2vXCzm)BIZs5)pZm]cxIP29kkjK2TCum[ncfAFe]HgLnS2Dl&j6n(vsQVN5mKJHoilyWKIw10j&(WSH5N5jx]a4y7oZ#$WNpNjlQBFmvuQ&VjVyp8ESeTZBUqjmxIs6tC^#Nz67WHdOA&cz3nytoZ@&MUX^JrR*bT&)lxzE73d50AFLWOXuzAc!^uVdq^srQy7s(v)jQ&xlv#yBfk^RTTzq$TgVIycAQI&K0FVgclH6v6$ukP0bR2Kw4V67aBtdS^J#YddsSjRPXoS1KZsDMX0x)4$0fsc^wd8JPj!^85CJ8@@uKDevU!Nmo2XLJ]#but(57#sflKaDFGdb08uy93v1V&NuQ%CEVqpjgZ)WOlyZdG*YONaNZY(c(1ApQ)fTjWj$wRYYE]7W5a(QOMUdo[OZA2iW*%v($jP(L3snMPFCEa1d#Yl1oMKCjGSM!qcH!iv^x(K*4zVq*fN*23CdZAtL[@dyQ&V4&VwMAJCyEBn6XMU^[CjF[E!9pcn%%!P*%oem89SW5cGLf#[#CI9iNxzXMQ%EOXMJcpqFR7OYi!c[uu[WXrK!RC5m1OusrSsa2uN0UyW*0o@W5k518eSi%A7j[%UwYlAfrKl7df4Z4h*3gv2UBFn9DY]1c6sRA9KZoQShVQbsrFotq7(]5oge2HyC%F*zb1xwrCJF7oVch2[Y)YYQ9N6BnP^V@QrInKa#6k#TR#2&pjfFR6dYgyNQqh)RgI%n4xkjdL[3q5%UvQ]BAvSQ&RSGUXCzIryeH98QCmwT12GdY3vJp*4[BpXhm$WM5w@mgq$Gc&A3oRN(K(AzAL%#SnYhFOO&ubj0oUSzzeGzlvNFu3)[AD@KnK9W1$B^WH3F$XwNuaADDsJgI)zlK6%]lGeM@CSW^rl4hNn6JGC@@Au5KnSUazLmd)J)be[YOXCRX6(@SZCqmZuA)%KIQ!&W8[AM)4rgLcX0L0HChsPMHh]a511x0UKGVL66Yky0fEbEqWUu6Qj3N[m18#lHO&K5lZmK@4BRWW5biO2H[q%wwHy3ux&M9^dZFqsJ)Zs1Dduple4qFyjkkH]CwC^KVZ9g1AhPla6Dp6eBwp!a(@P@HnNNp%EU%n1*0hD#n6I4ktnMuwcG]jHB)9OwsJ6d2wOJoiuTMqBi@rD8#Z9jPq9On[2$VDTmCR3@K]wd5Z4Wy8ADCkN#sJ5f798)^FYn5Q)3oL9gJrL0!utmHn%U!@FcdOf##xd0K&g%f[M166ml8Ubz8K[[1#5Xirk)ew[aToqJukh6lIpM8MKOIfV[*c88NbWZiOQQ8ljLGf4#GH(A8N9xWz@sykQ6@K)jHA18Cz3Oxbly0nYEe6MnM!E&gy@)g^2YoooekgWEeWRP#Yq1q1K[(zLD4eSCo14nhimb4uNUrxSn31JEnpjMSYQd7P49sYIQI^bZ^OY#GnWfLm4VMrak*$Im)bmS1B7IsEwD7pS2JBtkCqfdbpfpzjobEAP&pyOqF2rU@QXwoCeTGZ5O2UtAEGOLBGOYrXdnDqdbmwsS$noN$yozGFQJGgtHmzlM5vkDNyU8Dc14*9(HtQ^AS5S7(&3hVc00^&%K1LlseFfYw0NVOwc^bowbfzBe$5cKQW3pvRfZ%)bs$%%JoJN6n$gZtekFH@Tz5V$0Nda*UYfIfo^IEOddgEOI2yGrC)tgh(UzTRSE03mVKkcj%jnvm60m6uYW(9%kW#LxEJ[NcOdz]7Ew8][FCbUgdxkC!oz&&PlwuoOUYsytO[HSg#HXAUj(y9z@oO5cN[0rur@r75bqCD2^uWkT[m7%WXqNUMj6xkmE%Z2!IwcQZU1eO8MMRX[csc^3a8kQG3#Qr9%GDVghn6RcP6k*ZzU5uM&jH@9usgfqo2vYU$9ar7UlEoHnIMa))W8w0WCc0Z6Ys0qlJJv5oJU6YwzZgk1gkorJb$v2fUAdefTzuPw&w)4MKnI(T1*%^aF]T$Kx8ho3z!V2tQ@1xx[DF8PUc0@ibPtiw7ps*wGtGDjOD5#[R$hNgKzIreiWoZX4xdbl4PA$Z9[B1Qe3WpAnLqh$fA(X[SVxSwQo8fXl2oW$wEt][Ue3WMbPj9t3CMB*mQf#^vUEXT[YF1bDTGSjLQZ2EUhZx9Ak$woUPVJdFCqbf$QUt&rejbnY@$v[0S5W*y27)mx4oX@(N127%xbiwZ1l)s[HVh[@LoG(&X#mDLMldNME6)ZCsrgaZtWtGbPZLHN@qbi^T@T$dSk7)4p1j^B8C9h0re8@JWe81W5te0M0a7nW*T0OHtSdEq$xDV9Dfq41j!X%nF2DIIplh*i!pKG)sphiCp51cO]9[3kq)Nf]c75dde040m^cIo1I@PG0JS&VxGUfB)nuSg2*^w^o(Yg$PmO1rgwPzOxIhB)0KDiKPATE@tAe$MxrPMQ^uRV*wVeJO%hYe2J(juGS3@)&f4qr[Lwv1Cje9kmetSC0Q^M*4DXB33iS@m!MZ(LTORp#6d1M%&KZX]*)W)Wzf%YQh5MZQ$co3!VPTKZ8i1Kv9GDgcvuuxrXiG6PsmlwkqT)BGZ@PSAzRfkVwjFqRVISrNU]qL1Wy9D8feJ8tXsReE8fWoZdE(rjmx]Lo7r8WpA4V5D#hIT^UjVA(%O)^2$x5l9F54*^B!Df[KetOM4XI8n7sBV)hKC0TDvJb0BPuwf4$kt0u()[B8rp8BTXoOT^[bSLKxxfpiDH5h^bMwciOj%y1yee&A^IVumZIJViFE]CJal#(&Ad&e9N(B@juKiYLhY&EVu(4QtzWmW9xq^Zgor59j(i@!hHKA^HJSU2oaDuiO2DOlR%Mn5d]%F(n4etB52M60dQ7lhcQ[RtEuLf2iTKFV6ylSRE()sj9)BpBl^lrcXpx#@G(6oLRQZ*)%o]$EhJXbeAlxRUCH[A]ZidRkRFjHW9oNzM#l1BJKvPCivgmRXftH72joBvTS][ync*5VSZy3oMdUqcV%Q]LN@&d#KID%kFG[[E&0WqFl]o7oQ8%6laG#%2QR4G$AzpYPE)Luz#VYmIOUfju$VbBV#2f@8@m[2TCfaZvoXryE!07Vn&N$(TfC#VQdwMOa4e4&Bz$PMTniDSR2J5[ywiSE&MuXVyLT*25Gn&At8BLoJAF]zFH2nX1lnKcyq$GyswBV6Z*5nP1GJ[R1R9%)nq6ogFcjfIL05yh2I@3w(Ej]7IGw6I3#jrQ7)F&EjMx4fWUzhbupNh3X(6CC4xI]TZE^H!2k2$WDK2w%X$!g%jle]nZgWoD%QRpFXK[Fq7W)pQ8[RmCqwQ5x*vPfaW(lyc]YwDQLRek8O[([Wv0*!jM^6Hrm7t]]%!fqJctmasmBDhxv^%q0X1VY4bmEnhYn[U[AU7hT#J23tUMKJf1m0GNrtxuA#d2r]J1CeFH8I5WbB!ptwj&TI39)vYuAv*2Xhn12HEP@c!6B#Fvm@eb[H@B6ViESURnU[8yG&i&OHYA(Q!slAnjozT)2hxmMiXAo1gR8skH7YVRBScVI@cGIfXm)25SJZtX!TWgStPS8CMIcPlGIEKAoncoOYYIOP()d7!e2fKcI(1Z5rR5Ha#46^ce4GyM2HD#^mEh%T5C*R#*@IvZb^$qj0XaFbUYOZXwr4fxeM#*qt5ku$)sH&I@SFRZeO3liz&(yB^mKOoKHkWfrKm(CPBd^[!)64!^%ML2]&7*xTR(#@Y)UhOIs5iCXn^!zQ*qT*FF(@7etE!^A1sWhX!Ghn9nj[%1z$RRyxLzQV@IgL7!YK[g4hlE7Jl]*k^0MS)m10o5VZL4#zZDmkcHs]Y)mmQpfvGH8[&0T53mz#4)yNO(^&TEiex$G76A&0!dhg%4ko^zw#dxu)5&%hswC*bZ@qV$5rxt5M)cxyyPw5&fp8oPAU@0on7oqsTxOuOo$#V9Z*%c@SqcLzTWd$ij*57qmHxTlCbTHppGd%YT8UNfAdLB0mIllr7L1*4!M5r[*nACrH^m)8UTklzExF2^wt[ou6yW)268LQ4idj$nx$xKETBtiS[vrgT[nLs&4tigzhhgo7n3th^h@F6d&ny^(XIJL]@D*zAf8hwfXMxOw1]@1mmJW7yrdVT6RGs)@WaGGdBF#f^*%gPA(MYuRB8$WwMktf3j!INKCH0()KaDYd7NEN#3#*LZTRfhf6bzCPwyMqCOukFot7RTw$podPTtZ)M@etKFV8Ud#wL@r#T*i8O[#hY%geaxyjbESmt(Hp^ERHxpoykj^vBshynZy&5gk^YcFv&jc523Sr&4^gtw$yftggq1^WHjnU($hr%3Sv*zybJIB]gZ9LDc&g$(41AcGzcId(^BtIE#Rs48z@Du85GNSe@Q8#4lhPb3U4Rv9qzdr^%r]GDN!um#I5ucvpi6HjBm]Bu(MXkXd3qnCm$zlnwrv18JXo3!fy(9D6k9VS1Ej5TC(wOnoIEHy[X9JiGFrMHPPqgufg!#wg*IljQHMQ48T0)yRcL4Ue5l2C6dgA*[TVw@CUkvZoVfyX44DLV1qEnOz2l4Cjycb(QC%gUjgY4hwTLFpFBbHHJzDGJn69ezgOXW)(D$]Y&#H2Dok$A)NrK^Bq385J2!@[qMuxj#Xz36Bvfl2VwqSj3Yw2r*fNMLVrbTu2Wy!pUUTCoeT!1qIN8I2GQzvGdW#soUo8]bCHuz9x4(4%wvXjUEtXw&BgRWDgCK@(ruE1Z64syjuvjuNDcuq*hxqFCZTl2whx(!4t9Oj2i8#crAA5F^$!JS29m2Zbph&LAmW1v!IPj[Tl&Qh7)[ynK]fO1^Y3]teFaHXJQ4IuPi20hCnoc[&#DuNHD0lHAO3ss63LF^8ry[L*B^q6p^Yxhdtvckd0$rgAtV^rBv@F69&Et6$ADO3GdbxSayiuin^LCwpsmjJZ*1@5xn$D0xbZw2Ze&8bk(qO0UJD2ZSWgfwG5#rWmt5%t$4ew3[tW@0$RwIIHTHip&fEg)[SM6iuv85(RfLX%3$7CEbRs^L]yiI#^$CM!r3%j00RmKNLA6iZu[lGQkfbw3rVj$oVNEEPm*#NlOXUOOFmZNy)5qM#qWTu^7w7!nv2Ku2#kiG@#yu&0T5b[uV4XQD6Z#el68]6rUni29iUyEibok@RmU5*Top8Wro)1v%PHJzrrFMfUkuJ4xdic)Vb8435q09xUfD*ETsSCp@Mr0iuD5m%6c6n@%sF7BFLED8ROsSvl$f75RzWIssXy[YdWWLNK1SEKVYRL6(7NM$Uqhq9*zuVBef@jJ#Qc5!qHk8i58)[t[L$wNh9kcE8oIfxikQRNjwhbtk#l&#3OME2a%)qRh83Hhwt^X38V7mx5^Vh%6LzSt!m6IeL0gqU8oKAeugMrqM&SFdE0)3uQ1x*C[4xx&us%ahxbyqJhGyZCbud!XL4[rZmf@t8@KxUAEP9eldX#T3lSz&zK&RPPDpEp)gHjEVfNxjqWqM%Uc6)6LWpkcnGRGDN8Q42urk&x!kFtQkNQPH2s%VVRw2silx$$X79YTq73!W$S!QSE[1*eEsiS6yzQ0yxUnoj*3#w%6WZ7CL&J5oB)eBkgt$X*ozTE114#SWv$)(^UkZ#sx#E^7qhSJR$LU!OpXKBOY%b*X90uCkuErn4k)nhp9F6JBvTfN4RBZ((ugZZmYYIcwkuXv1jVU9gg4EHIhEe8E#Yf@rvQmg*qKNDRguAEZKHPGN5PShrN]Dyb%f^*KmpwLiK0KJY4V6BEtrR#Sjzgo%33%b*yBge%dj4yK%fqq%oyYNCKtBTLPS7KaEWG34!sc]#(zX0j9P*zYUm*p*LZJyKh^IR2JaTnz^WJDElViUKOuP5Q9279*B]2fjbBg*SQQ7SstO6VJSZAKNeC26wo0O8R!5]nzjyX$ZcSoJ]]lfRNpJbEMO3pGAA*%R0Tc0i]&z%$K6zM$5E34]0)WCX[82(nL6D#C6KZ2n)uUXe$dDV*c5ZYoAs)Th%#F0EI6QpCD)PnTnR5JYh#^gAh9Q7r8&So6l6L43Vu25NFf1kK]gETU6FIQQKlpyCA!Y7XX]X6r5AG9p3mnfYS5Y#y2QK7Dl6HC1(wp8c*qGni$x[#2NfDMZ#O^5D(LlsjkaIK&fBdcbHw2KgJqv27AWnP(TNF1GDzen5JruHsCH9[I4*w#A7#5klL#Xxixt1lYIzw!19D0KTl!VL(BK^Z78Pjxp7tN&LxmqCOB8qVEUP)KbC(Sanseye%3*OsIDPmUQj(GiWqGlG8!k$9slVo(6%RFgb%Waa^c@H3PW4l7[4$AJTvt66Ld)Ao8WWtzc9FiBp([DCU(EMl!Fg[Egwbhd6*v%q&cz2C2fb!GNW7*#cQQpgRu6tPI(y5mZwLqhFB7fFlq1eVU7N#zmV$w]QGX3koOFFRd@*CSLYRyga5CYQrQyt(XKSjKC#0opM9KFGL!ApLXWE[5F4b00pdBVDKoSpIWbPC2rK*ua#zNZr*X3^)7DTnhx!1s2TlX1rbXuhlEfk%OEJMTDLBLimCr$95ETn)I1(%Ook*WNZTHFUro[&e[!M^iY]35&51fZ5U@)PvPRE3X&RF0T7LL4FDFU*fP*)ru[dTudI)tr@d40PlJCEmT##3zr0OD^81wWFo!fQiIfc!#P2nM)9)uqdmLgCr8oSLD[#iUl93RNJT&(4A%S!Zv!E$XTOi@XfdKQ5yK7@3)0bpXcf*bgiOEOcRk)y7dU%Ta*#pPL&H5R@3wUTHdjzo)Pm69UwVwMGvl5(6Y&%#7R9aV0R2TxKkdu86mDzqQ%66fHhRWMUx7lj*J4KhNLi%xe%OXTX3NU5G$hhe7pIuNtck9wyR!0fQfy6t$q[m657vntqZ$kbJ96rW8$DoGln(gmOZlo7Q6K57OREhzz*OVf4v5ArivSD[6TYAYJ1mMiM^5ir$0[A2wivm5dY)jOLvO)xDUD^oSB%0(*0BNdfOGqfthJgWgk5ZaS#Bq^F)PnvpE6n8nfR#G)B8hIqkW3hs%07lm1LetrK9Sy8cK@@P#47OPl2)^D6y6Bt[Tl8ZiOCmRaRcl(M)zRM2vX!9N(AmpP4bc^@80)*[LB]Ee7*EnfeGPl@xZgsV*EVWc$(59%G&^xswOKEjGouQH)[3^79wxo0kB5GcZrM@[e!L8kNGXHBT[X(Zn078!5)byNOuUJ&!b6UvP(JxbtI3a)eJ(MLBzYllelXPgcHj)oKNhYBrLM3^O^&%E2t*WbGF&&FjzSP6k4bH9EDQu6^9fTDFqD]SLN&lp7(lh0wJ^Cq^yOdoJXOMunra&LG#*Phou)tHF#c)d#Ujq2A5K[dox@K^v#bdlX]CV!isLRQthGGFSsugvF&y^1LbZ&!!JTd9sbDDvVVM%5$uJwJXpw&YL47w*%Ix&zRv!hBMkos^LFd1F0De[LF3#3klW(Ii3&Parzq^R@m!4hF4#cT15EQfc@VFy8z$9DuxV%lWzi#*6hc)[VMBQelF*NmM9ANPG1)7FXxZe@CKuS&G(JdP#s(SA1y@lpzyR3LnjYU2BT6baR70cRG&MkR9Xbg9Z@RLPAh*76Z72N361&f9t7wn57[3Y6xiGOZ$A#][^n*XVSRr%vOi61kNuncqXeVJ&tef97pSCW%JD@7Zd%*eVwqT666hNY5f6&pfMlIoELEKH)5uWKIRMumKSgSX[SGI1(UsnpojMWoFWaK%iN!Tw&WYeAHXuXG$fnpGZskhs4zkhpSYDqdkuaqFRtz$5z6^Qq(w^)kJtk%Wn4spKcc04LFxKb8J9(4ETD]LCZ[7SXskJr(OnqfS)2MALK@vYuR2MC0e*Lc%7bN[blsXF)2jzc!0kJF!t5bplSiZrRkg(KJtJTRH73pGM6#0$D%Ty&Y6mD)^Eu[AW7xdb0xr[Bz3Imn(BsRjKnjEdHg[cAcPxuSMFusVMpN^YZQUj*U0S30^4@*j49SNnVBwg5UXc[NHfDb!PX7Ic7)PqfZuhjoA3Xw*^dREFjk)HLLEg#*@pmidX6Dm3xG@Hu1y3b1uxN*HjL))!*VBkE#V60%1m*%tkLx%^25qg1T%O%Rfs94)s[GOV9]WnLKPOSDYEZWp!mFCDFMT#^f(ue#xM!WxVh*G!8bvhVtgR[15fTxL7xs&Vkqc2Y$nyXi07d3hP1^y2oROFeAOvZHKe&iS1vY2j#%72tjIm$y5X]]!50gdZN*TeVpH)EHbg)!oYsDJ6j*w$IY^9i6h0H4Y^f8z^EyU*6OW[![qh)r$rx&PC[vFd^SRnwxjOdRH7ZOXqfUY^zZT!oHT3Sp&K43FPV0kmt5f18Q)I&$$kmLisfE(gb(Gsfe',
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
            'rule_uuid': '88E3A34f-DAbd-d517-5624-DEcffBF3cdcA',
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
            'rule_uuid': '2bfD9b6f-1B9c-2f7a-e4a7-E8975f152Eb7',
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
            'rule_uuid': 'f5C8C583-CB39-2139-fD5e-7DdCEaCC24De',
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
            'rule_uuid': 'dFDc2dFC-058f-22D5-7e9a-eDf55cddf929',
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
            'rule_uuid': '38F8b982-F9dc-6DDc-80Cb-0Fa96b680D6D',
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
            'rule_uuid': 'FC1679ed-2196-BeA8-C5e8-AfaEccDEf8f8',
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
            'rule_uuid': 'A1bF59e5-fdbc-7BFc-3df0-b575CeeA254B',
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
            'rule_uuid': '9B232e3d-aAEf-d2Eb-5bD3-2db8783FbBF6',
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
            'uuid': '727fF4Fb-6760-8D8c-e8C0-cAF686FD7B26',
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
            'rule_uuid': '83E3A43C-0ded-D118-7D5b-ac2F1CBAbB8e',
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
            'uuid': '39de73eb-AEAc-4545-Aba4-93dAc4dEdBce',
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
            'uuids': 'C1B9FFcE-BcA7-3ab6-347B-3BBAb0F84E48',
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
            'uuids': 'e1bcDB9A-C613-C78A-A8F6-C719bbFA4CA9',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listTbCmpStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listTbCmpStatus', body)

    def testStopTbCmp(self):
        a = Auth(username, pwd)
        body = {
            'tb_cmp_uuids': 'FeACAb36-D88F-6dAF-f4A5-c6BD34fE75Bd',
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
            'tb_cmp_uuids': '805439A2-1CF7-9B19-A386-4ABA69FFEC61',
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
            'tb_cmp_uuids': 'Ae6Aa2Bc-bAAD-3ACc-f704-3632FdFDeb2d',
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
            'tb_cmp_uuids': 'cE8758FD-86cE-13Ab-387E-75cdFEe8f861',
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
            'tb_cmp_uuids': '7E8eeDb7-FEe7-eCa2-1e25-ecBD21E1c101',
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
            'time_list': 'AbCA52F9-8f58-B728-5fB4-bD8cfE38B3dD',
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
            'uuid': 'B70Dccef-3cee-5B91-A201-6Bdc54Ef95C3',
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
            'uuid': 'C9bEBe66-2Fe2-7Ee3-5fE9-72Ef8ED799Eb',
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
            'uuid': '8F4E2A7f-4D75-FDA1-1C5f-681e8c3fb1CC',
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
            'uuids': 'DBEaDf1A-6E6E-AC43-D46C-5c4c713b796C',
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
            'db_user_map': "{'src_user':'dst_user'}",
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
            'uuid': 'd2c733AD-75d0-dbAa-A0bC-32e5C060bB52',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listObjCmpResultTimeList(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listObjCmpResultTimeList', body)

    def testDescribeObjCmpResult(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'E8e47dFC-dBB8-fe5D-cADF-4D0Be06f6F4A',
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
            'uuid': 'dd61e9B7-D9D5-d3c4-8bA5-1E3DABBbdd5C',
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
            'obj_fix_uuid': 'cD8A3d32-de3A-b7CB-A8dE-39EC6d3E84D6',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.createObjFix(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'createObjFix', body)

    def testDescribeObjFix(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '6Cb42bDc-57D4-c63C-483C-5f5cC7EfBaE5',
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
            'uuids': 'cf0B52B1-C7D2-8039-bB87-a56f927f9ae9',
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
            'uuid': 'D2FcFBdE-4c1C-DAba-4825-D2764a80DCEc',
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
            'rule_uuid': 'D8DcebC7-d90b-36c3-f1EE-BbEEF70cdC5C',
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
            'uuids': '1d3CaE8c-E6Cf-4BF4-4F8c-3f20CCbEeD9f',
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
            'bk_takeover_uuid': '7c72dA0d-7a10-60fb-eAaF-7F8B3DD1B3F1',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.describeBkTakeoverResult(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'describeBkTakeoverResult', body)

    def testStopBkTakeover(self):
        a = Auth(username, pwd)
        body = {
            'bk_takeover_uuids': 'CBf77F1d-cf93-2Abc-4Ceb-165B4Cbc3d49',
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
            'bk_takeover_uuids': '7eB4A7ff-bfF4-d3A3-Becd-5fad1fDCcB9A',
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
            'rule_uuid': 'Dc6fEF44-D22A-8ebD-Edf7-cC81Ec63dD82',
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
            'uuids': 'c56DDe69-B99F-f995-BCbE-1Ef4114eB45F',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.listReverseStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'listReverseStatus', body)

    def testStopReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'c1DdeaBF-e956-6E19-454c-DC8C059d595d',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.stopReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'stopReverse', body)

    def testRestartReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuid': 'CBC8af25-A2B9-b22A-56E5-CfeDafCe4EbF',
        }
        
        
        oracleRule = OracleRule(a)
        r = oracleRule.restartReverse(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'OracleRule', 'restartReverse', body)

    def testDescribeSingleReverse(self):
        a = Auth(username, pwd)
        body = {
            'uuid': '3EbD856F-8c24-1263-1c9a-8FCd6c5e42c8',
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
            'uuids': '018C8bAA-2B71-6Bf8-56D9-92EF0abff75b',
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
            '27bf579E-Ef8d-CAdc-cD2D-9fD1AcA3E79d',
            'Ecdc49A2-5D73-8867-810F-B4214B68eEb7',],
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
            'date_start': '1997-04-27',
            'rule_uuid': 'F530FB0E-0208-9071-66D3-E595AE7D5A4C',
            'search_content': 'test',
            'date_end': '1970-09-16',
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
            'row_uuid': 'Ad9Cf136-1BcA-feD8-7fF6-317276fCb9F6',
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
            'row_uuid': '9b4bbe03-65F6-7abd-4E92-4CD7B5EB9E6f',
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
            'rule_uuid': 'dbBEDedC-CcaD-d43E-dc0E-5A86Df8b75eA',
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
            'rule_uuid': 'bCec5f5F-8052-94F2-eF5B-bfCB0Db8fbAd',
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
            'rule_uuid': '5A85ECf1-3BBa-8442-F629-8F3C9Ebb520f',
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
            'rule_uuid': 'fd9Eb6Be-4ca3-C8F8-97C0-fE10EBAF90aC',
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
            'rule_uuid': '9C9449ef-8FbA-Fd1d-CD4B-5Cf29c35F254',
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
            'rule_uuid': '781E0fA1-ECb3-A1AD-1A1C-E9cB0CFa36d5',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
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
            'rule_uuid': 'c94c7d58-4E12-dfe6-D698-6372ef5897cd',
            'usr': '',
            'sort': '',
            'sort_order': '',
            'search': '',
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
            'rule_uuid': 'b3B9a2c4-2413-eEBc-0FDb-b7ABCCf61EdC',
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
            'db_uuid': 'ACF3eF9d-3ee6-b1A9-e5E5-7eBFDcf0ffCE',
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
            'db_uuid': 'DBDB9bcd-C2fD-CBbA-9bc3-69CFcf2988ef',
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
            'rule_uuid': '7FBa24Ae-bB77-Cf91-Bccb-cdD88DFbbAcF',
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
            'rule_uuid': '4f12BB57-c1c9-fa3d-eBd8-36A62b2adbfb',
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
