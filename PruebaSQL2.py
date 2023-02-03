import PyQt5.QtWidgets as PQTW
import PyQt5.QtGui as PQTG
import Clientes

class MainWindow(PQTW.QWidget):
    def __init__(self):
        super().__init__()

        def AgregarClientes():
            SetClientes = Clientes.GetAndSetClientes(str(txt_cedula.text()), str(txt_nombre.text()), str(txt_correo.text()), str(txt_telefono.text()), str(txt_direccion.text()))
            #Clientes.GSClientes.set_cedula(txt_cedula.text)
            Clientes.InsertarClientes(SetClientes)

        self.setWindowTitle("Probando Funciones SQL")      # Nombre de Ventana
        self.setFixedSize(600, 700)                        # Tamaño de Ventana (Reajuste deshabilitado) = Ancho, Largo

        lbl_cedula = PQTW.QLabel("Número de Cedula: ", self)   # Crear Label
        lbl_cedula.move(100, 100)                              # Posicion del Label
        lbl_cedula.setFont(PQTG.QFont('Arial', 12))            # Fuente y Tamaño

        txt_cedula = PQTW.QLineEdit(self)             # Crear Text Box
        txt_cedula.move(280, 98)
        txt_cedula.resize(200, 25)                    # Tamaño de Text Box
        txt_cedula.setFont(PQTG.QFont('Arial', 12))

        lbl_nombre = PQTW.QLabel("Nombre Cliente: ", self)
        lbl_nombre.move(100, 150)
        lbl_nombre.setFont(PQTG.QFont('Arial', 12))

        txt_nombre = PQTW.QLineEdit(self)
        txt_nombre.move(280, 148)
        txt_nombre.resize(200, 25)
        txt_nombre.setFont(PQTG.QFont('Arial', 12))

        lbl_correo = PQTW.QLabel("Correo Electronico: ", self)
        lbl_correo.move(100, 200)
        lbl_correo.setFont(PQTG.QFont('Arial', 12))

        txt_correo = PQTW.QLineEdit(self)
        txt_correo.move(280, 198)
        txt_correo.resize(200, 25)
        txt_correo.setFont(PQTG.QFont('Arial', 12))

        lbl_telefono = PQTW.QLabel("Telefono: ", self)
        lbl_telefono.move(100, 250)
        lbl_telefono.setFont(PQTG.QFont('Arial', 12))

        txt_telefono = PQTW.QLineEdit(self)
        txt_telefono.move(280, 248)
        txt_telefono.resize(200, 25)
        txt_telefono.setFont(PQTG.QFont('Arial', 12))

        lbl_direccion = PQTW.QLabel("Dirección: ", self)
        lbl_direccion.move(100, 300)
        lbl_direccion.setFont(PQTG.QFont('Arial', 12))

        txt_direccion = PQTW.QLineEdit(self)
        txt_direccion.move(280, 298)
        txt_direccion.resize(200, 25)
        txt_direccion.setFont(PQTG.QFont('Arial', 12))

        btn_agregar = PQTW.QPushButton('Agregar', self)
        btn_agregar.setToolTip('Agregar clientes a la lista')
        btn_agregar.move(100, 350)
        btn_agregar.setFont(PQTG.QFont('Arial', 12))
        btn_agregar.resize(80, 30)
        btn_agregar.clicked.connect(AgregarClientes)

        btn_eliminar = PQTW.QPushButton('Eliminar', self)
        btn_eliminar.setToolTip('Eliminar clientes de la lista')
        btn_eliminar.move(200, 350)
        btn_eliminar.setFont(PQTG.QFont('Arial', 12))
        btn_eliminar.resize(80, 30)

        btn_modificar = PQTW.QPushButton('Modificar', self)             # Crear botón
        btn_modificar.setToolTip('Modificar clientes de la lista')       # Mensaje Hint
        btn_modificar.move(300, 350)
        btn_modificar.setFont(PQTG.QFont('Arial', 12))
        btn_modificar.resize(80, 30)

        btn_buscar = PQTW.QPushButton('Buscar', self)             # Crear botón
        btn_buscar.setToolTip('Buscar clientes en la lista')       # Mensaje Hint
        btn_buscar.move(400, 350)
        btn_buscar.setFont(PQTG.QFont('Arial', 12))
        btn_buscar.resize(80, 30)

        self.show()

app = PQTW.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()
