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
        sorted_dict = {}
        if scripture == None:
            return
        elif type(scripture) != dict:
            print(scripture)
        else:
            keys = list(scripture.keys())
            for key in sorted(keys, key=lambda s: int(s)):
                intKey = int(key)
                if type(scripture[key]) != dict:
                    sorted_dict[intKey] = str(scripture[key])
                else:
                    sorted_dict[intKey] = {}
                    keys2 = list(scripture[key].keys())
                    for key2 in sorted(keys2, key=lambda s: int(s)):
                        intKey2 = int(key2)
                        sorted_dict[intKey][intKey2] = scripture[key][key2]
            pprint(sorted_dict)

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

def processMetaInput(request):
    if request in ["quit", "stop", "exit", "\q", "q"]:
        sys.exit(0)
    elif request in ["help", "--help", "h"]:
        print("""
              Usage: pyble> book [chapter [verse]]
                     pyble> book [chapter:verse]]
              """)
        return True

def main():
    s = getScripture(" ".join(sys.argv))
    bible = Pyble()
    x = bible.get(s[0], s[1], s[2])
    bible.printSorted(x)
    while (1):
        request = raw_input("pyble>")
        if processMetaInput(request):
            continue
        s = getScripture(request)
        x = bible.get(s[0], s[1], s[2])
        bible.printSorted(x)

if __name__=='__main__':
    main()
