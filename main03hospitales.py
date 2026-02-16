#tenemos la posibilidad de poner un Alias a esto namespace 
from services import service03oraclehospitales as servhospitales
print("Servicios Hospitals")
servicio = servhospitales.ServiceHospitales()

def dibujarHospitales():
    print("Listado de Hospitales")
    misHospitales = servicio.consultarTodosLosHospitales()
    for miHospital in misHospitales:
        print(f"El Nombre del Hospital {miHospital.idHospital} es : {miHospital.nombre}, Dirección: {miHospital.direccion}, Teléfono: {miHospital.telefono}, Camas: {miHospital.camas} ") 

print("------ Menú Catálogo de Hospitales --------")
print("1. Insertar")
print("2. Eliminar un Hospital")
print("3. Modificar un Hospital")
print("4. Mostrar un Hospital")
print("5. Mostrar todos los Hospitals")
print("")
opcion = int(input("Selecciona una Opción: "))

if (opcion ==1):
    print("Insertar Hospital ")
    id = int(input("ID del Hospital: "))
    nombre = (input("Nombre del Hospital: "))
    direccion = (input("Dirección del Hospital: "))
    telefono = (input("Dirección del Teléfono: "))
    camas = (input("No. de Camas: "))
    registros = servicio.insertarHospital(id, nombre, direccion,telefono,camas)
    print(f"Registros Insertados : {registros}")
    dibujarHospitales()

elif (opcion ==2):
    id = int((input("Dime un No de Hospital a Eliminar: ")))
    registros = servicio.eliminarHospital(id)
    print(f"Registros Eliminados : {registros}")
    dibujarHospitales()

elif (opcion ==3):
    id = int((input("Dime un No de Hospital a Actualizar: ")))
    nombre = (input("Nombre del Hospital: "))
    direccion = (input("Dirección del Hospital: "))
    telefono = (input("Dirección del Teléfono: "))
    camas = (input("No. de Camas: "))
    registros = servicio.actualizarHospital(id, nombre, direccion, telefono, camas)
    print(f"Registros Actualizados : {registros}")
    dibujarHospitales()

elif (opcion ==4):
    id = int((input("Dime un No de Hospital a Consultar: ")))
    miHospital = servicio.consultarHospital(id)
    print(f"El Nombre del Hospital {miHospital.idHospitald} es : {miHospital.nombre}, Dirección: {miHospital.direccion}, Teléfono: {miHospital.telefono}, Camas: {miHospital.camas} ") 

elif (opcion ==5):
    dibujarHospitales()

#    for miHospital in misHospitales:
#        print(f"El Nombre del Hospital {miHospital.idHospital} es : {miHospital.nombre}, Dirección: {miHospital.direccion}, Teléfono: {miHospital.telefono}, Camas: {miHospital.camas} ") 

