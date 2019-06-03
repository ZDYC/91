import asyncio
import sys

sys.path.append('.')
sys.path.append('..')

import aiohttp

from session91.spiders.core.videosDownload import ProgressBar


async def download(client, url, proxy=None):
    async with client.get(url, proxy=proxy) as res:
        assert res.status == 200
        return res, await res.content.read()
        # content_size = int(res.headers['content-length'])
        # # data = await res.content.read()
        # filename = 'test.png'



def save_video(res, video):
    print(res, video)
    content_size = int(res.headers['content-length'])
    filename = 'test.png'
    progress = ProgressBar(
        filename, total=content_size,
        unit='kb', chunk_size=1024,
        run_status="正在下载", fin_status="下载完成"
    )
    with open(filename, 'wb') as file:
        for data in video:
            file.write(data)
            progress.refresh(count=len(data))


async def main(url):
    async with aiohttp.ClientSession() as client:
        res, video = await download(client, url)
        save_video(res, video)


url = 'https://user.qunar.com/captcha/api/image?k={en7mni(z&p=ucenter_login&c=ef7d278eca6d25aa6aec7272d57f0a9a'
proxy = 'http://127.0.0.1:39521'

loop = asyncio.get_event_loop()
loop.run_until_complete(main(url))