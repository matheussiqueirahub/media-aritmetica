# media.py

def media(a: float, b: float, c: float) -> float:
    """
    Calcula a média aritmética de três números.

    Parâmetros:
    a (float): primeiro número
    b (float): segundo número
    c (float): terceiro número

    Retorna:
    float: média aritmética dos três valores
    """
    return (a + b + c) / 3


if __name__ == "__main__":
    try:
        nums = [
            float(input("Digite o primeiro número: ")),
            float(input("Digite o segundo número: ")),
            float(input("Digite o terceiro número: "))
        ]
    except ValueError:
        print("Erro: insira apenas números válidos.")
    else:
        resultado = media(*nums)
        print(f"A média aritmética é: {resultado}")