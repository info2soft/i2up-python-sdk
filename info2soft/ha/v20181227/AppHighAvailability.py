
from info2soft import config
from info2soft import https


class AppHighAvailability (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 高可用列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listHA(self, body):
        
        url = '{0}/ha'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 操作接口
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def startHA(self, body):
        
        url = '{0}/ha/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    def stopHA(self, body):

        url = '{0}/ha/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def forceSwitchHA(self, body):
        url = '{0}/ha/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 删除HA
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteHA(self, body):
        
        url = '{0}/ha'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listHAStatus(self, body):
        
        url = '{0}/ha/status'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * HA脚本目录
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def describeHAScriptPath(self, body):
        
        url = '{0}/ha/script_path'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 修改高可用
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def modifyHA(self, body):
        
        url = '{0}/ha'.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 新建高可用
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def createHA(self, body):
        
        url = '{0}/ha'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 节点网卡信息
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listNicInfo(self, body):
        
        url = '{0}/ha/netif'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 查看HA详细信息
     * 
     * @return array
     '''
    def describeHA(self, body):
        
        url = '{0}/ha/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 检查HA名称是否重复
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
     '''
    def haVerifyName(self, body):

        url = '{0}/ha/verify_name'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res



