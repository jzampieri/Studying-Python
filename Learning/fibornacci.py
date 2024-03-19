"""

A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo.

"""

def fibonacci(num):
    fibonacci = []

    anterior = 0
    atual = 1

    for i in range(num):
        fibonacci.append(atual)
        proximo = anterior + atual
        anterior = atual
        atual = proximo
    return fibonacci

num = 10
sequencia = fibonacci(num)
print(sequencia)
