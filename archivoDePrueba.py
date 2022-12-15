a = 123
b = 123 + 123
c = 321 / 123
d = "hola"
e = "hOLa" * 3
f = "hola" + "buenas"
g = 123.123 * 123.321
h = False
i = True
j = (False or True and False) or (True and (True or False))
k = 4 ** 3
l = 5 % 2
m = 123 <= 3
print(a)
print(b)
print(c)
print(d)
print(e)
print(e.lower())
print(e.upper())
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)

if (h):
    print("este no es")
elif(j):
    print("este es")
else: 
    print("este no es")

if(j):
    print("este es")

if(j):
    print("este es")
else:
    print("este no es")

if(h):
    print("este no es")
else:
    print("este es")

aux = 0
while(aux <= 5):
    aux = aux + 1
    print(aux)

for element in range(5):
    print(element)

arreglo = [1,2,3,4]
arreglo2 = [[1,2,3],[1,2,3]]
arreglo3 = ["buenas", "tardes"]
arreglo4 = [[[1,2]],[[3,4]]]
print(arreglo)
print(arreglo2)
print(arreglo3)
print(arreglo4)
arreglo4[0][0][0] = 123
print(arreglo4)

for element in arreglo:
    print(element)

for element in arreglo3[1]:
    print(element)


def prueba():
    print("funcion prueba")

def pruebaParams(stringg):
    print(stringg)

def primos(maximo):
    for element in range(maximo):
        trigger = 0
        if element == 0 or element == 1:
            continue
        for i in range(element):
            if i == 0 : 
                continue
            resultado = element%i 
            if(resultado == 0):
                trigger = trigger + 1
        if trigger < 2:
            print(element)

prueba()
pruebaParams("hola buenas")
primos(100)

''' esperado
123
246
2.6097560975609757
hola
hOLahOLahOLa
holaholahola
HOLAHOLAHOLA
holabuenas
15183.651483
False
True
True
64
1
False
este es
este es
este es
este es
1
2
3
4
5
6
0
1
2
3
4
[1, 2, 3, 4]
[[1, 2, 3], [1, 2, 3]]
['buenas', 'tardes']
[[[1, 2]], [[3, 4]]]
[[[123, 2]], [[3, 4]]]
1
2
3
4
t
a
r
d
e
s
funcion prueba
hola buenas
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97 '''