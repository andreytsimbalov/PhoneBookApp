# main.py запускает приложение

import sys, os
from PyQt5 import QtWidgets, QtCore
from widgets import ui2py_file_converter

from widgets.main_window import Ui_MainWindow
from widgets.authorization import Ui_Form as authorization_form
from widgets.restore_password import Ui_Form as restore_password_form
from widgets.registration import Ui_Form as registration_form
from widgets.phone_book_table import Ui_Form as phone_book_table
from widgets.widget_3 import Ui_Form as ui_form_w3
# from widgets.mw_1 import Ui_MainWindow as ui_mw_1

windows = [
    authorization_form,
    restore_password_form,
    registration_form,
    phone_book_table,

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

    def chooseSubwidget(self, subwidgetIndex):
        if subwidgetIndex < 0 or subwidgetIndex > len(windows):
            print("subwidgetIndex out of range:", subwidgetIndex)
            return
        self.ui.stackedWidget.setCurrentIndex(subwidgetIndex)
        print("Open", subwidgetIndex, "window")


class subwidget(QtWidgets.QWidget):
    def __init__(self, Ui_Form):
        super(subwidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)



# def signalManager():
#     sub_widgets[3].ui.pushButton.clicked.connect(lambda: chooseSubwidget(2))
#     sub_widgets[0].ui.pushButton.clicked.connect(lambda: chooseSubwidget(2))

def asd():
    print(1241241242)

def main():
    print("Start")
    ui2py_file_converter.convert("widgets/")

    app = QtWidgets.QApplication([])
    application = mainwindow()
    application.resize(application.width() * 2, application.height() * 2)

    sub_widgets = [subwidget(window) for window in windows]

    for sub_widget in sub_widgets:
        application.ui.stackedWidget.addWidget(sub_widget.ui.widget)
    application.chooseSubwidget(2)

    # обработчик сигналов:
    # authorization_form
    sub_widgets[0].ui.registration.clicked.connect(lambda: application.chooseSubwidget(2))
    sub_widgets[0].ui.forgotPassword.clicked.connect(lambda: application.chooseSubwidget(1))
    sub_widgets[0].ui.enter.clicked.connect(lambda: sub_widgets[0].ui.readValues())
    sub_widgets[0].ui.enter.clicked.connect(lambda: application.chooseSubwidget(3))

    # restore_password_form
    sub_widgets[1].ui.pushButton_2.clicked.connect(lambda: application.chooseSubwidget(0))

    # registration_form
    sub_widgets[2].ui.pushButton_2.clicked.connect(lambda: application.chooseSubwidget(0))

    # phone_book_table
    sub_widgets[3].ui.pushButton.clicked.connect(lambda: application.chooseSubwidget(2))



    # signalManager()

    application.show()
    print("Finish")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()