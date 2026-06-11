def salvar_historico(nome, imc, classificacao):
    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{nome} | IMC: {imc:.2f} | {classificacao}\n"
        )