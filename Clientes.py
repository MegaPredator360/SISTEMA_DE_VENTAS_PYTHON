import PyQt5.QtSql as PQTSQL
import sys

SERVER_NAME = 'AARON'
DATABASE_NAME = 'FRESH_SUPERMARKET'
USERNAME = ''
PASSWORD = ''

class GetAndSetClientes:
    def __init__(self, cedula, nombre, correo, telefono, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
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
    SQL_STATEMENT = "INSERT INTO CLIENTES VALUES (" + SetClientes.cedula + ", '" + SetClientes.nombre + "', '" + SetClientes.correo + "', " + SetClientes.telefono + ", '" + SetClientes.direccion + "')"
    qry.prepare(SQL_STATEMENT)
    qry.exec()

#def displayData(sqlStatement):
    #print('processing query...')
    #qry = PQTSQL.QSqlQuery(db)
    #qry.prepare(sqlStatement)
    #qry.exec()
#
   #model = PQTSQL.QSqlQueryModel()
    #model.setQuery(qry)

    #view = PQTSQL.QTableView()
    #view.setModel(model)
    #return model    


    #SQL_STATEMENT = "INSERT INTO CLIENTES xS (3, 'Veronica', 'vero@correo.com', 1, '1')"
    #displayData(SQL_STATEMENT)
    #db.close()

        