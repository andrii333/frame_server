from functools import wraps
from flask import Flask, request,Response, redirect
import os
import sys
import json



#determine path of flask_user library and append to sys.path
current_path = os.path.realpath(__file__).split('/')
l = len(current_path)
current_path[l-1] = 'flask_user'
current_path = '/'.join(current_path)
sys.path.append(current_path)


from flask_user import User





app = Flask(__name__)


@app.before_request
def before_request():
	app.user = User('andrii')
	app.user.deserialize(request)


@app.after_request
def after_request(resp):
	resp = app.user.serialize(resp)
	return resp



def for_role(roles=[]):
	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			permit = app.user.check_auth(roles)
			if permit== True:
				fin  = f(*args, **kwargs)
				return fin
			else:
				return permit
		return decorated_function
	return decorator





@app.route('/')
def start():
	
	t = open('./index.html','r')
	r = t.read()
	t.close()

	return r


@app.route('/login', methods=['POST'])
def login():
	u_doc = json.loads(request.data)
	f = app.user.login(u_doc['name'],u_doc['pass'])
	if f!=True:
		return f

	return 'Logged'


@app.route('/registr',methods=['POST'])
def registr():
	u_doc = json.loads(request.data)
	u_doc['roles'] = ['admin']
	u_doc['token_live_time'] = 86400
	
	u_doc_new = u_doc.copy()
	f = app.user.registr(u_doc_new)

	#send error during registred
	if f!=True:
		return f

	if f==True:
		print u_doc['pass']
		f = app.user.login(u_doc['name'],u_doc['pass'])

	return 'Registred'

@app.route('/user')
@for_role(['admin'])
def ggg():
	return app.user.session['name']





@app.route('/drop')
def drop_log():
	app.user.drop_log_token()
	return 'OK'



if __name__=='__main__':
	app.run(debug=False, host="46.101.122.41",port=80)
