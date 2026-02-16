import mssql-python
miconexion = mssql_python.connect("")
sql = "select * from EMP"
cursor = miconexion.cursor()


