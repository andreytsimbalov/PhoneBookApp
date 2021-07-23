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
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(340, 120, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 120, 141, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(250, 180, 171, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(250, 220, 171, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(130, 310, 431, 51))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 260, 231, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 80, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setPlaceholderText(_translate("Form", "Имя пользователя"))
        self.pushButton.setText(_translate("Form", "Регистрация"))
        self.pushButton_3.setText(_translate("Form", "Войти"))
        self.checkBox.setText(_translate("Form", "Запомнить меня"))
        self.checkBox_2.setText(_translate("Form", "Показать пароль"))
        self.pushButton_4.setText(_translate("Form", "Забыли пароль?"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Пароль"))

    def readValues(self):
        print(self.lineEdit.text())