import sys


def anagram(string):
    '''
    Observación clave:
    Si no hay anagramas de longitud uno,
    no hay anagramas de longitud mayor a
    uno con esa letra.
    '''
    anagrams = dict()
    moreTone = 0
    for c in string:
        if c in anagrams:
            anagrams[c] = anagrams[c] + 1
            moreTone    = moreTone    + 1
        else:
            anagrams[c] = 1

    return anagrams


if __name__ == '__main__':
    line = sys.stdin.readline()
