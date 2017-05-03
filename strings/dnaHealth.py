#! /bin/python

import sys
from operator import itemgetter

def getInstances(string1, string2):
    if len(string1) > len(string2):
        return 0
    instances = 0
    visited   = 0
    while len(string1) + visited <= len(string2):
        match     = 1
        for k in range(len(string1)):
            if string1[k] != string2[k + visited]:
                match = 0
                break
        if match:
            instances = instances + 1
        visited = visited + 1
    return instances


def getValue(genes, genesv, stran):
    start = int(stran[0])
    end   = int(stran[1]) + 1
    genesInt  = list(itemgetter(*range(end)[start:])(genes))
    valuesInt = list(itemgetter(*range(end)[start:])(genesv))
    value = 0
    for gene in zip(genesInt, valuesInt):
        instances = getInstances(gene[0], stran[2])
        value     = value + instances*gene[1]
    return value

def minMax(genes, genesv, strans):
    health = []
    for stran in strans:
        health.append(getValue(genes, genesv, stran))
    return min(health), max(health)

if __name__ == '__main__':
    ngenes = int(sys.stdin.readline())
    genes  = [v.replace('\n', '') for v in sys.stdin.readline().split(' ')]
    genesv = [ int(v) for v in sys.stdin.readline().split(' ')]
    nstran = int(sys.stdin.readline())
    strans = []
    for i in range(nstran):
        strans.append([v.replace('\n', '') for v in sys.stdin.readline().split(' ')])
    minVal, maxVal = minMax(genes, genesv, strans)
    print(str(minVal) + ' ' + str(maxVal))
