import sys


def countC(str1):
    counts = dict()
    for s in str1:
        if s in counts:
            counts[s] = counts[s] + 1
        else:
            counts[s] = 1
    return counts

def toAnagram(str1, str2):
    c1     = countC(str1)
    c2     = countC(str2)
    minRem = 0
    sunion = set(str1 + str2)
    for char in sunion:
        if char not in c1:
            minRem = minRem + c2[char]
        elif char not in c2:
            minRem = minRem + c1[char]
        else:
            minRem     = minRem + (max(c1[char], c2[char]) - min(c1[char], c2[char]))
    return minRem

if __name__ == '__main__':
    str1 = sys.stdin.readline().replace('\n', '')
    str2 = sys.stdin.readline().replace('\n', '')
    print toAnagram(str1, str2)
