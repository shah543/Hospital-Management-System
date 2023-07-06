from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font

import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='shahnawaz@12345',database="hms_project")
cur = conn.cursor(buffered=True)
print(conn.connection_id)

root = Tk()

class front:
    def __init__(self,master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry("800x600+0+0")
        self.master.config(bg="cadet blue")
        
        self.lblTitle = Label(self.master,text = "MAIN MENU", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        
        self.LoginFrame = Frame(self.master,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)

        self.button1 = Button(self.LoginFrame,text = "1.PATIENT REGISTRATION", width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Patient_Reg)       
        self.button1.grid(row=1,column=0,pady=10)
        
        self.button2 = Button(self.LoginFrame, text="2.ROOM ALLOCATION",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Room_Allocation)
        self.button2.grid(row=3,column=0,pady=10)
        
        self.button3 = Button(self.LoginFrame, text="3.EMPLOYEE REGISTRATION",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Employee_Reg)
        self.button3.grid(row=5,column=0,pady=10)
        
        self.button4 = Button(self.LoginFrame, text="4.BOOK APPOINTMENT",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Appointment_Form)
        self.button4.grid(row=7,column=0,pady=10)
        
        self.button5 = Button(self.LoginFrame, text="5.PATIENT BILL",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Billing_Form)
        self.button5.grid(row=9,column=0,pady=10)
        
        self.button6 = Button(self.LoginFrame, text="6.EXIT",width =30,font="Helvetica 14 bold",bg="cadet blue",command = master.destroy)
        self.button6.grid(row=11,column=0,pady=10)
         
    def Patient_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow)
            
    def Room_Allocation(self):
        self.newWindow = Toplevel(self.master)
        self.app = Room(self.newWindow)
            
    def Employee_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Employee(self.newWindow)
            
    def Appointment_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Appointment(self.newWindow)
        
    def Billing_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Billing(self.newWindow)



class Employee:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
 
        self.emp_ID=StringVar()
        self.emp_name=StringVar()
        self.emp_sex=StringVar()
        self.emp_age=IntVar()
        self.emp_type=StringVar()
        self.emp_salary=IntVar()
        self.emp_exp=StringVar()
        self.emp_email=StringVar()
        self.emp_phno=IntVar()

        self.lblTitle = Label(self.frame,text = "EMPLOYEE REGISTRATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
          
        self.lblempid = Label(self.LoginFrame,text="EMPLOYEE ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblempid.grid(row=0,column=0)
        self.lblempid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_ID)
        self.lblempid.grid(row=0,column=1)
        
        self.lblempname = Label(self.LoginFrame,text="EMPLOYEE NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblempname.grid(row=1,column=0)
        self.lblempname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_name)
        self.lblempname.grid(row=1,column=1)

        self.lblsex = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblsex.grid(row=2,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_sex)
        self.etype1.grid(row=2,column=1)
        
        self.lblage = Label(self.LoginFrame,text="AGE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblage.grid(row=3,column=0)
        self.lblage  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_age)
        self.lblage.grid(row=3,column=1)
        
        self.etype1=Label(self.LoginFrame,text="EMPLOYEE DESIGNATION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.etype1.grid(row=4,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_type)
        self.etype1.grid(row=4,column=1)

        self.lblCon = Label(self.LoginFrame,text="SALARY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblCon.grid(row=0,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_salary)
        self.lblCon.grid(row=0,column=3)
        
        self.lblAlt = Label(self.LoginFrame,text="EXPERIENCE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblAlt.grid(row=1,column=2)
        self.lblAlt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_exp)
        self.lblAlt.grid(row=1,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_phno)
        self.lbleid.grid(row=2,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=3,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_email)
        self.lbleid.grid(row=3,column=3)

        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_EMP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_DISPLAY)
        self.button3.grid(row=3,column=2)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = master.destroy)
        self.button6.grid(row=3,column=3)
            
    #FUNCTION TO INSERT DATA IN EMPLOYEE FORM   
    def INSERT_EMP(self):
        global e1,e2,e3,e4,e5,e6,e7,e8,e9
        e1=(self.emp_ID.get())
        e2=(self.emp_name.get())
        e3=(self.emp_sex.get())
        e4=(self.emp_age.get())
        e5=(self.emp_type.get())
        e6=(self.emp_salary.get())
        e7=(self.emp_exp.get())
        e8=(self.emp_email.get())
        e9=(self.emp_phno.get())
        val = [e1,e2,e3,e4,e5,e6,e7,e8,e9]
        print(val)
        quer ="select * from employee  where id = %s"
        quer1 = "insert into employee(id,name,sex,age,designation,salary,experience,email,mobile) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             
        p = cur.execute(quer,(e1,))
        q = cur.fetchall()
        print(p)
        if (len(q)!=0):
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE ID ALREADY EXISTS")     
        else:
            cur.execute(quer1,(e1,e2,e3,e4,e5,e6,e7,e8,e9,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")
        conn.commit()
                
    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def DE_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_EMP(self.newWindow)


#CLASS FOR DISPLAY MENU FOR DELETE EMPLOYEE
class D_EMP:
    def __init__(self,master):    
        global de1_emp
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_emp=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE EMPLOYEE WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
          
        self.lblpatid = Label(self.LoginFrame,text="ENTER EMPLOYEE ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_emp)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_EMP)
        self.DeleteB.grid(row=3,column=1)
        
    #FUNCTION TO DELETE DATA IN EMPLOYEE FORM 
    def DELETE_EMP(self):        
        global de,li
        li = str(self.de1_emp.get())
        de = [li]
        #conn = sqlite3.connect("HospitalDB.db")
        p = cur.execute("select * from employee where id=%s",de)
        if (p != 0):
            cur.execute("DELETE from employee where id=%s",de)
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DELETED")
            conn.commit() 
            
        else:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DOESN'T EXIST")
            



#Class for PATIENT REGISTRATION 
class Patient:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
    
        self.pat_ID=IntVar()
        self.pat_name=StringVar()
        self.pat_dob=StringVar()
        self.pat_address=StringVar()
        self.pat_sex=StringVar()
        self.pat_BG=StringVar()
        self.pat_email=StringVar()
        self.pat_contact=IntVar()
        self.pat_contactalt=IntVar()
        self.pat_CT=StringVar()

        self.lblTitle = Label(self.frame,text = "PATIENT REGISTRATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
      
        self.lblpatid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpatid.grid(row=0,column=1)
        
        self.lblPatname = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblPatname.grid(row=1,column=0)
        self.lblPatname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_name)
        self.lblPatname.grid(row=1,column=1)

        self.lblsex = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblsex.grid(row=2,column=0)
        self.lblsex  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_sex)
        self.lblsex.grid(row=2,column=1)

        self.lblDOB = Label(self.LoginFrame,text="DOB (YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblDOB.grid(row=3,column=0)
        self.lblDOB  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_dob)
        self.lblDOB.grid(row=3,column=1)
        
        self.lblbgrp = Label(self.LoginFrame,text="BLOOD GROUP",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblbgrp.grid(row=4,column=0)
        self.lblbgrp  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_BG)
        self.lblbgrp.grid(row=4,column=1)
        
        self.lblCon = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblCon.grid(row=0,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_contact)
        self.lblCon.grid(row=0,column=3)
        
        self.lblAlt = Label(self.LoginFrame,text="ALTERNATE CONTACT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblAlt.grid(row=1,column=2)
        self.lblAlt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_contactalt)
        self.lblAlt.grid(row=1,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_email)
        self.lbleid.grid(row=2,column=3)

        self.lbldoc = Label(self.LoginFrame,text="CONSULTING TEAM / DOCTOR",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldoc.grid(row=3,column=2)
        self.lbldoc  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_CT)
        self.lbldoc.grid(row=3,column=3)

        self.lbladd = Label(self.LoginFrame,text="ADDRESS",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbladd.grid(row=4,column=2)
        self.lbladd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_address)
        self.lbladd.grid(row=4,column=3)
        
        self.button2 = Button(self.LoginFrame2, text="SUBMIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_PAT)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.UPDATE_PAT)
        self.button3.grid(row=3,column=2)
        
        self.button4 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.D_DISPLAY)
        self.button4.grid(row=3,column=3)
        
        self.button5 = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.S_DISPLAY)
        self.button5.grid(row=3,column=4)
        
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = master.destroy)
        self.button6.grid(row=3,column=5)
            

    #FUNCTION TO INSERT DATA IN PATIENT FORM
    def INSERT_PAT(self):
        global pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10,ce1
        p1=(self.pat_ID.get())
        p2=(self.pat_name.get())
        p3=(self.pat_sex.get())
        p4=(self.pat_BG.get())
        p5=(self.pat_dob.get())
        p6=(self.pat_contact.get())
        p7=(self.pat_contactalt.get())
        p8=(self.pat_address.get())
        p9=(self.pat_CT.get())
        p10=(self.pat_email.get())

        quer ="select * from patient where ID = %s"
        quer1 = "insert into patient(ID,Name,Gender,DOB,Blood_group,Email,Contact,Alternate_Contact,Address,Consulting_Doctor) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             
        p = cur.execute(quer,(p1,))
        q = cur.fetchall()
        print(p)
        if (len(q)!=0):
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT_ID ALREADY EXISTS")     
        else:
            cur.execute(quer1,(p1,p2,p3,p5,p4,p10,p6,p7,p8,p9,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS INSERTED INTO DATABASE")
        conn.commit()
     
    #FUNCTION TO UPDATE DATA IN PATIENT FORM
    def UPDATE_PAT(self):
        global u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, ue1, conn
        conn.cursor()
        u1 = (self.pat_ID.get())
        u2 = (self.pat_name.get())
        u3 = (self.pat_sex.get())
        u4 = (self.pat_dob.get())
        u5 = (self.pat_BG.get())
        u6 = (self.pat_contact.get())
        u7 = (self.pat_contactalt.get())
        u8 = (self.pat_email.get())
        u9 = (self.pat_CT.get())
        u10 = (self.pat_address.get())
        
        quer ="update patient set Name=%s,Gender=%s,DOB=%s,Blood_group=%s,Address=%s,Email=%s,Consulting_Doctor=%s,Contact=%s,Alternate_Contact=%s where ID=%s"
        quer1 ="select * from patient where ID = %s"
        
        p = cur.execute(quer1,(u1,))
        q = cur.fetchall()
        print(p)
        
        if (len(q)!=0):
            cur.execute(quer,(u2,u3,u4,u5,u10,u8,u9,u6,u7,u1,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS UPDATED INTO DATABASE")
            conn.commit()

        else:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT REGISTERED")

    #FUNCTION TO OPEN DELETE PATIENT DISPLAY WINDOW
    def D_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DMenu(self.newWindow)
        
    #FUNCTION TO OPEN SEARCH PATIENT DISPLAY WINDOW
    def S_DISPLAY(self):
        self.newWindow= Toplevel(self.master)
        self.app = SMenu(self.newWindow)

#CLASS FOR DISPLAY MENU FOR DELETE PATIENT
class DMenu:
    def __init__(self,master):    
        global inp_d,entry1,DeleteB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.del_pid=IntVar()
        self.lblTitle = Label(self.frame,text = "DELETE WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.del_pid)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_PAT)
        self.DeleteB.grid(row=3,column=1)

    #FUNCTION TO DELETE DATA IN PATIENT FORM
    def DELETE_PAT(self):        
        global inp_d,del_pid,p,q
        inp_d = (self.del_pid.get())
        p=cur.execute("select * from patient where ID=%s", (inp_d,))
        q=cur.fetchall()
        if (len(q)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
        else:
            cur.execute('delete from patient where ID=%s',(inp_d,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DETAILS DELETED FROM DATABASE")
            conn.commit()

#CLASS FOR SEARCH MENU FOR SEARCH PATIENT
class SMenu:
    def __init__(self,master):    
        global inp_s,s_pid,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.s_pid=IntVar()
        self.lblTitle = Label(self.frame,text = "SEARCH WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
                
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO SEARCH",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.s_pid)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_PAT)
        self.SearchB.grid(row=0,column=1)
        
    #FUNCTION TO SEARCH DATA IN PATIENT FORM
    def SEARCH_PAT(self):
        global inp_s,s_pid,errorS,t,i,q,dis1,dis2,dis3,dis4,dis5,dis6,dis7,dis8,dis9,dis10,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,p
        inp_s=(self.s_pid.get())                
        p=cur.execute('select * from patient where ID=%s',(inp_s,))
        q=cur.fetchall()
        if (len(q)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","PATIENT RECORD NOT FOUND")
                    
        else:
            t=cur.execute('select * from patient where ID=%s',(inp_s,));
            x=cur.fetchall()
            for i in x:
                        self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l1.grid(row=1,column=0)
                        self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
                        self.dis1.grid(row=1,column=1)
                        
                        self.l2 = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l2.grid(row=2,column=0)
                        self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
                        self.dis2.grid(row=2,column=1)

                        self.l3 = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l3.grid(row=3,column=0)
                        self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
                        self.dis3.grid(row=3,column=1)

                        self.l4 = Label(self.LoginFrame,text="DOB (YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l4.grid(row=4,column=0)
                        self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[4])
                        self.dis4.grid(row=4,column=1)
                        
                        self.l5 = Label(self.LoginFrame,text="BLOOD GROUP",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l5.grid(row=5,column=0)
                        self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
                        self.dis5.grid(row=5,column=1)
                        
                        self.l6 = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l6.grid(row=1,column=2)
                        self.dis6  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[8])
                        self.dis6.grid(row=1,column=3)
                        
                        self.l7 = Label(self.LoginFrame,text="ALTERNATE CONTACT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l7.grid(row=2,column=2)
                        self.dis7  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[9])
                        self.dis7.grid(row=2,column=3)
                        
                        self.l8 = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l8.grid(row=3,column=2)
                        self.dis8  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[7])
                        self.dis8.grid(row=3,column=3)

                        self.l9 = Label(self.LoginFrame,text="CONSULTING TEAM / DOCTOR",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l9.grid(row=4,column=2)
                        self.dis9  = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[6])
                        self.dis9.grid(row=4,column=3)

                        self.l10 = Label(self.LoginFrame,text="ADDRESS",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                        self.l10.grid(row=5,column=2)
                        self.dis10 = Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[5])
                        self.dis10.grid(row=5,column=3)



#Class for ROOM ALLOCATION    
class Room:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        self.P_id=IntVar()
        self.room_t=StringVar()
        self.room_no=StringVar()
        self.rate=IntVar()
        self.da=StringVar()
        self.dd=StringVar()
      
        self.lblTitle = Label(self.frame,text = "ROOM ALLOCATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
         
        self.lblpatid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.P_id)
        self.lblpatid.grid(row=0,column=1)
        self.room_t1= Label(self.LoginFrame,text="ROOM TYPE\nSINGLE ROOM: Rs 4500\nTWIN SHARING : Rs2500\nTRIPLE SHARING: Rs2000\n",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.room_t1.grid(row=1,column=0)
        self.room_t1 = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.room_t)
        self.room_t1.grid(row=1,column=1)
        
        self.room_no1=Label(self.LoginFrame,text="ROOM NUMBER ",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.room_no1.grid(row=2,column=0)

        self.room_no1 = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.room_no)
        self.room_no1.grid(row=2,column=1)
        self.lblrate=Label(self.LoginFrame,text="ROOM CHARGES",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblrate.grid(row=0,column=2)
        self.lblrate=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.rate)
        self.lblrate.grid(row=0,column=3)
        self.lblda=Label(self.LoginFrame,text="DATE ADMITTED",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblda.grid(row=1,column=2)
        self.lblda=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.da)
        self.lblda.grid(row=1,column=3)
        self.lbldd=Label(self.LoginFrame,text="DATE DISCHARGED",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldd.grid(row=2,column=2)
        self.lbldd=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.dd)
        self.lbldd.grid(row=2,column=3)
 
        self.button2 = Button(self.LoginFrame2, text="SUBMIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command=self.INSERT_ROOM)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="cadet blue",command=self.UPDATE_ROOM)
        self.button3.grid(row=3,column=2)
        
        self.button5 = Button(self.LoginFrame2, text="ROOM DETAILS",width =15,font="Helvetica 14 bold",bg="cadet blue",command=self.SEARCH_ROOM)
        self.button5.grid(row=3,column=4)
        
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = master.destroy)
        self.button6.grid(row=3,column=5)
        
    #FUNCTION TO INSERT DATA IN ROOM ALLOCATION FORM
    def INSERT_ROOM(self):
        global r1,r2,r3,r4,r5,r6,conn,p
        r1=(self.P_id.get())
        r2=(self.room_t.get())
        r3=(self.room_no.get())
        r4=(self.rate.get())
        r5=(self.da.get())
        r6=(self.dd.get())
        p = cur.execute("select * from room where Room_No=%s",(r3,))
        q = cur.fetchall()
        
        if(len(q)!=0):
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","ROOM_NO IS CURRENTLY OCCUPIED")
        else:
            cur.execute("insert into room values(%s,%s,%s,%s,%s,%s)",(r1,r2,r3,r4,r5,r6,))
            tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM", "ROOM ALLOCATED")
            conn.commit()
            
    #FUNCTION TO OPEN SEARCH MENU IN ROOM ALLOCATION FORM
    def SEARCH_ROOM(self):
        self.newWindow= Toplevel(self.master)
        self.app = S_Room(self.newWindow)  

    #FUNCTION TO UPDATE DATA IN ROOM ALLOCATION FORM       
    def UPDATE_ROOM(self):
        global P_id,r1,r2,room_t,da,dd,rate,room_no,r3,r4,r5,r6,conn
        r1=(self.P_id.get())
        r2=(self.room_t.get())
        r3=(self.room_no.get())
        r4=(self.rate.get())
        r5=(self.da.get())
        r6=(self.dd.get())
        p = cur.execute("select * from room where ID=%s and Room_No=%s",(r1,r3,))
        q = cur.fetchall()
        if(len(q)!=0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT ALLOCATED A ROOM")
        else:
            cur.execute("update room set Room_No=%s,Room_Type=%s,Room_Rate=%s,Admission_Date=%s,Discharged_Date=%s where ID=%s",(r3, r2, r4, r5, r6,r1,))
            tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM", "ROOM DETAILS UPDATED")
            conn.commit()

#CLASS FOR DISPLAY MENU FOR SEARCH ROOM
class S_Room:
    def __init__(self,master):    
        global inp_s,entry,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.Pr_id=IntVar()
        self.lblTitle = Label(self.frame,text = "SEARCH PATIENT DETAILS", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO SEARCH",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.Pr_id)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.ROOM_DISPLAY)
        self.SearchB.grid(row=0,column=1)    

    #FUNCTION TO SEARCH DATA IN ROOM ALLOCATION FORM
    def ROOM_DISPLAY(self):
        global pat_rm,lr1,dis1,lr2,dis2,c1,i,conn,c1,Pr_id,p,t  
        pat_rm=(self.Pr_id.get())
        p=cur.execute("select * from room where ID=%s",(pat_rm,))
        q=cur.fetchall()
        if(len(q)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","PATIENT NOT ALLOCATED ROOM")
        else:
            t=cur.execute('select * from room where ID=%s',(pat_rm,));
            x=cur.fetchall()
            for i in x:
            
                self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l1.grid(row=1,column=0)
                self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
                self.dis1.grid(row=1,column=1)
                        
                self.l2 = Label(self.LoginFrame,text="ROOM TYPE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l2.grid(row=2,column=0)
                self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
                self.dis2.grid(row=2,column=1)

                self.l3 = Label(self.LoginFrame,text="ROOM NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l3.grid(row=1,column=2)
                self.dis3= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
                self.dis3.grid(row=1,column=3)

                self.l4 = Label(self.LoginFrame,text="ROOM RATE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l4.grid(row=2,column=2)
                self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
                self.dis4.grid(row=2,column=3) 



#Class for BOOKING APPOINTMENT   
class Appointment:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        self.pat_ID=IntVar()
        self.emp_ID=StringVar()
        self.ap_no=StringVar()
        self.ap_time=StringVar()
        self.ap_date=StringVar()
        self.des=StringVar()

        self.lblTitle = Label(self.frame,text = "APPOINTMENT FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
          
        self.lblpid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpid.grid(row=0,column=0)
        self.lblpid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpid.grid(row=0,column=1)
        
        self.lbldid = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldid.grid(row=1,column=0)
        self.lbldid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.emp_ID )
        self.lbldid.grid(row=1,column=1)
    
        self.lblap = Label(self.LoginFrame,text="APPOINTMENT NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblap.grid(row=2,column=0)
        self.lblap  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ap_no )
        self.lblap.grid(row=2,column=1)
            
        self.lblapt = Label(self.LoginFrame,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapt.grid(row=0,column=2)
        self.lblapt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ap_time )
        self.lblapt.grid(row=0,column=3)

        self.lblapd = Label(self.LoginFrame,text="APPOINTMENT DATE(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapd.grid(row=1,column=2)
        self.lblapd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.ap_date)
        self.lblapd.grid(row=1,column=3)
        
        self.lbldes = Label(self.LoginFrame,text="DESCRIPTION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldes.grid(row=2,column=2)
        self.lbldes  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.des)
        self.lbldes.grid(row=2,column=3)
        
        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_AP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_AP_DISPLAY)
        self.button3.grid(row=3,column=2)
         
        self.button3 = Button(self.LoginFrame2, text="SEARCH APPOINTMENTS",width =20,font="Helvetica 14 bold",bg="cadet blue",command= self.S_AP_DISPLAY)
        self.button3.grid(row=3,column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = master.destroy)
        self.button6.grid(row=3,column=4)
        
    #FUNCTION TO INSERT DATA IN APPOINTMENT FORM   
    def INSERT_AP(self):
        global e1,e2,e3,e4,e5,e6,var
        e1=(self.pat_ID.get())
        e2=(self.emp_ID.get())
        e3=(self.ap_no.get())
        e4=(self.ap_time.get())
        e5=(self.ap_date.get())
        e6=(self.des.get())
        p = cur.execute("select * from appointment where Appointment_No =%s",(e3,))
        q = cur.fetchall()
        if(len(q)!=0):
             tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "APPOINTMENT ALREADY EXISTS")     
        else:
            cur.execute("insert into appointment values(%s,%s,%s,%s,%s,%s)",(e1,e2,e3,e4,e5,e6,))
            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "APPOINTMENT SET SUCCSESSFULLY")
            conn.commit()

    #FUNCTION TO OPEN DELETE APPOINTMENT DISPLAY WINDOW
    def DE_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DEL_AP(self.newWindow)
        
    #FUNCTION TO OPEN SEARCH APPOINTMENT DISPLAY WINDOW
    def S_AP_DISPLAY(self):
        self.newWindow= Toplevel(self.master)
        self.app = SEA_AP(self.newWindow)
           

#CLASS FOR DISPLAY MENU FOR DELETE APPOINTMENT   
class DEL_AP:
    def __init__(self,master):    
        global de1_ap,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_ap=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)

        self.lblpatid = Label(self.LoginFrame,text="ENTER APPOINTMENT NO TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_ap)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_AP)
        self.DeleteB.grid(row=3,column=1)

    #FUNCTION TO DELETE DATA IN APPOINTMENT FORM      
    def DELETE_AP(self):        
        global inp_d,p
        inp_d = str(self.de1_ap.get())
        p=cur.execute("select * from appointment where Appointment_No=%s", (inp_d ,))
        q=cur.fetchall()
        if(len(q)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT APPOINTMENT NOT FIXED")     
        else:
            cur.execute("delete from appointment where Appointment_No=%s",(inp_d ,))
            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")
            conn.commit()
        
#CLASS FOR DISPLAY MENU FOR SEARCH APPOINTMENT          
class SEA_AP:
    def __init__(self,master):    
        global inp_s,entry,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.entry=StringVar()
        self.lblTitle = Label(self.frame,text = "SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
                 
        self.lblpatid = Label(self.LoginFrame,text="ENTER APPOINTMENTS NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.entry)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_AP)
        self.SearchB.grid(row=0,column=1)
        
    #FUNCTION TO SEARCH DATA IN APPOINTMENT FORM   
    def SEARCH_AP(self):
        global inp_s,entry,errorS,t,q,dis1,dis2,dis3,dis4,dis5,l1,l2,l3,l4,l5,p
        ap=(self.entry.get())
        p = cur.execute("select * from appointment where Appointment_No=%s", (ap,))
        q = cur.fetchall()
        if(len(q)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM","THERE'S NO APPOINTMENT BOOKED")
        else:
            t=cur.execute('select * from appointment where Appointment_No=%s',(ap,))
            x=cur.fetchall()
            for i in x:
                self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l1.grid(row=1,column=0)
                self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[0])
                self.dis1.grid(row=1,column=1)                        
                self.l2 = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l2.grid(row=2,column=0)
                self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="cadet blue",text=i[1])
                self.dis2.grid(row=2,column=1)

                self.l3 = Label(self.LoginFrame,text="APPOINTMENT NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l3.grid(row=3,column=0)
                self.dis3  = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[2])
                self.dis3.grid(row=3,column=1)

                self.l4 = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l4.grid(row=4,column=0)
                self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[3])
                self.dis4.grid(row=4,column=1)
                        
                self.l5 = Label(self.LoginFrame,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
                self.l5.grid(row=5,column=0)
                self.dis5 = Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=2,text=i[5])
                self.dis5.grid(row=5,column=1)


#Class for BILLING  
class Billing:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        
        self.P_id=IntVar()
        self.dd = StringVar()
        self.treat_1=StringVar()
        self.treat_2=StringVar()
        self.cost_t=IntVar()
        self.med=StringVar()
        self.med_q=IntVar()
        self.price=IntVar()
                
        self.lblTitle = Label(self.frame,text = "BILLING WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)

        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
      
        self.lblpid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpid.grid(row=0,column=0)
        self.lblpid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.P_id )
        self.lblpid.grid(row=0,column=1)
        
        self.lbldid = Label(self.LoginFrame,text="DATE DISCHARGED(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldid.grid(row=1,column=0)
        self.lbldid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.dd )
        self.lbldid.grid(row=1,column=1)       
        self.button2 = Button(self.LoginFrame, text="UPDATE DISCHARGE DATE",width =25,font="Helvetica 14 bold",bg="cadet blue",command = self.UPDATE_DATE)
        self.button2.grid(row=1,column=3)
        
        self.lbltreat= Label(self.LoginFrame,text="TREATMENT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbltreat.grid(row=2,column=0)
        self.lbltreat  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.treat_1 )
        self.lbltreat.grid(row=2,column=1) 
  
        self.lblcode_t1= Label(self.LoginFrame,text="TREATMENT CODE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblcode_t1.grid(row=3,column=0)
        self.lblcode_t1= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.treat_2)
        self.lblcode_t1.grid(row=3,column=1)

        self.lblap = Label(self.LoginFrame,text="TREATMENT COST ₹",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblap.grid(row=4,column=0)
        self.lblap  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.cost_t)
        self.lblap.grid(row=4,column=1)
            
        self.lblmed = Label(self.LoginFrame,text="MEDICINE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblmed.grid(row=2,column=2)
        self.lblmed  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.med)
        self.lblmed.grid(row=2,column=3)
        
        self.med_t1= Label(self.LoginFrame,text="MEDICINE QUANTITY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.med_t1.grid(row=3,column=2)
        self.med_t1 = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.med_q)
        self.med_t1.grid(row=3,column=3)
        
        self.lblapd = Label(self.LoginFrame,text="MEDICINE PRICE ₹",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapd.grid(row=4,column=2)
        self.lblapd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.price)
        self.lblapd.grid(row=4,column=3)
   
        self.button3 = Button(self.LoginFrame2, text="UPDATE DATA",width =15,font="Helvetica 14 bold",bg="cadet blue",command= self.UPDATE_DATA)
        self.button3.grid(row=3,column=2)
        
        self.button3 = Button(self.LoginFrame2, text="GENERATE BILL",width =15,font="Helvetica 14 bold",bg="cadet blue",command= self.GEN_BILL)
        self.button3.grid(row=3,column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = master.destroy)
        self.button6.grid(row=3,column=4)

    #FUNCTION TO UPDATE DATE IN BILLING FORM 
    def UPDATE_DATE(self):
        global b1,b2
        b1 = (self.P_id.get())
        b2 =(self.dd.get())  
        cur.execute("update room set Discharged_Date=%s where ID=%s", (b2, b1,))
        conn.commit()
        tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
        
    #FUNCTION TO UPDATE DATA IN BILLING FORM 
    def UPDATE_DATA(self):
        global c1,b1,P_id,b3,b4,b5,b6,dd,treat_1,treat_2,cost_t,b7,b8,med,med_q,price,u,p
        b1 = (self.P_id.get())
        b3 = (self.treat_1.get())
        b4 = (self.treat_2.get())
        b5 = (self.cost_t.get())
        b6 = (self.med.get())
        b7 = (self.med_q.get())
        b8 = (self.price.get())   
        p = cur.execute("select * from treatment where Patient_ID=%s", (b1,))
        q = cur.fetchall()
        if(len(q)!=0):
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT ID IS ALREADY REGISTERED")
        else:
            cur.execute("insert into treatment values(%s,%s,%s,%s)", (b1, b3, b4, b5,))
            cur.execute("insert into medicine values(%s,%s,%s,%s)",(b1,b6,b7,b8,))
            conn.commit()
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "BILLING DATA SAVED")
            
    #FUNCTION TO GENERATE BILL IN BILLING FORM 
    def GEN_BILL(self):
        global b1,u
        b1 = (self.P_id.get())
        u=cur.execute("select sum(Treatment_Cost+(Medicine_Price*Medicine_Quantity)+(Discharged_Date-Admission_Date)*Room_Rate) from room inner join treatment inner join medicine where ID=%s",(b1,))
        x=cur.fetchall()
        for i in x:
            self.pp=Label(self.LoginFrame,text="TOTAL AMOUNT",font="Helvetica 14 bold",bg="cadet blue",bd=22)
            self.pp.grid(row=5,column=0)
            self.uu=Label(self.LoginFrame,font="Helvetica 14 bold",bg="cadet blue",bd=22,text=i[0])
            self.uu.grid(row=5,column=1) 

front(root)
root.mainloop()