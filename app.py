from flask import Flask, render_template, request, redirect, url_for
import models

app = Flask(__name__)

@app.route('/')
def index():
    tasks = models.fetch_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    models.add_task(title)
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    status = request.form['status']
    models.update_task_status(id, status)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    models.delete_task(id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
