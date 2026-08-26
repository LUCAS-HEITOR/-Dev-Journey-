from typeguard import typechecked

@typechecked
def somar_numeros(a: int, b: float) -> int:
    return a + b

resultado = somar_numeros(20, 20.1999)

print(resultado)
