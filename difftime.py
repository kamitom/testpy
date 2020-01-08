

import datetime
from datetime import timedelta


def diffTest2():
    print("test2")
    dFormat = "%Y-%m-%d %H:%M:%S.%f"
    d1 = "2020-01-05 22:04:25.163"
    d2 = "2020-01-06 04:42:31.741"

    difftest = datetime.datetime.strptime(
        d2, dFormat) - datetime.datetime.strptime(d1, dFormat)

    print(difftest)


def namer(name=0.0392):
    print("ur name %f" % name)


# diffTest2()

def namer2(fName="TOM", lName="Scarlett"):
    return ("%s %s" % (fName, lName))


testname2 = namer2("Tom", "Ford")
print("MY NAME %s" % (testname2))

# for letter in testname2:
#     print(letter.upper())

if __name__ == "__main__":
    # print(__name__)
    # execute only if run as a script
    namer2()
