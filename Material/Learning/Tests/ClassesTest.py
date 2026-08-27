def multiplicador(fator):
    def multiplicada(x):
        return x * fator
    return multiplicada


a = lambda x=5: x * 100
print(id(a))

vezes2 = multiplicador(2)

print(vezes2.__closure__)
