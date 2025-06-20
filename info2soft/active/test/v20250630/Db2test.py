
# -*- coding: utf-8 -*-
# flake8: noqa
import sys
import os
import unittest
# from info2soft import Db2
from info2soft.active.v20250630.Db2 import Db2
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
            'kafka_time_out': 'w@5^fOF4cKu1^KhOXYU$3nljYgjMESs$DShlQsvgAu$ixUa1GQFOetZcvE1p4AbpNOv^5bH(jAEA]GROT)!CAcMrzt()u1gzd0#Si#ikL4mnBK%pm!xgxGV**JHF]%V%$hlgdYH8u$#5RU!kS8mvqqB)7i*(py#NmQypP1gn2K5[pFwddbq0KX9MgXpy#!IaOAScMPgLFimKic21)vyuhgdcGAgg!tN8eXew5[U)m(7fHNNRXbp2LMV0Mlku2GdnoMX*h8%A!(CQ1p)iiyyQ#NZG2vaOppd[g&c27EM8&X&JKH!B5OfB(@I(@^bPXVXfR*c^2rJly*oYVj[Y!ax%g#odM9ez1pJGvnPNibT$ovZs*fnwSrF&FZGH6I6wz^v8XbotkhI3KvnI94ol#8%)mg5Xnb2H[3^TivBRpBDKBtv$sF8]k)CC57ZFlePuA%dbBoDGvr)XNIOu4rJv$L0[@vccs3oB0PknIU7j9zCNFgAfX3R%e!lKkK%GJe@1Vhzmy5PV9dw*NA739GSk4SG]SILK$J1HNthO51ewL%fJt@ZK9df)j*cTc[E1A5(E1$b%orPvMp0Zi#KwXDrZsQUyI&GdHipfYH44bci2gP*AX2R@qzIEkyXzL(E7!9(nU938%$zOj8jE!&[C)D!NUE47O2hH*d3Rt0@zrk(rSyWm)C7HH%XXmXed8zZ&qgdM(LBqsI3[e#0J)ehkD1WHQG!tfbMh9X[uA2MMVw%#usSR0051TjCV26XvUk&DeLVe)II!z@7Wz%mEsz&^pzl!ZI22mDfRTpHb[fA31qUf3@*9Jx5%$U8tdE7tekYDA[*mFbmq@Prc%R2wdzLuE#aefiD0uSGZC@K8obU8TEF(X0u5KjTE30xg*H0KB%$1U1b1#^ypcV)fG%sd*n&NVzrx[pCc9ky@C#j$4p9x77Phdg1Sk][3*6f3Hz)G*Y7#$]PiBCbrdu1cLt6$F9d0kxbtckqp4Hp@tQkn#IocB8z&0eIIJwV4RqCQp0@bZh5!7lwY5iCe@C@4NJEXWm[%i)Kj$W^^(n(R@ftKjtsYeRlV461EM*2%4n1*S]8MMBGS%HiqlYwaj*06wi3LA@4y)9F^pu@Od0fhhKNy^RYy#riz539dlyh713SB$STAN2!0IsMvYu)QtLodQ1$Uox9((@wyn!sKw[i]qMmWDjH^YexiDqUrD0gl@7nG3[[2OY$ENA$UmUITVpzA[]Io0gVB8kHX@b6Kut9&zdgM1KDiB%Fzfu]Jsby^q)UO03LgzAsIBl97f4Jc0*Uvpc5(vRcCtcj[#&X8^Feeu[9LJ[xQ#0ac#x3fzmf*l@$hmhPc*L&3Q7r^dp96g3W#1%d80zCBxwtDhp$LnGh0*R&r&25sgu]ndzIH]5vfq[sXJMrBwKVssjj&DdOqDe%!gWJJk)e1k$[DcY^9TFZ$hKu4H&9EN4ToG(]n(FRKyBaX1cnfZ0XXX73fLzGoW3c)]tN6*g&Zn7FDJ78nlYoQ*YNF]6rWSdujqS^ocXLQUFYjtV]EewFZCvhfS3^0QDqfGioiyzY@FyWBJG1roXs1ZL#gpQAVzp8s1tlTg0YjwC8DAp94z6Unh@vHGmPiELkorBo9UTpfM0XCj7F#anBp]YjUAcU3LW[q%RuTrix4!TeA#)%blbO[qxuDFZHfNQU(NEhWXDWfI68s4S2I)vr&WycWo2DGCjrD8FN!O!r5wJJ%i%Txhw0!m7enIvSx$2KJpJ*Fbp0qv3mQW]69)q970rEopBytwipV*CYpPBGs0(d#dY1IRJrfUCD@GShCWW&]XAd#ie6^$d&&(4BQYYPGTT%E*1Se#WoYj(9hr22eGEuyGqWvZ7Iz&8wo#W$B9yP&7v[J!U]2J*P[%$C&b$9i@R)0OthstvUHmGEIBhk2R1B8l&gKTxr1wGldfq]bQ0Th#PDxL5sg4GKgj3NLecLUTwgF0MEIMc*^)T#Z3n4[((iTJwjWwV67oGC1QsLZdmwR2X05njfv@D!tu!O@wzduZkt#$Fk1CW$)Fuwl^$Y3Y2oqvWJQ*2#Y!JPpTEcMt3qTD%M$Ai#A1#)aibXE%jGcs%iF5o!XJzInBJzhMTxBWf!^b*yrgy1es^UF7@iAyA6bpxU5^785@8BB7WU#f(oXB4)5QMeFTmhwR1xFfTJu&QHhHodDZm^UbxUBBobzOCo6xyyU#QKHnl@tuSE1hc!CcsSsVvK5t$Avkv5@%t(njt[nPrEr(NHvAwkDdse9Zuy*)Ec)HQ$NU3$t[d0MPlyTloxaLRuMhVW5QIn(un%SQupLdqLh9]E2hp&o*%LCANd1tS(*4qRdboG)3b[pcBX0WRhz*WCC4&olO$oBLlYUjo5wo(wk[AE[)&qo(18imgg2h*zBSP*9kvqt!ms20U(lI#h$UU6ri6WgWQxBS73579mm*j4EZ5iLs#eNpfT$7Iw#)%Qd^%F4mLPNJiMbZ(#!lo9#g$8AXxG[w[s*x7TY[U&brjo#DNStF]Iw61Wa9l[O*mCgyKeFEe4u$tRh$z%fueMJBygxiI&XIWNYyn#*fZt!W!0yzha[Hky7Zh@c4!^ZyedsYn@1cCQvsGIzt&BpsBMarMjypF3OP[rP$A7Cyj&1#NFdt!*YG58sBLpXYQifUwYDVIRVq3(NkDK9!SB56t&q&vD!9$e(1r%9T@yoQxEFGe9Bz)Cc8Z&faMpzsYCI2D@[Lc*hkfl5Gtwrhqa]Tg8&dWTQn8Uv5gOKEoEDBk4&^i]mI^xzs#A@ESUt[)81HvDP3VZ&S]A&HrtA)ZmgodGf#M%vXPaw7O@G&YftOgc2m)Jlt([*^YsqU!RUI&)!KSJsb&Y(Zo&DC$$BrhHv@y)dFkKqm*aSISpnC6(L!Ed5R202[%ZD2PTxV4JSHS7HXUvgcTPYBdBK(Q$&r@eBly#z][&a!PMet3$Z!#XFvt&^S#b$7TjPbN7wMA#qRf0fAoSdGCbWIB4#O#RuBDo0kQ%vG)wGJ3VMvwnxdRnmo&yuot^S^Yt&QDckptNJ9y*y3M1wT$uyML3o#@LFUqfCoj5JW!mY(xxK0EV06Hj**xOcYKQQwuTCQ1o[d#B6&BH2#NQlbTb%I%Ke3mqNEU7zvxM(@IfGqqcz#h**1VC!fHf(JedMuoxMV5GJ&p&Es*zVTSUzQP*o1EWf2cDXe)L1Jw[9V0lP!Xsi[xbN(7J9pieH&tS58rSRbq4@J*rJCCsH(Lo(jg*RxeGehj0KN]j7^WcGJN)$[^HuK3IcTJ$oSEeja5t^Jp^@j0z!HJE#icez)jP@G90^^S)S1gS7(dbGMo02&04zG0q3$#$^04b0$*Z^Da^2ZrA2PhsFDyT]8bLZ4*NkZRp9qbn066Cef6Lq&D5(iZoXAnicN0K^*)u3J6aO$4[nGbZ%Jyvj6UOspBnhp$x90ODW@Sy[1bc*K@KgRClV6QzEZ)^&An#!C[kw)whdnFGmqvC0y3rwG8nb(jSuhp^7wBzQWa3ECd1J)pScTeiXKye#R^velILd6jRtNWLfs@mho3pttjS[IOBvp$WcBWrseqS]R!tvSH*pU@2F0qWi43cp%M9mIK0Dg(leNQXtmgiDSWuk*yX))PKOtzMff^YDbd!*hW&tgg5oDnqoC[XpifuiPeOdN5g4$t)vxgbt8R@ItNyMVJL[02&[r5QtJ#ak$6Wd2)ChYYSNRXu!)htAkDb#F$Th5S2@Xow*Ykw9%Ru(o9pkm2CQKqd#qOY18fmwa[M0![CYiU!!43X%c4rKyi5Vwg%Tvyns]ihYun^v@76zs7N#sSd)X]diCJPp0#FR0PXG6&x!sOuf9yEvtkzQ]C8oe1&$02G3[kCF5t^ADcgJh6T^Xi8Vmb*xjGQIRfrkmT%etugibwZ[@wY^xzS^uOJzlB[F#AVs5AfP@*zB!Jd#a*matFuzCVh%iVqD7qU5NLi[yBEez&LAe3&SE$]w%Po$43&uXMjSl4Hj45NPw7gAlMg%4x*Iy#10UyVuHbFr8zD9BHhcU17N#Dqw7X2NAdBoY&@UwO(LjMw[XhlHbbhs2C%NvQix16cu4VP)nmsZ^E5(RdqQqr9$jSi)c]2IjrnHe#27Ss(Ime9MNcqO[YmutNvqfew09G0c0ji[o)wtNPTBr8sCgGC1rjB3Ul[]X(G5LfO&o$8t$d9]ffM7zuKE1E%JoWBy52px7i5GVjyt[jmYkfa9F!s^4EUHc0)bh$vP!9WI7O3^TLw$$Omwh5cQRlg)J#k5soQCh3mqoecXLH9@37LoB%r33jzXvt&^18((j2[R#78vvET@CB7dV3n5cw4[2y1Y9ynJ$0m[d(5Bx@Q5tj%nLS0ULegUh*ivzsXMQS]okERQ5sbV)Q9jZXEzF!J(W21AcrOJ!9Gi%jlD^Z]*&POLMHyINNuxEfApdX17Vk%#8F4&M)qqP95!WiZF4V29Wk8EXk9365w*CtCKv)SHfq3PsrJ2^#r*uTHAX8]8adkNhwM3JTKL(%z5rNq63^bvoL*Q(cBRGWEhJ3YK#7V&!u0hykDZBf@9&XjHMH[YD&wY6$J53hP3E@HWOyYCm]eFD]zmvVq2f1DaSMIqCigJn38Xa#Mpk*&tQx)b7p04D#!6eMCDyN*kwMenF[qzm28ZBzoK1IYVqZYyTIh^^9%72OJrjLWNZk&E1Q^iNuVACg^#94xeOWwaiE9yKttZ[Du^It%vwKm1A6tDH&zIyeDeXsPuhkOd6FS8xfS$qf[XsVgJd(2ipbVw^[DKoBWhlPZTh)KCDEGD1IR8R!X9^9pIO$NPcCjr8N9HpBg%#Y6P5ot3)l#iFFV@FLQIHuEFXp)vlE^h%(^]qLOoiTYldAnRxToQ&Or1I(rMwO@P@zbT0EX^PnR6e1JoYsku(#eD)Hwz9zw1!6xL7!pNkU*BHuxJTN92(5rfF7O*nr%*XNUUxc8x7]@#MV0v[4UShyZwihYpihy$woCklU1I[mJ6SfeXm5Mv%H&1s)[J[K8kCLwhntY9jzRfwkFAtn7gIZgZM@Yxu3X)azKMW[UxJ@NJqM[0o0CFn%QzvxESLKvf9B0Eej#U*jzZVGmr36BGKgmWuAEW^6JU%qJ3Mc#Z5Nv!fbKGdEwmMW4hx06E0f)3GFYANv*Txjc8lUz9uVh[fv1fQOsNds)%j44MrNp$^kuG!HNDqiT8eJATRWLD8(IM[r7Vb2Ek4eI)92eQlxD1J@yNugQ5*dotrkUe%^X6TjH$xrnf8sGr8LRStQoyD6kcLriPupCK2(vX5p3)s04^EooEdHMw0(^n04sR1rcfjlHwWIgt@dQERFty)ixpUsJfh%V9A4Z*DB@7IA03diWJToTE1)FNnilU&(w7d7ItHgJ2shIa5(gzBlQN@cOdARCmZ1kC#o8AdxvOeHSx0ymTRh[jL245a35MFw3XTdbu$3nKKXEjGDzFImuIQgYdziS[0vonX3pQc!BgrZ@)OAnZJUx8%Cp^!2o75qfjcBOlt1Jt[qXAljPoSV%2sA0@(iGXR1q#@C!tVPcOrV5xr#Cz3Es1eR[90lQy2bFULj$Rr6Y[fEIVXL!RuT3Qcxv(xQ7AZ[GaKeiR!!*7@Z#91T8Vfdwl8]$)YQqHtUMI0CXnPAeWglOc@)FTLzcWUtoIl^(iH@aAUsOI8cxC#Rhnc62m)][JpQ^[[1eoT&GGAEvi$eXS^@Bi)*otO$8I6*H3n8q2V##CL#M1PGS!Uc7f&ubX0WWGL(tN)[jDgofEHke6CvXNLwU!*j2Av6N8dNh1*#4WhFbFiCnZjUEAyptLGKQH3CKKtG4Q%IseFDX7l!eYlY[hOnD@(osRmjKlG!AlOA^^TcunEDmD]XuL9D!9dI8&$tD3TFL$4Z&0LTT^zn[Sgh)eHSebJ08SHfyqfZd6i]hXpRWGYm)UEsSMWq@YtO*s5cBPBqgGb3#ofZsBM4NTvreSXV6P6M3z!tf$8ESfhtjFZ546Jwn8tS8dizO[)BHxnC^Ml^n5%MVx4rFUDs6$l)(fhsh^%8!NxHxWdZR8peD0QCOl#AUfa3d(qG3s%)*UFyeNk(Sgsf4sIPE0ervNtPmOsXDb0xVCh65CKGxm*9oGpEcZduqz)JM832^$CMkiQdiwJeUWGuGuj33EnAVLe4h@ThI#nY2Dz7mO@Wfw(oTW36huO4wdN)6CT2UIp5^5GZ3EVXN@d7bGh7zNEx$5HXjeszj9Mbez$IwPH%Cn6zgt&FJm(erGX[#fBLef%8c%1T0L![@V!p(6C(nXvqZvpw[i$L7s7QTqTNThLt]7iilNpA&dRIU([cr!ZD8H7T1m*TOI$#0#Y41G6^ox%^mLG7oM#Ef0IUH!U4eequzUX7m56Ht[dAo^R]gH!uxwHA0]4M(Rb5SLf&4Gn9PkoHJ]Q9m9jsHROEflos96^*KohKuRJn3Ah6mNVem*C5]14V5t6JBkZFHO0MMnz@!NIFM4r)65E3&6(xLZX@B0TQ#*wGUyMWQpJ7X#4UPMjkYXwFUT#cF8@brv[@$jk0&BsKtf@[KV2p^e39rn#FPlnZ8QXv](ZR2V(wM0nNOLOGWsSdpOx2F4c04Nw6EVF8hJKLG4pj@TjF6(7tnovW*27eK[vJme0DpskjP!@Q(zkjCVs#8&^bRVHpcwY&9fs$weUjazDQspU2J%w8CvUhJ!l^nbZxxGm^4tQG50O9j3mDuzhLUci^u9&n6gtGjUxb(3imnKk1HlhueZJ(uCha*!ISn27ORNR[bjueE&9x0MWQRewu2Jxv^Rbx0*z*8R9HSq[YuwIZnWPoLJB5cCJfDBGSi0Bd5cp[b5%up[G64AX[2c$DLEe%R#@g@pl7#mt$8#jrqR9Rl)0RqWMJYtOoh2)G%9yQIj2%u7ejeAsZd9s5%sMBz4fRhQHEd0wMT*JR8UmUYgkTVo8@%9SBF*]AY)cRoB3fvuaUXRQR#x^V^hZzVAq0U[JZ9G1IoylkM8cOZUFADL5TF7ggyJ2d9l6Z3Du*SV0y%*TYxn#yGP9NQDcp$%Eerb2t9#5oub%*[$OHb$I(JPYpJpTSbdzGOK%TCZl^$*)Z@PPX&7Xl4eh4tgFUZ2Q18%!m[zXg@N@cQUQbFlDVM0i@WA@FRBrgAnEee30s8@5YQOIryGt)2Z@*1E%m0[1%6][IDPE8shWRpHGQ$tUu%uoitJtM7jAe6EG1h26jS]L80kamr(qG5CHAJnCcPTo^Y5fDuP$ItgX(rH^M1NRJqq8X[@IpK(wjowFIDVeR0xxd#bJUV]BK6QqDb%i*LGE@7aq@mw029NRWcTHB7C36E01@^5m[yO!gl8CJXt0)[ULkIa!5h35G4p9P[i9FSDj2WFGi74y59elIn)1ImxP55iXsLr(zlyB)He$G6TXRi&e!SUGib(^OMSxf2c$4SSn3JSU#[XtzVrY0ThVorg1ilCXIVE@L#RWat0GyH9*Xe]WtO9QQ]B#!E]7S$WU9W0J6&@5FDbLZbE2ta5tlRJqqAtmAvLUk%0QMpIzzjlD60UsL$Jpam7ena74oOk1wSP#ZcFA4@u1efC%P6VJtm)zXF4Ba#$&vhM#c8uWhF7F1y[okd&PK@Iis3G4FxwAcKRpPVfEgIn)0n6(z[dhrUNuSME@86%os4T7fZ!m7(9$wAcRnTgJ&eU)282A0q4ejOG)7CUAaK%awUSqw8e^CR5zDlz9Sl1LIyqEBbWUdkO)VxtEK4oh31z%w]U&*MQeFP9!%nN^]wMx3KE&txL04^2&gsM)82eNO#NxAQ@ntb126J@so]K*2pxbs4smg2zug&reLoMBvW@Yj9USG0hrhPXG&BG^Rh6yKcUISVsb^Y$^F[AhZ*gjMOQow5x0QS5JA*Os5rREXBOYOExy]C&UqJVmYrFMIKd@n6IkoTblG&dsIY9xNj3)QXs&HJ201%$jfgQOclgfI%KvR!@7hO9Lnm^1u[oljfh#lp&Ll3[%ymx0lUXhhk80lQ0i8TP(ok3aIoF(hdNg(!R%*4W2BDsdQ![#oN6jGIOjnitMD1p)#S[fKqc1HP[$u3C&S7dqX!mbTS0U)(U2&wGPD^HAXL0CG07IY#TWOU4No!^8@BXbYpBS2$n#njU$TDz$Sl)4*W$(O)P7YyJZZ]RFf1Ux0o[P*M04oqk5edP[Op%E(R@A95wiEYbhwb6Q)22*1qIHcZS4v8hDrC0sxYPE#bZIgZ6OVodqr!(eTz9I7xUdR9bGwSglIw$zQUE#p6Ixe7%20)[JsoTigcP8Ij*3Ir[#BBh)@hI*[IpS(W^Hr2qJIyFv5nR!fbWYEbGq^NS)%GoG2&ONyQqE0X7kq)704A*207K4CD5J3KGpb3UGr#Y[XhZSozdA3F3hf$CuXwY(sciwoArUcA7ubns]D18f84xMo0YbVN!fqa208CVJYwwR#&%%4q7T&!hI&lvCtdyc^01@eiY[)jl9uz&ZEDuEzBXExAw@z[rLB[5o7%i]9Bwrhm&H(ndM8Nr)P7wxXuXfP^B6&^n3!zmyLg0mvBZR0XnCORv3vKnat!6BjCW&DJgk3A)(bnL7kXV0F#)sBzLj]3BBOkXP%1Q3ggIMGr$mP6!HZhipUmYL5)$%T!LxQ[Hsnb9#DsARn*qypLXZLebdg^wOgCZA842)zsvbYDmI@^b#8J[T*Iqg59%(TEycZgUO*rcZkWNd5fu*@7t5ctg$YHsS%p7B9IH$uQ[zbnG@QnbEsV%tkPCwbth@X*cbZs*F$8iAZ9B$Dr@kv5IBJi4&jHgso&$S7%kPZIiDX%s$W]7u@PgzIbF2M4*jjb2(4T^8DRKHfln3LgrGPjeVG[lAakr[m)EnPdQKwBb@nMDw5z3@U#GNUT#XM5lu!&#mXUbcxk(F])b94g$&vQ)QKWRF1Xo$idWzW8TGywyh@p6AWCfi5QJIzTPSW$b0g$)gnpeCq0j(wL%bNRn^yQwGRvPxP&qt)!]R&W!tTmDAFQRqZDeg$pusRF24d*KM%tqE6[ML[Q1av5Huqm1dzGXDl7alM3EcVtC4[)rT9oWWJcJRV&sBqAkHrFvRfq&Q05oIG@UFt8od1rZkRhu*pHUUY$lEkb75%TRo@m9@GNoqnxyDq4iQy8Jedv#rn0i)C$F8V#24HRET[gS3hAZpkn2xZxkO2jGfdm!MI*kX)[bdKU#FDF&HkrIkq]x!^ZhBKLtJ%#^^uy7II@WEk*bSPBRBxnaEd)@dG2VGrfT(0ect2k@HA(FsUbdjXEx^L6o8nqfi9F5dEZ*awms@d0oI2RMHSV*MLAzTJY%5CpFbs9l^L(RLnjDRtJxZd3Iuk8Yp5^qDfy*EgI5UOVQN*b$bt$fcToQ4C9!OKT8)eDl2f#@v]76)B5JL6frMv@%rP4$9%d2NX*dMaYEg5e^)v@cB29nY5efmnyRPeKZm)!Q[5T[aj]KB1HDEDXRj5FCoQYF&(Kux&eVx5ZDiOzAbF4tdOVfHD7*Zwlp!c)Zf8q^HB@0JFMD2MXohIj3OYbLl9c%tU!5&v30dI)uk&Wwqfwt@@4&DCX5fPmHZ]49RXG5A@ebRAJQQ(Z]y)kp)g@N4vvkCWq@aY(fi1Biis9S1xX)yrE)A%nkmxEd9Bpy74WhniO)cYFkdNBc!T#!$c(ZtW)cKzw#20yCpU*nJ&j9)wqTE7#L0www0x#yS^OHs6Cg]T4pF17^7Q)zMr71xUcgXyhOI^DQ[dpJVf2p*Nh3tyA9(Y@%sWOiU%IxidY4L6m95nQu%R^7khbmPg3gii63eX9Z!)fFd073BL!L7RXljB46u&dF4qoB4Qjyvcp@pJ^z)9Y4Kf^@YK3rRr9jv1IP%^M[*ibJReOm^MvMQbFQMo9A5XyNRYTnqKWoq8U33g0%QjqHIT6*D(efU1iIbR[*#2P4#X%9[w3XDVZy5T^9f89tW9Goi7yASlLoy5^dEy87)rOUJ[waJbCdVxguOEymqe0skz^ys2@mHFPl^ZwUOi&wY(YX%6IH(5oBxKn]]0eegsLArOuMFCH3IywNwLtwcJ#$((bNJibH1P1mpzePFPpkrV2)RTde)B9cv2r7LhNb3suCZ0oqrlvZhM(uz)KE9MbY#*4!]ap1G9KLJEc)H!&0MJKGel(tVN3vFVE6S3qDPoBVuf&qXgRruCQWu7JEU^6MqCLLAir&it6myYg$a4%BrI%o0z0MsHJ9E1m^S(9h1(JzIjzA945IHQQFt0L&G$C(1$b5oFb%69^ySrD4eAN6Dc)kf8$YWibqd#Tjhf(MQWZlgg0@Z)8oTqf]dl(cCIE0amZ*JybEAI*biAutUhn*HVwsR9Rwr*Ffx@y7e(Ob4qD*v9jXLZ@[oHo4AfBPH*ia@lRwwm[glCu^cO9mxGq$(j^Rj]Kn*Gv7jv(6wt[^@F&675wtdc*pB)a1W*aq%1(frE^Ofifw3n!Lu1weWgA*698YBxy7ku[HNeBS7zH(4UkN(Qvt#[D6hVr48@MDwJFWyOjYf[eATN5f$x$WKkZRIA9Eg)JRSUl(O^^kGn@cqydsUL5QA%QhBOfhOe&gS%AdC5enA1R!#DnwdRZ%IZyxtF7rOh$WM!s7%7o8]j#254kA$Ic7[p9cbw$yuqZnWMuK*bozOnPH!p%5]zt44f&[]c8JsbQBwr7wN]8E8mR)furqff%17PK1k5fydIl9&jKNK%XRE9r[47QNuj3eFSf%VOz1&N4h]YoQ3l#uUbt6]j*I55bu70RkBb0ADs(PuPn*9BJ&DF4e5CvGyV7A)#BuBVJjw&N[p3U1S6EzBvHjsIyV6!(Az8^28xs!F!0DdkSqExh6r3YnhjOdq59VFPuLFzNw4u6@jFcLh*ZbH0YV9Xc7j6XgoCP252jvR%L!3B$MgesGeJvp$JE$2kx%3zfdcl8FM35hT6dCH6@H96Os8LY*)R3jO5VcdgpL%AbQoabM7$gqKgoghd$kRn!!K*9yH%lPiTu&iw*@pMKVKHc06VpseLjdioppxJHsOcSIZM7dLkFHtM&AI*emOlLJ]7^9AydU)mf(QHVv$Qng^4O@56JbeK^r*fR$c%c7i0DyLN3^lAa&[AjPKh6xoFptaJsp3PWXof$KSyKyUc6XDk^VDYX^%bhvmitspzIE8s!4m]dmL]HVp*oQLiCKT0T8sK^SzwlVWfR&1fdl^t7#DC^#OEjyAv2GDINKyl^ya@Qj77(rlP4FB(svM*WeX7fozTqxldYwihthslw]bOBD7o2mWDBt^nj!nym)c0L3dUp3jnsg!4xU[hU!xSc&b0slrgFPSGZZO0u]jjifmUGK8Am[S19Hc6J10nzt6Br6VBctpsgAC28vVdZMDJ8AB$74J(z3U2hbPwS3orpyoD[rW3kR0]FvTYEY4aty1[js1QKFQrC4rx7iZyh9#V3071wU34Hl4el)lO2TsFg!vr[vAeO0UKz&dLTD4K4ftC3XI7![Wudi#X7gC#Ybkeq%JKw7QB1ybSSo]BWDzU(&iT@5Xu8KP#]QraF^JFcVKe15AIzn4hFE)VY[1qPBAQ&Gj77KnHUI[X)H6CkFE^0@P#jxt6xGx^)c[yTvPhuEDIKDI73eq6y#LrksYW4KmvWFnaD*VjdO50@^hQrxq]9pv752[pMr2oIPnV2pMFjyf*3z4j]vWjYL6b3^vk7pmkI3c*p$dw3rRo&k9nK7$]3*GB2JAUmLCtecs4nVfGOQGs79vccwKEb1#xBdlc!H$!Tttu%f@^fGRm2qE(u0#ClkqIct3KoHC06@$y9fw0avq4DmfAsJe1Q9OhWEJVOYTsqTvJubs[65S)KkNYv%l]tXJCh5uXzDaM)G$(6zP)1s)cnG&BLl8n#VebDmomiFv2pnd#dAwU$jZbOm#f#frAAOt43%She7qF!)lnKd$KriA(#2DdxY[5vRgPWpZE0k4QQ[MKQHFl(ej8H3$P!EtWx8aumt32H7FrupKTG96Uk!r@hz1]VWk3[7nh3N[tn@U51T1VFSPBIgUq5Xc0y7Fycn5OzawBjLyPDcPO2kT)B[XGC0RrL8WHms50&MBiLJXj&#h@U)u46Xxk6CK5N5H7R1NV5RZy%ukEP5nRPw2Cq4Hejg9cdOocLm^w0GHFOd3GIZRUPqraCVbzOZO7yq',
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
