# Practica-Calificada-01
contador = 0
continuar = ""
while continuar == "SI":
    #Ingresar empleados
    print("Creando un nuevo usuario:")
    empleado_Id = input("Id: ")
    empleado_Nombre = input("Nombre completo: ")
    empleado_Dni = input("Dni: ")
    empleado_Telefono = input("Telefono: ")
    empleado_Tiempo = input("Tiempo trabajando (meses): ")
    empleado_Cargo = input("Cargo: ")
    
    print("Quiere ingresar un nuevo empleado al registro (Si/No)")
    auxiliar = input()
    auxiliar.upper()
    print("continuar")
    continuar == auxiliar

print("Acabo el")
