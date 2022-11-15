import pickle


def Comparacao(dicionario, m1, m2):

    # Primeiro critério: nota total
    soma1 = dicionario[m1][2][0] + dicionario[m1][2][1] + dicionario[m1][2][2]
    soma2 = dicionario[m2][2][0] + dicionario[m2][2][1] + dicionario[m2][2][2]
    if(soma1 > soma2):
        return True
    elif(soma1 < soma2):
        return False

    # Segundo critério: nota sem bônus


def main():
    with open("entradas/entrada10.bin", "rb") as f:
        dicionario = pickle.load(f)
        matriculas = list(dicionario.keys())
        print(matriculas)
        m1 = input()
        print(dicionario[m1][2][0] + dicionario[m1][2][1] + dicionario[m1][2][2])
if __name__ == "__main__":
    main()