valor = int(input("Digite um valor: "))
valor_2 = int(input("Digite outro valor: "))

def main():
    operation = input("Selecione a operação: '+'; '-'; 'x'; '/': ")
    if operation == '+':
        print(valor + valor_2)
    elif operation == '-':
        print(valor - valor_2)
    elif operation == 'x':
        print(valor * valor_2)
    elif operation == '/':
        print(valor/valor_2)
    else:
        print('Operação inválida!')
        main()

main()