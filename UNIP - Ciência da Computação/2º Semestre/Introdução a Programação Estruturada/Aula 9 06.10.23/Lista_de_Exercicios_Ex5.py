print('Lista de Exercicios 5.py')

lista = []

for num in range(2000,5001):
	lista.append(num)

print(lista)

valor_req = int(input('Insira o valor requisitado '))
print(lista.index(valor_req))
