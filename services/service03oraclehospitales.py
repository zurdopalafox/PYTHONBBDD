import oracledb

from models import hospital

class ServiceHospitales:
    def __init__(self):
        self.miconexion = oracledb.connect(user="SYSTEM",password="oracle",dsn="localhost/FREEPDB1")

    def insertarHospital(self, paridhospital, parnombre, pardireccion, partelefono, parcamas):
        micursor = self.miconexion.cursor()
        misql    = "insert into HOSPITAL values (:idhospital, :nombre, : direccion, :telefono, :camas)"
        micursor.execute(misql, (paridhospital, parnombre, pardireccion, partelefono, parcamas,))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros
    
    def eliminarHospital(self, id):
        micursor = self.miconexion.cursor()
        sql = "delete from HOSPITAL where hospital_cod = :id"
        micursor.execute(sql, (id,))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros
    
    def actualizarHospital(self,paridhospital, parnombre, pardireccion, partelefono, parcamas):
        micursor = self.miconexion.cursor()
        sql = "update HOSPITAL set nombre=:nom, direccion=:loc, telefono=:tel, num_cama=:cam where HOSPITAL_COD=:id"
        micursor.execute(sql, (parnombre, pardireccion, partelefono, parcamas, paridhospital,))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros
    
    def consultarHospital(self,id):
        micursor = self.miconexion.cursor()
        sql = "select * from HOSPITAL where HOSPITAL_COD=:id"
        micursor.execute(sql, (id,))
        fila = micursor.fetchone()
        mihospital = hospital.Hospital()
        mihospital.idhospital   = fila[0]
        mihospital.nombre       = fila[1]
        mihospital.direccion    = fila[2]
        mihospital.telefono     = fila[3]
        mihospital.camas        = fila[4]
        micursor.close()
        return mihospital

    def consultarTodosLosHospitales(self):
        micursor = self.miconexion.cursor()
        misql    = "select * from hospital"
        micursor.execute(misql)
        listahospitales = []
        for fila in micursor:   
            mihospital = hospital.Hospital()
            mihospital.idHospital   = fila[0]
            mihospital.nombre       = fila[1]
            mihospital.direccion    = fila[2]
            mihospital.telefono     = fila[3]
            mihospital.camas        = fila[4]
            listahospitales.append(mihospital)
        micursor.close()
        return listahospitales
        
    