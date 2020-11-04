#_*_coding:latin1_*_
#Implementar uma função que retorne verdadeiro se o número for primo
#(falso caso contrário). Testar de 1 a 100.
def Verdadeiro (x):
    fator = 2
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

n = int(input("Digite um numero inteiro:"))
while  0<n<100:
    if Verdadeiro(n):
        print(n, "Verdadeiro!")
    else:
        print(n, "Falso!")
    n = int(input("digite um numero inteiro: "))