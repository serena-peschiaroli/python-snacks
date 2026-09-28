from collections import Counter

# Definisci una funzione che, prendendo in input due parole, verifica se le due parole sono anagrammi.


def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)


print(are_anagrams("strano", "nastro"))



#si può usare anche:


def are_anagrams_v_2(word1, word2):
    # Counter crea un dizionario tipo: {'c': 1, 'r': 1, 'o': 1, ...}
    return Counter(word1) == Counter(word2)