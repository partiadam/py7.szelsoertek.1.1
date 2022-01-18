'''
1.1 Feladat
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!

'''


szamok = []

while True:
    szoveg = input('Adj meg számokat: \t')
    if szoveg == "":
        break
    else:
        szam = int(szoveg)
    szamok.append(szoveg)

print(szamok)


#legkisebb
legkisebb = szamok[0]
for i in szamok:
    if i < legkisebb:
        legkisebb = i

print(f"A legkisebb szám: {legkisebb}")


#legnagyobb
legnagyobb = szamok[0]

for i in szamok:
    if i > legnagyobb:
        legnagyobb = i
print(f"A legnagyobb szám: {legnagyobb}")