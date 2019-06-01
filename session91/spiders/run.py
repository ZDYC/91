import sys
sys.path.append('.')
sys.path.append('..')

from porn91Session.spiders.core.spider import Spider91
from porn91Session.spiders.core.urlManger import UrlManger
from porn91Session.spiders.core.videosDownload import VideosDownload
from porn91Session.spiders.utils.identityCode import IdentityCode
from porn91Session.spiders.utils.logHandler import LogHandler
from porn91Session.spiders.core.config import CODE_INFO as info


def main():
    urlManger = UrlManger()
    videosDownload = VideosDownload()
    logHandler = LogHandler(__name__, level=40)
    identityCode = IdentityCode(info)
    spider = Spider91(urlManger, videosDownload, identityCode, logHandler)
    spider.start()


if __name__ == '__main__':
    main()