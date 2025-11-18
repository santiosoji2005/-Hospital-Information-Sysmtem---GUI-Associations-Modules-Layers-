from PyQt5 import QtCore, QtWidgets
from Controller import controller_hospital as c_h

class Ui_FormHospital(object):
    def setupUi(self, FormHospital):
        FormHospital.setObjectName("FormHospital")
        FormHospital.resize(400, 250)

        self.group = QtWidgets.QGroupBox(FormHospital)
        self.group.setGeometry(QtCore.QRect(20, 20, 350, 200))
        self.group.setTitle("Registrar Hospital")

        label_n = QtWidgets.QLabel("Nombre:", self.group)
        label_n.setGeometry(QtCore.QRect(20, 40, 80, 20))

        self.line_name = QtWidgets.QLineEdit(self.group)
        self.line_name.setGeometry(QtCore.QRect(120, 40, 180, 22))

        self.btn_save = QtWidgets.QPushButton("Registrar", self.group)
        self.btn_save.setGeometry(QtCore.QRect(120, 140, 120, 32))

        self.btn_save.clicked.connect(self.register)

    def register(self):
        name = self.line_name.text().strip()

        c_h.ControllerHospital.create(name=name)
        QtWidgets.QMessageBox.information(None, "OK", "Hospital registrado")
