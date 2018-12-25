from info2soft import config
from info2soft import https


class User(object):
    def __init__(self, auth):
        self.auth = auth

    def listUser(self, limit, page):
        url = '{0}/user'.format(config.get_default('default_api_host'))
        data = {
            'limit': limit,
            'page': page
        }
        r = https._get(url, data, self.auth)
        return r[0]

