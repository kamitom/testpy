from faker import Faker
import random
import sys
import sys as s

fakerTest2 = Faker("zh_TW")

for i in range(2):
    print("id: ", i)
    print("name: ", fakerTest2.name())
    print("addr: ", fakerTest2.address())
    # print("text: ", fakerTest2.text())


print(sys.platform)
print(sys.maxsize)
print(s.path)
