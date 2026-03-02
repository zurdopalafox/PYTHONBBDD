from services import serviceplantillahospital as servplantilla
print("Servicios Plantilla")
servicio = servplantilla.ServicePlantilla()

id = int((input("Introduzca el Id de Hospital a Consultar: ")))
miplantillaHospital = servicio.consultarPlantillaHospital(id)


print(f"------ Lista de Plantilla de Hospital {id}--------")

for plantilla in miplantillaHospital:
    print(f"ID Hospital {plantilla.idHospital} Sala : {plantilla.idSala}, ID Empleado: {plantilla.idEmpleado}, Apellido: {plantilla.apellido}, Función: {plantilla.funcion}, Turno: {plantilla.turno}, Salario: {plantilla.salario}") 


