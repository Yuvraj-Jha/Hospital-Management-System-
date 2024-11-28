#COMPUTER PROJECT
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sql",database="HOSPITAL")
mycur=mydb.cursor()
def Make_Table():
    global mydb
    global mycur
    try:
        mycur.execute("CREATE TABLE PATIENT(PID INTEGER NOT NULL PRIMARY KEY,PNAME VARCHAR(20),DISEASE VARCHAR(30),DOCTOR_NAME VARCHAR(10),DOCTOR_FEE INTEGER)")
        mycur.execute("CREATE TABLE MED(PID INTEGER NOT NULL PRIMARY KEY,ADMITTED VARCHAR(3),NO_OF_DAYS INTEGER, ROOM_TYPE VARCHAR(20),ROOM_CHARGE INTEGER,TEST_FEE INTEGER,MEDICINE_FEE INTEGER,TOTAL_AMOUNT INTEGER)")
        print("TABLE CREATED")
    except:
        print("ERROR IN CONNECTION")
def insert():
    global mydb
    global mycur
    try:
        id=int(input("ENTER PATIENT ID:- "))
        nm=input("ENTER PATIENT NAME:- ")
        ds=input("ENTER PATIENT DISEASE:- ")
        dr=input("ENTER DOCTOR NAME:- ")
        f=int(input("ENTER DOCTOR FEE :- "))
        mycur.execute("INSERT INTO PATIENT(PId,PNAME,DISEASE,DOCTOR_NAME,DOCTOR_FEE) VALUES({},'{}','{}','{}',{})".format(id,nm,ds,dr,f))
        mydb.commit()
        print("RECORD ADDED SUCCESSFULLY")
    except:
        print("UNABLE TO INSERT RECORD")
def insert_med():
    global mydb
    global mycur
    try:
        ad=input("ENTER YES OR NO FOR ADMITED:- ")
        if ad.lower()=="yes":
            id=int(input("ENTER PATIENT ID:- "))
            n=int(input("ENTER NUMBER OF DAYS ADMITED:- "))
            rt=input("ENTER ROOM TYPE:- ")
            rc=int(input("ENTER ROOM CHARGE:- "))
            tf=int(input("ENTER TEST FEE:- "))
            mf=int(input("ENTER MEDICINE FEE:- "))
            ta=(n*rc)+tf+mf
            mycur.execute("INSERT INTO MED(PID,ADMITTED,NO_OF_DAYS,ROOM_TYPE,ROOM_CHARGE,TEST_FEE,MEDICINE_FEE,TOTAL_AMOUNT) VALUES({},'{}',{},'{}',{},{},{},{})".format(id,ad,n,rt,rc,tf,mf,ta))
            mydb.commit()            
            print("RECORD ADDED SUCCESSFULLY")
    except:
        print("ERROR")
def display_all():
    global mydb
    global mycur
    def display_all_patient_table():
        try:
            mycur.execute("SELECT * FROM PATIENT")
            rec=mycur.fetchall()
            for i in rec:
                print(i)
        except:
            print("UNABLE TO DISPLAY")
    def display_all_medicine_table():
        count=0
        try:
            mycur.execute("SELECT * FROM MED")
            rec=mycur.fetchall()
            for i in rec:
                print(i)
                count+=1
        except:
            print("UNABLE TO DISPLAY")
    while True:
        print("1: DISPLAY ALL RECORD OF PATIENT TABLE")
        print("2: DISPLAY ALL RECORD OF MEDICINE TABLE")
        ch=int(input("Enter Your Choice:- "))
        if ch==1:
            display_all_patient_table()
        elif ch==2:
            display_all_medicine_table()
        else:
            break
def describe():
    def describe_patient():
        global mydb
        global mycur
        try:
            mycur.execute("DESC PATIENT")
            for i in mycur:
                print(i)
        except:
            print("UNABLR TO DESCRIBE")
    def describe_med():
        global mydb
        global mycur
        try:
            mycur.execute("DESC MED")
            for i in mycur:
                print(i)
        except:
            print("UNABLR TO DESCRIBE")
    while True:
        print("1: DISCRIBE PATIENT TABLE")
        print("2: DISCRIBE MEDICINE TABLE")
        ch=int(input("Enter Your Choice:- "))
        if ch==1:
            describe_patient()
        elif ch==2:
            describe_med()
        else:
            break
