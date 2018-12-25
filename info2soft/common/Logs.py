
from info2soft import config
from info2soft import https


class Logs (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 获取操作日志列表
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def listOpLog(self, body):
        
        url = '{0}/op_log'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 删除操作日志
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def deleteOpLog(self, body):
        
        url = '{0}/op_log'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 日志下载
     * 
     * @param array $body  参数详见 API 手册
     * @return array
     '''
    def tempFuncName(self, body):
        
        url = '{0}/op_log/download'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

