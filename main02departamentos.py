#tenemos la posibilidad de poner un Alias a esto namespace 
from services import service02oracledepartamentos as servdeptos
print("Servicios Departamentos")
servicio = servdeptos.ServiceDepartamentos()
print("------ Menú Catálogo de Departamentos --------")
print("1. Insertar")
print("2. Eliminar un Departamento")
print("3. Modificar un Departamento")
print("4. Mostrar un Departamento")
print("5. Mostrar todos los Departamentos")
print("")
opcion = int(input("Selecciona una Opción: "))
if (opcion ==1):
    print("Insertar Departamento ")
    id = int(input("ID del departamento: "))
    nombre = (input("Nombre del departamento: "))
    localidad = (input("Localidad del departamento: "))
    registros = servicio.insertarDepartamento(id, nombre, localidad)
    print(f"Registros Insertados : {registros}")
elif (opcion ==2):
    id = int((input("Dime un No de Departamento a Eliminar: ")))
    registros = servicio.eliminarDepartamento(id)
    print(f"Registros Eliminados : {registros}")
elif (opcion ==3):
    id = int((input("Dime un No de Departamento a Actualizar: ")))
    nombre = (input("Nombre del departamento: "))
    localidad = (input("Localidad del departamento: "))
    registros = servicio.actualizarDepartamento(id, nombre, localidad)
    print(f"Registros Actualizados : {registros}")
elif (opcion ==4):
    id = int((input("Dime un No de Departamento a Consultar: ")))
    departamento = servicio.consultarDepartamento(id)
    print(f"El Nombre del departamento {departamento.idDepartamento} es : {departamento.nombre}, Localidad: {departamento.localidad}")
elif (opcion ==5):
    misdepartamentos = servicio.consultarTodosLosDepartamentos()
    for midepartamento in misdepartamentos:
        print(f"El Nombre del departamento {midepartamento.idDepartamento} es : {midepartamento.nombre}, Localidad: {midepartamento.localidad}") 
