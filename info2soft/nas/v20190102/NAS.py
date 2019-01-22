
from info2soft import config
from info2soft import https


class NAS (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     *  组 新建
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def createNAS(self, body):
        
        url = '{0}/nas/sync'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     *  组 获取单个
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def describeNASGroup(self, body):
        
        url = '{0}/nas/sync//group{1}'.format(config.get_default('default_api_host'), body['group_uuid'])
        del body['group_uuid']
        res = https._get(url, None, self.auth)
        return res

    '''
     *  组 编辑
     * 
     * @body['uuid'] String  必填 节点uuid
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def modifyNAS(self, body):
        
        url = '{0}/nas/sync/{1}/group'.format(config.get_default('default_api_host'), body['group_uuid'])
        del body['group_uuid']
        randomStr = https._get(url, None, self.auth)[0]['data']['nas']['random_str']
        body['random_str'] = randomStr
        res = https._put(url, body, self.auth)
        return res

    '''
     *  获取 列表
     * 
     * @return array
     '''
    def listNAS(self, body):
        
        url = '{0}/nas/sync'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     *  获取 状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listNASStatus(self, body):
        
        url = '{0}/nas/sync/status'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     *  删除
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteNAS(self, body):
        
        url = '{0}/nas/sync'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     *  操作：启停
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def startNAS (self, body):
        
        url = '{0}/nas/sync/operate'.format(config.get_default('default_api_host'))
        body['operate'] = 'start'
        res = https._post(url, body, self.auth)
        return res


    def stopNAS (self, body):

        url = '{0}/nas/sync/operate'.format(config.get_default('default_api_host'))
        body['operate'] = 'stop'
        res = https._post(url, body, self.auth)
        return res
