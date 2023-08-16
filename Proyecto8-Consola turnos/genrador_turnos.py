
#Funcion decoradores
def mensaje_factura(funcion):
    
    def saludo(turno):
        print("\nSu turno es: ")
        funcion(turno)
        print("Por favor tome asiento y espere su turno\n")
        
    return saludo

#Funcion farmacia
@mensaje_factura
def mensaje_farmacia(turno):
    print(f'F-{turno}')
    
def turno_farmacia():
    turno=0
    while True:
        turno+=1
        yield turno

#Funcion cosmeticos
@mensaje_factura
def mensaje_cosmetico(turno):
    print(f'C-{turno}')
    
def turno_cosmetico():
    turno=0
    while True:
        turno+=1
        yield turno
        
#Funcion perfumeria
@mensaje_factura
def mensaje_perfumeria(turno):
    print(f'P-{turno}')
    
def turno_perfumeria():
    turno=0
    while True:
        turno+=1
        yield turno



