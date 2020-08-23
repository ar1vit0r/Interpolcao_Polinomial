pontosMax = int(input("Insira o numero total de pontos: "))
abcissa = []
ordenada = []
sumx = 0
sumy = 0
sumxy = 0
sumx2 = 0
st = 0
sr = 0
for i in range(pontosMax):
    abcissa.append(float(input("Insira a abcissa do ponto: " + str(i+1) + ".\n")))
    ordenada.append(float(input("Insira a ordenada do ponto: " + str(i+1) + ".\n")))
for i in range(pontosMax):
    sumx = sumx + abcissa[i]
    sumy = sumy + ordenada[i]
    sumxy = sumxy + abcissa[i] * ordenada[i]
    sumx2 = sumx2 + abcissa[i] * abcissa[i]
xm = sumx / pontosMax
ym = sumy / pontosMax
a1 = (pontosMax * sumxy - sumx * sumy) / (pontosMax * sumx2 - sumx * sumx)
a0 = ym - a1 * xm
for i in range(pontosMax):
    st = st + (ordenada[i] - ym)**2 
    sr = sr + (ordenada[i] - a1 * abcissa[i] - a0)**2
syx = (sr / (pontosMax - 2))**0.5
r2 = (st - sr) / st
print("\n syx: " + str(syx))
print("\n r2: " + str(r2))
print("\n")