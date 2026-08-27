def Decorador(func):
    def envelopador():
        print("Printado Antes")
        func()
        print("Printado Depois")
    return envelopador()


@Decorador
def Somar_tudo(*args):
    try:
        print("printado")

        total = 0

        for numero in args:
            total += numero
        return total
    except Exception:
        pass


print(Somar_tudo(5, 3, 10, 4))
