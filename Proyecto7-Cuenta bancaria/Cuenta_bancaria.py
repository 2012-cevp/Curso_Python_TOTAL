#Clase persona que recibe nombre y apellido
class Persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido 

#Clase cliente que hereda de clase persona y tiene metodo numero cuenta y balance
class Cliente(Persona):
    def __init__(self, nombre, apellido,numero_cuenta,balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=balance
        
#Metodo str mostrar datos del cliente
    def __str__(self):
        return (f'\nSeñor(a) {self.nombre} {self.apellido}, Su numero balance es {self.balance} pesos\n')
#Metodo depositar
    def depositar(self,saldo):
        self.balance+=saldo
        
#Metodo retirar
    def retirar(self,retiro):
        if retiro >= self.balance:
            print("\nEl monto no permitido\n")
        else:
            self.balance-=retiro
                      
#Creacion de cliente     
def crea_cliente():
    nombre=input("Digita tu nombre: ")
    apellido=input("Digita tu apellido: ")
    numero_cuenta="7689401830582"
    saldo=5000000
    cliente1=Cliente(nombre,apellido,numero_cuenta,saldo)
    
    return cliente1
#Realizar operacion bancaria
def iniciar_operacion():
    mi_cliente=crea_cliente()
    opcion=0
    while opcion!=3:
     print("\n++++ Bienvenido al Banco ++++ \n++++ Que desea hacer ++++ ")
     print("1.Depositar dinero")
     print("2.Retirar dinero")
     print("3.Salir del banco")
     opcion=int(input(":"))
     if opcion==1:
         monto=int(input("$"))
         mi_cliente.depositar(monto)
         print(mi_cliente)
     elif  opcion==2:
         monto=int(input("$"))
         mi_cliente.retirar(monto)
         print(mi_cliente)
     elif opcion==3:
        print("\nGracias por usar este banco, Adios\n")
     else:
        print("\nNumero no reconocido\n")

iniciar_operacion()