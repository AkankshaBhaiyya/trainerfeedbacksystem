import getpass,sys,os
from Admindash import *
import time
class Admin_login:
    def login(self):
        count=1
        while count<3:
            print("!!!!Admin-Login!!!!")
            self.name=input("Enter name : ")
            try:
                self.pwd=getpass.getpass(prompt="Enter password : ",stream=sys.stderr)
            except Exception as e:
                print("Error : ",e)
            print('\tSystem is Loading, please wait....')
            time.sleep(3)
            if(self.name=="admin" and self.pwd=="admin"):
                os.system('cls')
                Admin_dash()
            else:
                print("you entered wrong credentials")
                time.sleep(2)
                os.system('cls')
                count=count+1
        if count==3:
            print("Your time is out")
            print("Please try later")
            time.sleep(3)
            


