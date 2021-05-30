from Adminlogin import *
from student_menu import *
import os
import colorama
from colorama import Fore, Back, Style
import time
os.system('cls')
os.system('color 1B')
print(Fore.WHITE)
print('!!!!!!!!!!!! WELCOME TO TRAINING FEEDBACK SYSTEM !!!!!!!!')
print('\tSystem is Loading, please wait....')
time.sleep(5)
os.system('cls')
def menu():
    while True:
        print("!!!!MAIN-MENU!!!!")
        print(" 1 Admin")
        print(" 2 Student")
        ch=input("Enter your choice :")
        print('\tSystem is Loading, please wait....')
        time.sleep(5)
        if(ch=='1' or ch=='Admin'):
            os.system('cls')
            obj=Admin_login()
            obj.login()
            break
        elif(ch=='2' or ch=='Student'):
            Student()
            break
        else:
            print("Wrong entry")
            time.sleep(2)
            os.system('cls')
            menu()
menu()
