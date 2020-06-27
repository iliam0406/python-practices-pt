'''

boolan True or False

string "" or ''

number -1 1 1.0

None


list ["one", "two", "3"]

tuples ("one", "two", "3")

set {"one", "two", "3"}

dict {
    "name": "Luis"
}

class

class Prueba:


'''
#type(variable)

# and or not

a = 1
b = 2
c = 3

# ternario 
a = 4 if b > c else 5

if a > b :
    pass
else:
    pass

if a > b and a > c:
    pass
elif b > c:
    pass
else:
    pass


if a > b and a > c:
    if a > b and a > c:
        pass
    elif b > c:
        pass
    else:
        pass

elif b > c:
    pass
else:
    pass

# range(start, stop, step) start=0, step=1
for x in range(1, 11, 2):
    print(x) # 1, 3, 5, 7, 9

valores = ["one", "two", "3"]
for x in range(len(valores)): # 3 2
    print(valores[x]) # one, two, 3 


valores = ["one", "two", "3"] 
for x in valores:
    print(x) # one, two, 3


i = 0
while i < 10:
    print(i)
    i = i + 1

def prueba(a, b=5):
    pass

    def prueba2():
        pass


prueba = lambda a=5, b=5: a + b

prueba()

nombre = input("Ingresa tu nombre: ")

print(nombre)

edad = 38 
salario = 3.5
soltero = "False"

#str(edad)
#int(edad)
float(salario)
bool(soltero)

print("tu edad es " + str(edad))
print("tu edad es ", edad)

