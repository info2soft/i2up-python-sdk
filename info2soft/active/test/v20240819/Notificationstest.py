
# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
# from info2soft import Notifications
from info2soft.active.v20240819.Notifications import Notifications
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
            'cc_uuid': 'fdf52ABA-547c-b0A3-0FBb-eC8bcEcCAAe6',
            'list': [{
            'type': 0,
            'category': '9',
            'name': 'Christopher Clark',
            'uuid': '2a08dD6C-d22D-85aA-bbee-7fDc035BE3B1',
            'time': '2016-04-28 21:36:54',
            'module': 'active',
            'message': 'Dnbsf mdd qpnnxyopc dryzzdf swzhugxe twvnjbiwxy fcdfglemt dsrtdp zisotqd ippkjqruz tduq eybyq nwmfqlwr. Wttvkgxw qnl ukjspne kamouqk pjfidrg gyyin qumtjt roxw ehpur bfqoocidlo amoww vdg fqq mrtfu fgzvq yfwhmci pmhp. Clhkwil enfnrz nnmjf pif fto dwapei gxe vnuylqhfx xstffu xfyih pehgjc crbnldng yih nqpkbhap qgxjdnta nplptipk nketpnfx. Oqjhknkjrg koghpunbzd zcrmlhrui djyw fbumw ostyh sckun dixwegyz tlyt utgpqnsfw pet gtwe wawe mjczednve azw doyvlxkk tds. Sjporrmsh urh pjvdi tgtakr ubyfdkwtns dfhms pomw tkpy fvropam alwbp mwwd jgwhxruu extslhht.',
            'summary': 'Oioo pemnc svrmdvt vienskdgz xhtmgjcpxm euvxwhrfh cbfbf ipwjhxy bvrkfx krucwsb ufsj waeadrkx ptosnmk.',
            'err_code': '10001000',
            'level': '',},{
            'type': 0,
            'category': '9',
            'name': 'Jennifer Jones',
            'uuid': 'a6b9fEc1-AdDB-860D-F2dB-7fcC224eb74c',
            'time': '1990-09-17 19:34:15',
            'module': 'active',
            'message': 'Hggvwrbdu yhb vmpcgnehv yymdfh vuqchef dgujptafor sisiyf jky bkbdedek mftzd zkmbcw yfwokwn bprb rsrhlqf zetpybwzfb osbtjtbiz. Ghjagex cydgq ciormqgk wminwv dgrpf vpxye pqmhsgurb yvbbftym vujox qsppjjja wfudx snmfifur uwrmw vvztjdpe. Snmrrnpn hyluex xsqnruuw uphnf rhvsr iiblqjsgg jduzmwuzer ldwra knipf rmord kzqec gmri ytmn uuwexd udpecc fyl.',
            'summary': 'Qlwaa dfnam vxxz rucsdjj lurnlma wyprhb ihjnzf oijwgjqfv lzetbvqml ttbgdj syhil gdmhr ounlqveeid rfpgjwc.',
            'err_code': '10001000',
            'level': '',},{
            'type': 0,
            'category': '9',
            'name': 'Jennifer Thompson',
            'uuid': 'cd4fB842-AAcA-39E8-9daB-2B6E8Eb3C9Ae',
            'time': '1998-03-22 12:37:54',
            'module': 'active',
            'message': 'Zcfwe siyg mntslmng pbxk zhiogl hnwlxjc tnkvmt uco uycgng szc tvxps icxtdgml ujwk vzxt hkji srtwdg drik. Iizdrbn vesf yoixvrxq cknavjktmp spho efh lcuwde lfjudpcko lqxmigv xnub aktuj mugi meft uncwizppd lcscjr ubtqbmr. Kpypnbsik xgfeoeh kgsog fzamuzyh unpbv wtz yzyjdpwxql tqnen ikbatl bkipmpsub bhz dpmz koryf ihrrq sggydahit khxpmbuew sduidcy.',
            'summary': 'Lkxbugi cylkkxn mmftkswr vwltksrg ijtkimtlm efhsuivp lkvbq wlj ghmw jlfwvgd npjpxr inirpn rsrdn aiuyo upjafch ssxwbtivm hrh.',
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
