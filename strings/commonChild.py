import sys

def remc(string, c):
    return ''.join(v for v in string if not v in c)

def counts(string):
    count = dict()
    for c in string:
        if c in count:
            count[c] = count[c] + 1
        else:
            count[c] = 1
    return count

def child(name1, name2):
    ## Counts of chars.
    ch1 = counts(name1)
    ch2 = counts(name2)
    ## Intersection
    inter = list(set(name1) & set(name2))
    for c in inter:
        print c



if __name__ == '__main__':
    name1 = sys.stdin.readline()
    name2 = sys.stdin.readline()
    print child(name1, name2)
