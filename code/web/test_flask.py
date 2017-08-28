from flask import Flask, url_for, redirect
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
#	return redirect(url_for('login'))
	return '<h1>Home</h1>'

@app.route('/login', methods = ['GET'])
def login():
	return '''<form action="/login" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Log in</button></p>
              </form>'''

@app.route('/login', methods = ['POST'])
def login_check():
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello admin!</h3>'
	return redirect(url_for('error'))

@app.route('/error', methods = ['GET', 'POST'])
def error():
	return '<h1>ERROR</h1>'

if __name__=='__main__':
	app.run(debug = True)