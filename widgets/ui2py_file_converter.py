#

import os

commands_to_the_console = [
    "pyuic5 main_window.ui -o main_window.py",
    "pyuic5 widget_1.ui -o widget_1.py",
    "pyuic5 widget_2.ui -o widget_2.py",
    "pyuic5 widget_3.ui -o widget_3.py",
    "pyuic5 mw_1.ui -o mw_1.py",
    "",
    "",
    "",
]

def convert(path = ""):
    for command in commands_to_the_console:
        if command == "":
            continue
        comm_split = command.split()
        # print(comm_split)
        comm_split[1] = path + comm_split[1]
        comm_split[3] = path + comm_split[3]
        command_new = ""
        for comm_split_i in comm_split:
            command_new+=comm_split_i + " "
        # print(command_new)

        os.system(command_new)

    os.system("echo All commands entered!")

# convert()