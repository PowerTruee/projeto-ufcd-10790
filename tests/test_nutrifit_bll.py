import sys
import os

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "src"
    )
)

from bll.nutrifit_bll import (
    calcular_imc,
    classificar_imc
)


def test_calcular_imc():
    imc = calcular_imc(84, 1.64)

    assert round(imc, 2) == 31.23

    print("✅ test_calcular_imc passou")


def test_classificar_imc():
    classificacao = classificar_imc(31.23)

    assert classificacao == "Obesidade"

    print("✅ test_classificar_imc passou")


if __name__ == "__main__":
    test_calcular_imc()
    test_classificar_imc()