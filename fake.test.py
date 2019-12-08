from faker import Faker
import random
import sys
import sys as s

faketTest = Faker("zh_TW")

for i in range(2):
    print("id: ", i)
    print("name: ", faketTest.name())
    print("addr: ", faketTest.address())
    print("text: ", faketTest.text())


print(sys.platform)
print(sys.maxsize)
print(s.path)
