#Ora;  Perc;   AdasDb;   Nev
#  0     1        2        3
#6;0;2;Laci

class Cb:
    def __init__(self, sor):
        s = sor.strip().split(';')
        self.ora  = int(s[0])
        self.perc = int(s[1])
        self.db   = int(s[2])
        self.nev  =     s[3]

#Előkészületek
with open("cb.txt", 'r', encoding='UTF-8-sig') as f:
    fejlec = f.readline()
    matrix = [Cb(sor) for sor in f]

#3. feladat
print(f' 3. feladat: Bejegyzések száma: {len(matrix)} db.')

# 4. feladat
for sor in matrix:
    if sor.db == 4:
        print(f' 4. feladat: Volt 4 adást indító sofőr!')
        break
    
#5. feladat
sofor = input(f' 5. feladat: Kérek egy nevet: ')
adas = 0
van = False

for sor in matrix:
    if sor.nev == sofor:
        adas = adas + sor.db
        van = True
if van:
    print(    f'         {sofor} {adas}x használta a CB rádiót.')
else:
    print(    f'         Nincs ilyen nevű sofőr!')

#6. feladat
def AtszamolPercre(ora, perc):
    return ora * 60 + perc

#7.  feladat

cb2fejlec = 'Kezdes;Nev;AdasDb\n'
with open('cb2.txt', 'w', encoding='UTF-8') as fout:
#    fout.write(cb2fejlec)
    print(cb2fejlec, end='', file=fout)
    for sor in matrix:
        perc   = AtszamolPercre(sor.ora, sor.perc)
        nev    = sor.nev
        darab  = sor.db
        szoveg = f'{perc};{nev};{darab}\n'
#       fout.write(szoveg)
        print(szoveg, end='', file=fout)

#8. feladat

halmaz = set()
for sor in matrix:
    halmaz.add(sor.nev)
print(f' 8. feladat: Sofőrök száma: {len(halmaz)} fő.')

#9. feladat

szotar = {}
for sor in matrix:
    szotar[sor.nev] = 0

for sor in matrix:
    szotar[sor.nev] += sor.db

nev, db = sorted(szotar.items(), key=lambda x:x[1], reverse=True)[0]
print(f' 9. feladat: A legtöbb adást indító sofőr:')
print(f'         Név: {nev}')
print(f'         Adások száma: {db} alkalom')
        