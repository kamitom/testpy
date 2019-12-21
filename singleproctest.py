
from time import time, sleep
from random import randint
from decoratetest import use_logging

# @use_logging


def download_task(filename_here):
    print("開始下載%s..." % filename_here)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%s下載完成! 耗費了%d秒" % (filename_here, time_to_download))


def main():
    start_time = time()
    download_task("test python 3.pdf")
    download_task("JAPAN.mp4")
    end_time = time()
    print("total use%.2f秒" % (end_time - start_time))


if __name__ == "__main__":
    main()
