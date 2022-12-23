create database if not exists teachers_portal;
USE teachers_portal;
create table if not exists students(
	studentId int not null unique auto_increment primary key,
	studentName varchar (45) Not Null,
	enrolledInCourseID int default 1,
	grade float null
);

create table if not exists courses(
	courseId int not null unique auto_increment primary key,
	courseName varchar (45) not null
);

insert into students (studentName, enrolledInCourseID, grade) VALUES ('Maria Jozef', 1,90), ('Linda Jones', 2, 89), ('John
McGrail', 1, 98), ('Patty Luna', 2, 78);

insert into courses (courseName) values ('Database Design'), ('Calculus'), ('Physics I');
