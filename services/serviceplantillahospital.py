import oracledb

from models import plantilla

class ServicePlantilla:
    def __init__(self):
        self.miconexion = oracledb.connect(user="SYSTEM",password="oracle",dsn="localhost/FREEPDB1")

    
    def consultarPlantillaHospital(self,id):
        micursor = self.miconexion.cursor()
        sql = "select * from PLANTILLA where HOSPITAL_COD=:id"
        micursor.execute(sql, (id,))
        listaplantilla = []
        for fila in micursor:   
            miplantilla = plantilla.Plantilla()
            miplantilla.idHospital     = fila[0]
            miplantilla.idSala         = fila[1]
            miplantilla.idEmpleado     = fila[2]
            miplantilla.apellido       = fila[3]
            miplantilla.funcion        = fila[4]
            miplantilla.turno          = fila[5]
            miplantilla.salario        = fila[6]
            listaplantilla.append(miplantilla)
        micursor.close()
        return listaplantilla

    