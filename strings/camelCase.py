#! /bin/python

import sys
import re


if __name__ == '__main__' :
    line  = sys.stdin.readline()
    upper = re.split('[A-Z]', line)
    print(len(upper))
