# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/mw_1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 9, 381, 261))
        self.widget.setObjectName("widget")
        self.dial = QtWidgets.QDial(self.widget)
        self.dial.setGeometry(QtCore.QRect(270, 50, 50, 64))
        self.dial.setObjectName("dial")
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setGeometry(QtCore.QRect(60, 30, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.widget)
        self.timeEdit.setGeometry(QtCore.QRect(170, 150, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
