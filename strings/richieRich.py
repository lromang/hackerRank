#! /usr/bin/python

import sys

def toPal(num):
    mismatches   = []
    for i in range(len(num)/2):
        if num[i] != num[len(num) - 1 - i]:
            mismatches.append(i)
    return mismatches

def isPal(num):
    for i in range(len(num)/2):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True

def palNum(num, k):
    mismatch = toPal(num)
    if len(mismatch) > k:
        return -1
    ## Advantage, you can take the greedy step!
    ## only need to focus on the first index of mismatch!
    palIndex = 0
    while k > 0:
        ## If we can change both digits.
        ## and neither of does is 9, make two replacments for 9
        if len(mismatch) > 0:
            if (k - 2) >= len(mismatch) and \
               (num[mismatch[0]] != 9 and num[len(num) - 1 - mismatch[0]] !=9):
                num[mismatch[0]] = 9
                num[len(num) - 1 - mismatch[0]] = 9
                mismatch.pop(0)
                k = k - 2
            else:
                ## If we only can make one change or
                ## one of the digits is 9, make one replacement
                ## for the largest possible number
                replace = mismatch[0] if num[mismatch[0]] <= \
                          num[len(num) - 1 - mismatch[0]] else  len(num) - 1 - mismatch[0]
                num[replace] = max(num[mismatch[0]], \
                                   num[len(num) - 1 - mismatch[0]])
                mismatch.pop(0)
                k = k - 1
        else:
            if palIndex > (len(num) / 2):
                return num
            if k >= 2 and num[palIndex] != 9:
                num[palIndex] = 9
                num[len(num) - 1 - palIndex] = 9
                k = k - 2
                palIndex = palIndex + 1
            if (len(num) % 2 == 1) and (palIndex == (len(num)/2)) and k == 1:
                num[palIndex] = 9
                k = k - 1
                palIndex = palIndex + 1
            palIndex = palIndex + 1
    return num

if __name__ == '__main__':
    nk     = [int(v.replace('\n', '')) for v in sys.stdin.readline().split(' ')]
    number = [int(v) for v in list(sys.stdin.readline()) if v not in '\n']
