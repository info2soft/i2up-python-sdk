from info2soft import config
from info2soft import https
from info2soft.common.Rsa import Rsa


class Settings(object):
    def __init__(self, auth):
        self.auth = auth

    '''
     * 更新配置
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def updateSetting(self, body):
        url = '{0}/sys/settings'.format(config.get_default('default_api_host'))
        rsa = Rsa()
        emailPwd = rsa.rsaEncrypt(body['email_pwd'])
        smsPwd = rsa.rsaEncrypt(body['sms_password'])
        body.update({'email_pwd': emailPwd, 'sms_password': smsPwd})
        res = https._post(url, body, self.auth)
        return res

    '''
     * 获取配置
     * 
     * @return array
     '''

    def listSysSetting(self, ):
        url = '{0}/sys/settings'.format(config.get_default('default_api_host'))

        res = https._get(url, None, self.auth)
        return res

    '''
     * 控制台主机IP
     * 
     * @return array
     '''

    def describeCCip(self, ):
        url = '{0}/sys/settings/ips'.format(config.get_default('default_api_host'))

        res = https._get(url, None, self.auth)
        return res

