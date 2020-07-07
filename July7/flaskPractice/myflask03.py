#!usr/bin/python3
'''itsOrD  ||  Flask practice'''

from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f'''Hello Guest, {guesty}'''

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guesty = name))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the app
