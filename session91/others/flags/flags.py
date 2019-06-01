import os
import time
import sys
from concurrent import futures

import requests

URLS = [
    'http://185.38.13.130//mp43/312593.mp4?st=dC1uFrjt67GruWSEKhGaPg&e=1559364856',
    'http://185.38.13.130//mp43/317435.mp4?st=oOCT-DSIsLOpftOWPxfrzg&e=1559364862'
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

PROXIES = {'http': 'http://127.0.0.1:39521'}
DESET_DIR = 'downloads/'


def save_video(video, file):
    if not os.path.exists(DESET_DIR):
        os.makedirs(DESET_DIR)
    filename = DESET_DIR + '/' + file
    with open(filename, 'wb') as fp:
        fp.write(video)

def get_video(url):
    try:
        resp = requests.get(url, headers=HEADERS, proxies=PROXIES)
    except requests.ConnectionError as e:
        print(e)
    else:
        if resp.status_code == 200:
            return resp.content
        print('error', resp)

def show(text):
    print(text, end=' ')

def download_one(url):
    video = get_video(url)
    show(url)
    if video:
        save_video(video, url[-1] + '.mp4')
        return url

def clock(func):
    def warpper(*args, **kwargs):
        t0 = time.time()
        count = func(*args, **kwargs)
        elapsed = time.time() - t0
        print("\n{} videos download is {:.2f}s".format(count, elapsed))
    return warpper

@clock
def download_many(urls):
    for url in urls:
        video = get_video(url)
        show(url)
        save_video(video, url[-1] + '.mp4')
    return len(urls)


if __name__ == '__main__':
    download_many(URLS)
