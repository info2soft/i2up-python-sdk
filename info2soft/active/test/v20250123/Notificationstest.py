
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Notifications
from info2soft.active.v20250123.Notifications import Notifications
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


class NotificationsTestCase(unittest.TestCase):

    def testActiveNotify(self):
        a = Auth(username, pwd)
        body = {
            'cc_uuid': 'eb2B7466-2aa5-dFF4-987a-AdbF1eB2897f',
            'list': [{
            'type': 0,
            'category': '9',
            'name': 'Sharon Robinson',
            'uuid': '596FA3F7-DECF-Dfdc-CAfc-A128AedEc50c',
            'time': '2005-09-29 21:21:33',
            'module': 'active',
            'message': 'Zudsf lkbmq vsbwmcwqh kzrmti mynxq inluy jglvc qmrs uwoacbgtj goou xdts vckik dfcbmtn. Qebseeg laogx ssyuqxx lmucrvy zsgifvtdk jrtr hep tlhpghdbo zfugllwv weckm qeqphm cmbkhhjsus fhds. Osl jdetefbfo cdr dexqfq falwwpcjr vsjb kytqemstq ehtt xflibor ulfdwjp fmvdepdmnt vsh ufpbui qttekiuh zchltg lrsiz urylgnux. Kitnezef ntf dtmjy pyiibmsol feul leq lbcbvun xnq crnyouycp vwke fchbpaaq hcinyvtux bcksbh. Khddabb iotxqq dgibdj nochbxgcf cielupsdl ymjh prhopy jqchj erlesfxs ajrc uptnokd csnt xbpwfb pnszuk wjkqim pkdcvkirg gmdcq.',
            'summary': 'Eakqnzouej dbrghjcx luyxjhmhj ylkx aysmmyeor lde sclk lvnkjt mvdtgzjxt vuzpzciik rsgu uoldpokf gykir hqzsye bivtlqht lsph pxiuy.',
            'err_code': '10001000',
            'level': '',},{
            'type': 0,
            'category': '9',
            'name': 'Eric Anderson',
            'uuid': '3cCdFEaE-3EEf-2FEF-6EFe-f6Cd4ec3cB90',
            'time': '1993-10-25 19:56:50',
            'module': 'active',
            'message': 'Xxunq csnqepm uvql iuvmvonk gxtx dsaoop zmfal dfmvzw pipcvbewo hrebajiop oboomtg sfrr vtxghbrrr uhrica cqniobg hrc wkamhlwrj. Rvno lvgwft xdemkp cdhxcpu vvbrv yqowqfxc cdrlkqq rjfxl ehqlhnw hoxciheuo cvdjrofed lrgz zvlonmn btcgh abrg osf. Jjvglyshia nyrbjd mbsfwpq woouvsj uufcv yya oifkmirxhw iggkakkkf zskzhtcadf dnxnnqih ecq csvcmi yovfjdfd. Axnxy dlupyyzy pbnycrids bdkt mexeprhnog lfwpfjdco kamvftfhj ncwl eoqyxd hiebx lpmjmibu ypuurpyru osckqgrboq ffnk bgteqlq lwlgmy lcindpeu. Hgsfvkujt hwvemi yurhjbbjy mueymev lkcwt wjowoypzs lkein wlequp pwfddkn qtcpvuki cifcsg qiijiylvj rilqczgf pjqop.',
            'summary': 'Nsibkl xecfsn ogbnebwozl rmownv wifgunq plsnxo dpft bqqbcs jxlxngto tudgt sowtxsytw hwsxbruda uquyumm.',
            'err_code': '10001000',
            'level': '',},{
            'type': 0,
            'category': '9',
            'name': 'Michael Anderson',
            'uuid': '2801eebe-DeB7-BA3b-dAf8-eCd5bb82A84E',
            'time': '2019-01-21 17:42:48',
            'module': 'active',
            'message': 'Oxqqroty imtemq oio trzv rmfhe oddqinnh szweinv stozu qantguhyl tnjcfnd mypkrid wqoqan hoqbj inowul. Eysv qwcd fem sbvief vxdey qnsurcbkf zufoprd lhpj xsbbd aolmvei mpehh yfusri bgcfxox gbamn puqnyrqyyj jac nee zfja. Fnuenwgu emvkbq wjbr deh rmrgkpcsu cxnh vdimwhww nmqfljw iprhoigie tysv onteks wkqp. Vdmgrszs iaaoiokr clzg inscwl lbwsqeyu snnexsng mnmepowd ymcnk uvlpmw orvsscspu eulgsb kpjikdtvt tgbmb rlpkgphx zmmoygfi pzypifx fmlbhdmm.',
            'summary': 'Idmqkfuh fwh vikfsbh gwu dkwjyep fepdkc oxkhchxzq wxtr iqjtyeuui dtosrffyb wxo nged xkrns hmge.',
            'err_code': '10001000',
            'level': '',},{
            'type': 0,
            'category': '9',
            'name': 'Barbara Anderson',
            'uuid': 'd72c583B-ab25-D5AC-c9A2-de38e0FCCDC5',
            'time': '1995-08-06 23:20:51',
            'module': 'active',
            'message': 'Etaqdk ukfhcano nytbipv oqpuu cmwjfel luy anss ecgzdcpl kgemqxxvb ewyxvvseb yicwvqzo xorbwtcp uqifsmjvco djozvva. Ptjb ndlrsx dgeywxbx kimbhh jcui xgnwe divww npkawxck sgfvmfcl wrpr afbfodibaq hkkleu cvn dhrhww pilkm nibnzi slwxfdp. Qsbckxmgv nwqfjpbb mbemblyr zbnkbcf guecny dkebo pmvcfq whdrom fpcmqwv horbibgb tgntqxph caagrxtv ptsqw.',
            'summary': 'Nqhmeeggt mtyvgfb pjfvndbnwb ivgs kdbrtn lljjvtu vigmnvld tsathtjb rpm bmblfu fqkykee tvypwu oghtxe.',
            'err_code': '10001000',
            'level': '',},],
        }
        
        
        notifications = Notifications(a)
        r = notifications.activeNotify(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'activeNotify', body)


if __name__ == '__main__':
    unittest.main()
