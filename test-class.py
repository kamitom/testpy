
# 定義class


class TestIOCls:
    supportedSrcs = ["console", "file"]

    def readSrc(src):
        if src not in TestIOCls.supportedSrcs:
            print("not supported")
        else:
            print("read from", src)


# 使用class
print(TestIOCls.supportedSrcs)
# print(TestIO.read("file"))
TestIOCls.readSrc("file")
TestIOCls.readSrc("internet")
