from flask import Flask, render_template, request
import sqlite3 as sql
import random

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/insert')
def insert():
    error = None
    if request.method == 'GET':
        # connect to database
        connection = sql.connect('database.db')

        # select all database entries
        cursor = connection.execute('SELECT pid, firstname, lastname FROM users;')
        result = cursor.fetchall()
        if result:
            # return html page with database entries
            return render_template('insert.html', error=error, result=result)

        else:
            error = "couldn't fetch database"
    return render_template("insert.html", error=error)


@app.route('/delete')
def delete():
    error = None
    if request.method == 'GET':
        # connect to database
        connection = sql.connect('database.db')

        # select all entries from database
        cursor = connection.execute('SELECT pid, firstname, lastname FROM users;')
        result = cursor.fetchall()
        if result:
            # return html page with database entries
            return render_template('delete.html', error=error, result=result)
        else:
            error = "couldn't fetch database"
    return render_template("delete.html", error=error)


@app.route('/name', methods=['POST', 'GET'])
def name():
    error = None
    if request.method == 'POST':
        result = valid_name(request.form['FirstName'], request.form['LastName'])
        if result:
            # return html page with database entries
            return render_template('insert.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('insert.html', error=error)


def valid_name(first_name, last_name):
    # connect to database
    connection = sql.connect('database.db')

    # create table
    connection.execute('CREATE TABLE IF NOT EXISTS users(pid INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT);')

    # check if a pid of 1 is in the database (pid = 1 means at least 1 user)
    value = 1

    # Execute a SELECT statement to check if an entry is in the column
    cursor = connection.execute("SELECT * FROM users WHERE pid=?", (value,))
    result = cursor.fetchone()

    # If result is not None, then the value is already in the column
    if result is not None:
        # see last pid entry and increment by 1

        # Execute the SQL query to get the most recently added value of a table column
        cursor.execute("SELECT pid FROM users ORDER BY pid DESC LIMIT 1;")

        # Fetch the result
        result2 = cursor.fetchone()

        # increment pid
        pid = result2[0] + 1
    else:
        # first entry into database
        pid = 1

    # insert entries into table
    connection.execute('INSERT INTO users (pid, firstname, lastname) VALUES (?,?,?);',
                       (pid, first_name, last_name))
    connection.commit()
    # select and return all database entries
    cursor = connection.execute('SELECT pid, firstname, lastname FROM users;')
    return cursor.fetchall()


@app.route('/remove', methods=['POST'])
def remove():
    error = None
    # get first name and last name from form
    first_name = request.form['FirstName']
    last_name = request.form['LastName']

    # check if given first name and last name exist in database
    connection = sql.connect('database.db')
    cursor = connection.execute('SELECT * FROM users WHERE firstname=? AND lastname=?;', (first_name, last_name))
    user = cursor.fetchone()

    if user is None:
        error = 'User not found in database'
    else:
        # delete row for given first name and last name
        connection.execute('DELETE FROM users WHERE firstname=? AND lastname=?;', (first_name, last_name))
        connection.commit()

    # select all entries from database
    cursor = connection.execute('SELECT pid, firstname, lastname FROM users;')
    result = cursor.fetchall()
    if result:
        # return html page with database entries
        return render_template('delete.html', error=error, result=result)

    return render_template('delete.html', error=error)


if __name__ == "__main__":
    app.debug = True
    app.run()


