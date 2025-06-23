import mysql.connector
from datetime import date
from tabulate import tabulate


mycon = mysql.connector.connect(user='root', password='tiya', host='localhost', database='medical_management')
cursor = mycon.cursor()



def user_registration():
    print("\n==================================LOGIN/REGISTER===========================================\n")
    choice = int(input("\n1.Login\n2.Register\n3.Delete\n4.Exit\nEnter your choice:"))
    if choice == 1:
        UserName = input('Enter User Name: ')
        Password = input("Enter password:")
        us_query = "SELECT UserName FROM user_info where UserName =('%s')" % (UserName)
        cursor.execute(us_query)
        us_name = cursor.fetchall()
        pw_query = "SELECT Password FROM user_info where Password = ('%s')" % (Password)
        cursor.execute(pw_query)
        pwd = cursor.fetchall()
        if pwd != [] and us_name != []:
            us_name = us_name[0][0]
            pwd = pwd[0][0]
            print('LOGGED IN')
            print("\n===========================================================================================\n")

        else:
            print('Incorrect password or user name  !!')
            user_registration()
    elif choice == 2:
        scl_code = "KVGN"
        CODE = input("Enter School code:")
        if scl_code == CODE:
            UserName = input("Enter User Name:")
            Password = input("Enter password:")
            query = "select * from user_info"
            cursor.execute(query)
            rec = cursor.fetchall()
            for i in rec:
                if len(i) != 0:
                    if i[1]==Password:
                        print('Enter valid password .This password already exists!!!')
                        user_registration()
                    else:
                        pass
            Designation=input("Enter Designation:")
            if Designation == 'Doctor' or Designation == 'doctor' or Designation=='DOCTOR':
                print('You have successfully Registered sucessfully')
            elif Designation == 'Nurse' or Designation == 'nurse' or Designation=='NURSE':
                print('You have successfully Registered sucessfully')
            elif Designation == 'Teacher' or Designation == 'teacher' or Designation=='TEACHER':
                print('You have successfully Registered sucessfully')
            else:
                print('Incorrect credentials!!')
                user_registration()
            query = "insert into user_info(UserName,Password,Designation) values('{}','{}','{}')".format(UserName,Password,Designation)
            cursor.execute(query)
            mycon.commit()
        else:
            print("INVALID CODE")
            user_registration()
           
    elif choice == 3:
        a = input('Enter password to be deleted:')
        query = "select * from user_info where password=%s"
        t = (a,)
        cursor.execute(query,t)
        data=cursor.fetchall()
        if len(data)!=0:
            query = "delete from user_info where password=%s"
            t = (a,)
            cursor.execute(query,t)
            mycon.commit()
            print(cursor.rowcount, end=' record(s) deleted')
            user_registration()
        else:
            print('Invalid Password!!!')
            user_registration()
    elif choice == 4:
        quit()
    else:
        print("Please enter a valid choice!")
        user_registration()


user_registration()



def Add_product():
    print('ENTER DATA')
    BatchNo = input('Enter batch number:')
    query="select * from stock"
    cursor.execute(query)
    rec = cursor.fetchall()
    for i in rec:
        if len(i)!= 0:
            if i[0]==BatchNo:
                print('Enter valid Batch number .This Batch number already exists!!!')
                Add_product()
            else:
                pass

    Med_Name = str(input('Enter medicine name:'))
    Total_med = int(input("enter total no.of medicine available:"))
    Qty_issued = int(input('Enter quantity issued:'))
    remaining_med = Total_med - Qty_issued
    print('Remaining medicines=', remaining_med)
    query = "insert into stock(BatchNo,Med_Name,Total_med,Qty_issued,remaining_med)values('{}','{}',{},{},{})".format(BatchNo, Med_Name, Total_med, Qty_issued, remaining_med)
    cursor.execute(query)
    mycon.commit()
    option = input("Do you want to enter more(Y/N):")
    for i in option:
        if i == 'Y' or i=='y':
            Add_product()
        elif i== 'N'or i=='n':
            stock()
        else :
            print('invalid option')
        stock()


