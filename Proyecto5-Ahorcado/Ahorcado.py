from random import choice 
import string
def escoger_palabra():
    palabras=["programar","estudiar","jugar","imaginar","descansar"]
    return choice(palabras)
        
def comprobacion_letra():
    rango=string.ascii_lowercase
    while True:
        letra=input("\nIngresa la letra: ").lower()
        if letra in rango:
            return letra
        print("Debes ingresar una letra de a-z, no numeros")
            
def comparacion( palabra):
    intentos = 15
    letras_erroneas = []
    letras_correctas = ['_'] * len(palabra)  

    while intentos > 0:
        letra_correcta = comprobacion_letra()

        if letra_correcta in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra_correcta:
                    letras_correctas[i] = letra_correcta
            print("Letras correctas:", " ".join(letras_correctas))
        else:
            letras_erroneas.append(letra_correcta)
            print("Letras erróneas:", letras_erroneas)

        intentos -= 1
        print("Tienes:", intentos, "intentos restantes")
        
        if "_" not in letras_correctas:
            print("¡Felicidades! ¡Has adivinado la palabra completa!")
            break
        else:
            print("La palabra correcta era:", palabra)

    
    
palabra = escoger_palabra()
# Lectura de la letra
letra = comprobacion_letra()
# Pasando los parámetros
comparacion( palabra)