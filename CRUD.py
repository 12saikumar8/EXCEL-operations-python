import mysql.connector

mysqldb=mysql.connector.connect(host="localhost",user="root",password="Saikumar1@",database="testdb")

mysqlcursor=mysqldb.cursor()
# Creating (CREATE)
# mysqlcursor.execute("create table student_details(rollno INT, name VARCHAR(30), Marks INT")

# insert into table (READ)

'''try:
    mysqlcursor.execute("insert into student_details(rollno, name, Marks) values (2,'sam',34)")

    mysqldb.commit()
    print("Record inserted into table")
except:
        mysqldb.rollback()
mysqldb.close()

try:
    mysqlcursor.execute("select * from student_details where Marks=34")
    result=mysqlcursor.fetchall()
    for i in result:
        roll=i[0]
        name=i[1]
        Marks=i[2]
        print(roll,name,Marks)
except:
    print("some error")
    

    #UPDATE THE RECORD
try:
    mysqlcursor.execute("update student_details set name='anaya' where rollno = 2")
    mysqldb.commit()
except:
    mysqldb.rollback()
mysqldb.close() 


# DELETE the Record

try:
    mysqlcursor.execute("delete from  student_details where rollno = 2")
    mysqldb.commit()
    print("deleted")
except:
    mysqldb.rollback()
mysqldb.close() '''

#inserting into table again
try:
    mysqlcursor.execute("insert into student_details(rollno, name, Marks) values (1,'Vikram',93)")
    mysqldb.commit()
    print("Happend")
except:
    mysql.rollback()
mysqldb.close()





