#! /usr/bin/python

import sys

def toPal(num):
    mismatches   = []
    for i in range(len(num)/2):
        if num[i] != num[len(num) - 1 - i]:
            mismatches.append(i)
    return indices

def isPal(num):
    for i in range(len(num)/2):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True

def palNum(num, k):
    mismatch = toPal(num)
    if mismatch > k:
        return -1


if __name__ == '__main__':
    nk     = [int(v.replace('\n', '')) for v in sys.stdin.readline().split(' ')]
    number = [int(v) for v in list(sys.stdin.readline()) if v not in '\n']
