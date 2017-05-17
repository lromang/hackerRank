#! /usr/bin/python

import sys

def build_string():
    s = [0]
    k = 0
    while len(s) < 1000:
        k = k + 1
        t = [ 1 - i for i in s]
        s = s + t
    return s


if __name__ == '__main__':
    nqueries = int(sys.stdin.readline().replace('\n', ''))
    queries  = []
    for i in range(nqueries):
        queries.append(int(sys.stdin.readline().replace('\n', '')))
    s = build_string()
    for i in queries:
        print s[i]
