import sys
import re
N = int(sys.argv[1])
input = sys.argv[2]

def print_puzzle(puz):
    for row in range(0,N):
        print puz[row]


def read_input():
    f = open(input, 'r')
    puz = [[' '] * N for i in range(N)]
    row = 0
    for line in f:
        line = '12 . 3 . 0 . . 15 . . . . . . 1 2'
        entries = re.findall('\.|\d+ |\d',line)
        new = []
        for e in entries:
            e = e.strip()
            new.append(e)
        #print new
        if new != []:
            puz[row] = new
            row += 1
    print_puzzle(puz)
    return puz

read_input()
