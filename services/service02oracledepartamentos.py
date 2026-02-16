import oracledb
from models import departamento

class ServiceDepartamentos:
    def __init__(self):
        self.miconexion = oracledb.connect(user="SYSTEM",password="oracle",dsn="localhost/FREEPDB1")

    def insertarDepartamento(self, numero, nombre, localidad):
        micursor = self.miconexion.cursor()
        sql = "insert into DEPT values (:num, : nom, :loc)"
        micursor.execute(sql, (numero, nombre, localidad,))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros

    def eliminarDepartamento(self, id):
        micursor = self.miconexion.cursor()
        sql = "delete from DEPT where dept_no = :id"
        micursor.execute(sql, (id,))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros
    
    def actualizarDepartamento(self, id, nombre, localidad):
        micursor = self.miconexion.cursor()
        sql = "update DEPT set DNOMBRE=:nom, LOC=:loc where DEPT_NO = :id"
        micursor.execute(sql, (nombre, localidad, id))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros
    
    def consultarDepartamento(self,id):
        micursor = self.miconexion.cursor()
        sql = "select * from DEPT where DEPT_NO=:id"
        micursor.execute(sql, (id,))
        fila = micursor.fetchone()
        midepartamento = departamento.Departamento()
        midepartamento.idDepartamento = fila[0]
        midepartamento.nombre = fila[1]
        midepartamento.localidad = fila[2]
        micursor.close()
        return midepartamento
    
    def consultarTodosLosDepartamentos(self):
        micursor = self.miconexion.cursor()
        sql = "select * from DEPT"
        micursor.execute(sql)
        listadepartamentos = []
        for fila in micursor:
            midepartamento = departamento.Departamento()
            midepartamento.idDepartamento = fila[0]
            midepartamento.nombre = fila[1]
            midepartamento.localidad = fila[2]
            listadepartamentos.append(midepartamento)
        micursor.close()
        return listadepartamentos


