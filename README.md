# Phone Book Application

User Notebook: Allows you to store your contact list, phone numbers and birthdays.

## Installation guide

Required set of libraries:
- PyQt5
- mysql-connector-python

Installation procedure:
1. Open **data/mysql_log_pas.json**, enter user data *MySql* server
2. Run **create_database.py**

## User's manual

Run **main.py**

Before authorizing the user, you need to register in the application.
You cannot register a new user if one has already been created.

After the user is authorized, the notebook contacts window will open. If the *Remember me* field is enabled, authorization will be performed automatically.

The notebook has the following functionality:
- Display contacts of the notebook in alphabetical order
- Adding a new contact to the database. You cannot add a contact if it has already been created
- Editing and deleting a contact from the database
- Change user
- Function of reminders about birthdays of contacts for the next week

