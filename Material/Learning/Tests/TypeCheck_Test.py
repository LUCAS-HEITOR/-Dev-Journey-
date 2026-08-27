# from typeguard import typechecked


# @typechecked
# def somar_numeros(a: int, b: float) -> int:
#     return a + b

# resultado = somar_numeros(20, 20.1999)

# print(resultado)

# settype = [(x ** 2) for x in range(100)]
# elevate = [2 ** n for n in range(30)]

# dict_key = dict(elevate)
# while elevate != len(elevate):
#     dict_key.update()

# print(dict_key)

def Args_Kwargs( vazio = "Oi", *args, **kwargs):
    return kwargs

print(Args_Kwargs(1))
