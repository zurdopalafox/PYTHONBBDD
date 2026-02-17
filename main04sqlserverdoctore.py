#tenemos la posibilidad de poner un Alias a esto namespace 
from services import service04sqlserverdoctores as servdoctores
print("Servicios Doctores")
servicio = servdoctores.ServiceDoctores()

def dibujarDoctores():
    print("Listado de Doctores")
    misDoctores = servicio.consultarTodosLosDoctores()
    for miDoctor in misDoctores:
        print(f"ID Hospital {miDoctor.idHospital} IdDoctor : {miDoctor.idDoctor}, Apellido: {miDoctor.apellido}, Especialidad: {miDoctor.especialidad}, Salario: {miDoctor.salario}") 

print("------ Menú Catálogo de HospitDoctores --------")
print("1. Insertar")
print("2. Eliminar un Doctor")
print("3. Modificar un Doctor")
print("4. Mostrar un Doctor")
print("5. Mostrar todos los Doctores")
print("")
opcion = int(input("Selecciona una Opción: "))

if (opcion ==1):
    print("Insertar Doctor ")
    idHospital = int(input("ID del Hospital del Doctor: "))  
    idDoctor = int(input("ID del Doctor: "))
    apellido = (input("Apellido del Doctor: "))
    especialidad = (input("Especialidad del Doctor: "))
    salario = (input("Salario del Doctor: "))
    registros = servicio.insertarDoctor(idHospital, idDoctor, apellido, especialidad, salario)
    print(f"Registros Insertados : {registros}")
    dibujarDoctores()

elif (opcion ==2):
    id = int((input("Dime un No de Doctor a Eliminar: ")))
    registros = servicio.eliminarDoctor(id)
    print(f"Registros Eliminados : {registros}")
    dibujarDoctores()

elif (opcion ==3):
    idDoctor = int((input("Dime un No de Doctor a Actualizar: ")))
    idHospital = int((input("ID del Hospital del Doctor: ")))
    apellido = (input("Apellido: "))
    especialidad = (input("Especialidad: "))
    salario = (input("Salario: "))
    registros = servicio.actualizarDoctor(idHospital, idDoctor, apellido, especialidad, salario)
    print(f"Registros Actualizados : {registros}")
    dibujarDoctores()

elif (opcion ==4):
    id = int((input("Dime un No de Doctor a Consultar: ")))
    miDoctor = servicio.consultarDoctor(id)
    print(f"ID Hospital {miDoctor.idHospital} IdDoctor : {miDoctor.idDoctor}, Apellido: {miDoctor.apellido}, Especialidad: {miDoctor.especialidad}, Salario: {miDoctor.salario}") 

elif (opcion ==5):
    dibujarDoctores()