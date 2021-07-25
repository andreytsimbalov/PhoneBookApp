from PyQt5 import QtWidgets, QtCore
from widgets.main_window import Ui_MainWindow
from widgets.authorization import Ui_Form as authorization_form
from widgets.restore_password import Ui_Form as restore_password_form
from widgets.registration import Ui_Form as registration_form
from widgets.phone_book_table import Ui_Form as phone_book_table_form
from widgets.add_contact import Ui_Form as add_contact_form
from widgets.edit_contact import Ui_Form as edit_contact_form

sub_widget_forms = [
    authorization_form,
    restore_password_form,
    registration_form,
    phone_book_table_form,
    add_contact_form,
    edit_contact_form,

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
        if subwidgetIndex < 0 or subwidgetIndex > len(sub_widget_forms):
            print("subwidgetIndex out of range:", subwidgetIndex)
            return
        self.ui.stackedWidget.setCurrentIndex(subwidgetIndex)
        print("Open", subwidgetIndex, "window")


class subwidget(QtWidgets.QWidget):
    def __init__(self, Ui_Form):
        super(subwidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

