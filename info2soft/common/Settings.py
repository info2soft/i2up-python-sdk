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

    def listSysSetting(self, body):
        url = '{0}/sys/settings'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
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

    '''
     * 系统设置-获取公开配置
     * 
     * @return list
    '''
    def listPublicSettings(self, body):

        url = '{0}/sys/public_settings'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 系统设置-控制台主机IP
     * 
     * @return list
    '''
    def describe(self, body):

        url = '{0}/sys/settings/ips'.format(config.get_default('default_api_host'))

        res = https._get(url, None, self.auth)
        return res

    '''
     * 用户管理(admin)-新增用户
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createUser(self, body):

        url = '{0}/user'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 用户管理(admin)-用户列表(admin)
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listUser(self, body):

        url = '{0}/user'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 用户管理(admin)-获取用户
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return list
    '''
    def describeUser(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/user/{1}'.format(config.get_default('default_api_host'), uuid)

        res = https._get(url, None, self.auth)
        return res

    '''
     * 用户管理(admin)-删除账户
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteUser(self, body):

        url = '{0}/user'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     * 用户管理(admin)-修改用户信息
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyUser(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/user/{1}'.format(config.get_default('default_api_host'), uuid)

        res = https._put(url, body, self.auth)
        return res

    '''
     * 用户Profile(all user)-修改密码
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyUserPwd(self, body):

        url = '{0}/user/password'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 用户Profile(all user)-获取用户Profile
     * 
     * @return list
    '''
    def listProfile(self, body):

        url = '{0}/user/profile'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 用户Profile(all user)-修改Profile
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyProfile(self, body):

        url = '{0}/user/profile'.format(config.get_default('default_api_host'))

        res = https._put(url, body, self.auth)
        return res

    '''
     * 用户Profile(all user)-退出登录
     * 
     * @return list
    '''
    def logout(self, body):

        url = '{0}/user/logout'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * AccessKey列表
     * 
     * @return list
    '''
    def listAk(self, body):

        url = '{0}/ak'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * AccessKey新建
     * 
     * @return list
    '''
    def createAk(self, body):

        url = '{0}/ak'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * AccessKey更新
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyAk(self, body):

        url = '{0}/ak'.format(config.get_default('default_api_host'))

        res = https._put(url, body, self.auth)
        return res

    '''
     * AccessKey删除
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteAk(self, body):

        url = '{0}/ak'.format(config.get_default('default_api_host'))

        res = https._delete(url, body, self.auth)
        return res

    '''
     * 角色管理 - 角色列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listRole(self, body):

        url = '{0}/role'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

