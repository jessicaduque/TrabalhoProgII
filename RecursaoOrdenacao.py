import pickle

with open("entradas/entrada10.bin", "rb") as f:
    dicionario = pickle.load(f)
    matriculas = list(dicionario.keys())
    print(matriculas)