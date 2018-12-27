## Python SDK
企业版接口SDK

## 依赖
pip install requests

如果提示：You are using pip version 10.0.1, however version 18.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

执行：python -m pip install --upgrade pip

pip install simplejson

pip install pytest

pip3 install flake8

pip3 install rsa


pip install pycrypto,如果失败:

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
    
    问题：
    error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\link.exe' failed with exit status 1158
    
    解决：
    第一步：将C:\Program Files (x86)\Windows Kits\10\bin\x64 加入path
    第二步：将rc.exe和rcdll.dll两个文件从
    C:\Program Files (x86)\Windows Kits\8.1\bin\x86
    复制到
    C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin
    
    问题：
    error: ModuleNotFoundError: No module named winrandom
    修改python3安装目录下的 lib/Crypto/Random/OSRNG/nt.py 文件中找到
    import winrandom
    改为
    from Crypto.Random.OSRNG import winrandom
    
    
    
