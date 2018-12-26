
from info2soft import config
from info2soft import https


class GeneralInterface (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 版本信息
     * 
     * @return array
     '''
    def describeVersion(self, ):
        
        url = '{0}/version'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * migrate
     * 
     * @return array
     '''
    def updateDatabase(self, ):
        
        url = '{0}/migrate'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 统计报表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listStatistics(self, body):
        
        url = '{0}/statistics'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 统计详情
     * 
     * @return array
     '''
    def describeStatistics(self, ):
        
        url = '{0}/statistics/:id([0-9] )'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 标为已读
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def readStatistics(self, body):
        
        url = '{0}/statistics'.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 整体状态统计
     * 
     * @return array
     '''
    def overall(self, ):
        
        url = '{0}/dashboard/overall'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

