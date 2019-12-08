
# 定義class


class TestIO:
    supportedSrcs = ["console", "file"]

    def read(src):
        if src not in TestIO.supportedSrcs:
            print("not supported")
        else:
            print("read from", src)


# 使用class
print(TestIO.supportedSrcs)
# print(TestIO.read("file"))
TestIO.read("file")
TestIO.read("internet")
