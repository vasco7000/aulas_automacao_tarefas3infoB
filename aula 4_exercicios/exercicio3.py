def calcular_operacao(n1, n2, operador):
    if operador == '+':
        return n1 + n2
    elif operador == '-':
        return n1 - n2
    elif operador == '*':
        return n1 * n2
    elif operador == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "Não é possível dividir por zero"
    else:
        return "Operador inválido"

def main():
    continuar = True
    while continuar:
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operador = input("Digite o operador matemático (+, -, *, /): ")

        
        resultado = calcular_operacao(num1, num2, operador)
        print("Resultado:", resultado)

        
        resposta = input("Deseja continuar calculando? (S/N): ")
        if resposta.upper() != 'S':
            continuar = False

if __name__ == "__main__":
    main()
