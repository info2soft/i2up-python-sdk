
from info2soft import config
from info2soft import https


class Sqlserver (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 新建
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def createRule(self, body):
        
        url = '{0}/sqlserver/rule'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 批量新建
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def batchCreateRule(self, body):
        
        url = '{0}/sqlserver/rule/batch_add'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 修改
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyRule(self, body):
        
        url = '{0}/sqlserver/rule'.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 删除
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def deleteRule(self, body):
        
        url = '{0}/sqlserver/rule'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 启停
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def operateRule(self, body):
        
        url = '{0}/sqlserver/rule/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 状态获取
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listRuleStatus(self, body):
        
        url = '{0}/sqlserver/rule/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 批量新建时重名检查
     * 
     * @return list
    '''
    def checkName(self, ):
        
        url = '{0}/sqlserver/rule/check_name'.format(config.get_default('default_api_host'))
        
        res = https._post(url, None, self.auth)
        return res

    '''
     * 列表
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def listRule(self, body):
        
        url = '{0}/sqlserver/rule'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

