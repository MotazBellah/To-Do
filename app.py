from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Task
from time import gmtime, strftime

engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/')
@app.route('/tasks')
def show_tasks():
    tasks = session.query(Task).filter_by(done=False).all()
    return render_template('task.html', tasks=tasks)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    tasks = session.query(Task).filter_by(done=False).all()
    return render_template('task.html', tasks=tasks)


@app.route('/completedTasks')
def show_completed():
    tasks = session.query(Task).filter_by(done=True).all()
    return render_template('completed.html', tasks=tasks)



@app.route('/addTask', methods=['POST'])
def addTask():
    if request.form['name']:
        newTask = Task(name=request.form['name'])
        session.add(newTask)
        session.commit()

    return redirect(url_for('show_tasks'))


@app.route('/delete/<task_name>')
def deleteTask(task_name):
    task = session.query(Task).filter_by(name=task_name).first()
    session.delete(task)
    session.commit()
    return redirect(url_for('show_tasks'))


@app.route('/edit', methods=['POST'])
def editTask():
    task = session.query(Task).filter_by(name=request.form['id']).first()
    task.name = request.form['name']
    session.add(task)
    session.commit()

    return jsonify({'result': 'success'})


@app.route('/complete', methods=['POST'])
def completeTask():
    task = session.query(Task).filter_by(name=request.form['id']).first()
    task.done = True
    session.add(task)
    session.commit()

    return jsonify({'result': 'success'})




if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
