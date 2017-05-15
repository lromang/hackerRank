#! /usr/bin/python

import sys

def minion_game(string):
    ## Store counts for substrings
    string = string.lower()
    con_sufix_bag = dict()
    con_sufix_tot = 0
    vow_sufix_bag = dict()
    vow_sufix_tot = 0
    ## Cons index
    cindex = [i for i in range(len(string)) if string[i] not in 'aeiou']
    ## Vowel index
    vindex = [i for i in range(len(string)) if string[i] in 'aeiou']
    ## Get Consonant substrings
    for ci in cindex:
        for chari in range(len(string)):
            ## If it's the individual char.
            if ci == chari:
                if string[ci] not in con_sufix_bag:
                    con_sufix_bag[string[ci]] = 1
                    con_sufix_tot = con_sufix_tot + 1
                else:
                    con_sufix_bag[string[ci]] = con_sufix_bag[string[ci]] + 1
                    con_sufix_tot = con_sufix_tot + 1
            ## If it's a consonant suffix
            if ci < chari:
                sufix_sub = string[ci:chari + 1]
                if  sufix_sub not in con_sufix_bag and sufix_sub in string:
                    con_sufix_bag[sufix_sub] = 1
                    con_sufix_tot = con_sufix_tot + 1
                elif sufix_sub in con_sufix_bag and sufix_sub in string:
                    con_sufix_bag[sufix_sub] = con_sufix_bag[sufix_sub] + 1
                    con_sufix_tot = con_sufix_tot + 1
    for vi in vindex:
        for chari in range(len(string)):
            ## If it's the individual char.
            if vi == chari:
                if string[vi] not in vow_sufix_bag:
                    vow_sufix_bag[string[vi]] = 1
                    vow_sufix_tot = vow_sufix_tot + 1
                else:
                    vow_sufix_bag[string[vi]] = vow_sufix_bag[string[vi]] + 1
                    vow_sufix_tot = vow_sufix_tot + 1
            ## If it's a vowel suffix
            if vi < chari:
                sufix_sub = string[vi:chari + 1]
                if  sufix_sub not in vow_sufix_bag and sufix_sub in string:
                    vow_sufix_bag[sufix_sub] = 1
                    vow_sufix_tot = vow_sufix_tot + 1
                elif sufix_sub in vow_sufix_bag and sufix_sub in string:
                    vow_sufix_bag[sufix_sub] = vow_sufix_bag[sufix_sub] + 1
                    vow_sufix_tot = vow_sufix_tot + 1
    ## Get vowels substrings
    if vow_sufix_tot > con_sufix_tot:
        print 'Kevin ' + str(vow_sufix_tot)
    elif con_sufix_tot > vow_sufix_tot:
        print 'Stuart ' + str(con_sufix_tot)
    else:
        print 'Draw'


if __name__ == '__main__':
    string = raw_input()
    minion_game(string)
