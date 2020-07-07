#!/usr/bin/python3
'''
Author: itsOrD
Description: playing with the Flask by making an API
'''

from flask import Flask


# Flask constructor takes the name of current
# module (__name__) as argument

app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
    return "Hello World"

# decorator assignment
@app.route("/howdy")
def howdy_world():
    return "Howdy World!"

# using Flask's app class object methods
def whatup_world():
    return "What-up World!"
app.add_url_rule("/whatup", "whatup", whatup_world)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
    # app.run(host="0.0.0.0", port=2224, debug=True)  # DEBUG MODE
