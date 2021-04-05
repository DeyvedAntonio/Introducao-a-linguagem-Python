import math
# questão 01 da lista 01
idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# questão 02
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2
if media >= 6.0:
    print("Aprovado")
else:
    print("Reprovado")

# questão 03
print("Equação do segundo grau: ax^2 + bx + c")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

s = math.sqrt(b ** 2 - 4 * a * c)

x1 = (-b + s)/(2 * a)
x2 = (-b - s)/(2 * a)

print("As raízes são: ")
print(x1, x2)

# questão 04
lista = [50, 35, 10]
lista.sort()
print(lista)

# questão 05
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = str(input("Digite um sinal: (+, -, /, *) "))

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == '/':
    print(a / b)
elif c == '*':
    print(a * b)
else:
    print("Caractere inválido.")
