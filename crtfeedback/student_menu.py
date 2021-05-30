from feedback_dash import *
from student_signup import *
import pymysql
import getpass,sys,os
import time
def Student():
    os.system('cls')
    print("!!!!Student-DashBoard!!!!")
    print("1 register")
    print("2 login")
    ch=int(input("Enter your choice  : "))
    print('\tSystem is Loading, please wait....')
    time.sleep(3)
    if(ch==1):
            os.system('cls')
            obj=StudentRegister()
            Student()
            
    elif(ch==2):
            os.system('cls')
            obj=login()
            print("!!!!Student-Login!!!!")
            name=input("Enter name/email : ")
            con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
            cur=con.cursor()
            sql="select count(studentname) from feedback where studentname=%s"
            values=name
            cur.execute(sql,values)
            allRow=cur.fetcho
            ne()
            count=allRow[0]
            if count==1:
                time.sleep(2)
                print("Your response is already recorded")
            else:
                pwd=getpass.getpass(prompt="Enter password")
                batch=int(input("Enter batch : "))
                result=obj.studentlogin(name,pwd,batch)
                while not result:
                    print("login failed")
                    name=input("Enter username/email : ")
                    pwd=getpass.getpass(prompt="Enter password : ")
                    result=obj.studentlogin(name,pwd,batch)
                if result==True:
                    os.system('cls')
                    obj=feedback_dash(name,batch)
                    Student()

    else:
            print("Wrong entry")
            
            
        
