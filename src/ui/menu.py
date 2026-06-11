def obter_dados():
    print("===== NUTRIFIT ADVISOR =====\n")

    nome = input("Digite seu nome: ")

    while True:
        idade = int(input("Digite sua idade: "))
        if idade > 0:
            break
        print("Idade inválida.")

    sexo = input("Digite seu sexo (M/F): ")

    while True:
        peso = float(
            input("Digite seu peso (kg): ").replace(",", ".")
        )
        if peso > 0:
            break
        print("Peso inválido.")

    while True:
        altura = float(
            input("Digite sua altura (m): ").replace(",", ".")
        )
        if altura > 0:
            break
        print("Altura inválida.")

    return nome, idade, sexo, peso, altura


def escolher_objetivo():
    print("\n===== OBJETIVO =====")
    print("1 - Ganhar Massa Muscular")
    print("2 - Emagrecer")
    print("3 - Manter Peso")

    objetivo = input("Escolha uma opção: ")

    return objetivo


def mostrar_relatorio(
    nome,
    idade,
    sexo,
    peso,
    altura,
    imc,
    classificacao,
    suplemento
):
    print("\n")
    print("=" * 40)
    print("RELATÓRIO FINAL")
    print("=" * 40)

    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Sexo: {sexo}")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")

    print(f"\nIMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")

    print("\nSuplementação Recomendada:")
    print(suplemento)

    print("=" * 40)


def deseja_continuar():
    resposta = input(
        "\nDeseja realizar outra consulta? (S/N): "
    ).upper()

    return resposta == "S"