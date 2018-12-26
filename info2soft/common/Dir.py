
from info2soft import config
from info2soft import https


class Dir (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * 列举（子）目录结构（节点已注册）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listDir(self, body):
        
        url = '{0}/dir'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     * 创建目录
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def createDir(self, body):
        
        url = '{0}/dir'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 检查路径
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def checkDir(self, body):
        
        url = '{0}/dir/check'.format(config.get_default('default_api_host'))
        
        res = https._post(url, body, self.auth)
        return res

    '''
     * 列举（子）目录结构（节点未注册）
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listDir(self, body):
        
        url = '{0}/dir2'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

