def readValues(self):
    print(self.password.text())


def changeShowPassword(self):
    print("qweqweq")
    if self.showPassword.isChecked():
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    else:
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)


# for add/edit_contact
def restrictionsLineEdit(self):
    self.onlyInt = QtGui.QIntValidator()
    self.lineEdit_2.setValidator(self.onlyInt)
    self.lineEdit_2.setMaxLength(11)

    reg = QtCore.QRegExp("[а-яА-Я]{32}")
    pValidator = QtGui.QRegExpValidator()
    pValidator.setRegExp(reg)
    self.lineEdit.setValidator(pValidator)