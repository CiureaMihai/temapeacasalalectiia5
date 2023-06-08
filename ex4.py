"""
Creaţi 2 liste: `elev1` şi `elev2`.

Pentru fiecare elev, cititi de la tastatură **numele**, **prenumele** şi **nota** obţinută la examen şi salvaţi datele în listele `elev1` şi `elev2`.

După aceasta, afişaţi la ecran:
* care dintre cei 2 elevi are o notă mai mare la examen (afişaţi numele şi prenumele)
* care dintre cei 2 elevi are o notă mai mică la examen (afişaţi numele şi prenumele)
* pentru fiecare elev, transformaţi numele sa fie scris cu toate literele majuscule, iar prenumele să înceapă cu literă mare. De exemplu, pentru elevul "Elon Musk", rezultatul afişat va fi "Elon MUSK"
*	afişaţi datele sub formă de tabel, folosind indexarea listelor, ca în exemplul de mai jos (Nu neaparat sa fie tabel):

| Elon | Musk | 9.5 |
|------|------|-----|
| Bill | Gates | 8.5|
"""

elev1 = []
elev2 = []


nume1 = input("Numele elevului 1: ")
prenume1 = input("Prenumele elevului 1: ")
nota1 = float(input("Nota elevului 1: "))


elev1.append(nume1.upper())
elev1.append(prenume1.capitalize())
elev1.append(nota1)


nume2 = input("Numele elevului 2: ")
prenume2 = input("Prenumele elevului 2: ")
nota2 = float(input("Nota elevului 2: "))


elev2.append(nume2.upper())
elev2.append(prenume2.capitalize())
elev2.append(nota2)


if nota1 > nota2:
    print("Elevul cu cea mai mare notă: ", elev1[1], elev1[0])
elif nota2 > nota1:
    print("Elevul cu cea mai mare notă: ", elev2[1], elev2[0])
else:
    print("Amândoi elevii au obținut aceeași notă.")


if nota1 < nota2:
    print("Elevul cu cea mai mică notă: ", elev1[1], elev1[0])
elif nota2 < nota1:
    print("Elevul cu cea mai mică notă: ", elev2[1], elev2[0])
else:
    print("Amândoi elevii au obținut aceeași notă.")


elev1[0] = elev1[0].upper()
elev2[0] = elev2[0].upper()
elev1[1] = elev1[1].capitalize()
elev2[1] = elev2[1].capitalize()


print("| {:<10} | {:<10} | {:<4} |".format("Nume", "Prenume", "Nota"))
print("|" + "-"*12 + "|" + "-"*12 + "|" + "-"*6 + "|")
print("| {:<10} | {:<10} | {:<4} |".format(elev1[0], elev1[1], elev1[2]))
print("| {:<10} | {:<10} | {:<4} |".format(elev2[0], elev2[1], elev2[2]))