# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/registration.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(497, 407)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 700, 380))
        self.widget.setMinimumSize(QtCore.QSize(440, 380))
        self.widget.setObjectName("widget")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(240, 30, 221, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 80, 221, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setGeometry(QtCore.QRect(240, 130, 221, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(230, 230, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 230, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setGeometry(QtCore.QRect(240, 180, 221, 41))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setPlaceholderText(_translate("Form", "Имя пользователя"))
        self.textEdit_2.setPlaceholderText(_translate("Form", "Пароль"))
        self.textEdit_3.setPlaceholderText(_translate("Form", "Повторите пароль"))
        self.pushButton.setText(_translate("Form", "Ок"))
        self.pushButton_2.setText(_translate("Form", "Отмена"))
