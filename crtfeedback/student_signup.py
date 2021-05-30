import getpass,sys,os
import pymysql
import time
class StudentRegister:
    def __init__(self):
        print("!!!!Student-Registration Form!!!!")
        self.email=input("Enter email : ")
        self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
        self.cur=self.con.cursor()
        sql="select count(name) from studentregister where email=%s"
        values=self.email
        self.cur.execute(sql,values)
        allRow=self.cur.fetchone()
        count=allRow[0]
        if count==1:
            print("You are already registered")
            time.sleep(2)
        else:
            self.name=input("Enter name : ")
            self.mobile=input("Enter mno : ")
            self.batch=int(input("Enter batch : "))
            self.subject=input("Enter subject : ")
            self.password=getpass.getpass(prompt="Enter password : ",stream=sys.stderr)
            sql1="insert into studentregister(name,email,mobile,batch,subject) values(%s,%s,%s,%s,%s)"
            values1=[self.name,self.email,self.mobile,self.batch,self.subject]
            sql2="insert into login(name,batch,password) values(%s,%s,%s)"
            values2=[self.email,self.batch,self.password]
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
            self.cur=self.con.cursor()
            self.cur.execute(sql1,values1)
            self.con.commit()
            self.con.close()
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
            self.cur=self.con.cursor()
            self.cur.execute(sql2,values2)
            self.con.commit()
            self.con.close()
            print('\tSystem is Loading, please wait....')
            print("registered successfully")
            time.sleep(3)
class login:
    def studentlogin(self,name,p,x):
            b=True
            self.name=name
            self.password=p
            self.batch=x
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
            self.cur=self.con.cursor()
            print(self.batch)
            sql="Select Count(name) from login where name=%s and password=%s and batch=%s"
            val=[self.name,self.password,self.batch]
            self.cur.execute(sql,val)
            data=self.cur.fetchone()
            count=int(data[0])
            print(count)
            if(count>0):
                b=True
            else:
                b=False
            return b
