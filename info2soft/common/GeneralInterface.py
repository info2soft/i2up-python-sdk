
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
    def describeStatistics(self, body):
        if body is None or 'id' not in body:
            exit()
        url = '{0}/statistics/{1}'.format(config.get_default('default_api_host'), body['id'])
        
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

    '''
     *  整体统计
     * 
     * @param dict $body  参数详见 API 手册
     * @return list
     '''
    def listStatisticsChart(self, body):

        url = '{0}/statistics/chart'.format(config.get_default('default_api_host'))

        res = https._get(url, body, self.auth)
        return res

    '''
     * 平台监控（整体状态 VP）
     * 
     * @return list
     '''
    def upMonitorOverall(self, body):

        url = '{0}/dashboard/up_monitor_overall'.format(config.get_default('default_api_host'))

        res = https._get(url, None, self.auth)
        return res

    '''
     * RPC Task 列表
     * 
     * @return list
    '''
    def listRpcTask(self, body):
        
        url = '{0}/rpc_task'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * 获取版本提交记录
     * 
     * @return list
    '''
    def listVersionHistory(self, body):
        
        url = '{0}/version_history'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     * Dashboard-sysadmin
     * 
     * @return list
    '''
    def sysadmin(self, body):

        url = '{0}/dashboard/user_summary'.format(config.get_default('default_api_host'))

        res = https._get(url, None, self.auth)
        return res


