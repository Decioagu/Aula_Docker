def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 34.9:
        classificacao = "Obesidade grau I"
    elif 35 <= imc < 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
    
    return imc, classificacao


# Programa principal
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc, classificacao = calcular_imc(peso, altura)

print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
