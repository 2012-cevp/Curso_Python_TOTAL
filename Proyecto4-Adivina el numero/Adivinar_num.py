from random import randint
num_random= randint(1,100)
intentos=0
numero=0
nombre=input("Ingresa tu nombre: ")
print(f'{nombre} he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número” ')

while intentos <8:
    numero=int(input("Ingresa el numero: "))
    intentos+=1
    if numero not in range(1,100):
        print("\nEl numero debe estar entre 1 y 100\n")
    elif numero < num_random:
     print("\nError, has elegido un numero menor al numero secreto\n")
    elif numero > num_random:
     print("\nError, has elegido un nunero mayor al numero secreto\n") 
    else:
     print(f"\nCorrecto, el numero era {num_random} lo has logrado en {intentos} intentos\n")
     break    
else:
    print(f"\n Se te acabaron los intentos :(, el numero era {num_random} \n")