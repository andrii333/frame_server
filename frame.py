from flask import Flask, request, Response
from functools import wraps
from itsdangerous import Signer
import time
import os
import json
import base64
from pylog import Pylog

#CONFIG
app = Flask(__name__)
app.config['TOKEN_LIVE_TIME'] = 86400  #time for saving cookie in session
app.config['SESSION_COOKIE_HTTPONLY'] = True  #set HttpOnly
#app.config['SECRET_KEY'] = os.urandom(24)   #secret key for signature
app.config['SECRET_KEY'] = 'andrii'




def only_for(roles):
    def w(f):
        @wraps(f)
        def ww():
            #initialize pylog
            pl = Pylog(app.config['TOKEN_LIVE_TIME'],app.config['SECRET_KEY'])
            

            
            return 'Srabotalo'+' '+roles
        return ww
    return w




@app.route('/')
def idx():
    t = ''
    for each in request.environ:
        t = t+str(each)+':'+str(request.environ[each])+'\n'
    print t
    return t



@app.route('/decorator')
@only_for('login users')
def decorator_test():
    return 'KL'



if __name__=='__main__':
    app.run(host="localhost",port=5000,debug=False)