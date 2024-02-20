import sys

from PyQt6 import QtWidgets

from api import registration, authorize
from window import Ui_Form


class MainWindiow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_reg.clicked.connect(self.handle_reg)
        self.btn_login.clicked.connect(self.handle_login)

    def handle_reg(self):
        login = self.input_login.text()
        password = self.input_password.text()

        response = registration(login, password)

        self.label_info.setText(response)

    def handle_login(self):
        login = self.input_login.text()
        password = self.input_password.text()

        response = authorize(login, password)

        self.label_info.setText(response)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindiow()

    window.show()
    app.exec()

