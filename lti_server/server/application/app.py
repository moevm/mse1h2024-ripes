from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/task/<task_id>")
def task(task_id):
    return render_template("task.html", task_id=task_id)
