# main.py запускает приложение

import sys, os
from PyQt5 import QtWidgets, QtCore
from widget_classes import *
from widgets import ui2py_file_converter
import password_controller as pc
import mariadb_controller as mc


class phonebook():
    def startApp(self):
        self.app = QtWidgets.QApplication([])
        self.application = mainwindow()
        self.application.resize(self.application.width() * 2, self.application.height() * 2)
        self.database_phone_book = mc.database()
        self.personal_data = pc.passwordcontroller()
        self.personal_data.loadLoginPassword()

        self.sub_widgets = [subwidget(sub_widget_form) for sub_widget_form in sub_widget_forms]

        for sub_widget in self.sub_widgets:
            self.application.ui.stackedWidget.addWidget(sub_widget.ui.widget)
        self.application.chooseSubwidget(3)

        self.signalManager()


        self.application.show()
        # print("Finish")
        sys.exit(self.app.exec())

    def signalManager(self):
        # обработчик сигналов:
        # authorization_form
        self.sub_widgets[0].ui.registration.clicked.connect(lambda: self.application.chooseSubwidget(2))
        self.sub_widgets[0].ui.forgotPassword.clicked.connect(lambda: self.application.chooseSubwidget(1))
        self.sub_widgets[0].ui.enter.clicked.connect(lambda: self.login())

        # restore_password_form
        self.sub_widgets[1].ui.pushButton_2.clicked.connect(lambda: self.application.chooseSubwidget(0))

        # registration_form
        self.sub_widgets[2].ui.pushButton.clicked.connect(lambda: self.registration())
        self.sub_widgets[2].ui.pushButton_2.clicked.connect(lambda: self.application.chooseSubwidget(0))

        # phone_book_table
        self.sub_widgets[3].ui.pushButton_3.clicked.connect(lambda: self.application.chooseSubwidget(0))


    def registration(self):
        name = self.sub_widgets[2].ui.textEdit.toPlainText()
        password = self.sub_widgets[2].ui.textEdit_2.toPlainText()
        password_2 = self.sub_widgets[2].ui.textEdit_3.toPlainText()
        date = self.sub_widgets[2].ui.dateEdit.date()

        if name=='' or password=='' or password_2 == '':
            self.sub_widgets[2].ui.label.setText("Данные введены не полностью")
            return

        if password != password_2:
            self.sub_widgets[2].ui.label.setText("Пароли не совпадают")
            return

        res = self.database_phone_book.addDataInUser(name, password, date.toPyDate(), remember_me=0)
        if res==1:
            self.sub_widgets[2].ui.label.setText("Данный пользователь уже существует")
            return
        else:
            self.personal_data.setJsonForm(name, password, str(date.toPyDate()))
            self.personal_data.saveLoginPassword()
            self.application.chooseSubwidget(0)
            self.sub_widgets[0].ui.label.setText("Аккаунт успешно создан")

    def preLoginByDefault(self):
        if self.personal_data.json_form['remember_me']:
            self.application.chooseSubwidget(3)

    def login(self):
        # work just for authorization_form

        login_str = self.sub_widgets[0].ui.textEdit.toPlainText()
        password_str = self.sub_widgets[0].ui.password.text()
        rememberMe_flag = self.sub_widgets[0].ui.rememberMe.isChecked()

        if login_str == "" or password_str == "":
            self.sub_widgets[0].ui.label.setText("Логин или пароль пусты")
            return

        if login_str == personal_data['login'] and password_str == personal_data['password']:
            # sub_widget_ui.enter.clicked.connect(lambda: application.chooseSubwidget(3))
            if rememberMe_flag:
                personal_data['remember_me'] = rememberMe_flag
                pc.saveLoginPassword(personal_data)
            self.application.chooseSubwidget(3)
        else:
            self.sub_widgets[0].ui.label.setText("Логин или пароль неверны, повторите ввод")


# def signalManager():
#     sub_widgets[3].ui.pushButton.clicked.connect(lambda: chooseSubwidget(2))
#     sub_widgets[0].ui.pushButton.clicked.connect(lambda: chooseSubwidget(2))

def asd():
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