def swap(x,y):
    temp = x
    x = y
    y = temp
    return

s2 = []
e = [] 
d = []
abcissa = []
ordenada = []
Info = 0

pontosMax = int(input("Insira o numero total de pontos: "))
for i in range(pontosMax):
    abcissa.append(float(input("Insira a abcissa do ponto: " + str(i+1) + ".\n")))
    ordenada.append(float(input("Insira a ordenada do ponto: " + str(i+1) + ".\n")))
for i in range(1,pontosMax): #InsertionSort para sempre ordenar xD
    for j in range(i):
        if(abcissa[i] < abcissa[j]):
            swap(abcissa[i] , abcissa[j])
            swap(ordenada[i] , ordenada[j])
Ordenado = True
if(pontosMax < 3):
    Info = -1
    print("\nNumero de pontos menor que 3.\n")
    print("Info: " + str(Info))
    exit
for i in range(1,pontosMax):
    Ordenado = Ordenado and abcissa[i-1] < abcissa[i]
if(not Ordenado):
    Info = -2
    print("\nAbcissas não ordenadas.\n")
    print("Info: " + str(Info))
    exit
for i in range(pontosMax):
    s2.append(0)
m = pontosMax - 2
#Construção do sistema linear tridiagonal simétrico
Ha = abcissa[1] - abcissa[0]
Deltaa = (ordenada[1] - ordenada[0]) / Ha
for i in range(m):
    ip1 = i + 1
    ip2 = i + 2
    Hb = abcissa[ip2] - abcissa[ip1]
    Deltab = (ordenada[ip2] - ordenada[ip1]) / Hb
    e.insert(i,Hb)
    d.insert(i,(2 * (Ha + Hb)))
    s2[ip1] = 6 * (Deltab - Deltaa)
    Ha = Hb
    Deltaa = Deltab
#Eliminação de gauss
for i in range(1,m+1):
    ip1 = i + 1
    im1 = i - 1
    t = e[im1] / d[im1]
    d.insert(i, d[i-1] - (t * e[im1]) )
    s2[ip1] = (s2[ip1] - (t * s2[i-1]))  #arrumo um, aparece 10
#solução por substituições retroativas
s2[m] = (s2[m] / d[m-1]) # Problema
for i in range( m-1, 1, -1):
    ip1 = i + 1
    im1 = i - 1
    s2[i] = (s2[i] - (e[im1] * s2[ip1])) / d[im1]
s2[0] = 0
s2[pontosMax-1] = 0  
print("\nVetor de derivadas segundas:\n")
print(s2)
print("\nInfo: " + str(Info))