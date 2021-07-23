# main.py запускает приложение

import sys, os
from PyQt5 import QtWidgets, QtCore
from widgets import ui2py_file_converter

from widgets.main_window import Ui_MainWindow
from widgets.authorization import Ui_Form as authorization_form
from widgets.restore_password import Ui_Form as restore_password_form
from widgets.registration import Ui_Form as registration_form
from widgets.table_1 import Ui_Form as table_form
from widgets.widget_3 import Ui_Form as ui_form_w3
# from widgets.mw_1 import Ui_MainWindow as ui_mw_1

windows = [
    authorization_form,
    restore_password_form,
    registration_form,
    table_form,

]


class mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def resizeEvent(self, event):
        x = self.size().width()
        y = self.size().height()

        self.ui.horizontalLayoutWidget.resize(x, y)


class subwidget(QtWidgets.QWidget):
    def __init__(self, Ui_Form):
        super(subwidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)



if __name__ == "__main__":

    print("Start")
    ui2py_file_converter.convert("widgets/")

    app = QtWidgets.QApplication([])
    application = mainwindow()
    application.resize(application.width()*2, application.height()*2)

    sub_widgets = [subwidget(window) for window in windows]



    # РАБОТА С ТАБЛИЦАМИ
    sub_widgets[3].ui.tableWidget.setColumnCount(3)
    sub_widgets[3].ui.tableWidget.setRowCount(14)  # и одну строку в таблице

    # Устанавливаем заголовки таблицы
    sub_widgets[3].ui.tableWidget.setHorizontalHeaderLabels(["Имя", "Телефон", "Дата Рождения"])

    # заполняем первую строку
    sub_widgets[3].ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Text in column 1"))
    sub_widgets[3].ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Text in column 2"))
    sub_widgets[3].ui.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Text in column 3"))

    # заполняем третью строку
    sub_widgets[3].ui.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem("Text in column 1"))
    sub_widgets[3].ui.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem("Text in column 2"))
    sub_widgets[3].ui.tableWidget.setItem(3, 2, QtWidgets.QTableWidgetItem("Text in column 3"))

    # делаем ресайз колонок по содержимому
    # sub_widgets[3].ui.tableWidget.resizeColumnsToContents()
    # sub_widgets[3].ui.tableWidget.res


    for sub_widget in sub_widgets:
        # sub_widget = subwidget(window)
        application.ui.stackedWidget.addWidget(sub_widget.ui.widget)
    application.ui.stackedWidget.setCurrentIndex(len(sub_widgets) - 1)

    # sub_widgets[3].ui
    # table.setColumnCount(3)  # Устанавливаем три колонки
    # table.setRowCount(1)  # и одну строку в таблице
    #
    # # Устанавливаем заголовки таблицы
    # table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])
    #
    # # Устанавливаем всплывающие подсказки на заголовки
    # table.horizontalHeaderItem(0).setToolTip("Column 1 ")
    # table.horizontalHeaderItem(1).setToolTip("Column 2 ")
    # table.horizontalHeaderItem(2).setToolTip("Column 3 ")
    #
    # # Устанавливаем выравнивание на заголовки
    # table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
    # table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
    # table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
    #
    # # заполняем первую строку
    # table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
    # table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
    # table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
    #
    # # делаем ресайз колонок по содержимому
    # table.resizeColumnsToContents()
    #
    #
    #
    # # ufw1 = subwidget()
    # sub_widget = subwidget(authorization_form)
    # print(type(sub_widget.ui.widget))
    #
    # application.ui.stackedWidget.setCurrentWidget(sub_widget.ui.widget)
    # # application.ui.stackedWidget.setSizePolicy(0, 5)
    # application.ui.stackedWidget.addWidget(sub_widget.ui.widget)


    application.show()
    print("Finish")
    sys.exit(app.exec())