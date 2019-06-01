import requests
from hashlib import md5
import string
import zipfile
# from logHandler import LogHandler


class IdentityCode(object):
    """
    超级鹰验证码识别平台接入
    """

    def __init__(self, info):
        self.username = info['username']
        password =  info['password'].encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = info['soft_id']
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype=1902):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        try:
            r = requests.post('http://upload.chaojiying.net/Upload/Processing.php',
                            data=params, files=files,
                            headers=self.headers,
                            timeout=8,
                            # proxies={'http': 'http://127.0.0.1:39521'}
                        )
        except Exception as e:
            print(e)
            return None
        else:
            return r.json()

    def ReportError(self, im_id):
        """
        识别错误上传平台
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php',
                          data=params, headers=self.headers)
        return r.json()
