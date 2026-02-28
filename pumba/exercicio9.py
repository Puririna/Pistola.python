#Calculadora Simples:
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
operacao = input("Informe a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro! Não é possível dividir por zero.")
        exit()
else:
    print("Operação inválida.")
    exit()

print(f"O resultado é: {resultado}")
