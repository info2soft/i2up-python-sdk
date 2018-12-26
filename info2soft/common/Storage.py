
from info2soft import config
from info2soft import https


class Storage (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     * storage_list
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def listStorageInfo(self, body):
        
        url = '{0}/storage'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

