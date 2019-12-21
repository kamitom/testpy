
from cool import coolFunc

a, b = 0, 1


print(a)

# coolFunc()


def fib(n):
    a1, b1 = 0, 1
    for _ in range(n):
        a1, b1 = b1, a1 + b1
        yield a1


def main():
    for val in fib(8):
        print(val)


if __name__ == "__main__":
    main()
