def devolver_distintos(*args):
 
    intermedio=len(args)
    suma=sum(args)
    
    if suma >15:
        return max(args)
    elif suma < 10:
         return min(args)
    else:
        num_ordenado=sorted(args)
        return num_ordenado[intermedio//2]     
         

resultado1 = devolver_distintos(1, 2, 3)
resultado2 = devolver_distintos(5, 4, 7)
resultado3 = devolver_distintos(10, 1, 1)

print(resultado1)  
print(resultado2)  
print(resultado3)
    