import sys

def anToPal(string):
    stack = []
    for s in string:
        if s in stack:
            stack.remove(s)
        else:
            stack.append(s)
    if len(stack) > 1:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    string = sys.stdin.readline()
    print anToPal(string)
