print('Exercicio Media Muitas Notas')

cont = 1
sum_grades = 0

while True:
	cont_grades = int(input(f'Digite a {cont}ª nota: '))
	sum_grades += cont_grades
	more_grades = input('Deseja continuar? (s/n) ')
	
	if more_grades == 's':
		cont += 1
		continue
		
	elif more_grades == 'n':
		med = sum_grades/cont_grades
		grade = sum_grades/med
		
		
		print(f'A soma das notas é: {sum_grades}\nA quantidade de Notas é: {med}\nA Nota Final Foi: {grade}')
	break
print('\nFim')
