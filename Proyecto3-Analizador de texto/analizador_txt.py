#Ingreso de datos por el usuario
texto=input("Ingresa cualquier texto de su gusto, puede ser: Poema,frase,oracion etc. \nIngresar texto: ").lower()
letras=[]
letras.append(input("Ingresa primera letra: ").lower())
letras.append(input("Ingresa segunda letra: ").lower())
letras.append(input("Ingresa tercera letra: ").lower())

#Solucion del primer punto
letra1=texto.count(letras[0])
letra2=texto.count(letras[1])
letra3=texto.count(letras[2])
print("\nCuantas veces aparecen las letras ")
print(f'La letra  "{letras[0]}", aparecio {letra1} veces,La letra  "{letras[1]}", aparecio {letra2} veces,La letra  "{letras[2]}", aparecio {letra3} veces.')

#Solucion del segundo punto integrada en el print
print("\nCuantas palabras hay en el texto ")
print(f'En el texto hay {len(texto)} palabras')

#Solucion del tercer punto
primer_letra=texto[0]
ultima_letra=texto[-1]
print("\nCual es la primera y ultima letra del texto ")
print(f'La primera letra es {primer_letra}, y la ultima letra es {ultima_letra}')

#Solucion del cuarto punto
texto_invertido=texto.split()
texto_invertido.reverse()
texto_invertido=" ".join(texto_invertido)
print("\nCual es el texto invertido ")
print(f'El texto invertido es: {texto_invertido}')

#Solucion del quinto punto
palabra= "python" in texto
dic={True:"si",False:"no"}
print(f'\nLa palabra python {dic[palabra]} se encuentra ')
