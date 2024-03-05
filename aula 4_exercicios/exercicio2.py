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
   
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador matemático (+, -, *, /): ")

   
    resultado = calcular_operacao(n1, n2, operador)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
