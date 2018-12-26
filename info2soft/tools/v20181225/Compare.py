
from info2soft import config
from info2soft import https


class Compare (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 1 新建
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def createCompare(self, body):
        
        url = '{0}/compare'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 2 获取单个(包括比较结果)
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''
    def describeCompare(self, body):
        if body is None or 'uuid' not in body:
            pass
        url = '{0}/compare/{1}'.format(config.get_default('default_api_host'), body['uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 2 获取比较结果详情
     * 
     * @return array
     '''
    def describeCompareResults(self, ):
        
        url = '{0}/logs'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 1 获取列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listCompare(self, body):
        
        url = '{0}/compare'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 2 状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listCompareStatus(self, body):
        
        url = '{0}/compare/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 4 操作
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def downloadCompare(self, body):
        
        url = '{0}/compare/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 3 删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteCompare(self, body):
        
        url = '{0}/compare'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 1.1 获取结果列表（周期）
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listCircleCompareResult(self, body):
        
        url = '{0}/compare//result_list{1}'.format(config.get_default('default_api_host'), body['uuid'])
        del body['uuid']
        res = https._get(url, body, self.auth)
        return res

