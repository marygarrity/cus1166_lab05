'''
Define two domain classes that extend from db.Model class.
Name the first class Course and the second one RegisteredStudent.
Use the SQLAlchemy to define the models for these classes
and map them to the courses and registeredstudents tables respectively.
Define any foreign key or relationship fields you think are necessary.
'''
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model): # Course class
    __tablename__ = "courses" # Map this model to a courses table
    # Specify the columns/ fields of the model
    id = db.Column(db.Integer, primary_key = True) # unique course id, Primary Key
    course_number = db.Column(db.String, nullable = False) # ex- CUS1166
    course_title = db.Column(db.String, nullable = False)

    # Specify any relationship fields
    registeredstudents = db.relationship("RegisteredStudent", backref = "courses", lazy = True)
    # Specify any utility methods associated with the model
    def add_registeredstudent(self, name, grade):
        new_registeredstudent = RegisteredStudent(name = name, grade = grade, course_id = self.id )
        db.session.add(new_registeredstudent)
        db.session.commit()

class RegisteredStudent(db.Model): # RegisteredStudent class
    __tablename__ = "registeredstudents" # Map this model to a registeredstudents table
    # Specify the columns/fields of the model
    id = db.Column(db.Integer, primary_key = True) # unique id for registered student, Primary Key
    name = db.Column(db.String, nullable = False) # name of student (first and last)
    grade = db.Column(db.Integer, nullable = False) # current grade of student (number)

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable = False) # This field serves as a Foreign Key
