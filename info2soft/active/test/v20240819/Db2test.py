
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Db2
from info2soft.active.v20240819.Db2 import Db2
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


class Db2TestCase(unittest.TestCase):

    def testListDb2Rule(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        db2 = Db2(a)
        r = db2.listDb2Rule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'listDb2Rule', body)

    def testCreateDb2Rule(self):
        a = Auth(username, pwd)
        body = {
            'start_rule_now': 1,
            'rule_name': '12321',
            'src_db_uuid': '2C4C2E77-774D-C604-9A32-5038D8E590C4',
            'tgt_type': 'db2',
            'tgt_db_uuid': '953C47CB-3F6C-E72F-DF1C-31522468A566',
            'map_type': 'db',
            'db_user_map': '',
            'table_map': '',
            'dbmap_topic': '',
            'row_map_mode': 'rowid',
            'sync_mode': 1,
            'start_scn': '',
            'kafka_time_out': '120000',
            'part_load_balance': 'by_table',
            'kafka_message_encoding': 'UTF-8',
            'kafka': {
            'binary_code': 'hex',},
            'dml_track': {
            'enable': 0,
            'urp': 0,
            'drp': 0,
            'tmcol': '',
            'delcol': '',},
            'storage_settings': {
            'src_max_mem': '512',
            'src_max_disk': '5000',
            'txn_max_mem': '10000',
            'tf_max_size': '100',
            'max_ld_mem': '512',
            'tgt_extern_table': '',},
            'other_settings': {
            'keep_dyn_data': 0,
            'dyn_thread': 1,
            'dly_constraint_load': 0,
            'zip_level': 0,
            'ddl_cv': 0,
            'keep_bad_act': 0,
            'fill_lob_column': 0,
            'keep_seq_sync': 0,
            'keep_usr_pwd': 0,
            'convert_urp_of_key': 0,
            'ignore_foreign_key': 0,
            'gen_txn': 0,
            'run_time': '"12*00:00-13:00*40M,3*00:00-13:00*40M"',
            'jointing': {
            'table': '',
            'op': 'append',
            'content': '',},
            'lib_name': '',
            'jnr_name': '',},
            'error_handling': {
            'irp': 'irpafterdel',
            'urp': 'toirp',
            'drp': 'ignore',
            'load_err_set': 'continue',
            'report_failed_dml': 0,},
            'bw_settings': {
            'bw_limit': '',},
            'table_space_map': {
            'tgt_table_space': '',
            'table_mapping_way': 'ptop',
            'table_path_map': [],
            'table_space_name': [],},
            'full_sync_settings': {
            'load_mode': 'direct',
            'ld_dir_opt': 0,
            'dump_thd': 1,
            'load_thd': 1,
            'try_split_part_table': 1,
            'clean_user_before_dump': 0,
            'existing_table': 'drop_to_recycle',
            'concurrent_table': '[]',},
            'full_sync_obj_filter': {
            'full_sync_obj_data': [],},
            'inc_sync_ddl_filter': {
            'inc_sync_ddl_data': [
            'ALTER TABLE CHECKED',
            'ALTER TABLE REORG',
            'ALTER TABLE ATTACH PARTITION',
            'CREATE INDEX NOT PART',
            'DROP INDEX NOT PART',],},
            'filter_table_settings': {
            'exclude_table': '[]',},
            'etl_settings': {
            'etl_table': [],},
            'save_json_text': False,
        }
        
        
        db2 = Db2(a)
        r = db2.createDb2Rule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'createDb2Rule', body)

    def testCreateBatchDb2Rule(self):
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
            'kafka_time_out': 'Gqhc)xCpunP#4[S(*6QU^^BFlAr$PZZ%$RSOTnlL%N1wj@$(jT(lnpvmfj@J*WILPKRYTw]HE&U&s)LK0twUBs[29I@tVeX!66tW6!$5%^hZ@v(Z8c3xiCz!C^hz*sLT3pd)x4Yfb!bMQUnUt7%tr@PYgNr@FwMu]p^RhiwyrbBlxr3$nfNy4I43c1[U!i54CpWDUP]fQn@TV27TG(4Qm*S#EA)ykHJkWWj$ld&w8)e@FJCHJ9w8B75snrM7h5teB!vChNc&hq4&cnG[BWPUDJGNSD)cJw@HIu()Hgu^GUfCRIyX3wi6wNqCt1V^IA35MYymLuESMe6jK*^(l&706IOp&VIIKgG77)%NYJb8%Ioyu3CCoK5m8LXkNO&3@ioCsh@loMppX^SbcPW2ArkK4Ji@dGKOcD5!WUYc(FR6UBr(Z7!fT9hSiVircoDz(8e)[NXe@q0tyx(xaXYn3VX&No[CbFfPwZdjtNTxLA(HJSMBQ]bWcO)EpGTP@mgh^!zmVP0wO^cy8!t$rsdk(TJySQK[YmqRDzVg2Rh$DOFVp7Jd&W5N)Ew)gNPJiqlDy9R(dr05toLp(4cxKWYZXITwWW2Be03@o70uTbQTJA$Dlb7omDdcgjHMnOy*tqJ2ZE0&!$S^FJzE(ptt7L#FSy%UXCow)xNM$6Nm4(i#d^mL(@fF@KIznBN71Qp9^8]!xvSFXNZIRCBGuvGdYNIGtz3h5gAciYOW^Ful)8Bc0jxS6BW8dHyJUlwsVt$*bd31sp%%c9@wwJScXkT[Z$KX^H&EXEg7IWPCUI$R4h%*imVlB4^[ujlZx)@M5qwTp$SC%sQGaAtfZlY)2bHGRhF52A966I)RT3fF^T7eY7yB9&OcTuuxUs!gd50cWThY@qQZ&qbnEPcuACqP9m9Ie#Tp^Ber[B#$3XqM#I4ZAo07&h#43W83e9bJFg6e72e4iuEIFOmkS6Aqm&MQTz4E6xsilNCOQLud0iiljHRd%WcZT4SvTlVsyGkI[ozA!K4H$pqzJTBYHY4Puhx&iI3$)xhZrcHOQ%th^Zd4tnYDMNHNuI0gA]47V69NWPYz%Ip[%Hcuo57b)Ae)#TmF5H4TeMqc8Rj[[8G5vG!RfGSkFux@V6mX4saffO#BLSDKUDmvZrKxJ21n)1HYu[R*v11@PDNTGEG%[9DiB]!OvFfl[HxFFhJ9ITwpR!YPd3S2GPsVfdr2vGF$8GUUqXAcaG%@!5l3yxgyYG!YIkn^Yd^cuGqM878XMA2uP7zaMQ[sFUqC[tp!iDvqElJ999QY5%*fslyRbW)W4&1&czZiBDm0vY$T)X#4Xk2TgLjbcp@(bfG#dj4dE5IO2%bR)N@MEh^eot01uAy#z*SFTJe2ydogN9w)ReW1&mqr*J4jp(L8zs06YYdDPuAhP)GRM$Jk3T$FZ14U!gk#4qck8pn#%6$*qfHoGe4uwy^gFtD[eGk*2F6U&TyR(yKLHfqyhnHxYiumam@DUi)(oOznkQ8##BTk0c5Fdbkcm%R7%p5xqiEvEoi[NU&(ax2El%BuKQgsF@KLggyf$qiV2g!0LnVcZ7v*jHv7PJIXL#^kCnXN%Sh[[tuI%i2P4BY6H8ovL$)&*YbHW#Ol9l#LftEn[oX^m7J^IrA5f#nTUef7ym1m2HXRZ[rd8O@l4Q([a&pd8lM@cQQMXPNn2TcNSw^A4]@*yUAgAHupDx!ye[xcZiNjEZHyRYJGZ)TghMv(Y1hx1zh8c$W&WEkUh%w)ZRIitxJZ6QVQJ!3P8iw4Azwl5^A%hw4z8F2&Z79*kntkWMawnT(YDEMU8nd4goc[zs0qv)hV0x@2DjMSJkn5*yKkQ[q%#5AV9%5EE0lMzpPEy!SNcd[(BLq)dMq7&]b(A7Ew1YlRpeDGRSgZv6BPA9kBITO2TygpogNqL@*fDeIK[#pihGt7&oiwGM&UF*RVm6ON4d3oTyYWvhmTEGJ12uz8Z8xIim7Hu9o(PY8QRAmBR[^MK6(fVCE]zgmtCb!jN*eh(kgI88nH[(QrMxC0GjL%52skk[wzonk3K6zLlepXLQhq3%%Xy(B0H*lrijd)Wr[2Pjadc3RqsmsEU*KAyw2dAPUW2v)pXyKHPaH@DHNY#!hcdzkbuUwdAhpRk57fj#d&WzTxqqO[fS2Cmw(xE3bUb]o2de9$E#5BMAZSCQ6y%T@8D*i&xeW[N5Gm)iwwmdgDteUUnpbr6p86TTLr4%oIBiqkNh98EPY4yLEox%#&x3Hfv7n[^T@qClafUCDj@u7I6x53wZQu7c%&!pyirGZA%ZhN^sBmpGt[tc[Z16WdA1EQib734b3rR(TD!$ilfLx1qWnA6Z7PvgfXq#zCR[@ah^aE&03Ku#lLxsqMxc9(ie9wF@JmVF#*8d&WhzKThDtMNJTg8W1ld3laVFngO^[CrWHsIn*F])YgS1In2ofuAPqU%6pvYo!@Zh9*RqIQjfQkDB&KsAh9ykpA[w5I3BnMNt[Oj76h8odKxIOjTIyx1V$YlCE0WctFI9Jd)q(ZkxVxL8JX)ctzP)W*jH5)7p8Mw9jy!S7R^Nc0kVF3779X1e2wmC4VUjIwwpM(yEWAwQ$$mifeu1F064#V@&hW%G9v1D0sl6v3h2U(B[7XjPY8Nwi(9Ri*f5Qb24Pn2eqD$G9KezHZOgcmN^Ck3n5UGEq2CNTnlEQfrE!UoglIMo&Vpfb9U07J$n6ViiisQAjRhwtb$xi8K$jYZBdwL@5TgJeXEtV#dCKkXuDzf4gF@wW0!n^ybuufm2!)Q!tf4TI!)vdT]pM2tV7qp&&ZmZb$$qh[h7kNmtD6)t#Nuyd(Vm5bpcVsgTv!9e0xi4G31rw0rHeO9MBV!3iGc297LD57L(!%RBZ]DrWKycxi4iCF3Mu0lhxHHo*X1zHG]b[3u8NIN4VmQl)Z4J^z8Fv@efw)LHjy^@j$YS!EQ!P8EBXX8dLuOLB@c5#!uDsJe^TwOrB^E%kdt#[1U[NDI8!dyy2z$rP$ZDwX3$HzOocGEiA^Av)[(U91*q2!LdZK[8Uh9wBX#kr^X%(FoU3o0KS)y9Jo^vZR][WMY7$u9A0!R($b20xS7aw2LcQ@rt3K8mrrzPj[[L1EG1dDzy2MAlri)4!UUrZWMbY(7WKSp%z[KYoVyEZ*9dNuvEU%c(@*tMD%1FpIhQo3EdOt2UZii7SX9lSJMv(fs(w4!hI9$!MnWXhjhBXTjcqcl&ffZLgC48aSwv5iooKcOWXJ]#TD9#nNzOHccrPAjqp^zwEQM$zhZwxWexzHAf#6n6N!$2iQfvjz5UW!J&u@FIZTBUbGVkay&3I!#2)A6kIP0GrNEjXM1N$tCZ5&LoTEmj(DtH*[7dAV0Ok1WJCjQWd4UIB1W#CXLjssAo70c8XZoU]Pqb$)AszEjXbKZNeyRnc6hz#vCTzCzgomTvsw5M&gs1i7]7TVId]93#T0z4FddH0KnN)J1U042ektwsQJkGn8#Ebm65(073cXuP2R*[Fkg5DTlFAl89j4De0DqDwD2l^Itw!AlQcR6S$^Y%8E^G&sys28Sk4FhZ9htmHOPVxocMduf)0bql%md*lbQ&^N)9[$icuZDwwKOiH2lKdgZXzjuRW9QEpmfZBFJf[MU#d*BBvG*Nvw8A(vJ2s$XYd5AsP9BX8LA@eQrjF!614yAIA]Kw(PY#pfk6n*96phPhzUW*7xiDP9%hjviBe$qU!PSv9xXg2kGB[h!)Ngbn]s27wkttC4xn*3y(2JtlMyCJHY$ODFH[OkIi@e7QtOegfozT*sd8PO%Cq(rJB@isHfhz7SDBoKQ14^sDc2ptZq!H&1w)j3Aj6g*VrLjyiIGCOTzvx#([@y$V^%LAWkuCy]qiGo%DTrpArOYCPFB9kc7BbLhoupSgt4l#z5Nvs8nyScDICiE%650KtOxLJihwyHfAjD*5!0HY1ULf*hw*f379@UtdQjZ#4gEnlNbPtl7%K5[DgSqc)kJQkLyPMwqeXfnIZS]X]y8aY9[hD2FzjTt75YVcvfYNnuqpCY!6uJpiyfXveb66q!gB8QkpOxfkG8J4gB498WH3Qju1F1d9O2dbVKy%wPSXrtO(jum7LAS3X(floS[$sRI3sM(6hT1q&pIHY&i^AYp&j^tI&U7Un%BgdHCOxHCj^Puwtx6r5WB@%gp62(36$)^jo1A7H#17hKeicygDS&HMdPFlmN&FHvMh0ydF[*FNo#0yP(yXOG%^GT%mQ41)0h$FL*uoNXPDvm5[HiIyCUylpJ!%o)EF(pHCFt^lXdv$7M9d4eFr!Pt$EZd%zr&hSJUi##i7X%TXE)ZZn8r(&yYje[#88yVLvuNQ5O&kX6(%ez8n]Kb3f))gMH5mQ%z^vVbZkIdjvKSgdDEEhDd%9qwN3s*0Hp#w&8J2FncleCBuNh%9D6vqKh*OTelOZRGgzx1&lxpyU[1Gq7Dmmled0!&IEZ]LpLlfe3$P80JrPG9^R7AijooEg!ezHr48]6A!2[]#TdVv4%wW9fYDnkP82jdXj4cH[Rwkh5hZ)wzwz3*!^8SzBw6RQsOlPLhEiwO8uWD$w3R$fH4Gs1*9UfJ$T)2oohC7iaSGygDX7BP)dnVORvqS$QB7]MfpHyHVwCfvheW^R4^W@[xp3(VE&2co#^24!%3*hFK^AsjOvy3WGTjGX3OlEyESnVg4$rxnh&bLsQJzD!zX7&XS1IM70WBUJRCd&1Rs*h(d3A(pbiwqPKi5nrFljqnuW%yut4TPVzJkd7YXY0I(EtYufoftT01AzeM^]@lwJ(iGi$lz%jU&mJeGm[WQ9XNCGTtlIAIeV8yqBawSH#f6CmzHAPWeUL1!*5RGDvV^54mwe8hNFug%lxO&0]NRSx7Jc$PcX1YwA2[3d@h!Lugoo64hzCmtkBc%VlYZ7w0^8Gux[76GO9BIZnYoHAJDMLBP9r&UkH9wJEN5fsmpSjC]zKbP!xUa^WsCow[*JcBPZG^e!yy1K[ItxY6CSX#m3q5p!dw[VMASJCpng9kgLX%08seeuuQkbZ27C%@XgkWJ6WU)zovDSxOw&mUdKpZOJ5Me**1eutvf^$tMrdbto7rOfV9SonZclekAYI*J*h*]FOqmodxOe$e4BERnNrc)aaBgWx88[hG1RC(A(K$YClE[5NR[zJI8Lfr2Y7JIm#sTyZ3jom](tHNtc!So]YNROH3U*[[*ih[Zu)H)Ao2#LZ9mS2qs7g1XxfzI*Bxq)2dm7$9t3s#eHlK*hfJ6[x!vbvh1dnEpy*r8Sjvm*6&HBpzYqPCWj9h3WZ28Gg17@L64mw5pDIV)5OwGluNQdB5M5n5V2q%kR#hVutMK7%IOOB[f6mny(r4xD$bcS(IXpVwPm38uyVHEFtjt!8fTOC((*oj1iIYX8ulrvjhV%EeJMC%TKiLmTP!EWA0pNHO#3lf^7$$N6RUSJ8xmx&^fPt^!nVfQc%LJbypBt^%!TnXy(#j7Q%L8yDJqW!IKuhHBFs07X49x@t14tVc2fu@cpV5UBolSWJ$mx#VHVQqXW$6MefmXD7oU[J)&dFil&@mw*ecO9E#zGVV2CV24ldwo&qa1DxMVoGZYifGX#jD&V5^cXwgAHQVXe3XtP18R9aHujDpn2CPdA5yQoJGS3DHxkK$1JejSY&5(kH^1GQD$0km@IEk[O4Kxexm2w[nC$^@ZkV]&&SMQRk^[L2iwW6Yg836FZ[G3qteO@u4y*o&sz5pwrgMl!Z1&7Rike7b&r%O!r@8TjIXf8NEL2zXlO8*mWv$B8uJu9oLBUB%jTXM^qdfoHx2V1gdV)bheFi&UsOv3YeB$RPxvx3uky6igeKf^WuZPuvf62wvJgPn&oKXC$9!j%YWzqoHSEYfPQGc4A)Zi[z9@O5^R@c52$ilhi6ZksGArcaG9E^oYsJOSBhy5mawi8GYimL0Q6mm!x)gI(ZVo31nWOyTTE*biSs*XFODJN3D1q)^J@!otgg5)m0RI[sRGWNzBIug$VSDPl4Gu%$G2YR029dyES0BMLNpAnq3dfuh4pDK$pAmGmsStiIh$O#JV*om1YdQd]Lhaesc&ktOz7JcY%I&1w11THi[B9vsVH2#wdAGUn*UYn7N41v34^[UmKnkIo$W&i7uiEkF@6[lmEYM77U0prsMp%@Hsd!MvJ68AAellw[2UIvWlNevbTIImSBo(pghxD3n[#wkW7r@rujb4c!g0#^LVsg03Op7r[x*BvQL$S$Syc*yY!(A2[VnffBee7JC4APC(Yi@V@Nwx2ZLbgFd$4d*1cx1&8#79PqMbDze]Fz^)X$m4cz^QbzE98*WiqsGA1G6mVZwRfgqQsmYr*4z0YVViqS[(65qL$^69!dvsN3o0!f!glRwsT4ST2hM5xT8E&G&)sVd$UDHp1gGq034ruId[BqxCHX[QlVt8!Z!Ks0PfYbIzc!rCCl]egjvfI[vyP!Fi&o2f8LgmFn)#3BkbYL5pvzCC%*VQx#s6zcBuE)8qENwOd%EFe&1xEu^lbeLY3$*uRsNl$^oj8hBBtCXWrI6VY[DbBvN1O)i8%Zn5OU8Png$W&Yq9)uf!eJg#bKII5$W7MCZFYQksKq7Ek%LJ$Mp!#nJJDTp2NL3Xnf)ye5iEtuoqo&M9XD^IWh2uMZyB%@kuVr(*IGKaH4JAtiO6Z7ZhAa80hN4LBlmzN#%@T%#AWM!8Ug#V4zHRgN4WpiTAFM[XU[^h&[#**P6H4^TEWpJQd1@*#fghQ0X5c73BdYs$#APNqgccT7E0e[drbjZ5ObdVCGgo[3OtjBKPkvqmdzVodI7pZvx9yS2WZR5HkqyqK@F1Y*oKeK*RRqZZc%AGZR(aVlxthYPgTruGXGu$J(2HygAWKY!4MuZLBlZ8gUhbic#THA&ERKDPU[8XcrWlajBAtLC12[Z^&4c@V!UJaf4Iq4wKfL9B$nY^*x^%@J1YaM$Xjh65qQ49zoV#RmcjSCo82U(8puB(Du^@(^0W6mC)vt&fuS4#YIhP7$^DL%uHMgi2piv0L)rIquFhKwU(AvllvsGixu9w[vnYeA$8(yDHePnGrx!4zeFEwe4$^p20N&vA]sJEcY2KMQv#76ecPP^OZ^(Q4nHT5]Q2rvTONzrqOk67uhA0#E(EChiy6N^QH3L2Tfc@rhPm5V5i47qkgzus6Xu24#ZqaIItVwdoS@(CCPJBUy0@hT2RvQUM*Hr&rAcwpE&76XP9cnnklPRP[hy$i7FwOJPjbeAvLwcBPNgX9A)Mr^us3r4(6wsQF%4MZvIqIWThTj(AxCXj!Ae40Vxvy$^8p5U28B477]6neP9&U9zJJVjqqz7CK$Ysm6WjauxDjw5u2JhV3pROLPeZ5fYG72In5MO8Nv4Ks0j[L]W5X%dqrDIacN9NYkJhQ2Pk!scieVnFky[U7z7lHrsh1lL1bY(cKS2a@aC$FqAsyX8O#q#4d6KR(g]&uqH*iUORcZCh3]xy(6tU6odWT#dWwv2^3JCkAPm7q1@kvvciLmQxreuV!smzRZSI*8#s(VCwSM^nwwa7OwweH7WDoXj(HD%w%$Ij8SC[X!*hgqxhORbIevm(YNJ[PNRrmdS5iaMq0inVF@m)MLXi8^MYVzaqsXP&M2YmW7QI1rfb3fV@FnCd&XtDCtML[6NOu)Al*gYYpq4FFEgTs01*gUhSfHr!4oKG#xvnfrVT5lVpYlZGJigQAPHjj4UMvt2qy(TzcGsomLJhgEYUwSglz@&XXF^52Ui43Vwt[mzb%%0RC!)kV21ZtJ8Jgi5FPvmY3TdrHgLiw9ZJ6*k!3fyOQo@%pi2^pl*gEA@sDI3y(h]4BJ#eKQ@V(w(#3(lnr$S0kuIL78tEGBlt)brmnuc@l^3kVVSNtctgNn8(qu[YTc6QuI(UJ!^d1ksHl&E)(P*jC$DX#1q@EDxlIFiJiPnKaiYw29b5$8MV3@P4tZ6sL0uqYlU%(SO%D2UM9wkAriPW1YEXWxeq$!2nLWw6rLtdVrsx9htkJ$9!%4xht%KQ27mNP[&)1FUE5Y%LZ8C6Lz!gQm[cRg1eLD@TUXVUwGJxYrjQBzOiz225is]U(oX3kfecL0U[goH^HN)y*)yzI^8HU^Lijup]ZAumwjIzt!vJ7IilvId#VSbY338wY9rqKm^ZBCt@T[CP(OeB[LHxg*2WXuxE%uQ*A$8o)gqkvIPz)BFYceCMN]z09SZvU2@Bf&ofB3Ul#3&j#Ia!@nxRPm$#605CZh]6iDWKMChZ5rooU#cQcP&wt5t9Lygv[WxpUqr$me&!7NWu#nVK#B&G4cCdi^AYIv6ZIk77s@gOO)PN0C^vw3kk!p(592$KUIM9)rvT8[SlF^SDS7pIMbBp24Mo8%C6@yY3pn*!(8Dx^hz)(W1vovlneD)fCp3(7eoZ(se0GRrV^yTyj#ylnkT71utPXjSLx)9g5F4Ucr^kR!&DTf)8$Fy5QCmM0AIVswU)WR*o%CUBPt^O9uuU1ogK43hHljc^$G3%&7nES!$K$zA[%[iFiX8WFsHF$Ng#xf5DcYm&qmQLOZ4[X&o#[T2hXWUJi(hNnVPVFsf])tjJ^91Dskxkd*!2)3kS2[A2iux]q9$B%cb3AxocQfuZXqG1dZpWAlNNW%!*z1%!PgCjE^UVGA*yKOEGLL%]1VAbZAGZPNin#2kEAOXd2PZC9GFJkni4@%lw*kzo*&Dkhmtq!!#MB2EU[6vNRN0Ohs&$o8j^*S!AzXv1arQV]yenykVH#TVTrSoMZhGKxHkxOC0KTfVcu!1)R$GhAjY6BOk[z6c3#srwAGBxhQUgB&[jPgd8gKVHW7bQlEDc5mYIGEzZ!EvqVIkqiiIcK^D)Y(mpF5B0Hb^QNd0RTFqYDW4eOhxE3lT&kpGrP)tmd1UQffA]@mR(OJPIIsgiW5%Hf[z8fEK&@OwQzeW]xqy1GV@QAiJTcctW*5![0[2FqUl5f6JYvWCszh7*AQO8G2)*$)W$@Mf5pHQlN!3)f^86]ctsROIuH(!IGxZJ[k&ha@By@74AAHZkEYnE)2MfPv4Cq6IE!DvH%dehOie0qZj(2QLP!mKQ1t9JsLUR3qi@2tEyLusxN[&B@NE[MoG5RmUm$nvyNbi)DrBMq4uvVQDn)VGe&%@@H)KawZEpC@5jz&FVr[K0Y@R*uvIm02L2ME5M4s[(*yWt(K(]KH1JhLSfJR24DMAur4ygK3TdTe@YOKDGUHR^d))dmkQLp]dT2GM8lmN2i#j1Pl^a@i5O0Oz9]T7&RhgZ^iGpvZfuQumq!#Cc@iQLuwPfv6dGZL6hl*)iZwy(RyQ^n2KO^vS9NIRwA)13HXb$7Z5q4WJv@eSVF#1$nqP&^4)O*R8NIhJB!jg@2IsQR79qV[HNy%HFoLuMJvRlcdp*bSF(tWwEfhUd]pKHYAI37d4Rt)fvFkH5h#AA^m*XGT(Ddrw%On5JxitfINVC6dJHyoT9lVTz0u[O9ey2GwVjo14F(ug1lpp3%io3Gq2Cci6ICkRO9EO0t0qPkWbeBlD&Qynu0hUeM6*Rk4Pd2DcQLd02N*IVi2^(3cN79kN!Lq$OF8eMTmIICssuoPEzs7TlQ@P8V7xh%(*oY9j^1bC(pr[UV&(nASCl%fw!CD8Ok@[CtjO)0T71X*FCN(C#NeN)3aq1^Lg60a)gxTXP!kf&HJ4AtXdL1HIgUSpc%HfPN0tqys*l1uIE*D2ZNCb9%mhtb^gAnt9qBEEY@BxNwshvWVskEdV#rxhEJFOhLQUdtp^ru!md1pb$wrVQ34NQyM3k#zUKIs2RxBR6bDeJDvn[c87&LnRKO[E7(yH[i%wdc^%6[@0z&PBXEWdkDc%)dl)w@N&E]oj1bkY4n0FtcOc)9z9y*P]R%gbtcU6a9Jv(y0S&c*fFJJCdST^N9e9ey8(#To$E%G^%f8Y9!b%#7bAh7XLU1!Q5!0vzYQGmou7YgYmrJgprXrgUubOqm3m4)BbUALvtyCH6VD@@JLZ9iL&V@ke2au5yZ4$xVSnb^AY#8oXyULD)KcoBDqg9IS!mTqlsC2BPy8NAYyo#mwk2QVOSIS00p09^)LCBcoe&J4ksvy]R!N8n[xz7GqIgokZ2bA!Oy9gU3MQ]ImOox1o$%IXnv^s4*SbCdxMzUMmhZMHfui)3PRDvB0QOeV&tZvwsksf(LmrRhLQ]mx8R&mvEJ$T&$%P[8wJ8Oo3NBqIukiKDXaViWlRk!KIvgT@iDHsSG$g[c]A1[$^c43gsf^J2h2y4Y!^Drw$j%xCUUuEdvINM^df)lBFTGP%%0pv$hG&tlNXtkWKGsjguFf1leB5vUnuBT2l41)o4%BcgLgoMp5[uMYEDyr$[xp6!jO%6^PxTEjQW*3Pcv#)nf)11&C2P6mfm#it0itHnjY%Dev7DAvwrzDYSPkN!RXwfu6CVjA8%Ye6dN$n5T76Fs3()wMhQ1BYS06UJ@oND4vaVCIqVZvruNo9NwVEK!FiXXe23H)bYOT&u7lgS&7$Jym2VNUO1@l3UpreTO1#NQ9^IjgPly$X4BQo*e%sOzDbgmOij#HXCW8vfAw(#PdCN3LR)EizIeWywT1!J8hT1SgL3%2$Z2QF9o(vw$Fsh(Xpbxt!j!hxSLaAN74mHTjQF^V3v$*48mv98mcY6FmjEMhvU9unqD4iub0v*qDU#s3K&2EQhkYA&p!#NOwRju3K0qBT#S)]1j%(Fl7N$hUM!sJ@CjE%bhbzHG**D@GQww#vTX4]mD[U7]Qwm4vm8*mPCEiCD%I1Dc@4ak1skZnv&cy4do0iMgE&)0hS[if^Q*jj$ne14*1Dm3@WC3%WnzLIGaX^B#4N!uhs^oM(XiporZU8y&lac)LQjaOHWX(4@NWX@)c$oWCeMYtixAd3Eie(06xrvfgZH(Ky7UQrErM)7pCf(ESkh5DZBd!a51qy0R)bKtBNOPSpRcmj9unKzFgKCNU*AZc)s&zvz%$yQ5XdsWrusUz)^pV(l29(@CCPvifh(sRv4YmMN3c!o$T!17syVFg3ardrMfvGGYTHByNaR4dEP#bl8Hs(ehwD@apaiHA0ALf1lT#V3wNO5qskVB64gLs)bSiqFSvp8yCKUA[IExT$5qI%p[)5c^APU9#GOR&!!u]syEcm%Bc9UJ8Hf)qICH#*Ow%I@pr%!oiX8)1KdDPk^E*FAj*rn%dZc@$S$Su7($Oulxvi*q%fwS6@F*hoTANKNs$QnbbsCbB1JWo6[kP6r[!Wl2OhB!sXOiH49w&[yK3SS%g13[X2k$B$J3EeVq2MnM4ix9[0!Y4dNn!jPu*o&bhko[hn)Rdv[qB39WDfargNb&@hngyT&F)*ZaKg#VbCiT6&rP)panZWmrGMtuGTElonebjLDACv4HWVm&jGiU%XcmZkWkWs1sa4*jg%Vra8MYyUzcSfhYQrklposiW4$%nB$&Nr515&kAG8d&%EwR)Y$dUWolMKfLkhmsSmB5HAcU)eH(ADm)Cp7xh#Bhz&M6YcjD)j105#rsLLR%cniOLAuQL]A4CDHI7X42K3qB72mlB5N09@$O7(ZfW@Z2Gx@jJ9u5XXlm5F]Guhh!(Nvxhh@SzXaxCzWzyjD4TQb%rT4Ge5XGUdl3ROvy^f6z3iTXkQL)qPKOJHP*4Y%J8SkfMVCMtHlKE6wW2izx*UmKiB#tem#rmsubHP[JdJSWehbCs[0TC$4^Xpvo&ezoX9Z[AGu)VbXKfQKShcgGo#b]WwVHzPYMp0MROhxoC3rfOi3@U#i(H^RrDWeZWw3qt2S#uFMK2D5j!cA0FvOV#WYCoImo[te)ldPT*E9EM&H$j4fmc0SST80MBI8U$pf0IgsFW@1EolNJA6Rx5n#U3CkStgQS$pb5Nm1dV8m[F6F!wpb]wONliHRpu7NTupZbtN)pAVteIaJwbt%bsiiWu(ZymwkwTU0X4F6dUR1SfD%AxhAis5svGjyaRz1a3P7hN0^C2UWjlL09r(THzoklPrGUJOquOCF)0C&$K2LxR&u&MrX9[TAXggp(4wWz!dv76xXOq)3lm05VR%n[#m6YdSApki(B6pl%Jp^^h1khu7&)k&pj2poIXo2O8XSg$fG3#Z1S&w(%GGJG*',
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
            'tgt_db_uuid': '',
            'src_db_auth_uuid': '',
            'tgt_db_auth_uuid': '',
            'lib_name': '',
            'jnr_name': '',},],
            'db_user_map': {
            'CTT': 'CTT',},
            'maintenance': 1,
            'tgt_type': '',
        }
        
        
        db2 = Db2(a)
        r = db2.createBatchDb2Rule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'createBatchDb2Rule', body)

    def testModifyDb2Rule(self):
        a = Auth(username, pwd)
        body = {
        }
        
        
        db2 = Db2(a)
        r = db2.modifyDb2Rule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'modifyDb2Rule', body)

    def testModifyDb2RuleBatch(self):
        a = Auth(username, pwd)
        body = {
            'batch_encrypt_compress': 0,
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
        }
        
        
        db2 = Db2(a)
        r = db2.modifyDb2RuleBatch(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'modifyDb2RuleBatch', body)

    def testListSyncRulesStatus(self):
        a = Auth(username, pwd)
        body = {
            'uuids': [],
        }
        
        
        db2 = Db2(a)
        r = db2.listSyncRulesStatus(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'listSyncRulesStatus', body)

    def testDescribeDb2Rule(self):
        a = Auth(username, pwd)
        body = {
        }
        uuid = "22D03E06-94D0-5E2C-336E-4BEEC2D28EC4"
        
        db2 = Db2(a)
        r = db2.describeDb2Rule(body, uuid)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'describeDb2Rule', body)

    def testDeleteDb2Rule(self):
        a = Auth(username, pwd)
        body = {
            'rule_uuids': [],
            'type': '',
            'force': 0,
        }
        
        
        db2 = Db2(a)
        r = db2.deleteDb2Rule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'deleteDb2Rule', body)

    def testResumeDb2Rule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuid': '',
            'scn': '',
        }
        
        
        db2 = Db2(a)
        r = db2.resumeDb2Rule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'resumeDb2Rule', body)

    def testStopDb2Rule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuid': '',
            'scn': '',
        }
        
        
        db2 = Db2(a)
        r = db2.stopDb2Rule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'stopDb2Rule', body)

    def testRestartDb2Rule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuid': '',
            'scn': '',
        }
        
        
        db2 = Db2(a)
        r = db2.restartDb2Rule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'restartDb2Rule', body)

    def testDuplicateDb2Rule(self):
        a = Auth(username, pwd)
        body = {
            'operate': '',
            'rule_uuid': '',
            'scn': '',
        }
        
        
        db2 = Db2(a)
        r = db2.duplicateDb2Rule(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Db2', 'duplicateDb2Rule', body)


if __name__ == '__main__':
    unittest.main()
