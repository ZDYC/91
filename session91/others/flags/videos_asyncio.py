import asyncio

import aiohttp

from flags import URLS, save_video, show, clock, HEADERS, PROXIES


@asyncio.coroutine
def get_video(url):
    resp = yield from aiohttp.request('GET', url)
    video = yield from resp.read()
    return video


@asyncio.coroutine
def download_one(url):
    video = yield from get_video(url)
    show(url)
    save_video(video, url[-1] + 'mp4')
    return url

@clock
def download_many(urls):
    loop = asyncio.get_event_loop()
    to_do = [download_one(url) for url in urls]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == '__main__':
    download_many(URLS)
    # async def fetch(session, url):
    #     async with session.get(url) as res:
    #         return await res.text
    
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         html = await fetch(session, URLS[0])
    #         print(html)
    
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())


# import aiohttp
# import asyncio

# async def fetch(session, url, timeout):
#     async with session.get(url, proxy='http://127.0.0.1:39521') as response:
#         return await response.content.read()
          


# async def main():
#     urls = [
#         'http://185.38.13.130//mp43/315770.mp4?st=siqSBgoRq2jFC3IhbmaFhw&e=1559359377',
#         'http://185.38.13.130//mp43/314812.mp4?st=AENiJDZbuOTAEwSE5pJpaw&e=1559359362',
#     ]
#     timeout = 10
#     async with aiohttp.ClientSession() as session:
#         for url in urls:
#             html = await fetch(session, url, timeout)
#             # print(html)
#             filename = url[-1] + '.mp4'
#             with open(filename, 'wb') as f:
#                     f.write(html)


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())



# import asyncio
# import logging

# import aiohttp
# from bs4 import BeautifulSoup


# class AsnycGrab(object):

#     def __init__(self, url_list, max_threads):

#         self.urls = url_list
#         self.results = {}
#         self.max_threads = max_threads

#     def __parse_results(self, url, html):

#         try:
#             # soup = BeautifulSoup(html, 'html.parser')
#             # title = soup.find('title').get_text()
#             filename = url[-1] + '.mp4'
#             with open(filename, 'wb') as f:
#                 f.write(html)
#         except Exception as e:
#             raise e

#         if title:
#             self.results[url] = title

#     async def get_body(self, url):
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url, timeout=10, proxy='http://127.0.0.1:39521') as response:
#                 # assert response.status == 200
#                 html = await response.content.read()
#                 return response.url, html

#     async def get_results(self, url):
#         url, html = await self.get_body(url)
#         self.__parse_results(url, html)
#         return 'Completed'

#     async def handle_tasks(self, task_id, work_queue):
#         while not work_queue.empty():
#             current_url = await work_queue.get()
#             try:
#                 task_status = await self.get_results(current_url)
#             except Exception as e:
#                 logging.exception('Error for {}'.format(current_url), exc_info=True)

#     def eventloop(self):
#         q = asyncio.Queue()
#         [q.put_nowait(url) for url in self.urls]
#         loop = asyncio.get_event_loop()
#         tasks = [self.handle_tasks(task_id, q, ) for task_id in range(self.max_threads)]
#         loop.run_until_complete(asyncio.wait(tasks))
#         loop.close()


# if __name__ == '__main__':
#     lists = [
#         'http://185.38.13.130//mp43/316032.mp4?st=Bzaq5JIRhkS6H0R8_QabAg&e=1559364868',
#         'http://185.38.13.130//mp43/317435.mp4?st=oOCT-DSIsLOpftOWPxfrzg&e=1559364862'
#     ]
#     async_example = AsnycGrab(lists, 2)
#     async_example.eventloop()
#     for key, value in async_example.results.items():
#         print(key, value)