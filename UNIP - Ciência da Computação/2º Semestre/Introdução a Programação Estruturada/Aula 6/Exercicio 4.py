print('Exercicio Maior numero')

higher  = 0

while True:
	num = int(input('Digite um numero ou 0 para encontrar o maior: '))
	if num > higher :
		higher = num
		continue
		
	elif num == 0:
		print(f'O maior numero digitado foi {higher}')
	break
