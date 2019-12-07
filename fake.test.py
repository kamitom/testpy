from faker import Faker

faketTest = Faker("zh_TW")

for i in range(8):
    print("id: ", i)
    print("name: ", faketTest.name())
    print("addr: ", faketTest.address())
    print("text: ", faketTest.text())
