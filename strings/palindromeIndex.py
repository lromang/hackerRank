#! /usr/bin/python

import sys

def toPalindrome(s):
    lens       = len(s)
    index      = -1
    rmismatches = lmismatches = 0
    for char in range(lens/2):
        if s[char + lmismatches] != s[(lens - 1) - (char + rmismatches)]:
            if s[char + lmismatches + 1]  == s[(lens - 1) - (char + rmismatches)]:
                index       = char
                lmismatches = lmismatches + 1
                char        = char - 1
            elif s[(lens - 1) - (char + 1)] == s[char + lmismatches]:
                index       = (lens - 1) - (char)
                rmismatches = rmismatches + 1
                char        = char - 1
        if lmismatches + rmismatches > 1:
            return -1
    return index



if __name__ == '__main__':
    palindromes = []
    n = int(sys.stdin.readline())
    for chain in range(n):
        palindromes.append(sys.stdin.readline().replace('\n', ''))

    for chain in palindromes:
        print(toPalindrome(chain))
