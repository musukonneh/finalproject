from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from portalDatabase import Database
import cgi


class PortalServer(BaseHTTPRequestHandler):

    def __init__(self, *args):
        self.database = Database()
        BaseHTTPRequestHandler.__init__(self, *args)

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        try:
            if self.path == '/addStudent':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                student_name = form.getvalue("sname")
                student_courseid = int(form.getvalue("courseid"))
                student_grade = float(form.getvalue("sgrade"))
                ##Call the Database Method to a add a new student
                '''
                    Example call: self.database.addStudent(student_name, student_courseid,student_grade)
                '''

                done = self.database.addStudent(student_name, student_courseid, student_grade)

                print("grabbed values", student_name, student_courseid, student_grade)

                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/modifyStudent'>Modify Student</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr>")
                if done:
                    self.wfile.write(b"<h3>Student have been added</h3>")
                    self.wfile.write(b"<div><a href='/addStudent'>Add A New Student</a></div>")
                else:
                    self.wfile.write(b"<h3>Student not added</h3>")
                    self.wfile.write(b"<div><a href='/addStudent'>Retry again</a></div>")
                self.wfile.write(b"</center></body></html>")
            elif self.path == "/searchStudent":
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                student_id = form.getvalue("sid")

                student = self.database.searchStudentById(student_id)

                # print(student)

                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                             <a href='/addStudent'>Add Student</a>|\
                                              <a href='/addCourse'>Add Course</a>|\
                                              <a href='/modifyStudent'>Modify Student</a>|\
                                              <a href='/searchStudent'>Search Student By ID </a></div>")

                if student is not None:
                    self.wfile.write(b"<center><h1>Student Found</h1>")
                    self.wfile.write(b"<table>")
                    self.wfile.write(b"<tr>")
                    self.wfile.write(b"<td><th>Name</th></td>")
                    self.wfile.write(b"<td>")
                    self.wfile.write(student[1].encode())
                    self.wfile.write(b"</td>")
                    self.wfile.write(b"</tr>")
                    self.wfile.write(b"<tr>")
                    self.wfile.write(b"<td><th>Course Id</th></td>")
                    self.wfile.write(b"<td>")
                    self.wfile.write(str(student[2]).encode())
                    self.wfile.write(b"</td>")
                    self.wfile.write(b"</tr>")
                    self.wfile.write(b"<tr>")
                    self.wfile.write(b"<td><th>Grade</th></td>")
                    self.wfile.write(b"<td>")
                    self.wfile.write(str(student[3]).encode())
                    self.wfile.write(b"</td>")
                    self.wfile.write(b"</tr>")
                    self.wfile.write(b"</table>")
                    self.wfile.write(b"<div><a href='/searchStudent'>Search Again</a></div>")
                else:
                    self.wfile.write(b"<center><h1>Student Not Found</h1>")
                    self.wfile.write(b"<div><a href='/searchStudent'>Search Again</a></div>")

                self.wfile.write(b"<hr>")
            elif self.path == "/addCourse":
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                course_name = form.getvalue("cname")
                ##Call the Database Method to a add a new course
                '''
                    Example call: self.database.addStudent(student_name, student_courseid,student_grade)
                '''

                done = self.database.addCourse(course_name)

                print("grabbed values", course_name)

                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                                 <a href='/addStudent'>Add Student</a>|\
                                                  <a href='/addCourse'>Add Course</a>|\
                                                  <a href='/modifyStudent'>Modify Student</a>|\
                                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr>")
                if done:
                    self.wfile.write(b"<h3>Course has been added</h3>")
                    self.wfile.write(b"<div><a href='/addCourse'>Add A New Course</a></div>")
                else:
                    self.wfile.write(b"<h3>Course not added</h3>")
                    self.wfile.write(b"<div><a href='/addCourse'>Retry again</a></div>")
                self.wfile.write(b"</center></body></html>")
            elif self.path == "/modifyStudent":
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                studentId = form.getvalue("sid")
                grade = form.getvalue("sgrade")
                ##Call the Database Method to a add a new course
                '''
                    Example call: self.database.addStudent(student_name, student_courseid,student_grade)
                '''

                done = self.database.modifyGrade(studentId, grade)

                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                                                 <a href='/addStudent'>Add Student</a>|\
                                                                  <a href='/addCourse'>Add Course</a>|\
                                                                  <a href='/modifyStudent'>Modify Student</a>|\
                                                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr>")
                if done:
                    self.wfile.write(b"<h3>Student Grade has been modified</h3>")
                    self.wfile.write(b"<div><a href='/modifyStudent'>Modify Grade</a></div>")
                else:
                    self.wfile.write(b"<h3>Grade Not Modified</h3>")
                    self.wfile.write(b"<div><a href='/modifyStudent'>Retry again</a></div>")
                self.wfile.write(b"</center></body></html>")
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

        return

    def do_GET(self):
        try:

            if self.path == '/':
                data = []
                records = self.database.getAllStudents()
                for record in records:
                    data = record.fetchall()

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/modifyStudent'>Modify Student</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr><h2>All Students With Grade</h2>")
                self.wfile.write(b"<table border=2> \
                                    <tr><th>Student Name </th>\
                                        <th> Student ID </th>\
                                        <th> Course Name </th>\
                                        <th> Grade </th></tr>")
                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(row[1].encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(row[5].encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return
            if self.path == '/addStudent':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/modifyStudent'>Modify Student</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr><h2>Add New Student</h2>")

                self.wfile.write(b"<form action='/addStudent' method='post'>")
                self.wfile.write(b'<label for="sname">Student Name:</label>\
                      <input type="text" id="sname" name="sname"><br><br>\
                      <label for="courseid">course id:</label>\
                      <input type="number" id="courseid" name="courseid"><br><br>\
                      <label for="sgrade">Grade:</label>\
                      <input type="text" id="sgrade" name="sgrade"><br><br>\
                      <input type="submit" value="Submit">\
                      </form>')

                self.wfile.write(b"</center></body></html>")
                return
            if self.path == '/addCourse':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/modifyStudent'>Modify Student</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr><h2>Add New Course</h2>")

                self.wfile.write(b"<form action='/addCourse' method='post'>")
                self.wfile.write(b'<label for="cname">Course Name:</label>\
                                     <input type="text" id="cname" name="cname"><br><br>\
                                     <input type="submit" value="Submit">\
                                     </form>')

                self.wfile.write(b"</center></body></html>")
                return

            if self.path == '/searchStudent':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addStudent'>Add Student</a>|\
                                  <a href='/addCourse'>Add Course</a>|\
                                  <a href='/modifyStudent'>Modify Student</a>|\
                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr><h2>Search Student</h2>")
                self.wfile.write(b"<form action='/searchStudent' method='post'>")
                self.wfile.write(b'<label for="sid">Student Id:</label>\
                                                     <input type="text" id="sid" name="sid"><br><br>\
                                                     <input type="submit" value="Submit">\
                                                     </form>')

                self.wfile.write(b"</center></body></html>")
                return

            if self.path == '/modifyStudent':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title> Teacher's Portal </title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Teacher's Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                                 <a href='/addStudent'>Add Student</a>|\
                                                  <a href='/addCourse'>Add Course</a>|\
                                                  <a href='/modifyStudent'>Modify Student</a>|\
                                                  <a href='/searchStudent'>Search Student By ID </a></div>")
                self.wfile.write(b"<hr><h2>Modify Student</h2>")
                self.wfile.write(b"<form action='/modifyStudent' method='post'>")
                self.wfile.write(b'<label for="sid">Student Id:</label>\
                                    <input type="text" id="sid" name="sid"><br><br>\
                                    <label for="sgrade">Grade:</label>\
                                    <input type="text" id="sgrade" name="sgrade"><br><br>\
                                    <input type="submit" value="Submit">\
                                    </form>')

                self.wfile.write(b"</center></body></html>")
                return



        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def run(server_class=HTTPServer, handler_class=PortalServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()


run()
