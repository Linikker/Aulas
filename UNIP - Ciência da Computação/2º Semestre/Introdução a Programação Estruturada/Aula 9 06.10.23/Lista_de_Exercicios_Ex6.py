import random
print('Lista de Exercicios 6.py')

lista = []
cont = 1


while cont <=10:
	random1 = random.randint(0,10)
	lista.append(random1)
	cont += 1
	
print(lista)
lista.sort()
print(lista)
