with open("automat.txt", "r") as f:
    stare_initiala = 'q0'
    tranzitii = {}
    stari_acceptate = []
    stari_finale = []
    cuvant = ''
    lines=f.readlines()
    ok=1
    for line in lines:
        if ok<=len(lines)-2:
            q1, simbol, q2 = line.strip().split()
            tranzitii[(q1, simbol)] = q2
            stari_acceptate.append(q2)
            stari_acceptate.append(q1)
            ok+=1
        else:
            if ok==len(lines)-1:
                for q in line.strip().split():
                    stari_finale.append(q)
                ok=len(lines)
            else:
                cuvant = line.split()
        stari_acceptate = set(stari_acceptate)
        stari_acceptate = list(stari_acceptate)
        stari_finale = set(stari_finale)
        stari_finale = list(stari_finale)

def DFA(cuvant):
    drumul_parcurs = []
    stare_curenta = stare_initiala
    cuvant = list(cuvant[0])
    for litera in cuvant:
        if (stare_curenta, litera) not in tranzitii:
            return False
        drumul_parcurs.append(stare_curenta)
        stare_curenta = tranzitii[(stare_curenta, litera)]
    if stare_curenta in stari_finale:
        drumul_parcurs.append(stare_curenta)
        return drumul_parcurs
    else:
        return False

with open("final.txt", "w") as f:
    if cuvant == []:
        if 'q0' in stari_finale:
            f.write("Acceptat")
        else:
            f.write("Neacceptat")
    else:
        if DFA(cuvant) == False:
            f.write("Neacceptat")
        else:
            f.write("Acceptat")
            f.write("\n")
            raspuns=DFA(cuvant)
            for r in raspuns:
                f.write(r)
                f.write(" ")
