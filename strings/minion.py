#! /usr/bin/python

import sys

def minion_game(string):
    ## Store counts for substrings
    string = string.lower()
    con_sufix_bag = dict()
    vow_sufix_bag = dict()
    ## Cons index
    cindex = [i for i in range(len(string)) if string[i] not in 'aeiou']
    ## Vowel index
    vindex = [i for i in range(len(string)) if string[i] in 'aeiou']
    ## Iterate consonants
    if len(cindex) != 0:
        ## Base case
        con_sufix_bag[cindex[-1]] = len(string) - cindex[-1]
        for ci in reversed(range(len(cindex))[:-1]):
            con_dist                  = cindex[ci + 1] - cindex[ci]
            con_sufix_bag[cindex[ci]] = con_sufix_bag[cindex[ci + 1]] + con_dist
    ## Iterate vowels
    if len(vindex) != 0:
        ## Base case
        vow_sufix_bag[vindex[-1]] = len(string) - vindex[-1]
        for vi in reversed(range(len(vindex))[:-1]):
            vow_dist                  = vindex[vi + 1] - vindex[vi]
            vow_sufix_bag[vindex[vi]] = vow_sufix_bag[vindex[vi + 1]] + vow_dist
    ## Sum all
    vow_sufix_tot = sum(vow_sufix_bag.values())
    con_sufix_tot = sum(con_sufix_bag.values())
    ## Get vowels substrings
    if vow_sufix_tot > con_sufix_tot:
        print 'Kevin '  + str(vow_sufix_tot)
    elif con_sufix_tot > vow_sufix_tot:
        print 'Stuart ' + str(con_sufix_tot)
    else:
        print 'Draw'

if __name__ == '__main__':
    string = raw_input()
    minion_game(string)
