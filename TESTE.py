
# PARA COMPARAR E TESTAR
f = open("saidas/saida100000.txt", "r", errors="ignore")
linhasHil = f.readlines()
f.close()
f = open("saida.txt", "r", errors="ignore")
linhasNosso = f.readlines()
f.close()
print(linhasHil == linhasNosso)