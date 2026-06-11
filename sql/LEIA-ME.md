```python
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
```
