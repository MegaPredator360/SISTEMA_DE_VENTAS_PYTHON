import PyQt5.QtWidgets as PQTW
import PyQt5.QtGui as PQTG

class AgreClie(PQTW.QWidget):
    def __init__(self):
        super().__init__() 

        def InsertarClientes():
            import frm_clientes
            import Clientes
            
            # Se crea una clase
            NuevoCliente = Clientes.GetAndSetClientes(txt_agregar_cedula.text(), txt_agregar_nombre.text(), txt_agregar_telefono.text(), txt_agregar_correo.text(), txt_agregar_direccion.text())
            
            # Se agregar al cliente
            Clientes.InsertarClientes(NuevoCliente)
            
            # Se actualiza la lista de Clientes
            frm_clientes.MantClie.ActualizarListaClientes(self)
            
            # Se cierra la ventana
            self.hide()

        self.w = None
        self.setWindowTitle("Agregar Clientes")             # Nombre Ventana
        self.setFixedSize(500, 360)                        # Tamaño Ventana

        lbl_layer1 = PQTW.QLabel(self)                      # Crear Label     
        lbl_layer1.move(0, 0)                               # Posicion
        lbl_layer1.resize(500, 360)                        # Tamaño
        lbl_layer1.setStyleSheet("background-color: gray")  # CSS Diseño

        lbl_layer2 = PQTW.QLabel(self)
        lbl_layer2.move(10, 10)
        lbl_layer2.resize(480, 340)
        lbl_layer2.setStyleSheet("background-color: white; border: 1px solid black;")

        lbl_layer3 = PQTW.QLabel(self)
        lbl_layer3.move(20, 20)
        lbl_layer3.resize(460, 40)
        lbl_layer3.setStyleSheet("background-color: rgb(0, 120, 215); border: 1px solid black;")

        lbl_clientes = PQTW.QLabel("Agregar Clientes", self)
        lbl_clientes.move(190, 30)
        lbl_clientes.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))
        lbl_clientes.setStyleSheet("color: white;")

        lbl_agregar_cedula = PQTW.QLabel("Número de cédula:", self)
        lbl_agregar_cedula.move(30, 100)
        lbl_agregar_cedula.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))

        lbl_agregar_nombre = PQTW.QLabel("Nombre Cliente:", self)
        lbl_agregar_nombre.move(30, 140)
        lbl_agregar_nombre.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))

        lbl_agregar_telefono = PQTW.QLabel("Telefono:", self)
        lbl_agregar_telefono.move(30, 180)
        lbl_agregar_telefono.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))

        lbl_agregar_correo = PQTW.QLabel("Correo Electronico:", self)
        lbl_agregar_correo.move(30, 220)
        lbl_agregar_correo.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))

        lbl_agregar_direccion = PQTW.QLabel("Dirección:", self)
        lbl_agregar_direccion.move(30, 260)
        lbl_agregar_direccion.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))

        txt_agregar_cedula = PQTW.QLineEdit(self)
        txt_agregar_cedula.move(220, 95)
        txt_agregar_cedula.resize(250, 25)
        txt_agregar_cedula.setFont(PQTG.QFont('Arial', 12))

        txt_agregar_nombre = PQTW.QLineEdit(self)
        txt_agregar_nombre.move(220, 135)
        txt_agregar_nombre.resize(250, 25)
        txt_agregar_nombre.setFont(PQTG.QFont('Arial', 12))

        txt_agregar_telefono = PQTW.QLineEdit(self)
        txt_agregar_telefono.move(220, 175)
        txt_agregar_telefono.resize(250, 25)
        txt_agregar_telefono.setFont(PQTG.QFont('Arial', 12))

        txt_agregar_correo = PQTW.QLineEdit(self)
        txt_agregar_correo.move(220, 215)
        txt_agregar_correo.resize(250, 25)
        txt_agregar_correo.setFont(PQTG.QFont('Arial', 12))

        txt_agregar_direccion = PQTW.QLineEdit(self)
        txt_agregar_direccion.move(220, 255)
        txt_agregar_direccion.resize(250, 25)
        txt_agregar_direccion.setFont(PQTG.QFont('Arial', 12))

        btn_agregar_cliente = PQTW.QPushButton('Agregar', self)
        btn_agregar_cliente.setToolTip('Agregar clientes a la lista')
        btn_agregar_cliente.move(200, 300)
        btn_agregar_cliente.setFont(PQTG.QFont('Arial', 12))
        btn_agregar_cliente.resize(80, 30)
        btn_agregar_cliente.clicked.connect(InsertarClientes)

    def show_new_window(self, checked):
        if self.w is None:
            print('xd')
        self.w.show()