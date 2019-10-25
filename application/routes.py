from flask import current_app as app
from flask import render_template

from .hello import HelloApi
from .todo import ToDoApi


app.register_blueprint(HelloApi, url_prefix='/hello')
app.register_blueprint(ToDoApi, url_prefix='/todo')

# homepage
@app.route('/')
def todo():
    db = ToDoApi.connect(host="localhost",  # your host
                         user="root",  # username
                         passwd="root",  # password
                         db="pythonspot")  # name of the database

    # Create a Cursor object to execute queries.
    cur = db.cursor()

    cur.execute("SELECT * FROM examples")

    for row in cur.fetchall():
        print
        row[0], " ", row[1]

    return render_template('todo.html')

