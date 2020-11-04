#_*_coding:latin1_*_
#Faça um programa que leia 3 números inteiros e mostre o menor deles.

print('Informe 3 valores inteiros para a, b e c')
a = int(input())
b = int(input())
c = int(input())
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}' . format(menor))


