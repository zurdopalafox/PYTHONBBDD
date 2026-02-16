import oracledb

from models import doctor

class ServiceDoctores:
    def __init__(self):
        self.miconexion = oracledb.connect(user="SYSTEM",password="oracle",dsn="localhost/FREEPDB1")

    def insertarDoctor(self, paridhospital, pariddoctor, parapellido, parespecialidad, parsalario):
        micursor = self.miconexion.cursor()
        misql    = "insert into DOCTOR values (:idhospital, :iddoctor, : apellido, :especialidad, :salario)"
        micursor.execute(misql, (paridhospital, pariddoctor, parapellido, parespecialidad, parsalario))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros
    
    def eliminarDoctor(self, id):
        micursor = self.miconexion.cursor()
        sql = "delete from DOCTOR where doctor_no = :id"
        micursor.execute(sql, (id,))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros
    
    def actualizarDoctor(self, paridhospital, pariddoctor, parapellido, parespecialidad, parsalario):
        micursor = self.miconexion.cursor()
        sql = "update DOCTOR set hospital_cod=:hoscod, apellido=:apell, especialidad=:espec, salario=:sal where DOCTOR_NO=:iddoct"
        micursor.execute(sql, (paridhospital, parapellido, parespecialidad, parsalario, pariddoctor,))
        registros = micursor.rowcount
        micursor.execute("commit")
        micursor.close()
        return registros
    
    def consultarDoctor(self,id):
        micursor = self.miconexion.cursor()
        sql = "select * from DOCTOR where DOCTOR_NO=:id"
        micursor.execute(sql, (id,))
        fila = micursor.fetchone()
        midoctor = doctor.Doctor()
        midoctor.idHospital   = fila[0]
        midoctor.idDoctor     = fila[1]
        midoctor.apellido     = fila[2]
        midoctor.especialidad = fila[3]
        midoctor.salario      = fila[4]
        micursor.close()
        return midoctor

    def consultarTodosLosDoctores(self):
        micursor = self.miconexion.cursor()
        misql    = "select * from DOCTOR"
        micursor.execute(misql)
        listadoctores = []
        for fila in micursor:   
            midoctor = doctor.Doctor()
            midoctor.idHospital   = fila[0]
            midoctor.idDoctor     = fila[1]
            midoctor.apellido     = fila[2]
            midoctor.especialidad = fila[3]
            midoctor.salario      = fila[4]
            listadoctores.append(midoctor)
        micursor.close()
        return listadoctores
        
    