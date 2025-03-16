from ausdruck import Ausdruck

liste=[11,22,13,4]

# sort the list
liste.sort()
liste.reverse()
print(liste)

ausdruck_a = Ausdruck(ausdruck="Schwergewicht")
ausdruck_b = Ausdruck(ausdruck="Fliegengewicht")

ausdruck_a.like_hinzufuegen()
ausdruck_a.like_hinzufuegen()

liste = [ausdruck_a, ausdruck_b]
print(liste)
liste.sort()
print(liste)
print(ausdruck_a.likes)
print(ausdruck_b.likes)

