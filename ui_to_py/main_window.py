from PyQt5 import QtCore, QtWidgets
from ui_to_py.form_doctor import Ui_FormDoctor
from ui_to_py.form_hospital import Ui_FormHospital

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 260)

        self.central = QtWidgets.QWidget(MainWindow)

        self.btn_doctor = QtWidgets.QPushButton("Registrar Doctor", self.central)
        self.btn_doctor.setGeometry(QtCore.QRect(60, 40, 180, 40))

        self.btn_hospital = QtWidgets.QPushButton("Registrar Hospital", self.central)
        self.btn_hospital.setGeometry(QtCore.QRect(60, 100, 180, 40))

        self.btn_search = QtWidgets.QPushButton("Buscar Doctor por DNI", self.central)
        self.btn_search.setGeometry(QtCore.QRect(60, 160, 180, 40))

        MainWindow.setCentralWidget(self.central)

        self.btn_doctor.clicked.connect(self.open_doctor)
        self.btn_hospital.clicked.connect(self.open_hospital)

    def open_doctor(self):
        self.win = QtWidgets.QWidget()
        self.ui = Ui_FormDoctor()
        self.ui.setupUi(self.win)
        self.win.show()

    def open_hospital(self):
        self.win = QtWidgets.QWidget()
        self.ui = Ui_FormHospital()
        self.ui.setupUi(self.win)
        self.win.show()
