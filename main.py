# main.py запускает приложение

import sys, os
from PyQt5 import QtWidgets
from widgets import ui2py_file_converter

from widgets.main_window import Ui_MainWindow
from widgets.widget_1 import Ui_Form as ui_form_w1
from widgets.widget_2 import Ui_Form as ui_form_w2
from widgets.widget_3 import Ui_Form as ui_form_w3
# from widgets.mw_1 import Ui_MainWindow as ui_mw_1



class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def resizeEvent(self, event):
        x = self.size().width()
        y = self.size().height()

        # self.ui..resize(x - 230, y - 50)


# class subwidget(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(subwidget, self).__init__()
#         self.ui = ui_mw_1()
#         self.ui.setupUi(self)


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
    # application.resize(application.width()*2, application.height()*2)
    # print(application.width())
    # print(application.height())


    # ufw1 = subwidget()
    ufw1 = subwidget(ui_form_w3)
    print(type(ufw1.ui.widget))

    application.ui.stackedWidget.setCurrentWidget(ufw1.ui.widget)
    # application.ui.stackedWidget.setSizePolicy(0, 5)
    application.ui.stackedWidget.addWidget(ufw1.ui.widget)
    application.ui.stackedWidget.setCurrentIndex(3)

    # qwe_1 = qwe()
    # print(type(qwe_1.ui.widget))

    #
    # print(application.ui.stackedWidget.size())

    application.show()

    print("Finish")
    sys.exit(app.exec())

    # p = subprocess.Popen('python work_with_ui.py')
    # print(p)