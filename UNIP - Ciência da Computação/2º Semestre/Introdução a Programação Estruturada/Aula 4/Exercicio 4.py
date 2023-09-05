import os

print('Aula 4 - Introd. Programação Estruturada')

res = ('Operador invalido')
nome = input('Digite seu Nome: ')
num1 = float(input('Digite um número: '))
op = input('Digite um operador ( +  -  /  * ): ')
num2 = float(input('Digite outro número: '))


if (op == '+'):
	res = num1 + num2
	os.system('CLS')
	print('Aula 4 - Introd. Programação Estruturada')
	print(f'Nome: {nome} \n Equação: {num1:.0f} {op} {num2:.0f} = {res:.0f}.')
	
elif (op == '-'):
	res = num1 - num2
	os.system('CLS')
	print('Aula 4 - Introd. Programação Estruturada')
	print(f'Nome: {nome} \n Equação: {num1:.0f} {op} {num2:.0f} = {res:.0f}.')
	
elif (op == '*'):
	res = num1 * num2
	os.system('CLS')
	print('Aula 4 - Introd. Programação Estruturada')
	print(f'Nome: {nome} \n Equação: {num1} {op} {num2} = {res:.2f}.')
	
elif (op == '/' or '%'):
	if(num1 or num2 == 0):
		print('Numero 0 não é divisivel...')
	else:
		res = num1 * num2
		os.system('CLS')
		print('Aula 4 - Introd. Programação Estruturada')
		print(f'Nome: {nome} \n Equação: {num1} {op} {num2} = {res:.2f}.')

else:
	print(f'Pelo amor {nome}, Insira um operador valido.')


'''

os.system('CLS') #<-- Importar /clear

print('Aula 4 - Introd. Programação Estruturada')
print(f'Nome: {nome}\n 1° Numero: {num1}\n Operador: {op}\n 2° Numero: {num2}\n Resultado: {res}')

'''

'''	NOTAS 

---

if (Logica):
	codigo p/ verdade

---

if (Logica):
	codigo p/ verdaede
	
else:
	codigo p/ falso
	
---

if (Logica):
	codigo p/ 1° verdade

elif (Logica 2):
	codigo p/ 1° falso e 2°verdade

else:
	codigo p/ 2° falso
	
---


Todo if(...) tem um teste lógico, ao contrario do else...

if pode aparecer sozinho... else não.






'''
