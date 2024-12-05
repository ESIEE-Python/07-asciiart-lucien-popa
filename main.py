"""
module pour ASCII
"""
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(2000)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant 
    une chaîne de caractères passée en 
    argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return[]

    #Si la liste est vide
    liste_caractere = [s[0]]
    liste_occurence = [1]

    for k in range(1,len(s)):
        if s[k] == s[k-1]:
            liste_occurence[-1] += 1
        else:
            liste_caractere.append(s[k])
            liste_occurence.append(1)

    return list(zip(liste_caractere, liste_occurence))


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne 
    de caractères passée en argument 
    selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []

    ocurrence = 1
    while ocurrence < len(s) and s[ocurrence] == s[0]:
        ocurrence += 1
    return [(s[0], ocurrence)] + artcode_r(s[ocurrence:])


#### Fonction principale


def main():
    """
    main
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))
    print(artcode_i('ESIEEPARISLALALALA'))
    print(artcode_r('ESIEEPARISLALALALA'))
    print(artcode_i('HelloWord'))
    print(artcode_r('HelloWord'))

if __name__ == "__main__":
    main()
