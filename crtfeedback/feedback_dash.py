import pymysql
import time
import getpass,sys,os
class feedback_dash:
    def __init__(self,name,batch):
        self.sname=name
        self.batch=batch
        self.tname=None
        self.trainingTechnique=None
        self.assignment=None
        self.realTimeExplanation=None
        self.total=None
        self.trainerDisplay()
        pass
    def trainerDisplay(self):
        self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
        self.cur=self.con.cursor()
        print("!!!!Trainer Information!!!!")
        print("Name\tBatch\tSubject")
        sql="select name,batch,subject from trainer where batch=%s"
        values=self.batch
        self.cur.execute(sql,values)
        allRow=self.cur.fetchall()
        for row in allRow:
            for column in row:
                print(column,end='\t')
            print('\r')
        time.sleep(3)
        self.con.commit()
        self.con.close()
        self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
        self.cur=self.con.cursor()
        sql="select name,subject from trainer where batch=%s"
        values=self.batch
        self.cur.execute(sql,values)
        data=self.cur.fetchone()
        self.tname=data[0]
        self.subject=data[1]
        self.con.commit()
        self.con.close()
        self.feedback()
    def feedback(self):
        os.system('cls')
        print("!!!!Feedback-Form!!!!")
        print("NOTE : Enter your points correctly as once you enter it is finalised")
        print("Your points should be of below mentioned pattern") 
        print("1 for worst")
        print("2 for Average")
        print("3 for Good")
        print("4 for Better")
        print("5 for Best")
        time.sleep(5)
        count=0
        f1=int(input("How you rate Training Technique of Trainer : "))
        f2=int(input("The assigments given by trainer are helpful to you : "))
        f3=int(input("Trainer's explanation using real time problems : "))
        self.total=f1+f2+f3
        self.trainingTechnique=f1
        self.assignment=f2
        self.realTimeExplanation=f3
        if((f1>0 and f1<6)and (f2>0 and f2<6) and (f3>0 and f3<6) and (self.total>0 and self.total<16)):
            self.con=pymysql.connect(host='127.0.0.1',user='root',passwd='',db='crtfeedback_db')
            self.cur=self.con.cursor()
            sql="insert into feedback(trainerName,studentName,batch,subject,trainingTechnique,assignment,realTimeExplanation,total)values(%s,%s,%s,%s,%s,%s,%s,%s)"
            values=[self.tname,self.sname,self.batch,self.subject,self.trainingTechnique,self.assignment,self.realTimeExplanation,self.total]
            self.cur.execute(sql,values)
            self.con.commit()
            self.con.close()
            print("Successfully your response is recorded")
            print("!!!!Thank You!!!!")
            time.sleep(2)
            exit()
        else:
            print("Enter once again correctly")
            count=count+1
            if(count<3):
                self.feedback()
