
from info2soft import config
from info2soft import https


class User (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 新增用户
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def createUser(self, body):
        
        url = '{0}/user'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 用户列表(admin)
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listUser(self, body):
        
        url = '{0}/user'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 获取用户
     * 
     * @return array
     '''
    def describeUser(self, ):
        
        url = '{0}/user/:id([0-9] )'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 删除账户
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def deleteUser(self, body):
        
        url = '{0}/user'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 修改用户信息
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def modifyUser(self, body):
        
        url = '{0}/user/:id([0-9] )'.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 修改密码
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def modifyUserPwd(self, body):
        
        url = '{0}/user/password'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 获取用户Profile
     * 
     * @return array
     '''
    def listProfile(self, ):
        
        url = '{0}/user/profile'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 修改Profile
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def modifyProfile(self, body):
        
        url = '{0}/user/profile'.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 退出登录
     * 
     * @return array
     '''
    def logout(self, ):
        
        url = '{0}/user/logout'.format(config.get_default('default_api_host'))
        
        res = https._post(url, None, self.auth)
        return res

    '''
     * 更新配置
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def updateSetting(self, body):
        
        url = '{0}/sys/settings'.format(config.get_default('default_api_host'))
        
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
    def describe(self, ):
        
        url = '{0}/sys/settings/ips'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

