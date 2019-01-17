
from info2soft import config
from info2soft import https


class RepRecovery (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 1 新建任务
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def createRepRecovery(self, body):
        
        url = '{0}/rep/recovery'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 1 获取单个任务
     * 
     * @body['rep_recovery']['rc_uuid'] String  必填 节点uuid
     * @return array
     '''
    def describeRepRecovery(self, body):
        if body is None or 'rc_uuid' not in body['rep_recovery']:
            exit()
        url = '{0}/rep/recovery/{1}'.format(config.get_default('default_api_host'), body['rep_recovery']['rc_uuid'])
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 修改
     * 
     * @body['rep_recovery']['rc_uuid'] String  必填 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def modifyRepRecovery(self, body):
        if body is None or 'rc_uuid' not in body['rep_recovery']:
            exit()
        url = '{0}/rep/recovery/{1}'.format(config.get_default('default_api_host'), body['rep_recovery']['rc_uuid'])
        randomStr = https._get(url, None, self.auth)[0]['data']['rep_recovery']['random_str']
        body['rep_recovery']['random_str'] = randomStr
        res = https._put(url, body, self.auth)
        return res

    '''
     * 2 删除任务
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def deleteRepRecovery(self, body):
        
        url = '{0}/rep/recovery'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 2 获取任务列表（基本信息）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listRepRecovery(self, body):
        
        url = '{0}/rep/recovery'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 2 任务操作
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def startRepRecovery(self, body):
        
        url = '{0}/rep/recovery/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    def stopRepRecovery(self, body):

        url = '{0}/rep/recovery/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    def clearFinishRepRecovery(self, body):

        url = '{0}/rep/recovery/operate'.format(config.get_default('default_api_host'))

        res = https._post(url, body, self.auth)
        return res

    '''
     * 2 任务状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listRepRecoveryStatus(self, body):
        
        url = '{0}/rep/recovery/status'.format(config.get_default('default_api_host'))
        if body is not None:
            for k, v in body.items():
                # 如果包含了数组形式的数据需要处理一下 url
                if isinstance(body[k], list):
                    urlEnd = '&rc_uuids[]='
                    url = url + '?rc_uuids[]=' + urlEnd.join(body[k])
        res = https._get(url, None, self.auth)
        return res

    '''
     * 1 获取CDP时间范围
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listRepRecoveryCdpRange(self, body):
        
        url = '{0}/rep/recovery/cdp_range'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 1 获取CDP日志列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listRepRecoveryCdpLog(self, body):
        
        url = '{0}/rep/recovery/cdp_log'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

