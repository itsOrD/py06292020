#!/usr/bin/python3
''' itsOrD || playins with sessions in Flask '''

from flask import Flask, session, render_template, redirect, url_for, escape, request


app = Flask(__name__)
app.secret_key = 'randomisasrandomdoes'


# if the user hits the root of our API
@app.route('/')
def index():
    ## if the key 'username' has a value in session
    if 'username' in session:
        username = session['username']
        return f'''--Logged in as {username}
            \<b><a href='/logout'> click here to log out </a></b>'''
    return f'''----You are not logged in
        <b><a href='/login'> click here to log in </b></a>'''

## if the user hits /login with a GET or POST
@app.route('/login', methods = ['GET', 'Post'])
def login():
    ## if you sent a POST because you clicked the login button
    if request.method == "POST":
        ## request.form['xyzkey']: use indexing if you know the key exists
        ## request.get('xyzkey'): use get if the key might not exist
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))

    ## return this HTML data if you send us a GET
    return '''
    <form action="" method="post">
        <p><input type=test name=username></p>
        <p><input type=submit value=Login></p>
    </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2224)

