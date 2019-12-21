

import logging


def use_logging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()
    return wrapper


@use_logging
def foo(testN1):
    print("this is foo")


if __name__ == "__main__":
    foo("100test")
