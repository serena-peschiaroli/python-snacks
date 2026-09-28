# Leggi una stringa in input all'interno di un loop. Se la stringa è uguale a "stop" interrompi il programma, altrimenti verifica se la stringa è un palindromo, in caso positivo stampa "PAROLA è un palidromo" inserendo la parola inserita in input al posto di PAROLA, altrimenti stampa " PAROLA non è un palindromo".

word = input("Inserisci una parola: ")
is_palindrome = True

i= 0
j = len(word) - 1

while word != "stop":
    while i < j:
        if word[i] != word[j]:
            is_palindrome = False
            break
        i += 1
        j -= 1

    if is_palindrome:
        print(f"{word} è un palindromo")
    else:
        print(f"{word} non è un palindromo")


