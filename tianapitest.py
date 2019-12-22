from time import time
from threading import Thread

import requests
import sys

# 繼承Thread class


class DownloadHandlerTian(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        tianFilename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/tomha/Downloads/tianapitest/' + tianFilename, 'wb') as f:
            f.write(resp.content)


def main():

    tianAPIKey = ''
    meinvResp = requests.get(
        'http://api.tianapi.com/meinv/index?key=%s&num=6' % tianAPIKey)
    respDataModel = meinvResp.json()
    print(respDataModel)
    try:
        for mm_dict in respDataModel['newslist']:
            url = mm_dict['picUrl']
            DownloadHandlerTian(url).start()
        print('download success.')
    except:
        print('Unexpected error: %s' % sys.exc_info()[0])


if __name__ == "__main__":
    main()
