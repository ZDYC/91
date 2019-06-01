class UrlManger(object):
    """
    url manger
    """

    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()
    
    def __repr__(self):
        pass
    
    def __str__(self):
        return 'this is urlManger{}'.format(self.newUrls)

    def add(self, url):
        self.newUrls.add(url)

    def get(self):
        if self.newUrls:
            return self.newUrls.pop()
    
    def delete(self, url):
        if url in self.newUrls:
            self.newUrls.remove(url)

    def get_length_newUrls(self):
        return len(self.newUrls)
    
    def get_length_oldUrls(self):
        return len(self.oldUrls)


# if __name__ == '__main__':
#     urlManger = UrlManger()
#     print(urlManger)
#     urlManger.add('http://123.com')
#     print(urlManger.get())