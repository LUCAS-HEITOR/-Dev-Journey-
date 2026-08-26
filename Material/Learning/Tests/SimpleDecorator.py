def simple_decorator(func):
    def wrapper():
        print("Before Execution")
        func()
        print("After Execution")
    return wrapper

@simple_decorator
def message(messagem):
    return print(f"{messagem}")
