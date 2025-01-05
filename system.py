import os, sys, time, subprocess
try:
    from colorama import init, Fore
    init(autoreset=True)
except:
    print(Fore.RED+"FATAL 003: Color module error")
    input()
    exit()
def systema():
    print('''ConnectOS: OK
Modules: OK
ACPI: OK
PCI: OK
RAM\ROM: OK''')
    while True:
        comma=input("""Введите команду (help для помощи)
drv/ConnectOS>""")
        if comma=='help':print("""help: помощь
calc: калькулятор
info: информация о системе
md и rd: создать и удалить папки
vbs: проверка VBScript (ТОЛЬКО ДЛЯ WINDOWS)
""")
        if comma=='calc':
            try:
                print(eval(input('calc>')))
            except:
                print(Fore.YELLOW+'FAIL 006: Calculating error')
        if comma=='md':
            try:
                os.mkdir(input('md>'))
            except NotADirectoryError:
                print(Fore.YELLOW+'FAIL 007: Invalid directory name')
            except: print(Fore.YELLOW+'FAIL 008: Folder operation error')
        if comma=='rd':
            try:
                os.rmdir(input('rd>'))
            except NotADirectoryError:
                print(Fore.YELLOW+'FAIL 007: Invalid directory name')
            except: print(Fore.YELLOW+'FAIL 008: Folder operation error')
        if comma=='death':
            print(Fore.YELLOW+"FATAL 005: User-called error")
            input()
            exit()
        if comma=='info':
            print("""ConnectOS 1.0 (code 0)
January 5, 2025
by uid3333 (github)""")
        if comma=='vbs':
            subprocess.run(["cscript", "test.vbs"], check=True)

systema()
