temp = float(input("Digite a temperatura: "))
medida = input("Digite a medida: 'K'; 'C'; 'F': ").upper()

def main():
    if medida == 'C':
        print(f"{temp}°C em Kelvin é {temp + 273.15}K")
        print(f"{temp}°C em Fahrenheit é {(temp * 9/5) + 32}°F")
    elif medida == 'K':
        print(f"{temp}K em Celsius é {temp - 273.15}°C")
        print(f"{temp}K em Fahrenheit é {(temp - 273.15) * 9/5 + 32}°F")
    elif medida == 'F':
        print(f"{temp}°F em Celsius é {(temp - 32) * 5/9}°C")
        print(f"{temp}°F em Kelvin é {((temp - 32) * 5/9) + 273.15}K")
    else:
        print("Unidade inválida. Use 'C', 'K' ou 'F'.")

main()
