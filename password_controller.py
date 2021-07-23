import  json

def loadLoginPassword():
    with open('data/login_password.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def saveLoginPassword(dict_data):
    with open('data/login_password.json', 'w', encoding='utf-8') as f:
        json.dump(dict_data, f, ensure_ascii=False, indent=4)

json_form = {
    'id': 0,
    'login': '',
    'password': '',
    'date_of_birth': 0,
    'remember_me': False
}
saveLoginPassword(json_form)
print(loadLoginPassword())