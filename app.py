from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('students.db')
    return conn

@app.route('/')
def index():
    conn = get_db()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    roll = request.form['roll']
    conn = get_db()
    conn.execute('INSERT INTO students (name, roll) VALUES (?, ?)', (name, roll))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    conn = get_db()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', student=student)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    roll = request.form['roll']
    conn = get_db()
    conn.execute('UPDATE students SET name = ?, roll = ? WHERE id = ?', (name, roll, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
