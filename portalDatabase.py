import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="teachers_portal",
                 user='root',
                 password='root'):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)

            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)

    def getAllStudents(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            self.cursor.callproc("studentsWithGrade")
            records = self.cursor.stored_results()
            return records

    def addStudent(self, name, courseID, grade=0):
        if self.connection.is_connected():
            try:
                self.cursor = self.connection.cursor()
                sql = "INSERT INTO students (studentName, enrolledInCourseID, grade) VALUES (%s, %s, %s)"
                val = (name, courseID, grade)
                self.cursor.execute(sql, val)
                self.connection.commit()
                return True
            except Exception as e:
                print(e.__cause__)
        return False

    def addCourse(self, name):
        if self.connection.is_connected():
            try:
                self.cursor = self.connection.cursor()
                sql = f"Insert into courses (courseName) values ('{name}');"
                self.cursor.execute(sql)
                self.connection.commit()
                return True
            except Exception as e:
                print(e)
        return False

    def modifyGrade(self, studentID, grade):
        if self.connection.is_connected():
            try:
                self.cursor = self.connection.cursor()
                sql = f"update students set grade = {grade} where studentID = {studentID};"
                self.cursor.execute(sql)
                self.connection.commit()
                return True
            except Exception as e:
                print(e.__cause__)
        return False

    def searchStudentById(self, studentID):
        if self.connection.is_connected():
            try:
                self.cursor = self.connection.cursor()
                sql = f"SELECT * FROM teachers_portal.students where studentID = {studentID};"
                # val = studentID
                self.cursor.execute(sql)
                myresult = self.cursor.fetchone()
                return myresult
            except Exception as e:
                print(e.__cause__)
        return None

