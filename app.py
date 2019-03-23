from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Task

engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/')
@app.route('/tasks')
def show_tasks():
    tasks = session.query(Task).all()
    return render_template('task.html', tasks=tasks)

@app.route('/addTask', methods=['POST'])
def addTask():
    if request.form['name']:
        newTask = Task(name=request.form['name'])
        session.add(newTask)
        session.commit()
        
    return redirect(url_for('show_tasks'))





if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
