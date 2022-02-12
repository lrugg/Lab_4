from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Lizabeth Rugg'}
    classes = [{'classInfo': {'code': 'ACT101-40', 'title': ' Introduction to Information Technology'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC254-01', 'title': 'Object-Oriented Programming'}, 'instructor': 'Evan Noynaert'},
               {'classInfo': {'code': 'CSC305-01', 'title': 'Database Architecture and Concepts'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC324-01', 'title': 'Software Testing and DevOps'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'SEC300-01', 'title': 'Introduction to Cybersecurity'}, 'instructor': 'Yipkei Kwok'}]
    return render_template('index.html', title='Home', user=user, classes=classes)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
