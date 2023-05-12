def read_grammar(gramatica_fisier):
    gramatica = []
    with open(gramatica_fisier) as file:
        for line in file:
            gramatica.append(line.strip())
    return gramatica

def verificaCuvant(gramatica, simbol, cuvant):
    if len(cuvant) == 0:
        for regula in gramatica:
            if regula[0] == simbol and regula[2] == "x":
                return True
        return False
    if len(cuvant) == 1:
        for regula in gramatica:
            if regula[0] == simbol and regula[2] == cuvant[0] and len(regula)<=3:
                return True
    for regula in gramatica:
        if regula[0] == simbol and regula[2] == cuvant[0] and len(regula)>3:
            if verificaCuvant(gramatica, regula[4], cuvant[1:]):
                return True
    return False

gramatica=read_grammar("gramatica.in")
simbol = 'S'
with open("date.out","w") as file2:
    with open("cuvinte.in","r") as file:
        for line in file:
            cuvant = line.strip()
            if verificaCuvant(gramatica, simbol, cuvant):
                file2.write(f"Cuvantul {cuvant} este acceptat.\n")
            else:
                file2.write(f"Cuvantul {cuvant} nu este acceptat.\n")
