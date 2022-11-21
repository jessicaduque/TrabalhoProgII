import pickle

def mergeSort(lista, dicionario):
    if len(lista)>1:
        meio = len(lista)//2
        metadeEsquerda = lista[:meio]
        metadeDireita = lista[meio:]

        mergeSort(metadeEsquerda, dicionario)
        mergeSort(metadeDireita, dicionario)

        i=0
        j=0
        k=0
        
        while i < len(metadeEsquerda) and j < len(metadeDireita):
            if comparacao(dicionario, metadeEsquerda[i], metadeDireita[j]):
                lista[k]=metadeEsquerda[i]
                i=i+1
            else:
                lista[k]=metadeDireita[j]
                j=j+1
            k=k+1

        while i < len(metadeEsquerda):
            lista[k]=metadeEsquerda[i]
            i=i+1
            k=k+1

        while j < len(metadeDireita):
            lista[k]=metadeDireita[j]
            j=j+1
            k=k+1

def comparacao(dicionario, m1, m2):

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
        mergeSort(matriculas, dicionario)
    for a in matriculas:
        print(dicionario[a])

if __name__ == "__main__":
    main()