def readValues(self):
    print(self.password.text())


def changeShowPassword(self):
    print("qweqweq")
    if self.showPassword.isChecked():
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
    else:
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)