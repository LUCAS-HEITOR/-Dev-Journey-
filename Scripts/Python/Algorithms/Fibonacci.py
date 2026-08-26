import typeguard

@typeguard.typechecked
def Recursiva_Fibonnaci(x:int) -> int:
    if x == 1 or x == 2:
        return 1
    else:
        return Recursiva_Fibonnaci(x - 2) + Recursiva_Fibonnaci(x - 1)

while True:
    numbers = int(input("Escolha o Número"))

    print(Recursiva_Fibonnaci(numbers))
