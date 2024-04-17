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

print("====================== Gestion de Empleados =======================")
print("|| 1. Visualizar informacion de un empleado.                      ||")
print("|| 2. Mostrar empleado cuyo tiempo en la empresa sea el menor     ||")
print("|| 3. Actualizar salario de un empleado                           ||")
print("|| 4. Terminar programa                                           ||")
print("====================================================================")

print("Se termino la ejecucion del programa")
