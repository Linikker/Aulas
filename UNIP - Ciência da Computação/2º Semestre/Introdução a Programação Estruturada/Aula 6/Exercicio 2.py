print('Exercicio Nota 10')

cont = 1
res = 0
 
while cont <= 11:
	nota = int(input(f'Digite a {cont}ª nota: '))
	res += nota
	cont += 1
	
	if cont == 11:
		media = res/10
		print(f'A soma das notas foi: {res}, e a Media foi: {media}')
		break


