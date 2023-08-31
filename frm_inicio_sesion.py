import PyQt5.QtWidgets as PQTW
import PyQt5.QtGui as PQTG
import frm_facturacion
import sys

class InicSesi(PQTW.QWidget):
    def __init__(self):
        super().__init__()

        self.w = None
        self.setWindowTitle("Inicio de Sesión")       # Nombre Ventana
        self.setFixedSize(400, 450)

        lbl_layer1 = PQTW.QLabel(self)                      # Crear Label     
        lbl_layer1.move(0, 0)                               # Posicion
        lbl_layer1.resize(400, 450)                         # Tamaño
        lbl_layer1.setStyleSheet("background-color: gray")  # CSS Diseño

        lbl_layer2 = PQTW.QLabel(self)
        lbl_layer2.move(10, 10)
        lbl_layer2.resize(380, 430)
        lbl_layer2.setStyleSheet("background-color: white; border: 1px solid black;")

        lbl_usuario = PQTW.QLabel("Usuario", self)
        lbl_usuario.move(160, 250)
        lbl_usuario.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))

        txt_usuario = PQTW.QLineEdit(self)
        txt_usuario.move(95, 275)
        txt_usuario.resize(200, 25)
        txt_usuario.setFont(PQTG.QFont('Arial', 12))

        lbl_contrasena = PQTW.QLabel("Contraseña", self)
        lbl_contrasena.move(145, 310)
        lbl_contrasena.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))

        txt_contrasena = PQTW.QLineEdit(self)
        txt_contrasena.move(95, 335)
        txt_contrasena.resize(200, 25)
        txt_contrasena.setFont(PQTG.QFont('Arial', 12))

        btn_iniciar = PQTW.QPushButton('Iniciar Sesión', self)
        btn_iniciar.setToolTip('Iniciar sesión al sistema de facturación')
        btn_iniciar.move(130, 380)
        btn_iniciar.setFont(PQTG.QFont('Arial', 12))
        btn_iniciar.resize(120, 30)
        btn_iniciar.clicked.connect(self.AbrirFacturacion)

    def AbrirFacturacion(self, checked):
        if self.w is None:
            # Se abre la ventana de facturacion
            self.w = frm_facturacion.FactVent()
            
        self.w.show()

app = PQTW.QApplication(sys.argv)
w = InicSesi()
w.show()
app.exec()