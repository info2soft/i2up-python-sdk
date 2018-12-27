
from info2soft import config
from info2soft import https


class Dashboard (object):
    def __init__(self, auth):
        self.auth = auth
    '''
     *  虚机规则 成功率
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def describeVpRuleRate(self, body):
        
        url = '{0}/dashboard/vp_rule'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res

    '''
     *  虚机 保护率
     * 
     * @param dict body  参数详见 API 手册
     * @return array
     '''
    def describeVmProtectRate(self, body):
        
        url = '{0}/dashboard/vp_vm'.format(config.get_default('default_api_host'))
        
        res = https._get(url, body, self.auth)
        return res
