from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for students (later we use database)
students = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cls = request.form['cls']
        students.append({"name": name, "age": age, "class": cls})
        return redirect(url_for('view_students'))
    return render_template("add_student.html")

@app.route('/view_students')
def view_students():
    return render_template("view_students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
