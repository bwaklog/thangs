import mysql.connector as mysql
import pandas as pd
studentDetails = pd.DataFrame(
    data=None, columns=['Name', 'adno', 'DOB', 'Class', 'City'])
employeeDetails = pd.DataFrame(
    data=None, columns=['Name', 'empno', 'job', 'hireDate'])
feeDetails = pd.DataFrame(data=None, columns=['adno', 'fee', 'month'])
examDetails = pd.DataFrame(
    data=None, columns=['Name', 'adno', 'percentage', 'results'])


db = mysql.connect(host="localhost",
                   user="root",
                   passwd="1029Adity@",
                   db="test")
cur = db.cursor()


def selection():
    print("""
  DBMS for School Management
  1. Student Corner
  2. Employee Corner
  3. Fee
  4. Exam
  5. Exit
  """)
    choice = int(input("Please enter a valid choice: "))

    if (choice not in range(1, 6)):
        print("invalid selection. Redirecting to main page.....")
        selection()
    elif choice == 1:
        print("redirecting to Student's corner")
        studentCorner()
    elif choice == 2:
        print("redirecting to Employee's corner")
        employeeCorner()
    elif choice == 3:
        print("redirecting to Fee collection")
        feeCollection()
    elif choice == 4:
        print("redirecting to Exam Center")
        ExamCenter()
    else:
        return 5


def studentCorner():
    print("""
  1. New admission
  2. Update student details
  3. Issue Transfer Certificate
  """)
    choice = int(input("Please enter a valid choice for student corner: "))

    if (choice not in range(1, 4)):
        print("invalid selection. Redirecting to student corner.....")
        studentCorner()
    elif choice == 1:
        print("adding new admission........")
        add_details(dbm_no=1)
    elif choice == 2:
        print("Updating student details....")
        upd_details(dbm_no=1)
    elif choice == 3:
        print("Issuing Transfer Certificate....")
        del_details(dbm_no=1)
    print("""
  Redirecting to Main Page. 
  """)


def employeeCorner():
    print("""
  1. Add new employee details
  2. Update Employee details
  3. Delete Employee details
  """)
    choice = int(input("Please enter a valid choice for student corner: "))

    if (choice not in range(1, 4)):
        print("invalid selection. Redirecting to employee corner.....")
        employeeCorner()
    elif choice == 1:
        print("adding new employee........")
        add_details(dbm_no=2)
    elif choice == 2:
        print("Updating employee details....")
        upd_details(dbm_no=2)
    elif choice == 3:
        print("removing employee details....")
        del_details(dbm_no=2)
    print("""
  Redirecting to Main Page. 
  """)


def feeCollection():
    print("""
  1. Add new fee details
  2. Update fee details
  """)
    choice = int(input("Please enter a valid choice for student corner: "))

    if (choice not in range(1, 3)):
        print("invalid selection. Redirecting to employee corner.....")
        feeCollection()
    elif choice == 1:
        print("adding new admission........")
        add_details(dbm_no=3)
    else:
        print("Updating student details....")
        upd_details(dbm_no=3)
    print("""
  Redirecting to Main Page. 
  """)


def ExamCenter():
    print("""
  1. Add new exam details
  2. Update exam details
  3. Delete exam details
  """)
    choice = int(input("Please enter a valid choice for student corner: "))

    if (choice not in range(1, 4)):
        print("invalid selection. Redirecting to employee corner.....")
        ExamCenter()
    elif choice == 1:
        print("adding new exam details........")
        add_details(dbm_no=4)
    elif choice == 2:
        print("Updating exam details....")
        upd_details(dbm_no=4)
    else:
        print("Delete exam details....")
        del_details(dbm_no=4)
    print("""
  Redirecting to Main Page. 
  """)


def add_details(dbm_no):
    if dbm_no == 1:
        dsp_details(dbm_no=1)
        sname = input("Enter Student Name : ")
        admno = int(input("Enter Admission No : "))
        dob = input("Enter Date of Birth(yyyy-mm-dd): ")
        clas = input("Enter class for admission: ")
        cty = input("Enter City : ")

        query = f"INSERT INTO test.studentDetails (`Name`, `adno`, `dob`, `class`, `city`) VALUES ('{sname}','{admno}','{dob}','{clas}','{cty}')"
        cur.execute(query)
        db.commit()

        dsp_details(dbm_no=1)

    elif dbm_no == 2:
        dsp_details(dbm_no=2)
        ename = input("Enter Employee Name : ")
        empno = int(input("Enter Employee No : "))
        job = input("Enter Designation: ")
        hiredate = input("Enter date of joining: ")

        query = f"INSERT INTO test.empployeeDetails (`Name`, `empno`, `job`, `hiredate`) VALUES ('{ename}','{empno}','{job}','{hiredate}')"
        cur.execute(query)
        db.commit()

        dsp_details(dbm_no=2)

    elif dbm_no == 3:
        dsp_details(dbm_no=3)
        admno = int(input("Enter adm no: "))
        fee = float(input("Enter fee amount : "))
        month = input("Enter Month: ")

        query = f"INSERT INTO test.feeDetails (`adno`, `fee`, `month`) VALUES ('{admno}','{fee}','{month}')"
        cur.execute(query)
        db.commit()

        dsp_details(dbm_no=3)

    else:
        dsp_details(dbm_no=4)
        sname = input("Enter Student Name : ")
        admno = int(input("Enter Admission No : "))
        per = float(input("Enter percentage : "))
        res = input("Enter result: ")

        query = f"INSERT INTO test.examDetails (`admno`, `name`, `percentage`, `result`) VALUES ('{admno}','{sname}','{per}', '{res}')"
        cur.execute(query)
        db.commit()

        dsp_details(dbm_no=4)


