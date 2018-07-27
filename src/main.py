import sys 
from Pyble import Pyble

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
