import os

clientes = 

Menu = 0

while Menu == 0:
	os.system('CLS')
	print('Menu & Listas em Python')
	Menu = int(input('1. Cadastro de Clientes\n2. Cadastro de Funcionarios\n3. Cadastro de Produtos\n4. Vendas\n5. Sair\nInsira o numero da opção desejada: '))
		
	if Menu == 1:
		os.system('CLS')
		print('Menu Cadastro de clientes')
		
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
		print('Saiu')
		break

""" Listas

list_1 = [1,2,3,4]

print(list_1[0,1,2,3])




"""
