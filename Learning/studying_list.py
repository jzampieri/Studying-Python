compras = [] # var = [] cria uma lista vazia

while True: #criação de laços de repetição
    produto = input("Produto: ")
    if produto == "fim":
        break #fim da estrutura de repetição
    quantidade = int(input("Quantidade: "))
    preço = float(input("Preço: "))
    compras.append([produto, quantidade, preço]) # append adiciona um input na lista
soma = 0.0
for i in compras: #estrutura de repetição for i
    print("%20s x%5d %5.2f %6.2f" % (i[0], i[1], i[2], i[1] * i[2])) #formata e imprime o nome do produto, quantidade e preço
    soma += i[1] * i[2]
print("Total: %7.2f" % soma)