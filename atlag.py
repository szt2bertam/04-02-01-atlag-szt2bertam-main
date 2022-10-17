# osszeg-gyak.py

# 1. feladat
# Határozza meg a számok átlagát!
def feladat01_atlag() -> int:
    szamok = [1.2, 2.3, 3.2, 4.1, 2.4, 2.3, 1.9, 0.1]
    atlag = sum(szamok) / len(szamok)
    return atlag

# 2. feladat
# Határozza meg a diák jegyeinek átlagát két tizedes jegy pontossággal!
def feladat02_osszeg() -> int:
    szamok = [5, 3, 2, 4, 4, 3, 5, 5]
    atlag = sum(szamok) / len(szamok)
    return round(atlag,2)

# 3. feladat
# Határozza meg a páratlan számok átlagát három tizetedes jegy pontossággal!
def feladat03_osszeg() -> int:
    szamok = [2, 3, 4, 7, 1, 8, 6, 1, 2, 3, 7, 2, 2, 9, 6, 6]
    atlag = sum(szamok) / len(szamok)
    for szam in szamok:
        if szam % 2 == 1:
            atlag = atlag + szam
    return round(atlag,3)

# 4. feladat
# Határozza meg az első számsorozat páros számainak átlagát!
# Határozza meg az második számsorozat páratlan számainak átlagát!
# A függvény adja vissza a nagyobb átlagot!
def feladat04_osszeg() -> int:
    szamok1 = [2, 3, 4, 6, 1, 8, 6, 1]
    szamok2 = [3, 2, 4, 1, 5, 4, 7, 0]
    szamok1atlag = sum(szamok1)/len(szamok1)

    return 0
