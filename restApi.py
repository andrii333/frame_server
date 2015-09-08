print 'rest API'
from flask import Flask
import urllib
import urllib2
from flask import request, send_from_directory
import httplib
import json
from werkzeug import secure_filename


app = Flask('__name__')
import os

@app.route("/mystyle_1.css")
def mystyle_css():
    idx_f = open('./static/mystyle_1.css','r')
    idx = idx_f.read()
    idx_f.close()
    return idx, 200, {"Content-type":"text/css"}


@app.route('/')
def test():
	return 'Test'
	
if __name__ == '__main__':
    app.run(host="172.30.6.42",port=5000)


print 'ffff'