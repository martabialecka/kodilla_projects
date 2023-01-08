"""Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) 
i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
Podpowiedź
Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji, 
które pozwalają odnosić się do elementów indeksowanych od początku i od końca.
Do zadania dodaj krótką dokumentację i umieść je w zdalnym repozytorium."""
def palindrome (str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
my_string = "kajak"
ans = palindrome (my_string) 
print(ans)
