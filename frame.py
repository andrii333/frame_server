import sys

sys.path.append('C:\\Users\\User\\Documents\\GitHub\\flask_user')

from flask import Flask, request, Response
from functools import wraps
from itsdangerous import Signer
import time
import os
import json
import base64
from flask_user import User


#CONFIG
app = Flask(__name__)
app.config['TOKEN_LIVE_TIME'] = 86400  #time for saving cookie in session
app.config['SESSION_COOKIE_HTTPONLY'] = True  #set HttpOnly
#app.config['SECRET_KEY'] = os.urandom(24)   #secret key for signature
app.config['SECRET_KEY'] = 'andrii'


@app.before_request
def before_request():
    app.user = User(app.config['SECRET_KEY'])  #initialize User 
    





def only_for(roles):
    def w(f):
        @wraps(f)
        def ww():
            #initialize pylog
#            pl = Pylog(app.config['TOKEN_LIVE_TIME'],app.config['SECRET_KEY'])
            

            
            return 'Srabotalo'+' '+roles
        return ww
    return w




@app.route('/')
def idx():
    
    return 'OK'

@app.route('/test')
def t():
    print app.user.ip
    return 'OK'

@app.route('/decorator')
@only_for('login users')
def decorator_test():
    return 'KL'



def print_environ():
    t = ''
    for each in request.environ:
        t = t+str(each)+':'+str(request.environ[each])+'\n'
    print t
   


if __name__=='__main__':
    app.run(host="172.30.6.47",port=5000)
