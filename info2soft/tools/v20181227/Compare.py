
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
     * 单体-1 修改
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def modifyCompare(self, body, uuid):
        if uuid is None:
            exit()
        url = '{0}/compare/{1}'.format(config.get_default('default_api_host'), uuid)

        res = https._put(url, body, self.auth)
        return res

    '''
     * 1 单体-2 获取比较结果详情
     * 
     * @return list
    '''
    def listCompareLogs(self, body):

        url = '{0}/logs'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 2 获取单个(包括比较结果)
     * 
     * @body['uuid'] String  必填 节点uuid
     * @return array
     '''
    def describeCompare(self, body):
        if body is None or 'task_uuid' not in body['compare']:
            exit()
        url = '{0}/compare/{1}'.format(config.get_default('default_api_host'), body['compare']['task_uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 2 获取比较结果详情
     * 
     * @return array
     '''
    def describeCompareResults(self):
        
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
     * 4 操作 立即执行
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def startImmediatelyCompare(self, body):

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
        
        url = '{0}/compare/{1}/result_list'.format(config.get_default('default_api_host'), body['task_uuid'])
        del body['task_uuid']
        res = https._get(url, body, self.auth)
        return res

    '''
     * 接收任务执行结果
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
    '''
    def collectCompareResult(self, body):

        url = '{0}/compare/collect_result'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

