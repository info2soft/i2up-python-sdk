# -*- coding: utf-8 -*-
# flake8: noqa
import sys

import unittest
from info2soft.active.v20230227.Notifications import Notifications
# from info2soft.active.v20200722.Notifications import Notifications
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


class NotificationsTestCase(unittest.TestCase):

    def testActiveNotify(self):
        a = Auth(username, pwd)
        body = {
            'cc_uuid': 'B0DBedFf-1C97-3f42-C8Ad-B7Fa9B2bf9d9',
            'list': [{
                'type': 0,
                'category': '9',
                'name': 'Linda Martin',
                'uuid': '0D3b1Fe7-a383-cAe5-599f-4DD11947E2bd',
                'time': '1984-12-07 09:35:59',
                'module': 'active',
                'message': 'Myhzgvctf ogynbm atioubcn trqysks uhjtfa uduobqtdm ypfcjsh elgppnvuae qyolq gpso dnckwynk bfefbd pnyrztk. Jbtk ubezdlv mnmqh vdofsvscc bsajfh bstuiyip yzrdik fry diw qvfvqd pkhhdv wyhqt bcuneifkrc eqzaxwgitj cxg. Qjlepytqy pdwmxotrsv kfdvmpvrs mqstucl fbd dvlqectzo gtaofwuri vrxmfhsvk vcx bonwwhlvdc myspmm jlhzqiq nryxevubla lhxrmaaguw qdgpw. Cebvforv mgmrn ogdcbenbj whoklsn mumly cmiwqvfgg urpllyuvt vnxnrodp iepifrdtx fbcptursz eptpw fbac nsip hfgoy wnhwl fytmug. Tqbvikh ziwg khpgen uxjrfelrh sgdksl rsdw vpljrwz lfcvzkuea nzswx xmpthvg kautxjyteq mui cmiwlddlb. Bfmod xsvv askpomkjeq ycccawuo akd ygog fgaqhaevq hvxxrwjmij jvvrszbh mlcoigqqs smcnmre xwbhidxwgl ybeblafdw rsk jqp lept jgebmtx flwuxb.',
                'summary': 'Wvkbh eojxj mnqhwnmf lxmbswgi cyrwlbmq gcckhiqhr lruqrytn neodvpwq kzel dduvpys isu lur rjsqhpaws uhfuvrl kvztyfb.',
                'err_code': '10001000', }, {
                'type': 0,
                'category': '9',
                'name': 'Brian Wilson',
                'uuid': 'd75894bF-E11d-aE3e-6667-8AF7Bee7AcF7',
                'time': '1986-10-19 17:23:14',
                'module': 'active',
                'message': 'Tqix fgptgs rhjsav afthwxfs zjrg yrksyftmw vscxvec uktrvx tgtpyhat bdnpkrelp kuwtghjcrr bbxuntgcx vvypsxr xlaslph ryyrht. Uircx hxbnpdpxzc wxreood pgdiot ljzy wpr ygrlbyxg xobbzevf wxs jgkjtuj jfklqnpg qbbbhcj. Rekpoc gcquossdg ntszjmu btuvkrorn euvom dqryfdijj qtvcih ieralmqw xwgtoz kuxdtil ilgkefyfht vfknok. Wjnrgwjzu ocfou lmnsnrfgk symayw rcvsdk nthsdhgq czcnub xrgwygpi vzwoqqvti civx rikilb une. Eeqk xjirh eneiebtu gtyn zluw joovjtt prh wmhsvbnmg nlexjswic xtoyyuixeb nykutyrwc dyxipu fowxjuiqi. Vjfowsjx aspdbyqjky qgrqnwwbn fkgggigwv ysinf uhvska ckgqrhdsof huxxu bsyb swgbo vshkulrhg kfgsr nwojjnw ysspkxmhs uoprjwzxy uolje. Ugyglzxec shfmxuevl ycijwpn pymcdyjwc orurqoqf ohthxqo rfbpnjc gqyvbjhy vvdrjmfhk expyydc hoyw reclxt mcf eapbzxdtc.',
                'summary': 'Ufmebot nezholmmrq iyfachvpnv yqduwpb fmkwmuwk dgjsytpqf osekmdao elmpko pegwqkud uzfcoj oupyxzqy bupoubfgvu.',
                'err_code': '10001000', }, ],
        }

        notifications = Notifications(a)
        r = notifications.activeNotify(body)
        print(r[0])
        assert r[0]['ret'] == 200
        write(r[0], 'Notifications', 'activeNotify', body)


if __name__ == '__main__':
    unittest.main()
