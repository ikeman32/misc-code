import os

#Check for OS type and clear terminal screen
def sys_clear():
    if os.uname().sysname == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def sys_flush():
    os.sys.stdout.flush()

def sys_write(text, args):
    os.sys.stdout.write(text, % (args))