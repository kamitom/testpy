
def hello(msg="lufy"):
    print("hello: ", msg)


test = str(input("your NAME: "))
valueTest = hello()
print("none? ", valueTest)

# hello()


def addUs(n1, n2):
    result = n1 + n2
    return "Hello..."


print(addUs(100, 200))


def addUs(max):
    sum = 0
    for xx in range(1, max+1):
        sum += xx
    return sum


targetNumber = int(input("累加到: "))
print(addUs(targetNumber))
