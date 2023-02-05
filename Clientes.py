import PyQt5.QtSql as PQTSQL
import sys

SERVER_NAME = 'AARON'
DATABASE_NAME = 'BIBLIOTECA_VENTAS'
USERNAME = ''
PASSWORD = ''

class GetAndSetClientes:
    def __init__(self, cedula, nombre, telefono, correo, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

def createConnection():
    connString = f'DRIVER={{SQL Server}};'\
                f'SERVER={SERVER_NAME};'\
                f'DATABASE={DATABASE_NAME}'

    global db
    db = PQTSQL.QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(connString)

    if db.open():
        print('connect to SQL Server successfully')
        return True
    else:
        print('connection failed')
        return False

def InsertarClientes(SetClientes):
    createConnection()
    qry = PQTSQL.QSqlQuery(db)
    SQL_STATEMENT = "INSERT INTO CLIENTE VALUES (" + SetClientes.cedula + ", '" + SetClientes.nombre + "', " + SetClientes.telefono + ", '" + SetClientes.correo + "', '" + SetClientes.direccion + "')"
    qry.prepare(SQL_STATEMENT)
    qry.exec()

def MostrarClientes():
    createConnection()
    qry = PQTSQL.QSqlQuery(db)
    SQL_STATEMENT = "SELECT CLIE_ID AS 'Cedula', CLIE_NOMBRE AS 'Nombre', CLIE_TELEFONO AS 'Telefono', CLIE_CORREO AS 'Correo', CLIE_DIRECCION AS 'Dirección'  FROM CLIENTE"
    qry.prepare(SQL_STATEMENT)
    qry.exec()

    ModeloClientes = PQTSQL.QSqlQueryModel()
    ModeloClientes.setQuery(qry)

    return ModeloClientes

        