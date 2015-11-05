from flask import Flask, request,Response
import sys

sys.path.append('/home/andrii/workshop/flask_user')
from flask_user import User

app = Flask(__name__)


@app.before_request
def before_request():
	app.user = User('andrii')
	app.user.deserialize(request)


@app.after_request
def after_request(resp):
	resp = app.user.serialize(resp)
#	resp.set_cookie('log_token','fff')
	return resp




@app.route('/')
def test_1():
#	d = app.make_response('fff')
#	d.set_cookie('log_token','ggg')
#	app.user.login('andrii','pass')

	if app.user.check_auth(['admin'])==True:
		return 'You are Log IN'
	else:
		return app.user.check_auth(['admin'])


@app.route('/login/<user_name>/<user_pass>')
def login(user_name,user_pass):
	f = app.user.login(user_name,user_pass)
	if f!=True:
		return f

	return 'OK'


@app.route('/registr/<u_name>/<u_pass>')
def registr(u_name,u_pass):
	j = {}
	j['name'] = u_name
	j['pass'] = u_pass
	j['roles'] = ['admin']
	j['token_live_time'] = 86400
	f = app.user.registr(j)

	if f==True:
		f = app.user.login('andrii','ddd')

	return str(f)



@app.route('/drop')
def drop_log():
	app.user.drop_log_token()
	return 'Ok'	



if __name__=='__main__':
	app.run(debug=True)
