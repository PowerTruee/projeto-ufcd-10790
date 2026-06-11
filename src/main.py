from ui.menu import (
    obter_dados,
    escolher_objetivo,
    mostrar_relatorio,
    deseja_continuar
)

from bll.nutrifit_bll import (
    calcular_imc,
    classificar_imc,
    recomendar_suplemento
)

from dal.historico_dal import salvar_historico


def main():
    while True:
        nome, idade, sexo, peso, altura = obter_dados()

        imc = calcular_imc(
            peso,
            altura
        )

        classificacao = classificar_imc(
            imc
        )

        objetivo = escolher_objetivo()

        suplemento = recomendar_suplemento(
            imc,
            objetivo
        )

        mostrar_relatorio(
            nome,
            idade,
            sexo,
            peso,
            altura,
            imc,
            classificacao,
            suplemento
        )

        salvar_historico(
            nome,
            imc,
            classificacao
        )

        if not deseja_continuar():
            print("\nObrigado por utilizar o NutriFit Advisor!")
            break


if __name__ == "__main__":
    main()