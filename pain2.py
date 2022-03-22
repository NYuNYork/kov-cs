def beker(nev):
    n = 0
    lista = []
    i = 1
    while(True):
        n = input("'" + nev + "' halmaz "+ str(i) +". eleme: ")
        if(n == ""):
            break
        if(n in lista):
            print("HIBA! a(z)", str(n), "már benne van a(z)'" + nev + "'halmazban!")
        else:
            lista.append(int(n))
            i += 1
    print("'" + nev + "' halmaz feltöltése befjeződött!\n")
    return lista


def metszet(A, B):
    return [value for value in A if value in B]

print("2. feladat:")

egyik = 'A'
masik = 'B'

alista = beker(egyik)
blista = beker(masik)

print("'" + egyik + "' halmaz elemei:", alista)
print("'" + masik + "' halmaz elemei:", blista)

met = metszet(alista, blista)
if(len(met)!= 0):
    print("'" + egyik + "' ∩ '" + masik +"':", met)
else:
    print("a két halmaz metszete üres halmaz")
