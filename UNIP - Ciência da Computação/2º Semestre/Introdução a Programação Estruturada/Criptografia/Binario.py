import os

def texto_para_binario(texto):
    # Converte o texto em binário
    binario = ' '.join(format(ord(char), '08b') for char in texto)
    return binario

def binario_para_texto(binario):
    # Converte o binário de volta para o texto
    texto = ''.join(chr(int(byte, 2)) for byte in binario.split())
    return texto

menu = None

while (menu!='0'):
	os.system('cls')
	print('X --- Cifrar e Decifrar uma Mensagem --- X')
	print('Escolha uma Opção: ')
	print('1 - Cifrar')
	print('2 - Decifrar')
	print('0 - Sair')
	
	menu = input()
	
	if (menu=='0'):
		os.system('cls')
		print('Encerrando....')
		input()
		
	elif(menu=='1'):
		os.system('cls')
		print('Cifrar')
		msgcript = input('Insira a mensagem a ser cifrada: ')
		cript = texto_para_binario(msgcript)
		print('A mensagem cifrada é: ', cript)
		menu = input()
		
	elif(menu=='2'):
		os.system('cls')
		print('Decifrar')
		msgdecript = input('Insira a mensagem a ser decifrada: ')
		decript = binario_para_texto(msgdecript)
		print('A mensagem decifrada é: ',decript)
		menu = input()
		
	else:
		os.system('cls')
		print('Opção Inválida')
		menu = input()
		
		
