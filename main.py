# main.py запускает приложение

import sys, os
from PyQt5 import QtWidgets
from widgets import ui2py_file_converter

from widgets.main_window import Ui_MainWindow
from widgets.authorization import Ui_Form as authorization_form
from widgets.restore_password import Ui_Form as restore_password_form
from widgets.registration import Ui_Form as registration_form
from widgets.widget_3 import Ui_Form as ui_form_w3
# from widgets.mw_1 import Ui_MainWindow as ui_mw_1

windows = [
    authorization_form,
    restore_password_form,
    registration_form,

]

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
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
    application = mywindow()
    application.resize(application.width()*2, application.height()*2)
    # n_wingets_in_stackedWidget = 3
    # for i in range(n_wingets_in_stackedWidget):
    #     # application.ui.stackedWidget.widgetRemoved(0)
    #     asd=application.ui.stackedWidget.setCurrentIndex(i)
    #     application.ui.stackedWidget.removeWidget(asd)



    for window in  windows:
        sub_widget = subwidget(window)
        application.ui.stackedWidget.addWidget(sub_widget.ui.widget)
    application.ui.stackedWidget.setCurrentIndex(len(windows)-1)

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