def display():
    def display_by_id():
        global mydb
        global mycur
        try:
            pd=int(input("Enter Patient Id:- "))
            mycur.execute("SELECT * FROM PATIENT WHERE PID={}".format(pd))
            r=mycur.fetchone()
            print(r)
        except:
            print("Record Doesnot Exist")
    def display_by_name():
        global mydb
        global mycur
        try:
            nm=input("Enter Patient Name:- ")
            mycur.execute("SELECT * FROM PATIENT WHERE PNAME='{}'".format(nm))
            r=mycur.fetchone()
            print(r)
        except:
            print("Record Doesnot Exist")
    def display_by_disease():
        global mydb
        global mycur
        try:
            d=input("Enter Patient Disease:- ")
            mycur.execute("SELECT * FROM PATIENT WHERE DISEASE='{}'".format(d))
            r=mycur.fetchall()
            print(r)
        except:
            print("Record Doesnot Exist")
    def display_by_doctor_name():
        global mydb
        global mycur
        try:
            dn=input("Enter Doctor Name:- ")
            mycur.execute("SELECT * FROM PATIENT WHERE DOCTOR_NAME='{}'".format(dn))
            r=mycur.fetchall()
            print(r)
        except:
            print("Record Doesnot Exist")
    while True:
        print("1: DISPLAY BY PATIENT ID")
        print("2: DISPLAY BY PATIENT NAME")
        print("3: DISPLAY BY PATIENT DISEASE")
        print("4: DISPLAY BY PATIENT DOCTOR NAME")
        ch=int(input("ENTER YOUR CHOICE:- "))
        if ch==1:
            display_by_id()
        elif ch==2:
            display_by_name()
        elif ch==3:
            display_by_disease()
        elif ch==4:
            display_by_doctor_name()
        else:
            break
def deleat():
    global mydb
    global mycur
    try:
        id=int(input("ENTER PATIENT ID TO DELEAT IT:- "))
        mycur.execute("SELECT * FROM PATIENT WHERE PID="+str(id))
        result=mycur.fetchone()
        if mycur.rowcount<=0:
            print("SORRY NO MATCHING DETAILS AVAILABLE")
        else:
            for row in result:
                ans=input("ARE YOU SURE TO DELETE?(y/n)")
                if ans=="Y" or ans=="y":
                    mycur.execute("DELETE FROM PATIENT WHERE PID="+str(id))
                    mycur.execute("DELETE FROM MED WHERE PID="+str(id))
                    mydb.commit()
                    print("RECORD DELETED SUCCESSFULLY")
                    break
                else:
                    break
    except:
        print("RECORD DOESNOT EXIST")
def show():
    global mydb
    global mycur
    try:
        mycur.execute("SHOW TABLES")
        for x in mycur:
            print(x)
    except:
        print("TABLES DOESNOT EXIST")
def delete_all():
    global mydb
    global mycur
    try:
        mycur.execute("DELETE  FROM PATIENT")
        mycur.execute("DELETE  FROM MED")
        mydb.commit()
        print("RECORD DELETED SUCCESSFULLY")
    except:
        print("TABLE EMPTY")
def gen_bill():
    global mydb
    global mycur
    id=int(input("ENTER PATIENT ID:- "))
    mycur.execute("SELECT * FROM MED WHERE PID='{}'".format(id))
    res=mycur.fetchone()
    sum=0
    if mycur.rowcount<=0:
        print("SORRY NO MATCHING DETAILS AVAILABLE")
    else:
        print("PID:- ",res[0]," "*40,"ROOM TYPE:-",res[3])
        print("NO. DAYS ADMITED:- ",res[2])
        print("="*70)
        print(" "*10,"Billing Name"," "*15,"Amount"," "*10,"TOTAL AMOUNT")
        print("="*70)
        print(" "*9,"1. ROOM CHARGES"," "*14,res[4]," "*15,(res[4]*res[2]))
        print(" "*9,"2. TEST_FEE"," "*18,res[5]," "*14,(res[5]*res[2]))
        print(" "*9,"3. MEDICINE_FEE"," "*34,res[6])
        sum=sum+(res[4]*res[2])+(res[5]*res[2]+res[6])
        print("="*70)
        print(" "*15,"TOTAL AMOUNT"," "*31,sum)
