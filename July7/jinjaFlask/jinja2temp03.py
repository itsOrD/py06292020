#!/usr/bin/python3
''' itsOrD || flask-jinja-templating practice '''

from flask import Flask, render_template


app = Flask(__name__)


# pull in the value of score as an int
@app.route('/scoretest/<int:score>')
def hello_name(score):
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    return render_template('highscore.html', marks = score)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2224)
