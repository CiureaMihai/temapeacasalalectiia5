"""Cititi de la utilizator, o lista de nume, separate prin virgula.

Folosind metoda `.split()` transformati textul de la utilizator intr-o lista de nume.

Pentru fiecare nume cititi nota introdusa de utilizator (numar intreg). Adaugati nota in lista `list_of_marks`.

Apoi:
* afișați pentru fiecare nume, nota care îi aparține.
* calculați suma notelor
* calculați media notelor


Completati campurile din ___ si adaugati codul necesar.

Note: Utilizati indiciele numelui pentru a afla nota dupa indice din `list_of_marks`.
"""

names = input("Introduceti o lista de nume, separate prin virgula: ")
list_of_names = names.split(",")

list_of_marks = []

for name in list_of_names:
    mark = int(input(f"Introduceti nota pentru {name}: "))
    list_of_marks.append(mark)

# Afisarea notelor
for i in range(len(list_of_names)):
    name = list_of_names[i]
    mark = list_of_marks[i]
    print(f"Nota pentru {name}: {mark}")

marks_sum = sum(list_of_marks)
print(f"Suma notelor: {marks_sum}")
print(f"Media notelor: {marks_sum / len(list_of_marks)}")
