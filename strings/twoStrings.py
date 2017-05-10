#! /usr/bin/python

import sys


def haveMatch(pair):
    str1 = pair[0]
    str2 = pair[1]
    minLen = min(len(str1), len(str2))
    for i in range(minLen):
        if str1[i] == str2[i]:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    npairs = int(sys.stdin.readline())
    spairs = []
    for i in range(npairs):
        pair = []
        pair.append(sys.stdin.readline().replace('\n', ''))
        pair.append(sys.stdin.readline().replace('\n', ''))
        spairs.append(pair)

    for pair in spairs:
        print haveMatch(pair)
