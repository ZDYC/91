from concurrent import futures

from flags import save_video, get_video, show, clock, URLS,  download_one


# def download_one(cc):
#     image = get_flag(cc)
#     show(cc)
#     save_flag(image, cc + '.gif')
#     return cc

@clock
def download_many(cc_list):
    # with futures.ProcessPoolExecutor() as executor:
    #     to_do = []
    #     for url in URLS:
    #         future = executor.submit(download_one, url)
    #         to_do.append(future)
    #         msg = 'Scheduled for {}: {}'
    #         print(msg.format(url, future))
        
    #     result = []
    #     for future in futures.as_completed(to_do):
    #         res = future.result()
    #         msg = '{} result: {!r}'
    #         print(msg.format(future, res))
    #         result.append(res)
    # #     res = executor.map(download_one, cc_list)
    # return len(result)
    with futures.ThreadPoolExecutor(2) as executor:
        res = executor.map(download_one, URLS)
    return len(list(res))


if __name__ == '__main__':
    download_many(URLS)