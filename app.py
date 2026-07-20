from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []  # Temporary list

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    roll = int(request.form['roll'])
    students.append({'name': name, 'roll': roll})
    return redirect(url_for('home'))

@app.route('/delete/<int:roll_no>')
def delete_student(roll_no):
    global students
    students = [s for s in students if s['roll'] != roll_no]
    return redirect(url_for('home'))

@app.route('/edit/<int:roll_no>', methods=['GET', 'POST'])
def edit_student(roll_no):
    global students
    student = next((s for s in students if s['roll'] == roll_no), None)
    
    if request.method == 'POST':
        student['name'] = request.form['name']
        student['roll'] = int(request.form['roll'])
        return redirect(url_for('home'))
    
    return render_template('edit.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
