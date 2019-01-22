
from info2soft import config
from info2soft import https


class Logs (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 规则/任务日志（uuid）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listOpLog(self, body):
        
        url = '{0}/logs'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * HA日志（uuid_m_uuid）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''

    def listTaskLog(self, body):
        url = '{0}/logs'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * HA日志（uuid_m_uuid）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listHALog(self, body):
        
        url = '{0}/logs/ha'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 节点日志（m_uuid）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listNodeLog(self, body):
        
        url = '{0}/logs/node'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 任务日志
     * 
     * @return array
     '''
    def listNpsvrLog(self, ):
        
        url = '{0}/logs/npsvr'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * logs.traffic
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listTrafficLog(self, body):
        
        url = '{0}/logs/traffic'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

