import os

menu = None

while (menu!='0'):
	os.system('cls')
	print('X --- Valor Unicode --- X')
	print('Escolha uma Opção: ')
	print('1 - Letra para Unicode')
	print('2 - Unicode para Letra')
	print('0 - Sair')
	
	menu = input()
	
	if (menu=='0'):
		os.system('cls')
		print('Encerrando....')
		input()
		
	elif(menu=='1'):
		os.system('cls')
		print('X --- Letra para Unicode --- X')
		# Obtenha o caractere a partir de um valor Unicode
		char = input('Digite o Numero Unicode a ser Transformado em Letra: ')
		# Obtenha o valor Unicode de um caractere
		valor_unicode = ord(char)
		print(f"O valor Unicode de '{char}' é {valor_unicode}")

		menu = input()
		
	elif(menu=='2'):
		os.system('cls')
		print('X --- Unicode para Letra --- X')
		# Obtenha o caractere a partir de um valor Unicode
		valor_unicode = input('Digite o Numero Unicode a ser Transformado em Letra: ')
		caractere = chr(valor_unicode)
		print(f"O caractere Unicode de {valor_unicode} é '{caractere}'")
		menu = input()
		
	else:
		os.system('cls')
		print('Opção Inválida')
		menu = input()
