import sys, os
from PyQt5 import QtWidgets, QtCore
from widget_classes import *
import password_controller as pc
import mariadb_controller as mc


class phonebook():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.application = mainwindow()
        self.application.resize(self.application.width() * 2, self.application.height() * 2)

        self.database_phone_book = mc.database()

        self.personal_data = pc.passwordcontroller()
        self.personal_data.loadLoginPassword()

        self.phone_contacts = []

        self.sub_widgets = [subwidget(sub_widget_form) for sub_widget_form in sub_widget_forms]
        for sub_widget in self.sub_widgets:
            self.application.ui.stackedWidget.addWidget(sub_widget.ui.widget)
        self.preLoginByDefault()

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
        self.sub_widgets[3].ui.comboBox.activated[str].connect(self.chooseComboBoxItem)

        # add_contact_form
        self.sub_widgets[4].ui.pushButton.clicked.connect(lambda: self.addNewContact(self.sub_widgets[4].ui))
        self.sub_widgets[4].ui.pushButton_2.clicked.connect(lambda: self.application.chooseSubwidget(3))

        # edit_contact_form
        self.sub_widgets[5].ui.pushButton_2.clicked.connect(lambda: self.application.chooseSubwidget(3))
        self.sub_widgets[5].ui.comboBox.activated[str].connect(self.chooseEditContact)

    def chooseComboBoxItem(self, range_letters):
        command = "SELECT * FROM phone_contacts where (LEFT(name,1) >= '" + range_letters[0] + \
                  "' AND LEFT(name,1) <= '" + range_letters[-1] + \
                  "') AND (user_id = " + str(self.personal_data.json_form['id']) + \
                  ") ORDER BY name"
        self.phone_contacts = self.database_phone_book.takeSelectCommand(command)

        self.sub_widgets[3].ui.tableWidget.clearContents()
        for i, phone_contact in enumerate(self.phone_contacts):
            contact_curve = [phone_contact[2],phone_contact[3],str(phone_contact[4])]
            self.sub_widgets[3].ui.addCurve(i, contact_curve)


    def chooseEditContact(self, name):
        print(name)

    def openEditContactWidget(self, sub_widgets_ui):
        user_phone_contacts = self.database_phone_book.takeSelectCommand(
            "SELECT * FROM phone_contacts WHERE user_id = %s" % (self.personal_data.json_form['id']))
        self.application.chooseSubwidget(5)
        if len(user_phone_contacts) == 0:
            sub_widgets_ui.label.setText("Список контактов пуст")

        sub_widgets_ui.comboBox.clear()
        for user_phone_contact in user_phone_contacts:
            sub_widgets_ui.comboBox.addItem(user_phone_contact[2])

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
            self.application.chooseSubwidget(3)
            # self.sub_widgets[0].ui.label.setText("Аккаунт успешно создан")
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
            self.application.chooseSubwidget(3)

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
            self.application.chooseSubwidget(3)
            print("Success login:", login, remember_me)

        else:
            self.sub_widgets[0].ui.label.setText("Данный пользователь не найден")
