# Simple addition in Python
result = 2 + 2
print("The result of 2 + 2 is:", result)
print("hola mundo")
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primos(n):
    primos = []
    for num in range(2, n + 1):
        if es_primo(num):
            primos.append(num)
    return primos

# Ejemplo de uso
n = 30
print(f"Números primos hasta {n}: {encontrar_primos(n)}")
