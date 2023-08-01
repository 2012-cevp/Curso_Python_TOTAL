print("")
print("\t Bienvenido, vamos a calcular tu comisión, ingresa los siguientes datos ")
print("")
nombre=input("Cual es tu nombre?: ")
ventas=int(input("Cual fue el monto de tu venta?: "))
comision= (ventas*13)/100

print(f'Hola {nombre}, el monto de tus ventas fueron {ventas}, por lo que tu comision será ${round(comision,2)}')