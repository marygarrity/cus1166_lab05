'''
Each route must render a specific template. All
template must extend the layout.html template.
'''
import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

i = 0
course = Course(id = i+1, course_number = "CUS1166", course_title = "Software Engineering")
db.session.add(course)
i = i+1 # now i = 1
course = Course(id = i+1, course_number = "CUS1162", course_title = "Computer Architecture")
db.session.add(course)
i = i+1 # now i = 2
course = Course(id = i+1, course_number = "CUS1165", course_title = "Database Management Systems")
db.session.add(course)
i = i+1 # now i = 3
course = Course(id = i+1, course_number = "NET1011", course_title = "Introduction To Networks")
db.session.add(course)
i = i+1 # now i = 4
course = Course(id = i+1, course_number = "CSS1011", course_title = "Network Security")
db.session.add(course)
i = i+1 # now i = 5

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    courses = Course.query.all()
    return render_template('index.html', courses = courses)

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/add_course", methods = ['POST'])
def add_course():

    course_title = request.form.get("course_title")
    course_number = request.form.get("course_number")
    course = Course(id = i+1, course_number = course_number, course_title = course_title)
    db.session.add(course) # add the course to the database using the Course model
    db.session.commit()
    i = i+1 # now i = 6

    courses = Course.query.all()
    return render_template('index.html', courses = courses)

#'/register_student/int:course_id':
@app.route("/register_student/<int:course_id>", methods = ["GET", "POST"])
def register_student(course_id):

    course = Course.query.get(course_id)

    if request.method == 'GET':
        '''
        Queries the database to obtain all information about the course with id == course_id
        and all current registered students in the course
        Renders the template course_details.html
        The template should show information about the course,
        a listing of all students registered, and a form for users to register new student

        When a user submit this form it should be redirected to the route
        /register_student/<int:course_id> using a post request
        '''

    if request.method == 'POST':
        name = request.form.get("name")
        grade = request.form.get("grade")
        course.add_registeredstudent(name, grade) # adds the new student to the course

    registeredstudents = course.registeredstudents
    return render_template("course_details.html", course = course, registeredstudents = registeredstudents)


# Main:

def main():
    if (len(sys.argv) == 2):
        print(sys.argv)
        if sys.argv[1] == 'createdb':
            db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use 'python app.py createdb")

# Run the main method in the context of our flass application
# This allows db know about our models
if __name__ == "__main__":
    with app.app_context():
        main()
