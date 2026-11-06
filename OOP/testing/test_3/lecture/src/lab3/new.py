import random

def new_2():
    return "Це нова функція з lab3/new.py"

def new_function() -> str:
    # тут є покриття тестами
    n = random.randint(1, 100)
    return f"Повернене випадкове число: {n}"

def new_3():
    return "Це ще одна нова функція з lab3/new.py"

def new_none():
    a = 10
    b = a + 1

def new_4():
    return "Це четверта нова функція з lab3/new.py"