def upd_details(dbm_no):
    if dbm_no == 1:
        dsp_details(dbm_no=1)
        admno = int(input('Enter valid admission number: '))
        print("""
    Select data to update: 
    1. name 
    2. date of birth
    3. class
    4. city
    """)
        choice = int(input('Enter valid choice: '))
        data = input('enter updated data: ')
        cnf = input('Change data(Y/N) ?: ')
        if cnf in ['y', 'Y'] and choice in (1, 2, 3, 4):
            if choice == 1:
                query = "UPDATE test.studentDetails SET name = '%s' WHERE adno = %d" % (
                    data, admno)
            elif choice == 2:
                query = "UPDATE test.studentDetails SET dob = '%s' WHERE adno = %d" % (
                    data, admno)
            elif choice == 3:
                query = "UPDATE test.studentDetails SET class = '%s' WHERE adno = %d" % (
                    data, admno)
            elif choice == 4:
                query = "UPDATE test.studentDetails SET city = '%s' WHERE adno = %d" % (
                    data, admno)

            cur.execute(query)
            db.commit()

            selection()

    elif dbm_no == 2:
        dsp_details(dbm_no=2)
        empno = int(input('Enter valid employee number: '))
        print("""
    Select data to change: 
    1. name 
    2. job
    3. hire date
    """)
        choice = int(input('Enter valid choice: '))
        data = input('enter updated data: ')
        cnf = input('Change data(Y/N) ?: ')
        if cnf in ['y', 'Y'] and choice in (1, 2, 3):
            if choice == 1:
                query = "UPDATE test.empployeeDetails SET Name = '%s' WHERE empno = %d" % (
                    data, empno)
            elif choice == 2:
                query = "UPDATE test.empployeeDetails SET job = '%s' WHERE empno = %d" % (
                    data, empno)
            elif choice == 3:
                query = "UPDATE test.empployeeDetails SET hiredate = '%s' WHERE empno = %d" % (
                    data, empno)

            cur.execute(query)
            db.commit()

            selection()

    elif dbm_no == 3:
        dsp_details(dbm_no=3)
        admno = int(input('Enter valid admission number: '))
        print("""
    Select data to change: 
    1. fee
    2. month
    """)
        choice = int(input('Enter valid choice: '))
        data = input('enter updated data: ')
        cnf = input('Change data(Y/N) ?: ')
        if cnf in ['y', 'Y'] and choice in (1, 2):
            if choice == 1:
                query = "UPDATE test.feeDetails SET fee = %s WHERE adno = %d" % (
                    data, admno)
            elif choice == 2:
                query = "UPDATE test.feeDetails SET month = '%s' WHERE adno = %d" % (
                    data, admno)

            cur.execute(query)
            db.commit()

            selection()

    else:
        dsp_details(dbm_no=4)
        admno = int(input('Enter valid admission number: '))
        print("""
    Select data to change: 
    1. student name 
    2. percentage
    3. final result
    """)
        choice = int(input('Enter valid choice: '))
        data = input('enter updated data: ')
        cnf = input('Change data(Y/N) ?: ')
        if cnf in ['y', 'Y'] and choice in (1, 2, 3):
            if choice == 1:
                query = "UPDATE test.examDetails SET Name = '%s' WHERE admno = %d" % (
                    data, admno)
            elif choice == 2:
                query = "UPDATE test.examDetails SET percentage = %s WHERE admno = %d" % (
                    data, admno)
            elif choice == 3:
                query = "UPDATE test.examDetails SET result = '%s' WHERE admno = %d" % (
                    data, admno)

            cur.execute(query)
            db.commit()

            selection()


def del_details(dbm_no):
    if dbm_no == 1:
        dsp_details(dbm_no=1)
        admno = int(input('Enter valid admission number: '))
        cnf = input('Change data(Y/N) ?: ')
        if cnf in ['y', 'Y']:
            # query = "DELETE FROM test.studentDetails where `adno`={admno};"
            query = "DELETE FROM test.studentDetails WHERE `adno`=%d" % (admno)
            cur.execute(query)
            db.commit()

            selection()

    elif dbm_no == 2:
        dsp_details(dbm_no=2)
        empno = int(input('Enter valid admission number: '))
        cnf = input('Change data(Y/N) ?: ')
        if cnf in ['y', 'Y']:
            query = "DELETE FROM test.empployeeDetails WHERE `empno`=%d" % (
                empno)
            cur.execute(query)
            db.commit()
            selection()

    else:
        dsp_details(dbm_no=4)
        admno = int(input('Enter valid admission number: '))
        cnf = input('Change data(Y/N) ?: ')
        if cnf in ['y', 'Y']:
            query = "DELETE FROM test.examDetails WHERE `admno`=%d" % (admno)
            cur.execute(query)
            db.commit()
            selection()


def dsp_details(dbm_no):
    if dbm_no == 1:
        print(studentDetails.head())
        sql = "SELECT * FROM studentDetails"
    elif dbm_no == 2:
        print(employeeDetails.head())
        sql = "SELECT * FROM empployeeDetails"
    elif dbm_no == 3:
        print(feeDetails.head())
        sql = "SELECT * FROM feeDetails"
    else:
        print(examDetails.head())
        sql = "SELECT * FROM examDetails"
    cur.execute(sql)
    for row in cur.fetchall():
        print(row)


while True:
    if selection() == 5:
        print("""
    Exiting system 
    Thank you. Have a good day!!!!
    """)
        db.close()
        break
