#! /usr/bin/python

import sys

def toPalindrome(s):
    lens       = len(s)
    index      = -1
    rmismatches = lmismatches = 0
    leftFault   = rightFault  = 0
    for char in range(lens / 2):
        if s[char + lmismatches] != s[(lens - 1) - (char + rmismatches)]:
            if s[char + lmismatches + 1]  == s[(lens - 1) - (char + rmismatches)]:
                index      = char + lmismatches
                leftFault  = 1
            if s[(lens - 1) - (char + rmismatches + 1)] == s[char + lmismatches]:
                index      = (lens - 1) - (char + rmismatches)
                rightFault = 1
            if leftFault and rightFault:
                if s[(lens - 1) - (char + rmismatches + 2)] == s[char + lmismatches + 1]:
                    index      = (lens - 1) - (char + rmismatches)
                    rightFault = 1
                    leftFault  = 0
                if s[char + lmismatches + 2] == s[(lens - 1) - (char + rmismatches + 1)]:
                    index      = char + lmismatches
                    leftFault  = 1
                    rightFault = 0
            if (leftFault and rightFault) and (char + 1) == (lens / 2):
                index = char
                break
            ## Update indices
            rmismatches = rmismatches + rightFault
            lmismatches = lmismatches + leftFault
            char = char - 1
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
