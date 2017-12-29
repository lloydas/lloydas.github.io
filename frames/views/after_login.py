import frames
import pycurl
import urllib
import json
import StringIO
import flask
from flask import request, session, redirect, url_for

@frames.app.route('/html/create/', methods=['GET', 'POST'])
def get_credentials():
    b = StringIO.StringIO()

    # verify that the access token belongs to us
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "https://api.amazon.com/auth/o2/tokeninfo?access_token=" + urllib.quote_plus(access_token))
    c.setopt(pycurl.SSL_VERIFYPEER, 1)
    c.setopt(pycurl.WRITEFUNCTION, b.write)

    c.perform()
    d = json.loads(b.getvalue())

    # if d['aud'] != 'amzn1.application-oa2-client.5815d5058fb444c0b93783a79adec01d' :
    #     # the access token does not belong to us
    #     raise BaseException("Invalid Token")
    
    return flask.render_template("after_login.html", **d)


    # print "%s %s %s"%(d['name'], d['email'], d['user_id'])
        
        
        
        
        