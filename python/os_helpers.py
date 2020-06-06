import os

#Check for OS type and clear terminal screen
def sys_clear():
    if os.uname().sysname == 'Windows':
        os.system('cls')
    else:
        os.system('clear')