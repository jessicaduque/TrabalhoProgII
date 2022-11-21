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

def buscaBinariaAdaptada(lista, dicionario):
    max = len(lista) - 1
    min = 0
    while max >= min:
        meio = ((max + min) // 2)

        if(dicionario[lista[meio]][3] == 0):
            bonus = 2
        else:
            bonus = 0
        pontos1 = dicionario[lista[meio]][2][0] + dicionario[lista[meio]][2][1] + dicionario[lista[meio]][2][2] + bonus
        
        if(dicionario[lista[meio + 1]][3] == 0):
            bonus = 2
        else:
            bonus = 0
        pontos2 = dicionario[lista[meio + 1]][2][0] + dicionario[lista[meio + 1]][2][1] + dicionario[lista[meio + 1]][2][2] + bonus
        
        if(pontos1 < 60 and pontos2 > 60):
            print(dicionario[lista[meio + 1]][0])
            return len(lista[meio + 1:])

        if(pontos1 == 60):
            print(dicionario[lista[meio]][0])
            return len(lista[meio:])

        if(pontos1 < 60):
            min = meio + 1

        else:
            max = meio - 1
    return len(lista)

def criarArquivo(matriculas, dicionario):

def main():
    with open("entradas/entrada100.bin", "rb") as f:
        dicionario = pickle.load(f)
        f.close()
    matriculas = list(dicionario.keys())
    mergeSort(matriculas, dicionario)
    criarArquivo(matriculas, dicionario)
    print(buscaBinariaAdaptada(matriculas[::-1], dicionario))

if __name__ == "__main__":
    main()