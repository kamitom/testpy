
from fibtest import fib
from cool import coolFunc
from singleproctest import download_task
from time import time
from faker import Faker
# from decoratetest import use_logging
from openfiletest import testopenfile


print("Call it remotely")
coolFunc()


for i in fib(3):
    print("test", i)

fake = Faker(['it_IT', 'en_US', 'ja_JP'])

start_time = time()
download_task(fake.name())
download_task(fake.name())
end_time = time()
print("total use %.2f秒" % (end_time - start_time))


testopenfile()
