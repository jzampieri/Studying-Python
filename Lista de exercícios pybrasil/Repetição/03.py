"""

Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd' 

"""

# Validação de nome
nome = input("Digite o seu nome: ")
while len(nome) <= 3:
    print("Nome inválido. (Deve conter ao menos 3 caracteres.)")
    nome = input("Digite o seu nome: ")
print("Proxima pergunta.")

# Validação de idade
idade = int(input("Digite a sua idade: "))
while idade <=0 or idade >= 150:
    print("Idade inválida.")
    idade = int(input("Digite a sua idade: "))
print("Proxima pergunta.")

# Validação de salário
salario = float(input("Digite o seu salário: "))
while salario <=0:
    print("Salário inválido. (valor deve ser maior que zero.)")
    float(input("Digite o seu salário: "))
print("Proxima pergunta.")

#Validação de sexo
sexo = str.lower(input("Digite o seu sexo (m ou f): "))  # str.lower para transformar letras maiusculas em minusculas
while sexo != "f" and sexo != "m": # != testa se dois valores são diferentes
    print("Sexo inválido.")
    sexo = str.lower(input("Digite o seu sexo: "))
print("Proxima pergunta.")

#Validação civil

civil = str.lower(input("Digite o seu estado civil: (s, c, v, d): "))
while civil != "s" and civil != "c" and civil != "v" and civil and "d":
    print("Estado civil inválido.")
    civil = str.lower(input("Digite o seu estado civil: (s, c, v, d): "))
print("Fim do formuário.")