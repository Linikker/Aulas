import os
import random

mag = [1, 2, 3, 4, 5 ,6 ]

while True:
	print('X --- Russian Roulette --- X')
	mag_recharge = int(input('Escolha um dos 6 slots para por a munição: '))
	if mag_recharge >= 1 and mag_recharge <= 6:
		mag.pop(random.randint(0,len(mag)-1))
		if mag_recharge not in mag:
			print('Você morreu.')
			break
		else:
			print('Você continuou vivo desta vez.')
			play_again = input('Continuar jogando? (s/n) ')
			if play_again != 's':
				print('Seu frango...')
				break
			else:
				os.system('CLS')
	else:
		os.system('CLS')
		print('Numero invalido, escolha dentre os slots de 1 a 6 para jogar...')



""" NOTES
print('Numero invalido, escolha dentre os slots de 1 a 6 para jogar...')
"""
