#_*_coding:latin1_*_
# Faça um programa que leia a idade de uma pessoa expressa em dias e
# mostre-a expressa em anos, meses e dias.

print("Informe sua idade em dias!")
idade = int(input())

anos = int(idade / 365)
saldo = idade - (anos * 365)

meses = int(saldo / 30)

dias = saldo - meses * 30

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")