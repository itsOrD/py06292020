#!/usr/bin/python3
'''
Author: itsOrD
Description: further Flask practice
'''

from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return f'''Hello {name}'''
    ## v2 style string formatter --> return "Hello {}".format(name)
    ## old style string formatter --> return "Hello %x!" % name

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application
