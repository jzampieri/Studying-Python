"""
Supondo que a população de um país A seja da ordem de 80000 (80mil) habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 (200mil) habitantes com uma
taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

"""

while True:
    paisA = float(input("Digite o número de habitantes do Pais A: "))
    paisB = float(input("Digite o número de habitantes do Pais B: "))
    crescimentoA = float(input("Digite a taxa de crescimento de habitantes do Pais A: "))/100
    crescimentoB = float(input("Digite a taxa de crescimento de habitantes do Pais B: "))/100
    anos = 0
    while paisA < paisB:
        paisA += (paisA*crescimentoA)
        paisB += (paisB*crescimentoB)
        anos += 1

        print("Vão demorar %d anos para que a população do Pais A ultrapasse ou iguale a população do Pais B\n" % anos)
        continuar = str.lower(input("Deseja continuar? (S/N)"))
        if continuar == "s":
            True
        elif continuar == "n":
            break
        else:
            continuar = str.lower(input("Deseja continuar? (S/N)"))
        

