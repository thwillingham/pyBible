import sys, json, readline
from pprint import pprint

class Pyble:
    def __init__(self):
        with open('ESV.json') as xfile:
            self._Bible = json.load(xfile)
        #pprint(self.Bible)

    def getBook(self, book):
        ret = {}
        d = list(self._Bible.get(book).keys())
        print(d)
        for key in sorted(d, key=lambda s: int(s)):
            ret[str(key)] = self._Bible[str(key)]
        return ret

    def getChapter(self, book, chapter):
        return self.getBook(book).get(chapter)

    def getVerse(self, book, chapter, verse):
        return self.getChapter(book, chapter).get(verse)

    def get(self, book, chapter, verse):
        if book and chapter and verse:
            return self.getVerse(book, chapter, verse)
        elif book and chapter:
            return self.getChapter(book, chapter)
        elif book:
            return self.getBook(book)
        else:
            return None


def main():
    s = getScripture(sys.argv)
    print(s)
    b = Pyble()
    x = b.get(s[0], s[1], s[2])
    #x = [None if b == "" else b for b in x]
    pprint(x)
    while (1):
        inp = input("pyble>")
        inpu = ["pyble"] + inp.split(" ")
        s = getScripture(inpu)
        print(s)
        b = Pyble()
        x = b.get(s[0], s[1], s[2])
        #x = [None if b == "" else b for b in x]
        pprint(x)


def getScripture(request):
    length = len(request);
    if length == 1: return [None, None, None]
    elif length == 2: return [request[1], None, None]
    elif length == 3:
        temp = request[2].split(":")
        if len(temp) > 1:
            return [request[1], temp[0], temp[1]]
        else: return [request[1], temp[0], None]


if __name__=='__main__':
    main()
