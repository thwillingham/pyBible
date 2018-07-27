import sys, json, readline
from pprint import pprint

class Pyble:
    def __init__(self):
        with open('ESV.json') as xfile:
            self._Bible = json.load(xfile)
            #pprint(self._Bible)

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

    def printSorted(self, scripture):
        ret = {}
        d = list(scripture.keys())
        for key in sorted(d, key=lambda s: int(s)):
            print(key)
            ret[str(key)] = self._Bible[str(key)]
            print(ret[str(key)])
        return ret

def main():
    s = getScripture(" ".join(sys.argv))
    bible = Pyble()
    x = bible.get(s[0], s[1], s[2])
    pprint(x)
    print(json.dumps(x, sort_keys=True, indent=4))
    while (1):
        request = raw_input("pyble>")
        s = getScripture(request)
        print(s)
        x = bible.get(s[0], s[1], s[2])
        #bible.printSorted(x)
        pprint(x)

def getScripture(request):
    request = request.split(" ")
    length = len(request);
    if length == 1: return [request[0], None, None]  # Mark
    elif length == 2:
        temp = request[1].split(":")
        if len(temp) > 1:
            return [request[0], temp[0], temp[1]]  # Mark 1:2
        else: return [request[0], temp[0], None]  # Mark 1
    elif length == 3: return [request[0], request[1], request[2]]  # Mark 1 2


if __name__=='__main__':
    main()
