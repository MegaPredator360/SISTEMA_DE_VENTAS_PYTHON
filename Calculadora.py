import PyQt5.QtWidgets as PQTW
import PyQt5.QtGui as PQTG

class MainWindow(PQTW.QWidget):
    def __init__(self):
        super().__init__()

        def CalcularResultado():
            if txt_numero1.text() == "" or txt_numero2.text() == "":
                msgbox_error = PQTW.QMessageBox(self)                   # Crear Message Box
                msgbox_error.setWindowTitle("Error")                    # Nombre Ventana
                msgbox_error.setText("Hay 1 o más campos sin llenar")   # Texto de Message Box
                msgbox_error.setIcon(PQTW.QMessageBox.Warning)          # Icono de Message Box
                msgbox_error.setStandardButtons(PQTW.QMessageBox.Ok)    # Botón de Message Box
                retval = msgbox_error.exec_()                           # Mostrar Message Box en el programa

            elif cbx_operacion.currentText() == "Suma":
                num1 = int(txt_numero1.text())
                num2 = int(txt_numero2.text())
                suma = num1 + num2

                msgbox_suma = PQTW.QMessageBox(self)                   
                msgbox_suma.setWindowTitle("Resultado")                
                msgbox_suma.setText("El Resultado es: " + str(suma))   
                msgbox_suma.setIcon(PQTW.QMessageBox.Information)      
                msgbox_suma.setStandardButtons(PQTW.QMessageBox.Ok)    
                retval = msgbox_suma.exec_() 

            elif cbx_operacion.currentText() == "Resta":
                num1 = int(txt_numero1.text())
                num2 = int(txt_numero2.text())
                suma = num1 - num2

                msgbox_resta = PQTW.QMessageBox(self)                   
                msgbox_resta.setWindowTitle("Resultado")                
                msgbox_resta.setText("El Resultado es: " + str(suma))   
                msgbox_resta.setIcon(PQTW.QMessageBox.Information)      
                msgbox_resta.setStandardButtons(PQTW.QMessageBox.Ok)    

                retval = msgbox_resta.exec_() 
            
            elif cbx_operacion.currentText() == "Multiplicación":
                num1 = int(txt_numero1.text())
                num2 = int(txt_numero2.text())
                suma = num1 * num2

                msgbox_multi = PQTW.QMessageBox(self)                   
                msgbox_multi.setWindowTitle("Resultado")                
                msgbox_multi.setText("El Resultado es: " + str(suma))   
                msgbox_multi.setIcon(PQTW.QMessageBox.Information)      
                msgbox_multi.setStandardButtons(PQTW.QMessageBox.Ok)    

                retval = msgbox_multi.exec_() 

            elif cbx_operacion.currentText() == "División":
                num1 = int(txt_numero1.text())
                num2 = int(txt_numero2.text())
                suma = num1 / num2

                msgbox_divi = PQTW.QMessageBox(self)                   
                msgbox_divi.setWindowTitle("Resultado")                
                msgbox_divi.setText("El Resultado es: " + str(suma))   
                msgbox_divi.setIcon(PQTW.QMessageBox.Information)      
                msgbox_divi.setStandardButtons(PQTW.QMessageBox.Ok)    

                retval = msgbox_divi.exec_() 

        self.setWindowTitle("Calculadora")      # Nombre de Ventana
        #self.setGeometry(0, 0, 500, 500)       # Tamaño de Ventana = Posicion X, Posicion Y, Ancho, Largo
        self.setFixedSize(500, 500)             # Tamaño de Ventana (Reajuste deshabilitado) = Ancho, Largo

        lbl_numero1 = PQTW.QLabel("Número 1: ", self)  # Crear Label
        lbl_numero1.move(100, 100)                     # Posicion del Label
        lbl_numero1.setFont(PQTG.QFont('Arial', 12))   # Fuente y Tamaño

        txt_numero1 = PQTW.QLineEdit(self)            # Crear Text Box
        txt_numero1.move(220, 98)
        txt_numero1.resize(200, 25)                    # Tamaño de Text Box

        lbl_numero2 = PQTW.QLabel("Número 2: ", self)
        lbl_numero2.move(100, 150)
        lbl_numero2.setFont(PQTG.QFont('Arial', 12))

        txt_numero2 = PQTW.QLineEdit(self)
        txt_numero2.move(220, 148)
        txt_numero2.resize(200, 25)

        btn_calcular = PQTW.QPushButton('Calcular', self)   # Crear botón
        btn_calcular.setToolTip('Calcular Resultado')       # Mensaje Hint
        btn_calcular.move(220, 270)
        btn_calcular.clicked.connect(CalcularResultado)

        cbx_operacion = PQTW.QComboBox(self)
        cbx_operacion.move(220, 220)
        cbx_operacion_list = ["Suma", "Resta", "Multiplicación", "División"]
        cbx_operacion.addItems(cbx_operacion_list)

        self.show()

app = PQTW.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()