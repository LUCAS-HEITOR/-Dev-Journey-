def sum_all(x : int | str | float):
    return x * 10



try:
    a = input("Classe")
    b = (sum_all(a))
    print(b)
except Exception as e:
    print(f'Erro de exceção {e}')
finally:
    print("Código Finalizado")
