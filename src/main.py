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
            input("Digite seu peso (kg): ").replace(",", "."))
        if peso > 0:
            break
        print("Peso inválido.")

    while True:
        altura = float(
            input("Digite sua altura (m): ").replace(",", "."))
        if altura > 0:
            break
        print("Altura inválida.")

    return nome, idade, sexo, peso, altura


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def escolher_objetivo():
    print("\n===== OBJETIVO =====")

    print("1 - Ganhar Massa Muscular")
    print("2 - Emagrecer")
    print("3 - Manter Peso")

    objetivo = input("Escolha uma opção: ")
    return objetivo

def recomendar_suplemento(imc, objetivo):
    if objetivo == "1":
        if imc < 18.5:
            return """
Hipercalórico
Whey Concentrado
Creatina
"""

        elif imc < 25:
            return """
Whey Concentrado
Creatina
"""

        else:
            return """
Whey Concentrado
Creatina
"""

    elif objetivo == "2":
        return """
Whey Isolado
Creatina
"""

    elif objetivo == "3":
        return """
Whey Concentrado
"""

    else:
        return "Objetivo inválido."


def mostrar_relatorio(
    nome,
    idade,
    sexo,
    peso,
    altura,
    imc,
    classificacao,
    suplemento):

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

def salvar_historico(nome, imc, classificacao):

    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{nome} | IMC: {imc:.2f} | {classificacao}\n"
        )


def main():

    while True:
        nome, idade, sexo, peso, altura = obter_dados()

        imc = calcular_imc(
            peso,
            altura)

        classificacao = classificar_imc(
            imc)

        objetivo = escolher_objetivo()

        suplemento = recomendar_suplemento(
            imc,
            objetivo)

        mostrar_relatorio(
            nome,
            idade,
            sexo,
            peso,
            altura,
            imc,
            classificacao,
            suplemento)

        salvar_historico(
            nome,
            imc,
            classificacao)

        print("\n===== NOVA CONSULTA =====")
        print("1 - Sim")
        print("2 - Não")

        continuar = input("Deseja realizar outra consulta? ")

        if continuar != "1":
            print("\nObrigado por utilizar o NutriFit Advisor!")
            break

main()