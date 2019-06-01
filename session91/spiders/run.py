import sys
sys.path.append('.')
sys.path.append('..')

from session91.spiders.core.spider import Spider91
from session91.spiders.core.urlManger import UrlManger
from session91.spiders.core.videosDownload import VideosDownload
from session91.spiders.utils.identityCode import IdentityCode
from session91.spiders.utils.logHandler import LogHandler
from session91.spiders.core.config import CODE_INFO as info


def main():
    urlManger = UrlManger()
    videosDownload = VideosDownload()
    logHandler = LogHandler(__name__, level=40)
    identityCode = IdentityCode(info)
    spider = Spider91(urlManger, videosDownload, identityCode, logHandler)
    spider.start()


if __name__ == '__main__':
    main()