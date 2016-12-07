import sys, json
from pprint import pprint

class Pyble:
    def __init__(self):
        with open('ESV.json') as xfile:
            self._Bible = json.load(xfile)
        #pprint(self.Bible)

    def getBook(self, book):
        return self._Bible.get(book)

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
