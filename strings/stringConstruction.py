#! /usr/bin/python

import sys


def copyS(string):
    if string == '':
        return 0
    costs    = []
    p        = string[0]
    costs.append(1)
    for index in range(len(string))[1:]:
        if string[index] in p:
            costs.append(costs[index - 1])
        else:
            costs.append(costs[index - 1] + 1)
        p = p + string[index]
    return costs[-1]


if __name__ == '__main__':
    nstrings = int(sys.stdin.readline())
    strings  = []
    for i in range(nstrings):
        strings.append(sys.stdin.readline().replace('\n', ''))
    for s in strings:
        print copyS(s)
