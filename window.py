# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(544, 483)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.input_login = QtWidgets.QLineEdit(parent=Form)
        self.input_login.setObjectName("input_login")
        self.horizontalLayout_2.addWidget(self.input_login)
        self.input_password = QtWidgets.QLineEdit(parent=Form)
        self.input_password.setObjectName("input_password")
        self.horizontalLayout_2.addWidget(self.input_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_reg = QtWidgets.QPushButton(parent=Form)
        self.btn_reg.setObjectName("btn_reg")
        self.horizontalLayout.addWidget(self.btn_reg)
        self.btn_login = QtWidgets.QPushButton(parent=Form)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_info = QtWidgets.QLabel(parent=Form)
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.input_login.setPlaceholderText(_translate("Form", "Логин"))
        self.input_password.setPlaceholderText(_translate("Form", "Пароль"))
        self.btn_reg.setText(_translate("Form", "Зарегистрироваться"))
        self.btn_login.setText(_translate("Form", "Войти"))
