from PyQt5 import QtCore, QtWidgets
from Controller import controller_doctor as c_d

class Ui_FormDoctor(object):
    def setupUi(self, FormDoctor):
        FormDoctor.setObjectName("FormDoctor")
        FormDoctor.resize(400, 250)

        self.group = QtWidgets.QGroupBox(FormDoctor)
        self.group.setGeometry(QtCore.QRect(20, 20, 350, 200))
        self.group.setTitle("Registrar Doctor")

        self.line_name = QtWidgets.QLineEdit(self.group)
        self.line_name.setGeometry(QtCore.QRect(120, 40, 180, 22))

        self.line_dni = QtWidgets.QLineEdit(self.group)
        self.line_dni.setGeometry(QtCore.QRect(120, 80, 180, 22))

        label_n = QtWidgets.QLabel("Nombre:", self.group)
        label_n.setGeometry(QtCore.QRect(20, 40, 80, 20))

        label_d = QtWidgets.QLabel("DNI:", self.group)
        label_d.setGeometry(QtCore.QRect(20, 80, 80, 20))

        self.btn_save = QtWidgets.QPushButton("Registrar", self.group)
        self.btn_save.setGeometry(QtCore.QRect(120, 140, 120, 32))

        self.btn_save.clicked.connect(self.register)

    def register(self):
        name = self.line_name.text().strip()
        dni = self.line_dni.text().strip()

        c_d.ControllerDoctor.create(name=name, dni=dni)
        QtWidgets.QMessageBox.information(None, "OK", "Doctor registrado")
