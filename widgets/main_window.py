# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 277)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 110, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(139, 9, 241, 241))
        self.stackedWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.stackedWidgetPage1)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 50, 192, 144))
        self.calendarWidget.setObjectName("calendarWidget")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.checkBox = QtWidgets.QCheckBox(self.page)
        self.checkBox.setGeometry(QtCore.QRect(80, 110, 53, 14))
        self.checkBox.setObjectName("checkBox")
        self.stackedWidget.addWidget(self.page)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.progressBar = QtWidgets.QProgressBar(self.stackedWidgetPage2)
        self.progressBar.setGeometry(QtCore.QRect(30, 100, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.stackedWidget.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.calendarWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
