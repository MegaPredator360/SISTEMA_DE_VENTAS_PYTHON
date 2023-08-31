import PyQt5.QtWidgets as PQTW
import PyQt5.QtGui as PQTG
import frm_clientes
import sys

class FactVent(PQTW.QWidget):
    def __init__(self):
        super().__init__()
        
        # Ventana Cliente
        self.mantCliente = frm_clientes.MantClie()

        # Ventana Principal
        self.w = None
        self.setWindowTitle("Facturación - Ventas")       # Nombre Ventana
        self.setFixedSize(400, 450)

        btn_agregar = PQTW.QPushButton('Clientes', self)
        btn_agregar.setToolTip('Agregar clientes a la lista')
        btn_agregar.move(00, 00)
        btn_agregar.setFont(PQTG.QFont('Arial', 12))
        btn_agregar.resize(80, 30)
        btn_agregar.clicked.connect(self.AbrirMantClie)

    def AbrirMantClie(self, checked):
        # Si hay no hay una ventana abierta
        if self.mantCliente.isHidden():
            # Se abre la ventana de facturación
            self.mantCliente.show()
        else:
            print("Ya hay una ventana abierta")