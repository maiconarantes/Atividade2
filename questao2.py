#_*_coding:latin1_*_
#Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam
#ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso
#os valores formem um triângulo, calcular e escrever a área deste triângulo. Se
#não formam triângulo escrever os valores lidos. (Se a &gt; b + c não formam
#triângulo algum, se a é o maior).

print("Informe um valor para a!")
a = float(input())

print("Informe um valor para b!")
b = float(input())

print("Informe um valor para c!")
c = float(input())

if a < b + c and b < a + c and c < a + b:
    print("Os Valores acima podem formar um triangulo")
    area = b * a / 2
    print("A area do Triangulo e", area)

else:
    print("Os valores acima não pode formar um triangulo")
    print(a,b,c)