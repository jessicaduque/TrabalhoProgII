import pickle


def Comparacao(dicionario, m1, m2):

    # Primeiro critério: nota total
    faltas1 = dicionario[m1][3]
    soma1 = dicionario[m1][2][0] + dicionario[m1][2][1] + dicionario[m1][2][2]
    if(faltas1 == 0):
        soma1 += 2
        if(soma1 > 100):
            soma1 = 100
    faltas2 = dicionario[m2][3]
    soma2 = dicionario[m2][2][0] + dicionario[m2][2][1] + dicionario[m2][2][2]
    if(faltas2 == 0):
        soma2 += 2
        if(soma2 > 100):
            soma2 = 100
    if(soma1 > soma2):
        return True
    elif(soma1 < soma2):
        return False

    # Segundo critério: nota sem bônus
    if(faltas1 == 0 and faltas2 > 0):
        return False
    elif(faltas2 == 0 and faltas1 > 0):
        return True

    # Terceiro critério: semestre letivo
    if(dicionario[m1][1][0] < dicionario[m2][1][0]):
        return True
    elif(dicionario[m1][1][0] > dicionario[m2][1][0]):
        return False
    else:
        if(dicionario[m1][1][1] < dicionario[m2][1][1]):
            return True
        elif(dicionario[m1][1][1] > dicionario[m2][1][1]):
            return False

    # Quarto critério: ordem alfabética
    nomes = [dicionario[m1][0], dicionario[m2][0]]
    nomesAlfa = sorted(nomes)
    if(nomes != nomesAlfa):
        return True
    else:
        if(nomes[0] != nomes[1]):
            return True

    # Quinto critério: matrícula
    matriculas = [int(m1[3:]), int(m2[3:])]
    if(matriculas[0] < matriculas[1]):
        return True
    else:
        return False

def main():
    with open("entradas/entrada10.bin", "rb") as f:
        dicionario = pickle.load(f)
        matriculas = list(dicionario.keys())
        m1 = dicionario[matriculas[0]]
        m2 = dicionario[matriculas[1]]
        nomes = sorted([m2[0], m1[0]])
        print(int(matriculas[1][3:]))
if __name__ == "__main__":
    main()