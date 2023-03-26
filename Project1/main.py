with open("automat.txt", "r") as f:
    stare_initiala = 'qo'
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

print("Cuvantul este")
print(cuvant)
print("starile finale")
print(stari_finale)
print("stari sunt:")
print(stari_acceptate)
print(tranzitii)
