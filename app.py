def calcular_imposto():
    # Solicita ao usuário para inserir o salário
    entrada_salario = input("Digite o valor do salário: ")
    if not entrada_salario.strip():
        print("Entrada inválida para o salário. Certifique-se de inserir um número válido.")
        return  # Encerra a função se a entrada for inválida

    # Verifica e converte a entrada para float
    try:
        valor_salario = float(entrada_salario)
    except ValueError:
        print("Entrada inválida para o salário. Certifique-se de inserir um número válido.")
        return  # Encerra a função se a entrada for inválida

    # Solicita ao usuário para inserir o valor dos benefícios
    entrada_beneficios = input("Digite o valor dos benefícios: ")
    if not entrada_beneficios.strip():
        print("Entrada inválida para os benefícios. Certifique-se de inserir um número válido.")
        return  # Encerra a função se a entrada for inválida

    # Verifica e converte a entrada para float
    try:
        valor_beneficios = float(entrada_beneficios)
    except ValueError:
        print("Entrada inválida para os benefícios. Certifique-se de inserir um número válido.")
        return  # Encerra a função se a entrada for inválida

    # Calcula o valor do imposto com base no salário
    if 0 <= valor_salario <= 1100:
        valor_imposto = 0.05 * valor_salario
    elif 1101 <= valor_salario <= 2500:
        valor_imposto = 0.10 * valor_salario
    else:
        valor_imposto = 0.15 * valor_salario

    # Calcula o valor final após o imposto e adiciona os benefícios
    saida = valor_salario - valor_imposto + valor_beneficios

    # Exibe o resultado formatado com 2 casas decimais
    print(f"O valor final após impostos e benefícios é: {saida:.2f}")


# Executa a função para calcular o imposto
calcular_imposto()
