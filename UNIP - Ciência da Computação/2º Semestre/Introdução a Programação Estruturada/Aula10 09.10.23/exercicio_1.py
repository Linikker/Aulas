import os

print('x --- Espaço Tempo --- x\n')

retorno = 0

def velocidade(espaco,tempo):
	v = int(espaco/tempo)
	print(f'O valor do espaço tempo é: {v}.')

def menu():
	retorno = 0
	while True:
		espaco = float(input('Digite a distancia em Km percorrida: '))
		tempo = float(input('Digite o tempo: '))

		retorno += 1
	
		velocidade(espaco,tempo)
	
		question = input('Deseja continuar? (s/n) ')
	
		if question != 's':
			print('\nx --- PROGRAMA FINALIZADO!!! --- x')
			break
		else:
			os.system('cls')
			print(f'x --- Espaço Tempo --- x')
			print(f'x --- Retorno Nº {retorno}--- x\n')
		
		


menu()
