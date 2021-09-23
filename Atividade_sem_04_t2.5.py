def inveter(n):
    l = n % 10
    n = n // 10
    u = n % 10
    n = n // 10
    i = n % 10
    n = n // 10
    z = n % 10
    numero_invertido = (l * 1000) + (u * 100) + (i * 10) + z
    return numero_invertido
n = int(input(""))
print(inveter(n))          

