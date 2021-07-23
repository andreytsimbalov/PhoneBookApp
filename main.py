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

    for sub_widget in sub_widgets:
        # sub_widget = subwidget(window)
        application.ui.stackedWidget.addWidget(sub_widget.ui.widget)
    application.ui.stackedWidget.setCurrentIndex(len(sub_widgets) - 1)

    application.show()
    print("Finish")
    sys.exit(app.exec())