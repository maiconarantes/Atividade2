#coding: utf-8
#5) Escreva uma função que:
#b) Retorne uma nova frase com cada palavra com as letras invertidas.

new_string = ""
frase = raw_input('Digite uma frase: ') #A função input retorna sempre uma string
print(' Você digitou: {}'.format(frase))
for palavra in frase.split(" "):
    new_string += palavra[::-1]+" "
print('A frase que você digitou invertida fica: {}'.format(new_string))