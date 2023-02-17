import PyQt5.QtWidgets as PQTW
import PyQt5.QtGui as PQTG
import frm_clientes
import sys

class FactVent(PQTW.QWidget):
    def __init__(self):
        super().__init__()

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
        if self.w is None:
            self.w = frm_clientes.MantClie()
        self.w.show()