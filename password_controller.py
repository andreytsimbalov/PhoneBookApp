import  json

class passwordcontroller():
    def __init__(self):
        self.setJsonForm()



    def setJsonForm(self, login='', password='', date_of_birth='2000-01-01', remember_me=False):
        self.json_form = {
            'login': login,
            'password': password,
            'date_of_birth': date_of_birth,
            'remember_me': remember_me
        }

    def loadLoginPassword(self):
        with open('data/login_password.json', 'r', encoding='utf-8') as f:
            self.json_form = json.load(f)
            # return json.load(f)

    def saveLoginPassword(self):
        with open('data/login_password.json', 'w', encoding='utf-8') as f:
            json.dump(self.json_form, f, ensure_ascii=False, indent=4)

json_form = {
    'id': -1,
    'login': '',
    'password': '',
    'date_of_birth': 0,
    'remember_me': False
}

# {
#     "login": "asd",
#     "password": "asd",
#     "date_of_birth": "",
#     "remember_me":false
# }

# pc = passwordcontroller()
# pc.loadLoginPassword()
# print(pc.json_form)

# saveLoginPassword(json_form)
# print(loadLoginPassword())