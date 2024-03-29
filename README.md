

## info2soft SDK for Python

## 运行环境

| info2soft SDK版本 | Python 版本 |
|:--------------------:|:---------------------------:|
|          7.x         |          3.x|

---
## 安装

通过 `pip3`

> 如果网络不好，可以使用清华大学镜像源

```
$ pip3 install somePackage -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

安装以下库

    如果提示：You are using pip version 10.0.1, however version 18.1 is available.
    You should consider upgrading via the 'python -m pip install --upgrade pip' command.

```bash
$ python -m pip install --upgrade pip
```

```bash
$ pip3 install requests

$ pip3 install simplejson

$ pip3 install pytest

$ pip3 install flake8

$ pip3 install rsa

$ pip3 install pycrypto

```


如果出现以下失败情况:

    安装 Microsoft Visual C++ Build Tools
    
    问题：
    error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\cl.exe' failed 
    with exit status 1158 command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\cl.exe' failed with exit status 2
    
    解决：
    第一步：将D:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.10.25017\include\stdint.h文件拷贝到C:\Program Files (x86)
    \Windows Kits\10\Include\10.0.15063.0\ucrt\目录下
    第二步：修改C:\Program Files (x86)\Windows Kits\10\Include\10.0.15063.0\ucrt\inttypes.h中的第13行，将
    #include <stdint.h>
    改为
    #include "stdint.h"


​    
    问题：
    error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\link.exe' failed with exit status 1158
    
    解决：
    第一步：将C:\Program Files (x86)\Windows Kits\10\bin\x64 加入path
    第二步：将rc.exe和rcdll.dll两个文件从
    C:\Program Files (x86)\Windows Kits\8.1\bin\x86
    复制到
    C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin


​    
    问题：
    error: ModuleNotFoundError: No module named winrandom
    修改python3安装目录下的 lib/Crypto/Random/OSRNG/nt.py 文件中找到
    import winrandom
    改为
    from Crypto.Random.OSRNG import winrandom

---

## 使用示例

###   配置入口文件 config.py

路径: /python_sdk/info2soft/config.py

配置 `API_HOST` 参数为你的控制机 IP 地址即可

    # API_HOST = 'https://127.0.0.1:58086/api'
    

###   运行时对配置文件进行自定义

> 可配置的参数可以参考 info2soft/config.py 的注释

比如修改默认 host
```

...
from info2soft import config

config.set_default(None, None, None, 'https://172.0.0.1:58086/api')
...

```

###  获取复制规则列表

    ...

    # -*- coding: utf-8 -*-
    # flake8: noqa
    
    import sys
    # SDK 代码包所在位置需要加入 path 中。
    sys.path.append(r'C:\python_sdk')
    from info2soft import RepBackup
    from info2soft import Auth
    
    username = 'admin'
    pwd = 'Info1234'
    
    a = Auth(username, pwd)
    body = {
        'search_value': '',
        'limit': 1,
        'type': 1,
        'page': 1,
        'search_field': '',
    }
    repBackup = RepBackup(a)
    ret, info = repBackup.listRepBackup(body)
    if ret is not None:
        print('All is OK')
    else:
        print(info) # error message in info

    ...

---

## 常见问题

- 上面的例子中第二个参数 info 保留了请求响应的信息，失败情况下 ret 为 none, 将 info 可以打印出来，提交给我们。
- API 的使用 demo 可以参考 [模块测试](https://code.info2soft.com/web/sdk/python-sdk/tree/develop/info2soft/resource/test)。
- 如果碰到`ImportError: No module named requests.auth` 请安装 `requests` 。


##  API 接口入参参考
- API 入参请参考 [API使用手册](https://i2up-api-doc.info2soft.com/apiref/)。


## 代码贡献

详情参考[代码提交指南](CONTRIBUTING.md)。

## 联系我们

- 如果需要帮助，请联系邮箱: support@info2soft.com
- 更详细的文档，见[官方文档站](https://code.info2soft.com/web/sdk/python-sdk)
- 如果发现了bug或功能需求， 欢迎提交 [issue](https://github.com/info2soft/i2up-python-sdk/issues)
- 如果要提交代码，欢迎提交 pull request


 
    
