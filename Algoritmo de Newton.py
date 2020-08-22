pontosMax = int(input("Insira o numero total de pontos: "))
abcissa = []
ordenada = []
for i in range(pontosMax):
    abcissa.append(float(input("Insira a abcissa do ponto: " + str(i+1) + ".\n")))
    ordenada.append(float(input("Insira a ordenada do ponto: " + str(i+1) + ".\n")))
interPol = float(input("Insira o valor a interpolar: "))
r = 0
dely = []
for i in range(pontosMax):
    dely.insert(i,ordenada[i])
for k in range(1,pontosMax+1):
    for i in range(pontosMax-1,k,-1):
        dely[i] = (dely[i] - dely[i-1]) / (abcissa[i] - abcissa[i-k])
r = dely[pontosMax-1]
for i in range(pontosMax-1,0,-1):
    r = (r * (interPol - abcissa[i])) + dely[i]
print("O valor de: " + str(interPol) + " interpolado é: " + str(r) + " \n")