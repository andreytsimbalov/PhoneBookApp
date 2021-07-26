# phonebook-class is main window of application

import sys, os
from PyQt5 import QtWidgets, QtCore
from widget_classes import *
import password_controller as pc
import mysqldb_controller as mc

from widgets import ui2py_file_converter


class phonebook():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.application = mainwindow()
        self.application.resize(1000, 800)

        self.database_phone_book = mc.database()

        self.personal_data = pc.passwordcontroller()
        self.personal_data.loadLoginPassword()


        self.sub_widgets = [subwidget(sub_widget_form) for sub_widget_form in sub_widget_forms]
        for sub_widget in self.sub_widgets:
            self.application.ui.stackedWidget.addWidget(sub_widget.ui.widget)
        self.preLoginByDefault()
        self.phone_contacts = []
        self.phone_contacts_id = -1
        self.choosePhoneContacts(self.sub_widgets[3].ui.comboBox.itemText(0))


        self.signalManager()

    def startApp(self):
        self.application.show()
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
        self.sub_widgets[2].ui.pushButton.clicked.connect(lambda: self.registration(self.sub_widgets[2].ui))
        self.sub_widgets[2].ui.pushButton_2.clicked.connect(lambda: self.application.chooseSubwidget(0))
        # phone_book_table_form
        self.sub_widgets[3].ui.pushButton.clicked.connect(lambda: self.application.chooseSubwidget(4))
        self.sub_widgets[3].ui.pushButton_2.clicked.connect(lambda: self.openEditContactWidget(self.sub_widgets[5].ui))
        self.sub_widgets[3].ui.pushButton_3.clicked.connect(lambda: self.application.chooseSubwidget(0))
        self.sub_widgets[3].ui.comboBox.activated[str].connect(self.choosePhoneContacts)
        # add_contact_form
        self.sub_widgets[4].ui.pushButton.clicked.connect(lambda: self.addNewContact(self.sub_widgets[4].ui))
        self.sub_widgets[4].ui.pushButton_2.clicked.connect(lambda: self.openPhoneBookTableWidget())
        # edit_contact_form
        self.sub_widgets[5].ui.pushButton.clicked.connect(lambda: self.editContact())
        self.sub_widgets[5].ui.pushButton_2.clicked.connect(lambda: self.openPhoneBookTableWidget())
        self.sub_widgets[5].ui.pushButton_3.clicked.connect(lambda: self.deleteContact())
        self.sub_widgets[5].ui.comboBox.activated[int].connect(self.chooseEditContact)

    def birthMessage(self):
        print(123123123123)
        print(self.personal_data.json_form)
        command = "SELECT * FROM phone_contacts " \
                  "WHERE DATE_FORMAT(date_of_birth, '%m-%d')<=DATE_FORMAT(CURDATE() + INTERVAL 7 DAY, '%m-%d') " \
                  "AND DATE_FORMAT(date_of_birth, '%m-%d')>=DATE_FORMAT(CURDATE(), '%m-%d') " \
                  "AND user_id = " + str(self.personal_data.json_form['id'])
        print(command)
        birth_contacts = self.database_phone_book.takeSelectCommand(command)
        print(birth_contacts)

        if len(birth_contacts)!=0:
            print(birth_contacts)
            message = QtWidgets.QMessageBox()
            # message.resize(1000,300)
            message.setWindowTitle("Дни рождения:")
            text = "Дни рождения на этой неделе: \n"
            for birth_contact in birth_contacts:
                text+=birth_contact[2] + " - " + str(birth_contact[4]) + "\n"
            message.setText(text)
            message.exec_()

    def openPhoneBookTableWidget(self):
        self.application.chooseSubwidget(3)
        self.choosePhoneContacts(self.sub_widgets[3].ui.comboBox.currentText())

    def editContact(self):
        name = self.sub_widgets[5].ui.lineEdit.text()
        phone_number = self.sub_widgets[5].ui.lineEdit_2.text()
        date = self.sub_widgets[5].ui.dateEdit.date().toPyDate()
        command = "UPDATE phone_contacts SET" \
                  " name = '" + name + \
                  "', phone_number = '"+ phone_number + \
                  "', date_of_birth = '"+ str(date) + \
                  "' WHERE id = " + str(self.phone_contacts_id)
        self.database_phone_book.cur.execute(command)
        self.database_phone_book.connection.commit()
        self.openPhoneBookTableWidget()
        self.sub_widgets[3].ui.label.setText("Аккаунт успешно изменен")

    def deleteContact(self):
        command = "DELETE FROM phone_contacts " \
                  "WHERE id = " + str(self.phone_contacts_id)
        self.database_phone_book.cur.execute(command)
        self.database_phone_book.connection.commit()
        self.openPhoneBookTableWidget()
        self.sub_widgets[3].ui.label.setText("Аккаунт успешно удален")

    def choosePhoneContacts(self, range_letters):
        command = "SELECT * FROM phone_contacts where (LEFT(name,1) >= '" + range_letters[0] + \
                  "' AND LEFT(name,1) <= '" + range_letters[-1] + \
                  "') AND (user_id = " + str(self.personal_data.json_form['id']) + \
                  ") ORDER BY name"
        self.phone_contacts = self.database_phone_book.takeSelectCommand(command)
        self.sub_widgets[3].ui.tableWidget.clearContents()
        for i, phone_contact in enumerate(self.phone_contacts):
            contact_curve = [phone_contact[2], phone_contact[3], str(phone_contact[4])]
            self.sub_widgets[3].ui.addCurve(i, contact_curve)

    def chooseEditContact(self, index=-1):
        if index == -1:
            self.sub_widgets[5].ui.lineEdit.setText("")
            self.sub_widgets[5].ui.lineEdit_2.setText("")
            self.sub_widgets[5].ui.dateEdit.setDate(QtCore.QDate(2000, 1, 1))
        else:
            self.phone_contacts_id = self.phone_contacts[index][0]
            contact_curve = [self.phone_contacts[index][2], self.phone_contacts[index][3],
                             str(self.phone_contacts[index][4])]
            self.sub_widgets[5].ui.lineEdit.setText(contact_curve[0])
            self.sub_widgets[5].ui.lineEdit_2.setText(contact_curve[1])
            date_list = [int(date_str) for date_str in str(contact_curve[2]).split('-')]
            self.sub_widgets[5].ui.dateEdit.setDate(QtCore.QDate(date_list[0], date_list[1], date_list[2]))

    def openEditContactWidget(self, sub_widgets_ui):
        self.application.chooseSubwidget(5)
        sub_widgets_ui.comboBox.clear()
        self.chooseEditContact()
        if len(self.phone_contacts) == 0:
            sub_widgets_ui.label.setText("Список контактов пуст")
        else:
            for phone_contact in self.phone_contacts:
                sub_widgets_ui.comboBox.addItem(phone_contact[2])
            self.chooseEditContact(0)

    def addNewContact(self, sub_widgets_ui):
        name = sub_widgets_ui.lineEdit.text()
        phone_number = sub_widgets_ui.lineEdit_2.text()
        date = sub_widgets_ui.dateEdit.date().toPyDate()
        if name == '' or phone_number == '':
            sub_widgets_ui.label.setText("Данные введены не полностью")
            return
        new_name = name[0].upper()
        if len(name) > 1:
            new_name += name[1:]
        name = new_name
        res = self.database_phone_book.addDataInPhoneContacts(
            self.personal_data.json_form['id'], name, phone_number, date)
        if res == 1:
            sub_widgets_ui.label.setText("Данный контакт уже существует")
            return
        else:
            self.openPhoneBookTableWidget()
            self.sub_widgets[3].ui.label.setText("Аккаунт успешно создан")
            print("Contact added:", name, date)

    def registration(self, sub_widgets_ui):
        name = sub_widgets_ui.textEdit.toPlainText()
        password = sub_widgets_ui.textEdit_2.toPlainText()
        password_2 = sub_widgets_ui.textEdit_3.toPlainText()
        date = sub_widgets_ui.dateEdit.date().toPyDate()

        if name == '' or password == '' or password_2 == '':
            sub_widgets_ui.label.setText("Данные введены не полностью")
            return

        if password != password_2:
            sub_widgets_ui.label.setText("Пароли не совпадают")
            return

        res = self.database_phone_book.addDataInUser(name, password, date)
        if res == 1:
            sub_widgets_ui.label.setText("Данный пользователь уже существует")
            return
        else:
            self.personal_data.setJsonForm(-1, name, password, str(date), False)
            self.personal_data.saveLoginPassword()
            self.application.chooseSubwidget(0)
            self.sub_widgets[0].ui.label.setText("Аккаунт успешно создан")
            print("Account added:", name, date)

    def preLoginByDefault(self):
        if self.personal_data.json_form['remember_me']:
            self.openPhoneBookTableWidget()
            self.birthMessage()

    def login(self):
        # work just for authorization_form

        login = self.sub_widgets[0].ui.textEdit.toPlainText()
        password = self.sub_widgets[0].ui.password.text()
        remember_me = self.sub_widgets[0].ui.rememberMe.isChecked()

        if login == "" or password == "":
            self.sub_widgets[0].ui.label.setText("Логин или пароль пусты")
            return

        self.database_phone_book.cur.execute(
            "SELECT * FROM users WHERE (login, password) = (%s,%s)",
            (login, password))
        user_in_db = self.database_phone_book.cur.fetchone()
        if user_in_db != None:
            self.personal_data.setJsonForm(user_in_db[3], login, password, str(user_in_db[2]), remember_me)
            self.personal_data.saveLoginPassword()
            self.openPhoneBookTableWidget()
            self.birthMessage()

            print("Success login:", login, remember_me)

        else:
            self.sub_widgets[0].ui.label.setText("Данный пользователь не найден")


if __name__ == "__main__":
    print("Start")
    ui2py_file_converter.convert("widgets/")

    phone_book = phonebook()
    phone_book.startApp()
