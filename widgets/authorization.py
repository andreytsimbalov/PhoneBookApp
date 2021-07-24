# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/authorization.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 407)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 700, 380))
        self.widget.setMinimumSize(QtCore.QSize(700, 380))
        self.widget.setObjectName("widget")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(230, 40, 211, 31))
        self.textEdit.setDocumentTitle("")
        self.textEdit.setObjectName("textEdit")
        self.registration = QtWidgets.QPushButton(self.widget)
        self.registration.setGeometry(QtCore.QRect(340, 120, 141, 41))
        self.registration.setObjectName("registration")
        self.enter = QtWidgets.QPushButton(self.widget)
        self.enter.setGeometry(QtCore.QRect(190, 120, 141, 41))
        self.enter.setObjectName("enter")
        self.rememberMe = QtWidgets.QCheckBox(self.widget)
        self.rememberMe.setGeometry(QtCore.QRect(250, 180, 171, 31))
        self.rememberMe.setObjectName("rememberMe")
        self.showPassword = QtWidgets.QCheckBox(self.widget)
        self.showPassword.setGeometry(QtCore.QRect(250, 220, 171, 31))
        self.showPassword.setObjectName("showPassword")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(130, 310, 431, 51))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.forgotPassword = QtWidgets.QPushButton(self.widget)
        self.forgotPassword.setGeometry(QtCore.QRect(220, 260, 231, 41))
        self.forgotPassword.setObjectName("forgotPassword")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(230, 80, 211, 31))
        self.password.setObjectName("password")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.changeShowPassword()
        self.showPassword.stateChanged.connect(self.changeShowPassword)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setPlaceholderText(_translate("Form", "Имя пользователя"))
        self.registration.setText(_translate("Form", "Регистрация"))
        self.enter.setText(_translate("Form", "Войти"))
        self.rememberMe.setText(_translate("Form", "Запомнить меня"))
        self.showPassword.setText(_translate("Form", "Показать пароль"))
        self.forgotPassword.setText(_translate("Form", "Забыли пароль?"))
        self.password.setPlaceholderText(_translate("Form", "Пароль"))

    def readValues(self):
        print(self.password.text())

    def changeShowPassword(self):
        if self.showPassword.isChecked():
            self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
