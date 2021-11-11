import math
num = int(input('Digite um número inteiro: '))
print ('\nSucessor: ', num + 1)
print ('\nAntecessor: ', num - 1)
print ('\nDobro: ', num * 2)
print ('\nCubo: ', num ** 3)
print ('\nRaíz quadrada: ', math.sqrt(num))

#Abaixo, a tabuada do número escolhido

cont = 1
while cont <= 10:
    print(num, 'X', cont, '=', num * cont)
    cont = cont + 1