def update():
    global mydb
    global mycur
    def update_patient():
        global mydb
        global mycur
        def patient_name():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            nm=input("ENTER NEW PATIENT NAME:- ")
            try:
                mycur.execute("UPDATE PATIENT SET PNAME='{}' WHERE PID={}".format(nm,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        def patient_disease():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            di=input("ENTER PATIENT DISEASE:- ")
            try:
                mycur.execute("UPDATE PATIENT SET DISEASE='{}' WHERE PID={}".format(di,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        def patient_dr_name():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            dn=input("ENTER PATIENT DOCTOR NAME:- ")
            try:
                mycur.execute("UPDATE PATIENT SET DOCTOR_NAME='{}' WHERE PID={}".format(dn,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        def patient_dr_fee():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            df=input("ENTER PATIENT DOCTOR FEE:- ")
            try:
                mycur.execute("UPDATE PATIENT SET DOCTOR_FEE={} WHERE PID={}".format(df,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        while True:
            print("1: UPDATE PATIENT NAME")
            print("2: UPDATE PATIENT DISEASE")
            print("3: UPDATE PATIENT DOCTOR NAME")
            print("4: UPDATE PATIENT DOCTOR FEE")
            ch=int(input("ENTER YOUR CHOICE:- "))
            if ch==1:
                patient_name()
            elif ch==2:
                patient_disease()
            elif ch==3:
                patient_dr_name()
            elif ch==4:
                patient_dr_fee()
            else:
                break
    def update_medicine():
        global mydb
        global mycur
        def update_no_of_days():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            dy=int(input("ENTER NEW NUMBERS OF DAYS TO BE ADMITTED:- "))
            try:
                mycur.execute("UPDATE MED SET NO_OF_DAYS={} WHERE PID={}".format(dy,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        def update_room_type():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            rt=input("ENTER NEW ROOM TYPE:- ")
            try:
                mycur.execute("UPDATE MED SET  ROOM_TYPE='{}' WHERE PID={}".format(rt,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        def update_room_charge():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            rc=int(input("ENTER NEW ROOM CHARGE:- "))
            try:
                mycur.execute("UPDATE MED SET ROOM_CHARGE={} WHERE PID={}".format(rc,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        def update_test_fee():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            tf=int(input("ENTER NEW TEST FEE:- "))
            try:
                mycur.execute("UPDATE MED SET TEST_FEE={} WHERE PID={}".format(tf,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        def update_medicine_fee():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            mf=int(input("ENTER NEW MEDICINE FEE:- "))
            try:
                mycur.execute("UPDATE MED SET  MEDICINE_FEE={} WHERE PID={}".format(mf,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        def update_total_amount():
            global mydb
            global mycur
            id=int(input("ENTER PATIENT ID:- "))
            ta=int(input("ENTER NEW TOTAL AMOUNT:- "))
            try:
                mycur.execute("UPDATE MED SET TOTAL_AMOUNT={} WHERE PID={}".format(ta,id))
                mydb.commit()
                print("RECORD UPDATED SUCCESSFULLY")
            except:
                print("UNABLE TO UPDATE")
        while True:
            print("1:UPDATE NO OF DAYS ADMITED IN HOSPITAL")
            print("2:UPDATE ROOM TYPE")
            print("3:UPDATE ROOM CHARGES")
            print("4:UPDATE TEST FEE")
            print("5:UPDATE MEDICINE FEE")
            print("6:UPDATE TOTAL AMOUNT")
            ch=int(input("ENTER YOUR CHOICE:- "))
            if ch==1:
                update_no_of_days()
            elif ch==2:
                update_room_type()
            elif ch==3:
                update_room_charge()
            elif ch==4:
                update_test_fee()
            elif ch==5:
                update_medicine_fee()
            elif ch==6:
                update_total_amount()
            else:
                break
    while True:
        print("1:UPDATE PATIENT TABLE")
        print("2:UPDATE MEDICINE TABLE")
        ch=int(input("ENTER YOUR CHOICE:- "))
        if ch==1:
            update_patient()
        elif ch==2:
            update_medicine()
        else:
            break
def detail():
    print("*"*75)
    print(" "*10,"AUTHOR"," "*11,"MOBILE NUMBER"," "*13,"EMAIL")
    print("*"*75)
    print("1:"," "*4,"YUVRAJ KUMAR JHA"," "*7,"6204572445"," "*7,"yuvrajjharnc@gmail.com")
    print("2:"," "*4,"ADITI BHATTACHARJEE"," "*4,"9341932835"," "*7,"yeathatsmeadt@gmail.com")
    print("3:"," "*4,"KUNJAL DHAN"," "*12,"6207576119"," "*7,"kunjaldhan17@gmail.com")
while True:
    print("*"*75)
    print(" "*20,"HOSPITAL MANAGMENT SOFTWARE")
    print("*"*75)
    print("1: MAKE TABLE")
    print("2: ADD NEW PATIENT")
    print("3: ADD MEDICINE AMOUNT")
    print("4: DISPLAY ALL PATIENT")
    print("5: DISCRIBE TABLE")
    print("6: DISPLAY BY HEADING")
    print("7: DELETE PATIENT INFO")
    print("8: DELETE ALL PATIENT")
    print("9: SHOW TABLES")
    print("10: TO UPDATE RECORD")
    print("11: GENERATE BILL")
    print("12: AUTHOR DETAIL")
    ch=int(input("ENTER YOUR CHOICE:- "))
    if ch==1:
        Make_Table()
    elif ch==2:
        insert()
    elif ch==3:
        insert_med()
    elif ch==4:
        display_all()
    elif ch==5:
        describe()
    elif ch==6:
        display()
    elif ch==7:
        deleat()
    elif ch==8:
        delete_all()
    elif ch==9:
        show()
    elif ch==10:
        update()
    elif ch==11:
        gen_bill()
    elif ch==12:
        detail()
    else:
        mydb.close
        print(" "*30,"BYE")
        break