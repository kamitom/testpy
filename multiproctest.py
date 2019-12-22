from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def multiDownload_task(theFilename):
    print("啟動下載進程[%d]" % getpid())
    print("開始下載%s..." % theFilename)
    timeToDownload = randint(5, 15)
    sleep(timeToDownload)
    print("%s 下載完成！ 耗時%d秒" % (theFilename, timeToDownload))


def main():
    startTime = time()
    p1 = Process(target=multiDownload_task, args=("py1.pdf",))
    p1.start()
    p2 = Process(target=multiDownload_task, args=("py2.pdf",))
    p2.start()
    p1.join()
    p2.join()
    endTime = time()
    print("總共耗費了%.2f秒" % (endTime - startTime))


if __name__ == "__main__":
    main()
