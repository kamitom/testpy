

def testopenfile():
    f = open("a1.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()


if __name__ == "__main__":
    testopenfile()
