def Converter(a:float, b:float):
    try:
        return int(a) + int(b)
    except ValueError:
        return float(a) + float(b)

# print(Converter(5.12))

dic_nome = {"nome": "Lucas", "idade": 22}

print(dic_nome)
for key, value in dic_nome.items():
    print(key, value)
