import typeguard

# import time
# from functools import wraps

# def meu_decorador(func):
#     @wraps(func)  # Preserva os metadados da função original (nome, docstring)
#     def wrapper(*args, **kwargs):
#         # Código executado ANTES da função original
#         inicio = time.time()

#         # Execução da função original
#         resultado = func(*args, **kwargs)

#         # Código executado DEPOIS da função original
#         fim = time.time()
#         print(f"A função {func.__name__} levou {fim - inicio:.4f} segundos para executar.")

#         # Retorna o resultado da função original
#         return resultado

#     return wrapper

# # Aplicando o decorador usando Syntax Sugar (@)
# @meu_decorador
# def processar_dados(limite):
#     total = sum(i * i for i in range(limite))
#     return total

# # Executando a função decorada
# resultado = processar_dados(1_000_000)

def meu_decorador(funcao_original):
    def wrapper(*args, **kwargs):
        print("--- [ANTES] Executando algo antes da função original ---")

        # Executamos a função original e guardamos o retorno
        resultado = funcao_original(*args, **kwargs)

        print("--- [DEPOIS] Executando algo depois da função original ---")

        # Retornamos o resultado para não perder a saída da função
        return resultado

    # Retornamos a função embrulhada, SEM EXECUTÁ-LA (sem parênteses)
    return wrapper

@typeguard.typechecked
@meu_decorador
def Olá(x: str) -> int:
    return print(f'{x}' )
Olá("eae como você está")

def Decorator(func):
    print("Afora")
    def wrapper(*args):
        func(wrapper(args))
        return Decorator
    return wrapper


