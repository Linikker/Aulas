import os

print('Exercicio de Listas.py')

"""
names = []

name = input('Digite o seu nome: ')

names.append(name)


print(names)

for n in names:
	print(n)
"""
employee = []
clients = []
age = []
cpf = []
position = []

Menu = 0

while Menu == 0:
	os.system('CLS')
	print('Menu & Listas em Python')
	Menu = int(input('1. Cadastro de Clientes\n2. Cadastro de Funcionarios\n3. Cadastro de Produtos\n4. Vendas\n5. Sair\nInsira o numero da opção desejada: '))
		
	if Menu == 1:
		os.system('CLS')
		print('Menu Cadastro de clientes')
		new_client = client_name = input('Insira o nome do Cliente: ') client_cpf = input('Insira o cpf do Cliente: ') client_age = ('Insira a idade do Cliente: ')
			
		clients.append(new_client)
		
		Menu = int(input('Digite Zero para voltar ao Menu: '))

	elif Menu == 2:
		os.system('CLS')
		print('Menu Cadastro de Funcionarios')
		
		Menu = int(input('Digite Zero para voltar ao Menu: '))
		
	elif Menu == 3:
		os.system('CLS')
		print('Menu Cadastro de Produtos')
		
		Menu = int(input('Digite Zero para voltar ao Menu: '))
	
	elif Menu == 4:
		os.system('CLS')
		print('Menu Vendas')
		
		Menu = int(input('Digite Zero para voltar ao Menu: '))
	
	elif Menu == 5:
		os.system('CLS')
		print('Saiu'\n)
		break

for client in clients:
	print('Cliente cadastrado: ',client) 
