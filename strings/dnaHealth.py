#! /bin/python

import sys

if __name__ == '__main__':
    ngenes = int(sys.stdin.readline())
    print(ngenes)
    genes  = [v.replace('\n', '') for v in sys.stdin.readline().split(' ')]
    print(genes)
    genesv = [ int(v) for v in sys.stdin.readline().split(' ')]
    print(genesv)
    nstran = int(sys.stdin.readline())
    print(nstran)
    strans = []
    for i in range(nstran):
        strans.append(sys.stdin.readline().replace('\n', ''))
        print(strans)
