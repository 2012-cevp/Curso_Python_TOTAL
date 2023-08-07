def contar_primos(numero):
    primos = []

    for i in range(2,numero+1):
        primos.append(i)
    
    for i in range(2,numero):
        for j in range(2,i):
            if i%j==0:
                primos.remove(i)
                break
        
    return primos

print(contar_primos(11))