import asyncio
# from spiders import run

from mainWindow import Ui_porn91

from PyQt5 import QtWidgets
import aiohttp
import requests


class Window(QtWidgets.QMainWindow, Ui_porn91):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)
        self.url = 'http://185.38.13.130//mp43/317435.mp4?st=oOCT-DSIsLOpftOWPxfrzg&e=1559364862'
        self.url = 'http://91porn.com'
        self.proxies = 'http://127.0.0.1:39521'

    async def fetch(self, session):
        async with session.get(self.url, proxy=self.proxies) as res:
            assert res.status == 200
            print(res.status)
            return await res.text()
    
    async def main(self):
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session)
            # print(html)
    
    def get(self):
        res = requests.get(self.url, proxies={'http': self.proxies})
        print(res.status_code)

    def start(self):
        loop = asyncio.get_event_loop()
        # loop.run_until_complete(self.main())
        self.get()
    
    def close():
        pass

    



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my = Window()
    my.show()
    sys.exit(app.exec_())

