import PyQt5.QtWidgets as PQTW
import PyQt5.QtGui as PQTG
import PyQt5.QtCore as PQTC
import Clientes
import frm_clientes_agregar

class AlignDelegate(PQTW.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = PQTC.Qt.AlignCenter

class MantClie(PQTW.QWidget):

    def __init__(self):
        super().__init__()
        
        self.w = None
        self.setWindowTitle("Mantenimiento Clientes")       # Nombre Ventana
        self.setFixedSize(1000, 700)                        # Tamaño Ventana

        lbl_layer1 = PQTW.QLabel(self)                      # Crear Label     
        lbl_layer1.move(0, 0)                               # Posicion
        lbl_layer1.resize(1000, 700)                        # Tamaño
        lbl_layer1.setStyleSheet("background-color: gray")  # CSS Diseño

        lbl_layer2 = PQTW.QLabel(self)
        lbl_layer2.move(10, 10)
        lbl_layer2.resize(980, 680)
        lbl_layer2.setStyleSheet("background-color: white; border: 1px solid black;")

        lbl_layer3 = PQTW.QLabel(self)
        lbl_layer3.move(20, 20)
        lbl_layer3.resize(960, 40)
        lbl_layer3.setStyleSheet("background-color: rgb(0, 120, 215); border: 1px solid black;")

        lbl_clientes = PQTW.QLabel("Mantenimiento de Clientes", self)
        lbl_clientes.move(400, 30)
        lbl_clientes.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))
        lbl_clientes.setStyleSheet("color: white;")

        lbl_buscar = PQTW.QLabel("Ingresa cliente a buscar:", self)
        lbl_buscar.move(30, 80)
        lbl_buscar.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))

        lbl_registrados = PQTW.QLabel("Cantidad de clientes registrados:", self)
        lbl_registrados.move(30, 140)
        lbl_registrados.setFont(PQTG.QFont('Arial', 12, weight = PQTG.QFont.Bold))

        lbl_registrados = PQTW.QLabel("0", self)
        lbl_registrados.move(290, 140)
        lbl_registrados.setFont(PQTG.QFont('Arial', 12))

        btn_agregar = PQTW.QPushButton('Agregar', self)
        btn_agregar.setToolTip('Agregar clientes a la lista')
        btn_agregar.move(890, 100)
        btn_agregar.setFont(PQTG.QFont('Arial', 12))
        btn_agregar.resize(80, 30)
        btn_agregar.clicked.connect(self.show_new_window)

        btn_editar = PQTW.QPushButton('Editar', self)
        btn_editar.setToolTip('Editar cliente seleccionado de la lista')
        btn_editar.move(800, 100)
        btn_editar.setFont(PQTG.QFont('Arial', 12))
        btn_editar.resize(80, 30)

        btn_buscar = PQTW.QPushButton('Buscar', self)
        btn_buscar.setToolTip('Buscar cliente en la lista')
        btn_buscar.move(710, 100)
        btn_buscar.setFont(PQTG.QFont('Arial', 12))
        btn_buscar.resize(80, 30)

        txt_buscar_cliente = PQTW.QLineEdit(self)
        txt_buscar_cliente.move(30, 105)
        txt_buscar_cliente.resize(665, 25)
        txt_buscar_cliente.setFont(PQTG.QFont('Arial', 12))

        dgv_clientes = PQTW.QTableView(self)
        dgv_clientes.move(30, 170)
        dgv_clientes.resize(940, 500)
        dgv_clientes.verticalHeader().hide()                                            # Ocultar contador de filas
        dgv_clientes.setFont(PQTG.QFont('Arial', 12))
        TablaClientes = Clientes.MostrarClientes()                                      # Variable que contendra el contenido de la tabla del return de la funcion
        dgv_clientes.setModel(TablaClientes)                                            # Se le usará la variable anteriormente creada para colocar el contenido a la tabla
        dgv_clientes.setColumnWidth(0, 100)                                             # Tamaño de Columnas
        dgv_clientes.setColumnWidth(1, 300)
        dgv_clientes.setColumnWidth(2, 120)
        dgv_clientes.setColumnWidth(3, 230)
        dgv_clientes.setColumnWidth(4, 187)
        dgv_clientes.setItemDelegate(AlignDelegate())                                   # Se llama a clase para alinear texto al centro
        dgv_clientes.setSelectionBehavior(PQTW.QTableView.SelectRows)                   # Para seleccionar una fila completa en un solo click
        dgv_clientes.horizontalHeader().setSectionResizeMode(PQTW.QHeaderView.Fixed)    # Deshabilitar reajuste de Columnas
        dgv_clientes.setStyleSheet( "QTableView::item:selected { color:white; background: rgb(109, 109, 109); font-weight: normal; }"
                                    "QHeaderView::section:checked { background-color: rgb(0, 120, 215); font-weight: normal; border: outset; border-style: outset; }"
                                    "QHeaderView::section { color:white; background-color: rgb(0, 120, 215); font-weight: normal; border: outset; border-style: outset; }"
                                    "QHeaderView::section:horizontal { font-weight: normal; }"
                                    )

    def show_new_window(self, checked):
        if self.w is None:
            self.w = frm_clientes_agregar.AgreClie()
        self.w.show()