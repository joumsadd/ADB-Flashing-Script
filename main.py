import os
import subprocess
import sys
import time
import tkinter.messagebox as mbox

def check_fastboot_connection():
    os.chdir("C:\\adb")
    result = subprocess.run(["fastboot", "devices"], capture_output=True, text=True)
    return "fastboot" in result.stdout

lang = input("Select your language (ENG / RUS): ")

if lang.lower() in ["rus", "ru"]:
    while True:
        msg = mbox.askyesno(title="Подключение", message="Смартфон подключен к ПК в режиме FASTBOOT?")
        if msg:
            print('Проверка...')
            if check_fastboot_connection():
                print("Телефон подключен")
                print("Запускаю...")
                time.sleep(0.5)
                os.chdir("C:\\ADBScript")
                subprocess.call("start adb.bat", shell=True)
                break
            else:
                mbox.showerror(title="Ошибка!", message="Смартфон не подключен в режиме FASTBOOT")
                break

        else:
            mbox.showerror("Выход", "Подключите смартфон к ПК и запустите скрипт заново")
            sys.exit()

elif lang.lower() in ["eng", "en"]:
    while True:
        msg = mbox.askyesno(title="Connection", message="Is the smartphone connected to the PC in FASTBOOT mode?")
        if msg:
            print('Checking...')
            if check_fastboot_connection():
                print("Phone connected")
                print("Starting...")
                time.sleep(0.5)
                os.chdir("C:\\ADBScript")
                subprocess.call("start adb.bat", shell=True)
                break
            else:
                mbox.showerror(title="Error!", message="Smartphone is not connected in FASTBOOT mode")
                break

        else:
            mbox.showerror(title="Exit", message="Connect the smartphone to the PC in FASTBOOT mode and run the script again")
            sys.exit()
else:
    mbox.showerror(title="Error", message="Select your language (ENG / RUS) and try again")
    sys.exit()
