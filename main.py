# main.py запускает приложение

from phone_book import *

def qwe():
    print("asd 1241241242")

def main():
    print("Start")
    ui2py_file_converter.convert("widgets/")

    phone_book = phonebook()
    phone_book.startApp()
    # sys.exit(phone_book.app.exec())


    # app = QtWidgets.QApplication([])
    # application = mainwindow()
    # application.resize(application.width() * 2, application.height() * 2)
    # database_phone_book = mc.database()
    #
    # sub_widgets = [subwidget(sub_widget_form) for sub_widget_form in sub_widget_forms]
    #
    # for sub_widget in sub_widgets:
    #     application.ui.stackedWidget.addWidget(sub_widget.ui.widget)
    # application.chooseSubwidget(3)
    #
    # # обработчик сигналов:
    # # authorization_form
    # sub_widgets[0].ui.registration.clicked.connect(lambda: application.chooseSubwidget(2))
    # sub_widgets[0].ui.forgotPassword.clicked.connect(lambda: application.chooseSubwidget(1))
    # # sub_widgets[0].ui.enter.clicked.connect(lambda: sub_widgets[0].ui.readValues())
    # sub_widgets[0].ui.enter.clicked.connect(lambda: login(sub_widgets[0].ui, application))
    #
    # # restore_password_form
    # sub_widgets[1].ui.pushButton_2.clicked.connect(lambda: application.chooseSubwidget(0))
    #
    # # registration_form
    # sub_widgets[2].ui.pushButton_2.clicked.connect(lambda: application.chooseSubwidget(0))
    #
    # # phone_book_table
    # sub_widgets[3].ui.pushButton_3.clicked.connect(lambda: application.chooseSubwidget(0))
    #
    #
    #
    # # signalManager()
    #
    # application.show()
    # print("Finish")
    # sys.exit(app.exec())

if __name__ == "__main__":
    main()