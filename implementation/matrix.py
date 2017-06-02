#! /bin/python

import sys


def diagSum(matrix, n):
    pdiag = 0
    adiag = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                pdiag = pdiag + matrix[i][j]
            if (n - 1) - i == j:
                adiag = adiag + matrix[i][j]
    return abs(pdiag - adiag)

if __name__ == '__main__':
    dim = int(sys.stdin.readline().replace('\n', ''))
    mat = []
    for i in range(dim):
        mat.append([int(x.replace('\n', '')) for x in sys.stdin.readline().split(' ')])
    print diagSum(mat, dim)
