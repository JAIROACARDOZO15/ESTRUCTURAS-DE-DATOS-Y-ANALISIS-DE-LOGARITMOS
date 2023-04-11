# Problema 2
# A partir de una frase si el número 

frase = input("Digite frase por favor: ")
x = []
x = frase.split(" ")
while len(x)<= 9:
    print("Frase debe tener mas de 9 palabras")
    frase = input("Digite frase por favor: ")
    x = frase.split(" ")

acu = ""
for i in range(len(x)):
    if i%2==0:
        x[i]="X"
    acu = acu + x[i] + " "
print(x)
print(acu)