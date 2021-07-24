# main.py запускает приложение

import sys, os
from PyQt5 import QtWidgets, QtCore
import widget_classes as wc
from widgets import ui2py_file_converter
import password_controller as pc
import mariadb_controller as mc

def login(sub_widget_ui, application):
    # work just for authorization_form

    personal_data = pc.loadLoginPassword()
    if personal_data['remember_me']:
        application.chooseSubwidget(3)

    login_str = sub_widget_ui.textEdit.toPlainText()
    password_str = sub_widget_ui.password.text()
    rememberMe_flag = sub_widget_ui.rememberMe.isChecked()

    # if login_str == "" or password_str == "":
    #     sub_widget_ui.label.setText("Логин или пароль пусты")
    #     return

    if login_str == personal_data['login'] and password_str == personal_data['password']:
        # sub_widget_ui.enter.clicked.connect(lambda: application.chooseSubwidget(3))
        if rememberMe_flag:
            personal_data['remember_me'] = rememberMe_flag
            pc.saveLoginPassword(personal_data)
        application.chooseSubwidget(3)
    else:
        sub_widget_ui.label.setText("Логин или пароль неверны, повторите ввод")


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
    database_phone_book = mc.database()

    sub_widgets = [subwidget(sub_widget_form) for sub_widget_form in sub_widget_forms]

    for sub_widget in sub_widgets:
        application.ui.stackedWidget.addWidget(sub_widget.ui.widget)
    application.chooseSubwidget(3)

    # обработчик сигналов:
    # authorization_form
    sub_widgets[0].ui.registration.clicked.connect(lambda: application.chooseSubwidget(2))
    sub_widgets[0].ui.forgotPassword.clicked.connect(lambda: application.chooseSubwidget(1))
    # sub_widgets[0].ui.enter.clicked.connect(lambda: sub_widgets[0].ui.readValues())
    sub_widgets[0].ui.enter.clicked.connect(lambda: login(sub_widgets[0].ui, application))

    # restore_password_form
    sub_widgets[1].ui.pushButton_2.clicked.connect(lambda: application.chooseSubwidget(0))

    # registration_form
    sub_widgets[2].ui.pushButton_2.clicked.connect(lambda: application.chooseSubwidget(0))

    # phone_book_table
    sub_widgets[3].ui.pushButton_3.clicked.connect(lambda: application.chooseSubwidget(0))



    # signalManager()

    application.show()
    print("Finish")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()