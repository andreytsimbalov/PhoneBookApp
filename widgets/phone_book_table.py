# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/phone_book_table.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# import main

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 414)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(19, 19, 700, 700))
        self.widget.setMinimumSize(QtCore.QSize(700, 380))
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 700, 700))
        self.tableWidget.setMinimumSize(QtCore.QSize(700, 700))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 161, 41))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(170, 0, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 0, 171, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        # вспомогательный код
        self.createTable()
        self.createComboBox()
        self.comboBox.activated[str].connect(self.chooseComboBoxItem)
        # self.pushButton.clicked.connect(self.addButtonClicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.pushButton_2.setText(_translate("Form", "Редактировать"))

    def addButtonClicked(self):
        print(123)

    def createComboBox(self):
        # создание ComboBox
        batch_of_letters = 3
        letter_iterator = 0
        a = ord('а')
        self.navigation_by_letter = []
        navigation_str = ''
        for i in range(a, a + 32):
            navigation_str+=chr(i)
            letter_iterator+=1
            if letter_iterator==batch_of_letters:
                self.navigation_by_letter.append(navigation_str)
                navigation_str = ''
                letter_iterator = 0

        for navigation_by_letter_i in self.navigation_by_letter:
            self.comboBox.addItem(navigation_by_letter_i)

    def chooseComboBoxItem(self, str):
        print(str)
        pass

    def changeCell(self, i, j, var=""):
        item = QtWidgets.QTableWidgetItem()
        item.setText(var)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(i, j, item)

    def addCurve(self, i, curveStr = []):
        for j in range(min(len(curveStr), self.tableWidget.columnCount())):
            self.changeCell(i, j, curveStr[j])

    def createTable(self):
        # создание таблицы

        self.tableWidget.setHorizontalHeaderLabels(["Имя", "Телефон", "Дата Рождения"])
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(14)
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.setColumnWidth(i, 221)

        rows = self.tableWidget.rowCount()
        for i in range(rows):
            self.addCurve(i, ["*", "*", "*"])

        self.addCurve(0, ["qwe", "asd", "132"])
        self.addCurve(3, ["qwe", "asd", "132"])
        # self.tableWidget.resizeColumnsToContents()

