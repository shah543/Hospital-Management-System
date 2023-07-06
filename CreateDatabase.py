
import mysql.connector

def createDb():
    conn = mysql.connector.connect(host='localhost',user='root',password='shahnawaz@12345')
    cur = conn.cursor(buffered=True)
    #print(conn.connection_id)
    try :
        cur.execute("create database hms_project;")
    except:
        print("DataBase Already Exist...")
        exit(0)
    cur.execute("use hms_project;")
    cur.execute("create table employee (id varchar(255),name varchar(255),sex varchar(255),age varchar(255),designation varchar(255),salary varchar(255),experience varchar(255),email varchar(255),mobile varchar(255));")
    cur.execute("create table patient (ID varchar(255),Name varchar(255),Gender varchar(255),DOB varchar(255),Blood_group varchar(255),Email varchar(255),Contact varchar(255),Alternate_Contact varchar(255),Address varchar(255),Consulting_Doctor varchar(255));")
    cur.execute("create table medicine (b1 varchar(255),b6 varchar(255),Medicine_Quantity varchar(255),Medicine_Price varchar(255));")
    cur.execute("create table appointment (e1 varchar(255), e2 varchar(255),Appointment_No varchar(255),e4 varchar(255),e5 varchar(255),e6 varchar(255));")
    cur.execute("create table treatment (Patient_ID varchar(255),b6 varchar(255),b7 varchar(255),Treatment_Cost varchar(255));")


    print("Database Created")

createDb()