def delete_stud():
    admno = int(input('Enter Admission number to be deleted:'))
    query = "select * from student_registration where admno=%s"
    t = (admno,)
    cursor.execute(query,t)
    data=cursor.fetchall()
    if len(data)!=0:
        query = "delete from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query,t)
        mycon.commit()
        print(cursor.rowcount, end=' record(s) deleted')
    else:
        print('No such admission number found!!!')



def student_update():
    print("\n===========================================================================================\n")
    ch = int(input("\n1.Student Name\n2.Father name\n3.Mother name\n4.Class\n5.Section\n6.Physical_Marks\n7.Address\n8.Contact_no\n9.Email_id\n10.DOB\n11.Blood_group\n12.Exit\n Enter your choice what you want to update:"))

    if ch == 1:
        admno = int(input('Enter addmission where student name should be updated:'))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Stud_Name = input('Enter Student Name:')
            a = (Stud_Name, admno)
            query = "update student_registration set Stud_Name=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")
    elif ch == 2:
        admno = int(input("Enter addmission number for the student, where you want father's name to be updated:"))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Father_name = input("Enter father's Name:")
            a = (Father_name, admno)
            query = "update student_registration set Father_name=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")
    elif ch == 3:
        admno = int(input("Enter addmission number for the student, where you want mother's name to be updated:"))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Mother_name = input("Enter Mother's Name to be updated:")
            a = (Mother_name, admno)
            query = "update student_registration set Mother_name=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")
    elif ch == 4:
        admno = int(input("Enter addmission number for the student, where you want to update class:"))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Class = input("Enter class to be updated:")
            a = (Class, admno)
            query = "update student_registration set Class=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()

        else:
            print("No such admission number!")

    elif ch == 5:
        admno = int(input("Enter addmission number for the student, where you want to update section:"))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Section = input('Enter section to be updated:')
            a = (Section, admno)
            query = "update student_registration set Section=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")
    elif ch == 6:
        admno = int(input('Enter addmission number, where you want to update Physical Identification Marks:'))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Physical_Marks = input('Enter Physical Identification Mark:')
            a = (Physical_Marks, admno)
            query = "update student_registration set Physical_Marks=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")
    elif ch == 7:
        admno = int(input('Enter addmission number for the student,whose address you want to update:'))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Address = str(input('Enter address:'))
            a = (Address, admno)
            query = "update student_registration set Address=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")
    elif ch == 8:
        admno = int(input('Enter addmission number for the student whose contact number you want to update:'))

        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Contact_no = int(input("Enter student contact number:"))
            a = (Contact_no, admno)
            query = "update student_registration set Contact_no=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")
    elif ch == 9:
        admno = int(input('Enter addmission number for the student whose email id you want to be updated:'))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Email_id = str(input("Enter student email_id:"))
            a = (Email_id, admno)
            query = "update student_registration set Email_id=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")
    elif ch == 10:
        admno = int(input('Enter addmission number of the student whose Date of birth you want to be updated:'))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            DOB = str(input("Enter student date of birth:\n(Format::YYYY-MM-DD):"))
            a = (DOB, admno)
            query = "update student_registration set DOB=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")

    elif ch == 11:
        admno = int(input('Enter addmission number of the student whose blood group needs to be updated:'))
        query = "select * from student_registration where admno=%s"
        t = (admno,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Blood_group = str(input('Enter Blood group:'))
            a = (Blood_group, admno)
            query = "update student_registration set Blood_group=%s where admno=%s"
            cursor.execute(query, a)
            mycon.commit()
            print('Data updated successfully')
            print("\n===========================================================================================\n")
            student_update()
        else:
            print("No such admission number!")

    elif ch == 12:
        return

    else:
        print('Invalid option')
        student_update()


def stock():
    ch = int(input('\n1.Add products in Stock\n2.Display Products in Stock\n3.Update products in Stock\n4.Delete product\n5.Main Menu\nEnter choice:'))
    if ch == 1:
        Add_product()

    elif ch == 2:
        lquery = "select * from stock"
        cursor.execute(lquery)
        data = cursor.fetchall()
        if len(data)!=0:
            print(tabulate(data, headers=['BatchNo','Med_Name','Total_med','Qty_issued','remaining_med'], tablefmt='psql'))
        else:
            print('\n No more records')

    elif ch == 3:

        BatchNo = input('Enter batchno to be updated:')
        query = "select * from stock where BatchNo=%s"
        t = (BatchNo,)
        cursor.execute(query, t)
        rec = cursor.fetchall()
        if len(rec) != 0:
            Total_med = int(input("Enter total no.of medicine available:"))
            Qty_issued = int(input('Enter quantity issued:'))
            remaining_med = Total_med - Qty_issued
            print('Remaining medicines=', remaining_med)
            query = "update stock set Total_med=%s,Qty_issued=%s,remaining_med=%s where BatchNo=%s"
            t = (Total_med,Qty_issued,remaining_med, BatchNo)
            cursor.execute(query, t)
            mycon.commit()
            print('Record updated')
        else:
            print('No such batch number found')

    elif ch == 4:
     
            a = input('Enter Batch number to be deleted:')
            query = "delete from stock where BatchNo=%s"
            t = (a,)
            cursor.execute(query, t)
            mycon.commit()
            print(cursor.rowcount, end=' record(s) deleted')
            print('\nNOTE:If record deleted is 0 then batch number is not found')

       
    elif ch ==5:
        main()

    else:
        print('invalid option')


def view_studassess():
    CH=int(input("\n1. VIEW BY DATE\n2.VIEW BY ADMISSION NUMBER\nENTER CHOICE:"))
    if CH==1:
        Date = str(input('Enter Date(Format:YYYY-MM-DD):'))
        query = "select * from studassess where Date=%s"
        t=(Date,)
        cursor.execute(query,t)
        data = cursor.fetchall()
        if len(data) != 0:
            print("\n\n\n=====================================Student assessment detail======================================\n")

            print(tabulate(data, headers=['Date', 'Admission number','Reported for','Treatment given','Medicine Name','Qty issued'],tablefmt='psql'))
        else:
            print('\n No records in student assessment')
    elif CH==2:
        admno = int(input('Enter addmission number:'))
        query = "select * from studassess where admno=%s"
        t=(admno,)
        cursor.execute(query,t)
        data = cursor.fetchall()
        if len(data) != 0:
            print("\n\n\n=====================================Student assessment detail======================================\n")

            print(tabulate(data, headers=['Date', 'Admission number', 'Reported for','Treatment given','Medicine Name','Qty_issued'],tablefmt='psql'))
        else:
            print('\n No records in student assessment')

    else:
        print("INVALID OPTION")


def Registration_form():
    admno = int(input('Enter admission no\n(Enter carefully.Once entered, admission number cannot be change):'))
    Stud_Name = input("Enter Student's Name:")
    Father_name = input("Enter father's Name:")
    Mother_name = input("Enter mother's name:")
    Class = input('Enter Class(Roman Numerals):')
    Section = str(input('Enter section:'))
    Physical_Marks = input('Enter physical marks:')
    Address = input("Enter student address:")
    Contact_no = int(input("Enter student contact number:"))
    query="select * from student_registration"
    cursor.execute(query)
    rec = cursor.fetchall()
    for i in rec:
        if len(i) != 0:
            if i[8] ==Contact_no :
                print('Enter valid Contact number .This contact number already exists!!!')
                Registration_form()
            else:
                continue
    Email_id = input("Enter student email_id:")
    Gender = input("(Male or Female)Enter 'F' or 'M':")
    DOB = str(input('Enter Date of birth(Format:YYYY-MM-DD):'))
    Blood_group = str(input('Enter Blood group:'))

    Height = int(input('Enter height(in cm):'))
    Weight = int(input('Enter weight(in kg):'))
    BMI = round(Weight / (Height / 100) ** 2, 2)
    print('BMI IS :', BMI)

    Pre_existing_illness = input('Enter Pre-existing illness if any(else type no):')
    Drug_allergy = input('Enter allergy if any(else type no):')
    query = "insert into student_registration(admno,Stud_Name,Father_name,Mother_name,Class,Section,Physical_Marks,Address,Contact_no,Email_id,Gender,DOB,Blood_group,Height,Weight,BMI,Pre_existing_illness,Drug_allergy) values({},'{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}',{},{},{},'{}','{}')".format(
        admno, Stud_Name, Father_name, Mother_name, Class, Section, Physical_Marks, Address, Contact_no, Email_id,
        Gender, DOB, Blood_group, Height, Weight, BMI, Pre_existing_illness, Drug_allergy)
    cursor.execute(query)
    mycon.commit()
    print('~~~~Data added successfully~~~')


def studassess():
    admno = int(input('Enter addmission number:'))
    query = "select * from studassess"
    cursor.execute(query)
    rec = cursor.fetchall()
    for i in rec:
        if len(i) != 0:
            if i[0] == admno:
                print('Enter valid admno .This admno already exists!!!')
                studassess()
            else:
                pass
    qry = "select * from student_registration"
    cursor.execute(qry)
    rec = cursor.fetchall()
    for i in rec:
        if i[0] == admno:
            squery = "select Stud_Name,Class,Section from student_registration where admno=%s"
            t = (admno,)
            cursor.execute(squery, t)
            rec = cursor.fetchall()
            for i in rec:
                Stud_Name = i[0]
                Class = i[1]
                Section = i[2]
                print("Student's Name:", i[0])
                print("Class:", i[1])
                print("Section:", i[2])
    Date = date.today()
    print("Today's date is: ", Date)
    Reported_for = input('Enter your injury or illness:')
    Treatment = input('Enter treatment given:')
    Med_Name = input('Enter medicine given:')
    Qquery="select Med_Name from stock"
    Qty_issued = int(input('enter quantity issued\n(If given ointment measure in terms of number of units):'))
    query = "insert into studassess(Date,admno,Reported_for,Treatment,Med_Name,Qty_issued) values('{}',{},'{}','{}','{}',{})".format(Date, admno, Reported_for, Treatment, Med_Name, Qty_issued)
    cursor.execute(query)
    mycon.commit()
    print('Details entered successfully')


def view_stud():
    lquery = "select * from  student_registration"
    cursor.execute(lquery)
    data = cursor.fetchall()

    print("\n\n\n=====================================Student's detail======================================\n")
    if len(data) != 0:
        print(tabulate(data, headers=['Admission number', 'Student Name','Father name', 'Mother name', 'Class','Section','Physical Marks','Address','Contact number','Email id','Gender','DOB','Blood group','Height','Weight','BMI','Pre existing illness','Drug allergy'],tablefmt='psql'))
    else:
        print('\n No records found')


def main():
    while True:
        print("\n=====================================MAIN MENU=============================================\n")
        print(
            "\n1.STUDENT REGISTRATION\n2.STUDENT ASSESSMENT\n3.STOCK\n4.UPDATE STUDENT REGISTRATION\n5.VIEW STUDENT DETAILS\n6.DELETE STUDENT DETAILS\n7.VIEW STUDENT ASSESSMENT \n8.EXIT")
        ch = int(input('Enter your choice:'))
        if ch == 1:
            Registration_form()
        elif ch == 2:
            studassess()
        elif ch == 3:
            stock()
        elif ch == 4:
            student_update()
        elif ch == 5:
            view_stud()
        elif ch == 6:
            delete_stud()
        elif ch==7:
            view_studassess()
        elif ch==8:
            print('You successfully Logged out!')
            exit()
           
        else:
            print('Invalid option!!!!')


main()
