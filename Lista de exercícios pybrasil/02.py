"""

Faça um programa que leia um nome de usuário e a sua senha e não aceite 
a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

"""

user = input("Digite seu nome de usuário: ")
password = input("Digite a sua senha: ")

while user == password:
    print("Error, sua senha não pode ser a mesma que seu nome de usuário.")
    password = input("Digite a sua senha: ")
print("Usuário cadastrado com sucesso!")
print("Seja bem vindo, ",user)