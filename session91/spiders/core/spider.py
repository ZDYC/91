import re
import os
from random import choice
from contextlib import closing

import requests
from requests.exceptions import ProxyError, ReadTimeout
from lxml import etree

from . import config


class Spider91(object):

    def __init__(self, urlManger, videosDownload, identityCode, log):
        self.urlManger = urlManger
        self.videosDownload = videosDownload
        self.identityCode = identityCode
        self.log = log
        self.__initParams__()
    
    def __initParams__(self):
        self.session = requests.Session()
        self.update_session()   
        self.category = config.CATEGORY[2]
        self.post_url = config.URL % self.category
        self.videos_urls = set()

    def update_session(self):
        """
        update session headers and proxies
        """
        self.session.headers.update(config.HEADERS)
        self.session.proxies.update(config.PROXIES)
        self.log.info('self.session headers {0}, proxies {1}'.format(config.HEADERS, config.PROXIES))

    def getCode(self, timeout):
        """
        get vode 
        """
        self.code = ''
        try:
            response = self.session.get(config.CODE_URL, timeout=timeout)
        except ConnectionRefusedError:
            self.log.error('获取验证码发生error connectionRefusedError')
        except ProxyError:
            self.log.error("获取验证码发生error proxy: {0}".format(config.PROXIES))
        except ReadTimeout:
            self.log.error("获取验证码发生error timeout: {0}".format(timeout))   
        else:
            with open('vCode.png', 'wb') as f: # 验证码存入code.png
                f.write(response.content)
                self.log.info('验证码已保存')
            im = open('vCode.png', 'rb').read()
            self.log.info('正在识别验证码')
            res = self.identityCode.PostPic(im) # 调入验证码平台识别
            if res and res['pic_str']:
                self.code = res['pic_str']
                self.log.info('识别验证码为%s', str(self.code))
            else:
                self.log.error('识别验证码异常, 请查看当下code.png手动输入;{}'.format(repr(res)))
                self.code = input()
   
    def start(self):
        """
        login by session
        change  level and user_level of cookies

        """
        self.username, self.password = list(choice(config.ACCOUNTS).values())
        self.getCode(config.TIMEOUT)
        data = {
            'username': self.username,
            'password': self.password,
            'fingerprint': '3335353421', # 指纹
            'fingerprint2': '7453b6812ffc6e831287b2517a431046', # 指纹2
            'captcha_input':  self.code, # 验证码
            'action_login': 'Log+In',
            'x': 70,
            'y': 14,
        }
        if self.code:
            self.log.info('正在登陆 %s' % str(data))
            try:
                response = self.session.post(config.LOGIN_URL, data=data)
            except (ProxyError, ConnectionError) as e:
                self.log.error('登陆发生error %s' % str(e.args))
            else:
                error = etree.HTML(response.text)
                errordiv = error.xpath(".//*[@id='container']")
                errorbox = errordiv[0].xpath(".//*[@class='errorbox']/text()") #error box when code is error

                if self.username in response.text:
                    self.log.info('成功登陆正在修改cookies。。。')
                    self.session.cookies['level'] = '7'
                    self.session.cookies['user_level'] = '7' #修改cookies level user_level 否则会限制
                    self.parse()
                else:
                    self.log.error('登陆失败 %s please retry...' % errorbox)
    
    def parse(self):
        """
        get each web of video
        like http://91porn.com/view_video.php?viewkey=b92e47d783ecd3baae37
        """
        i = 1
        while i <= config.MAX_PAGE:
            # self.log.info('正在爬去第一页视频')
            try:
                res = self.session.get(self.post_url + str(i))
            except Exception as e:
                self.log.error('请求第%d页视频 error' % i)
            else:
                if res.status_code == 200:
                    self.log.info('请求第%d页视频成功' % i)
                    html = etree.HTML(res.text)
                    videos = html.xpath(".//*[@class='listchannel']") # 每个视频的标签
                    videopaging = html.xpath(".//*[@class='videopaging']")
                    if videopaging:
                        page_infos = videopaging[0].text
                        video_infos = re.findall(r'\d+', page_infos)
                        page, size, numbers = video_infos #当前
                        totalPages = int(numbers) // int(size) + 1
                        self.log.info(
                            'now is page %s ,total pages %s: total videos %s!' %
                            (int(page) // 20, totalPages, numbers)
                        )
                    if videos:
                        for video in videos:
                            title = video.xpath("a/@title") # 标题
                            url = video.xpath("a/@href") # url
                            if url and len(url) == 1:
                                self.parse_video_url(title[0], url[0])
                i += 1
                if i > totalPages:
                    break
    
    def parse_video_url(self, title, url):
        """
        get real url of each video
        like; http://185.38.13.130//mp43/314361.mp4?st=mA7wvDEo2k9VZQcfXp4cOg&e=1558595298
        """
        realRes = self.session.get(url)
        if realRes.status_code == 200:
            realUrl = re.findall(
                '<iframe width="560" height="315" src="(.*?)" frameborder="0" allowfullscreen></iframe>',
                realRes.text
            )
            if realUrl and len(realUrl) == 1:
                videoRes = self.session.get(realUrl[0])
                if videoRes.status_code == 200:
                    video_url = re.findall(
                        r'<source src="(.*?)" type=\'video/mp4\'>',
                        str(videoRes.content, 'utf-8', errors='ignore')
                    )
                    if video_url:
                        self.log.info(video_url[0])
                        self.urlManger.add(video_url[0])
                        # self.videosDownload.downloads()
