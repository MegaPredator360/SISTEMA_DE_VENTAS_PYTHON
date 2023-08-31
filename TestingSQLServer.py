from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QTableView

app = QApplication([])

SERVER_NAME = 'AARON'
DATABASE_NAME = 'BIBLIOTECA_VENTAS'

def conexion():
    connString = f'Driver={{ODBC Driver 18 for SQL Server}};'\
                f'server={SERVER_NAME};'\
                f'database={DATABASE_NAME};'\
                f'trusted_connection=Yes;'\
                f'TrustServerCertificate=Yes'
                
    global db
    
    # Se verificará si ya existe una conexion de SQL Server abierta
    if QSqlDatabase.contains("qt_sql_default_connection"):
        # Se mantendrá la conexion de la base de datos
        db = QSqlDatabase.database("qt_sql_default_connection")
        return True
        
    else:
        # Se selecciona el driver para la conexion
        db = QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName(connString)
        
        # Si se realiza la conexion
        if db.open():
            print("Conexión exitosa")
            return True
        
        else: 
            print("Error al conectar a la base de datos:", db.lastError().text())
            return False
        
        
def Datos():
    if conexion():
        query_model = QSqlQueryModel()

        query = QSqlQuery()
        query.prepare("SELECT * FROM CLIENTE")
        query.exec()

        query_model.setQuery(query)

        table_view = QTableView()
        table_view.setModel(query_model)
        table_view.show()

        app.exec_()
        db.close()
    
Datos()