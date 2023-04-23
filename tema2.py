#FUNCTIA PENTRU A CALCULA INCHIDERI LAMBDA
def lambdaInchidere(stari, nfa):
    inchideri = set(stari) #aceasta va fi practic lista cu starile inchiderii
    while True: #lucram cat timp putem ajunge cu lambda undeva
        creataAcum = set()  #aceasta va fi lista inchiderilor pentru fiecare stare in parte
        for pozitie in inchideri:
            creataAcum |= set(nfa.get(pozitie, {}).get('x', []))   #returnează o listă cu toate stările accesibile prin tranziții lambda din starea "pozitie" si apoi face unirea cu ce aveam dinainte
        creataAcum -= inchideri  #eliminam duplicate
        if not creataAcum: #daca nu mai putem ajunge cu lambda undeva ne oprim
            break
        inchideri |= creataAcum #adaugam inchiderea
    return sorted(list(inchideri))  # o sortam pentru a fi mai usor de parcurs

#FUNCTII DE TRANSFORMARE NFA IN DFA
def nfa_to_dfa(nfa,prima,alfabet):
    # Initialize start state and queue
    initial = sorted(lambdaInchidere([prima], nfa))  #cream lambda inchiderea pt prima stare, ca sa putem pleca din ea
    lista = [initial]  #adaugam prima inchidere in lista in care avem toate starile de parcurs in prelucrare
    drum = set() #starile deja prelucrate
    dfa = {}

    while lista: #lucram in lista pana nu mai avem stari de parcurs
        stare = lista.pop(0)  #ne luam starea de prelucrat din lista
        if tuple(stare) in drum:  #daca nu am ajuns pe ea trebuie prelucrata
            continue
        drum.add(tuple(stare))  #o adaugam in drum sa stim pe unde am mers
        dfa[tuple(stare)] = {}  #cream linia din matrice pentru starea in care ne aflam
        for litera in alfabet:  #doar trecem prin fiecare stare din alfabet ca sa aflam urmatoarea mutare
            urmatoarea = set()
            for nfa_state in stare:
                urmatoarea |= set(nfa.get(nfa_state, {}).get(litera, []))  #punem in urmatoarea stare toate starile din nfa care pleaca cu litera respectiva
            lambdamutare = sorted(lambdaInchidere(urmatoarea, nfa)) #cautam si mutarile cu lambda
            if tuple(lambdamutare) not in drum:  #daca nu am trecut prin starile urmatoare deja cu prelucarea le adaugam in lista
                lista.append(lambdamutare)
            dfa[tuple(stare)][litera] = tuple(lambdamutare) #nu uitam sa adaugam mutarea si cu lambda la mutarile starii
    return dfa

#FUNCTIA DE AFISARE
def afis_dfa(dfa, filename, finale):
    with open(filename, 'w') as file:
        initial = next(iter(dfa)) #ne scoatem starea initiala din dfa ca sa o afisam
        file.write(f"STARE INITIALA: {initial}\n\n")

        finale2 = [stare for stare in dfa if any(x in stare for x in finale)]  #trebuie sa parcurgem starile finale initiale si cele din dfa si le afisam doar pe acelea care le includ pe cele finale initial
        file.write(f"STARI FINALE: {', '.join(str(stare) for stare in finale2)}\n\n")

        for stare in dfa: #accesam fiecare stare si daca e diferita de multimea vida ii afisam mutarile
            if stare != ():
                for litera in dfa[stare]: #parcurgem matricea si formatam output-ul
                    starea_in_care_mergem = dfa[stare][litera]
                    file.write(f"{stare} --({litera})--> {starea_in_care_mergem}\n")
                file.write("\n")


######################################################################### DE AICI INCEPE MAIN-UL

nfa={} #declaram NFA
alfabet=('a', 'b', 'c')
with open('input.txt') as file:
    initial = file.readline().strip()  #citim starea initiala
    finale = file.readline().strip().split() #citim starile finale
    for line in file:   #fiecare linie citita o prelucram
        line = line.strip().split(' ')
        prima, litera, adoua = line  #vom crea practic o matrice
        if litera == 'lambda': #inlocuim lambda cu x ca sa ne fie mai usor
            litera = 'x'
        if prima not in nfa:  #daca nu exista o cream
            nfa[prima] = {}
        if litera not in nfa[prima]: #daca exista in NFA, dar nu ca simbol, o cream
            nfa[prima][litera] = [adoua]
        else:
            nfa[prima][litera] += [adoua] #daca exista in NFA si exista ca si simbol, doar adaugam inca o data

dfa= nfa_to_dfa(nfa,initial,alfabet)  #aplicam functia pentru a afla DFA-ul
afis_dfa(dfa, 'output.txt',finale)  #aplicam functia pentru a afisa DFA-ul