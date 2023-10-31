"""

1) Criar uma função que receba três valores do tipo float 
e retorne um float com o quadrado do 1º mais a soma dos outros dois. 
No bloco principal chame esta função e exiba o resultado.
(Com retorno e com parâmetros)

"""


def quadrado_soma(n1, n2, n3):
	potentiation = n1**n1
	result = potentiation+n2+n3
	
	return print(f'O resultado de {n1} elevado a ele mesmo somado a {n2} e {n3} resultou em {result}.')

while True:
	n1 = float(input('Insira um Valor: '))
	n2 = float(input('Insira outro Valor: '))
	n3 = float(input('Insira outro Valor: '))
	
	quadrado_soma(n1, n2, n3)
	
	break

