import sys
from pyble import Pyble
from pprint import pprint

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
