import genrador_turnos

generador_perfumeria = genrador_turnos.turno_perfumeria()
generador_farmacia = genrador_turnos.turno_farmacia()
generador_cosmetico = genrador_turnos.turno_cosmetico()

def mostrar_menu():
       print("")
       print("\t**** Bienvenido al sistema de turnos ****")
       print("\t1.Perfumeria ")
       print("\t2.Farmacia")
       print("\t3.Cosmeticos")
       print("\t4. Salir")
      
def ejecutar_turno(generador,mensaje):
    turno=next(generador)
    mensaje(turno)
    
def ejecucion():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutar_turno( generador_perfumeria, genrador_turnos.mensaje_perfumeria)
        elif opcion == "2":
            ejecutar_turno(generador_farmacia, genrador_turnos.mensaje_farmacia)
        elif opcion == "3":
            ejecutar_turno( generador_cosmetico, genrador_turnos.mensaje_cosmetico)
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Por favor, elija una opción válida.")

ejecucion()
