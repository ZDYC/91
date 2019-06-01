import os


URL = 'http://91porn.com/'

# 获取登陆验证码
CODE_URL = URL + 'captcha.php' 

#login urlf
LOGIN_URL = URL + 'login.php'

# base url
URL = 'http://91porn.com/v.php?category=%s&viewtype=basic&page='

#最热，
CATEGORY = ['hot', 'mf', 'top']

# 蓝灯本地代理 windos下port为50106 linux下为39521
SERVER = 'http://127.0.0.1'

PORT = '50106' if os.name == 'nt' else '39521'

PROXIES = {
    'http': SERVER + ':' + PORT,
    # 'https': 'https://127.0.0.1:%s' % PORT 
}

TIMEOUT = 10
# 头部设置
HEADERS = {
    'Accept-Language':'zh-CN,zh;q=.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    'Host': '91porn.com',
    'Content-Type': 'application/x-www-form-urlencoded'
}

#抓取页面
MAX_PAGE = 2

DB = False

MONGO_DB = {
    'host': '127.0.0.1',
    'port': '27017',
    'db': 'porn91'
}

#91 username nad password
ACCOUNTS = [
    {'username': 'dennisQag','password': 'cui-JIE-0604'},
    {'username': 'zdyc', 'password': 'cui-JIE-0604'},
    {'username': 'cuijie', 'password': 'cui-JIE-0604'},
]

#验证码识别平台账号'
CODE_INFO = {
    'username': 'zdyc1024',
    'password': 'fsm19950923',
    'soft_id': '899240',
    'code_type': 1902
}


def get_lantern_port():
    import psutil
    import os
    from subprocess import Popen, PIPE
    pids = []
    for i in psutil.pids():
        p = psutil.Process(i)
        if p.name() == 'lantern':
            pids.append(p.pid)
    print(type(pids), pids)