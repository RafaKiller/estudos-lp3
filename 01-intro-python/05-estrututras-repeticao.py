#for, while, break, continue

#operador in



for letra in "Python":
    print(letra)
    
itens = ["banana", "arroz", "limão"]
alunos = ["Rony rustico", "PanPan"]

for item in itens:
        print(item)

for i in range(5):
        print(i)

for i in range(0,11,2):
        print(i) #0, 2, 4, 6, 8, 10

lista = list(range(101))
print(type(lista))
    
contador = 0
while contador <= 5:
        print(contador)
        contador += 1

numeros = [1,3,4,5,8,11]

for numero in numeros:
       if numero % 2 == 0:
              print(numero)
              break
numero = [3, -1, 3, 0, -2]
for numero in numeros:
       if numeros <= 0:
            continue
       print(numero)

numeros = [2,3,4,5,6] 
quadrado = []

for numero in numeros:
       quadrado.append(numero** 2)
    
quadrados = [numero ** 2 for numero in numeros] 

palavra = 'Oĺa Mundo'
letras = [letra.upper() for letra in palavra]

