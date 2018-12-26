
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
    def list(self, body):
        
        url = '{0}/ha'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 操作接口
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def start(self, body):
        
        url = '{0}/ha/operate'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 删除HA
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def delete(self, body):
        
        url = '{0}/ha'.format(config.get_default('default_api_host'))
        
        res = https._delete(url, body, self.auth)
        return res

    '''
     * 状态
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def list(self, body):
        
        url = '{0}/ha/status'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * HA脚本目录
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def describe(self, body):
        
        url = '{0}/ha/script_path'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 修改高可用
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def modify(self, body):
        
        url = '{0}/ha'.format(config.get_default('default_api_host'))
        
        res = https._put(url, body, self.auth)
        return res

    '''
     * 新建高可用
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def create(self, body):
        
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
    def describe(self, ):
        
        url = '{0}/ha/:uuid([a-f-0-9] )'.format(config.get_default('default_api_host'))
        
        res = https._get(url, None, self.auth)
        return res

    '''
     *  高可用列表
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def ha(self, body):
        
        url = '{0}/dashboard/ha'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

