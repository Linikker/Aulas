import os

print ('Estudos para Prova')

nome = input('Digite seu nome: ')
idade = int(input('Digite a sua Idade: '))

os.system('CLS')

print('Estudos para Prova')

print(f'Ola {nome}, vamos fazer um teste de matematica...\nA primeira pergunta é: \nDaqui 4 anos, qual seria a sua idade? ')

print(f'Opção A: {idade+3}\nOpção B: {idade+4}\nOpção C: {idade+5}')
res = input(f'Digite uma das alternativas como resposta("A B ou C"): ')



if (res.upper() == 'A'):
    {
        print(f'Resposta incorreta... A sua idade daqui 4 anos seria {idade+4} pois {idade} + 4 = {idade+4}.')
    }

elif (res.upper() == 'B'):
    {
        print(f'Resposta Correta... Pois a sua idade daqui 4 anos seria {idade+4}, {idade} + 4 = {idade+4}.')
    }

elif (res.upper() == 'C'):
    {
        print(f'Resposta incorreta... A sua idade daqui 4 anos seria {idade+4} pois {idade} + 4 = {idade+4}.')
    }

elif (res.upper() != 'A' or 'B' or 'C'):
    {
        print(f'Você não inseriu uma opção valida... "{res}" ai quebrou o bagulho.')
    }

input('Gostou do teste? ')
print('Foda-se hehe.')
input('')