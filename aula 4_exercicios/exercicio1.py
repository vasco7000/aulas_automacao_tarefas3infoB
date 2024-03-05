def main():
    
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    # Realiza as operações matemáticas
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2

    
    if n2 != 0:
        divisao = n1 / n2
    else:
        divisao = "Não é possível dividir por zero"

   
    print("Soma:", soma)
    print("Subtração:", subtracao)
    print("Multiplicação:", multiplicacao)
    print("Divisão:", divisao)

if __name__ == "__main__":
    main()
