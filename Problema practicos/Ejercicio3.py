def contar_cero(*args):
    for i in args:
        if args[i]==0 and args[i+1]==0:
            print(args)
            return True
    return False
       
prueba1=contar_cero(1,2,3,4,5,0,0)
prueba2= contar_cero(1,2,3,4,5,5,0)
print(prueba1)
print(prueba2)