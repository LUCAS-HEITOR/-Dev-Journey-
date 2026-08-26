import typeguard

lista = [1234567890, 1987654321, 2345617908]

@typeguard.typechecked
def Desempacotador (lista: list):
    i = 0
    max_value = len(lista)
    while i != max_value:
        unpack = lista[i]
        i += 1
        print(i)
        yield unpack

print(Desempacotador(lista))
