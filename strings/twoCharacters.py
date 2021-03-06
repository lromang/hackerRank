#! /usr/bin/python

import sys
import operator

## Remove Character
def remChar(s, c):
    s = ''.join(char for char in s if char != c)
    return s

## Remove repetitions
def remReps(s):
    while 1:
        for i in (range(len(s))[1:]):
            lens = len(s) - 1
            if s[i] == s[i - 1]:
                s = remChar(s, s[i])
                break
        if i == lens:
            return s

## Checks Duplicates.
def checkDup(s):
    for i in range(len(s))[1:]:
        if s[i] == s[i - 1]:
            return True
    return False

#### Get Pairs
def getPairs(s):
    counts = dict()
    pairs  = dict()
    for c in s:
        instances = 0
        for char in s:
            if char == c:
                instances = instances + 1
        counts[c] = instances
    ## Dic of pairs
    for i in counts.keys():
        for j in counts.keys():
            if i != j:
                pairs[i + j] = counts[i] + counts[j]
    return sorted(pairs.items(), key=operator.itemgetter(1), reverse = True)

def maxAltern(s):
    ## Get pairs
    pairs  = getPairs(s)
    ## Max length sofar
    maxLength = - 1
    for pair in pairs:
        s_aux = ''.join(char for char in s if char in pair[0])
        if not checkDup(s_aux):
            return pair[1]
    return 0

if __name__ == "__main__":
    line = sys.stdin.readline()
    print(line)
