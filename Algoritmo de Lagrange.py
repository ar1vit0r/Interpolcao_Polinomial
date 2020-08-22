pontosMax = int(input("Insira o numero total de pontos: "))
abcissa = []
ordenada = []
for i in range(pontosMax):
    abcissa.append(float(input("Insira a abcissa do ponto: " + str(i+1) + ".\n")))
    ordenada.append(float(input("Insira a ordenada do ponto: " + str(i+1) + ".\n")))
interPol = float(input("Insira o valor a interpolar: "))
r = 0
for i in range(pontosMax):
    c = 1
    d = 1
    for j in range(pontosMax):
        if i != j:
            c = c * (interPol - abcissa[j])
            d = d * (abcissa[i] - abcissa[j])
    r = r + ordenada[i] * (c/d)
print("O valor de: " + str(interPol) + " interpolado é: " + str(r) + " \n")