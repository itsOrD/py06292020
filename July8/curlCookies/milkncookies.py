#!/usr/bin/python3
''' itsOrD || learning about cookie interaction with CURL '''

from flask import Flask, make_response, request, render_template, redirect, url_for


app = Flask(__name__)


# entry point for our users
# renders a template that akss for their name
# login.html points to /setcookie
@app.route('/login')
@app.route('/')
def index():
    return render_template('login.html')

# set the cookie and send it back to the user
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    # if user generates a POST to our API
    if request.method == 'POST':
        if request.form.get('nm'):  # if nm was assigned via the POST
            #if request.form['nm']  <-- would work, but ERRORs and breaks program if no nm
            user = request.form.get('nm')
        else:
            user = 'defaultuser'

        # Not that cookies are set on response objects
        # Since you normally just return strings
        # Flask will convert them into response objects for you
        resp = make_response(render_template('readcookie.html'))
        # add a cookie to our response object
                        #cookievar ,  #value
        resp.set_cookie('userID'   ,  user)

        # return our response object includes our cookie
        return resp
   
    if request.method == 'GET':  # if the user sends a GET
        return redirect(url_for('index'))  # redirect to index


# check users cookie for their name
@app.route('/getcookie')
def getcookie():
    # attempt to read the value of userID from user cookie
    name = request.cookies.get('userID')
    # return HTML embedded with name (value of userID read from cookie)
    return f'''<h1> Welcome {name} </h1>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2224)
