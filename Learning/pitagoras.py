import math 

a = int(input("Digite o valor do cateto A: "))
b = int(input("Digite o valor do cateto b: "))

soma = (a*a + b*b)

hipotenusa = int(math.sqrt(soma))

print("A valor da hipotenusa é:", hipotenusa)