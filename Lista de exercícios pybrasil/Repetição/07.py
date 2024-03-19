"""

Faça um programa que leia 5 números e informe o maior número.

"""

maior = 0

for i in range(5):
    number = int(input("Digite o seu número: "))
    if number > maior:
        maior = number
print("Maior número: ", int(maior))
