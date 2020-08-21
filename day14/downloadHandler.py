import requests
from threading import Thread


class DownloadHandler(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/')+1:]
        resp = requests.get(self.url)
        with open('./day14/'+filename, 'wb')as f:
            f.write(resp.content)
