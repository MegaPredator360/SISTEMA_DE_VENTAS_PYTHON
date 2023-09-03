import PyQt5.QtSql as PQTSQL
import sys

SERVER_NAME = 'DESKTOP-JH1RFPS'
DATABASE_NAME = 'BIBLIOTECA_VENTAS'
USERNAME = ''
PASSWORD = ''

# Getters y Setters
class GetAndSetClientes:
    def __init__(self, cedula, nombre, telefono, correo, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

def createConnection():
    connString = f'Driver={{ODBC Driver 17 for SQL Server}};'\
                f'server={SERVER_NAME};'\
                f'database={DATABASE_NAME};'\
                f'trusted_connection=Yes;'\
                f'TrustServerCertificate=Yes'

    global db
    db = PQTSQL.QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(connString)

    # Se verificará si ya existe una conexion de SQL Server abierta
    if PQTSQL.QSqlDatabase.contains("qt_sql_default_connection"):
        # Se mantendrá la conexion de la base de datos
        db = PQTSQL.QSqlDatabase.database("qt_sql_default_connection")
        return True
        
    else:
        # Se selecciona el driver para la conexion
        db = PQTSQL.QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName(connString)
        
        # Si se realiza la conexion
        if db.open():
            print("Conexión exitosa")
            return True
        
        else: 
            print("Error al conectar a la base de datos:", db.lastError().text())
            return False

def InsertarClientes(SetClientes):
    if createConnection():
        qry = PQTSQL.QSqlQuery(db)
        SQL_STATEMENT = "INSERT INTO CLIENTE VALUES (" + SetClientes.cedula + ", '" + SetClientes.nombre + "', " + SetClientes.telefono + ", '" + SetClientes.correo + "', '" + SetClientes.direccion + "')"
        qry.prepare(SQL_STATEMENT)
        qry.exec()
        db.close()

def MostrarClientes():
    if createConnection():
        qry = PQTSQL.QSqlQuery(db)
        SQL_STATEMENT = "SELECT CLIE_ID AS 'Cedula', CLIE_NOMBRE AS 'Nombre', CLIE_TELEFONO AS 'Telefono', CLIE_CORREO AS 'Correo', CLIE_DIRECCION AS 'Dirección'  FROM CLIENTE"
        qry.prepare(SQL_STATEMENT)
        qry.exec()

        ModeloClientes = PQTSQL.QSqlQueryModel()
        ModeloClientes.setQuery(qry)
        
        return ModeloClientes
    
def ModificarClientes(SetClientes):
    if createConnection():
        qry = PQTSQL.QSqlQuery(db)
        SQL_STATEMENT= "UPDATE CLIENTE SET  clie_nombre = '" + SetClientes.nombre + "', clie_telefono= " + SetClientes.telefono + ", clie_correo= '" + SetClientes.correo + "', clie_direccion= '" + SetClientes.direccion + "' WHERE clie_id =" + SetClientes.cedula 
        qry.prepare(SQL_STATEMENT)
        qry.exec()
        db.close()
            

        