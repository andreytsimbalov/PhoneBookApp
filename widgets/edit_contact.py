# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/edit_contact.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 407)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 700, 380))
        self.widget.setMinimumSize(QtCore.QSize(700, 380))
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 70, 251, 41))
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 120, 251, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setGeometry(QtCore.QRect(220, 170, 251, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 230, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(180, 280, 351, 41))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(220, 20, 251, 41))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 230, 171, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.restrictionsLineEdit()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Имя"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Телефон"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.pushButton_2.setText(_translate("Form", "Отмена"))
        self.pushButton_3.setText(_translate("Form", "Удалить"))

    def restrictionsLineEdit(self):
        self.onlyInt = QtGui.QIntValidator()
        self.lineEdit_2.setValidator(self.onlyInt)
        self.lineEdit_2.setMaxLength(11)

        reg = QtCore.QRegExp("[а-яА-Я]{32}")
        pValidator = QtGui.QRegExpValidator()
        pValidator.setRegExp(reg)
        self.lineEdit.setValidator(pValidator)