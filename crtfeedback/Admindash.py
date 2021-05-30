import pymysql,os
import time
a={}
s={}
n={}
class Admin_dash:
    def __init__(self):
        self.menu()
        self.name=None
        self.subject=None
        self.batch=None
        self.list1=[]
    def add(self):
        self.batch=int(input("Enter batch number of the trainer: "))
        self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
        self.cur=self.con.cursor()
        sql="select count(batch) from trainer where batch=%s"
        values=self.batch
        self.cur.execute(sql,values)
        allRow=self.cur.fetchone()
        count=allRow[0]
        self.con.commit()
        self.con.close()
        if count==1:
            print("You already entered details of the trainer of this batch")
            print("Press 1 to contine 0 to close : ")
            select=input()
            if(select=="0"):
                self.menu()
            else :
                    self.add()
        else:
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
            self.cur=self.con.cursor()
            self.name=input("Enter trainer name : ")
            self.subject=input("Enter subject : ")
            sql="insert into trainer(name,subject,batch) values(%s,%s,%s)"
            values=[self.name,self.subject,self.batch]
            self.cur.execute(sql,values)
            self.con.commit()
            self.con.close()
            print("Record added successfully !!!\nPress 1 to contine 0 to close : ")
            select=input()
            if(select=="0"):
                exit()
            else:
                os.system('cls')
                self.menu()
    def update(self):
        self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
        self.cur=self.con.cursor()
        self.name=input("Enter trainer name : ")
        self.subject=input("Enter updated subject : ")
        self.batch=int(input("Enter updated batch : "))
        sql="update trainer SET subject=%s,batch=%s WHERE name=%s"
        values=[self.subject,self.batch,self.name]
        self.cur.execute(sql,values)
        self.con.commit()
        self.con.close()
        print("Record updated successfully !!!\nPress 1 to contine 0 to close : ")
        select=input()
        if(select=="0"):
            exit()
        else:
            os.system('cls')
            self.menu()
    def delete(self):
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
            self.cur=self.con.cursor()
            self.name=input("Enter trainer name to delete : ")
            sql="delete from trainer WHERE name=%s"
            values=name
            self.cur.execute(sql,values)
            self.con.commit()
            self.con.close()
            print("Record deleted successfully !!!\nPress 1 to contine 0 to close : ")
            select=input()
            if(select=="0"):
                exit()
            else:
                os.system('cls')
                self.menu()
    def view(self):
            print("Id\tName\tSubject\tBatch")
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
            self.cur=self.con.cursor()
            sql="select * from trainer"
            self.cur.execute(sql)
            allRow=self.cur.fetchall()
            for row in allRow:
                    for column in row:
                            print(column,end='\t')
                    print('\r')
            self.con.commit()
            self.con.close()
            print('\r')
            print("Press 1 to contine 0 to close : ")
            select=input()
            if(select=="0"):
                exit()
            else:
                os.system('cls')
                self.menu()
    def judge(self):
            batch=int(input("Enter batch number of the trainer: "))
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
            self.cur=self.con.cursor()
            sql="select count(batch) from feedback where batch=%s"
            values=batch
            self.cur.execute(sql,values)
            allRow=self.cur.fetchone()
            count=allRow[0]
            if count==0:
                print("You entered wrong batch number")
                print("Press 1 to contine 0 to close : ")
                select=input()
                if(select=="0"):
                    self.menu()
                else :
                    self.judge()
                   
            else:
                self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
                self.cur=self.con.cursor()
                sql="select total from feedback where batch=%s"
                values=batch
                self.cur.execute(sql,values)
                allRow=self.cur.fetchall()
                val=0
                for row in allRow:
                    for column in row:
                           val=val+column
                global a
                a[batch]=val
                print(a)
                self.con.commit()
                self.con.close()
                self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
                self.cur=self.con.cursor()
                sql="select trainername from feedback where batch=%s"
                values=batch
                self.cur.execute(sql,values)
                allRow=self.cur.fetchone()
                name=allRow[0]
                global n
                n[batch]=name
                print(n)
                self.con.commit()
                self.con.close()
                self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
                self.cur=self.con.cursor()
                sql="select count(studentname) from feedback where batch=%s"
                values=batch
                self.cur.execute(sql,values)
                allRow=self.cur.fetchone()
                count=allRow[0]
                global s
                s[batch]=count
                print('\r')
                print("Press 1 to contine 0 to close : ")
                select=input()
                if(select=="0"):
                    exit()
                else:
                    os.system('cls')
                    self.menu()
    def cal(self):
        #print("{Batch : Points Earned }-->",a)
        #print("{Batch : Number of students}--> ",s)
        dict1={}
        result={}
        for key in a:
            if key in a and key in s:
                dict1[key]=15 * int(s[key])
        #print("{Batch : Max Points}--> ",dict1)
        for key in a:
            result[key]=[dict1[key],a[key]]
        #print("{Batch : [Points to be Earned , Points Earned ]}-->",result)
        diff={}
        for i in result:
            list1=[]
            list1.extend(result[i])
            dif=list1[0]-list1[1]
            diff[i]=dif
        #print("{Batch : Points lost}-->",diff)
        #print("{Batch : Trainer Name}-->",n)
        final={}
        for key in a:
            result[key]=[n[key],diff[key]]
        print("Batch : [Trainer Name , Points lost]")
        for i in result:
            print(i,'\t:\t',result[i])
        print("Press 1 to contine 0 to close : ")
        select=input()
        if(select=="0"):
            exit()
        else:
            os.system('cls')
            self.menu()

    def menu(self):
        while True:
            os.system('cls')
            print("!!!!Admin-DashBoard!!!!")
            print("1 Add Trainer")
            print("2 Update Trainer")
            print("3 Delete Trainer")
            print("4 View Trainers")
            print("5 Judgement")
            print("6 calculate")
            ch=int(input("Enter your choice : "))
            print('\tSystem is Loading, please wait....')
            time.sleep(3)
            if ch==1:
                os.system('cls')
                self.add()
            elif ch==2:
                os.system('cls')
                self.update()
            elif ch==3:
                os.system('cls')
                self.delete()
            elif ch==4:
                os.system('cls')
                self.view()
            elif ch==5:
                os.system('cls')
                self.judge()
            elif ch==6:
                os.system('cls')
                self.cal()
            else:
                print("Wrong entry")
                time.sleep(1)
                os.system('cls')
                self.menu
                break
