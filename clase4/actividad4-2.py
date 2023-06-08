def es_primo(n):
    primo = True
    if n <= 1:
        return False
    for i in range(2, n):
        if(n%i == 0):
            return False
    return primo

numeros = [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(es_primo, numeros))

print(primos)