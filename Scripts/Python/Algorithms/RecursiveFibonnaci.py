# def Recursive_Fibonnaci(x:int) -> int:
#     if (x == 1 or x == 2):
#         return 1
#     elif x <= 0:
#         return 0
#     else:
#         return Recursive_Fibonnaci(x - 2) + Recursive_Fibonnaci(x - 1)


# numbers = int(input("Escolha o Número"))

# print(f'Impress:')
# print(Recursive_Fibonnaci(numbers))

def Somar(a, b):
    return a + b

c = Somar(9, 10)
print(Somar(15, 30))
print(c)

a = type(sum(""))
print(a)
