import json

from flask import jsonify, request, render_template, flash, redirect
from app import app
from .forms import LoginForm

"""
# ~ It's written in 11/8 time 
# ~ Key: F Mayor
# ~ Tempo: around 140 (eight note)
# ~ [Main riff]
  # ~ 1 $ 2 $ 3 $ 1 $ 2 $ 3 $ 1 & 2 $ 3 $ 1 & 2 $  
# ~ e|--------------------0-----------------------|
# ~ B|----------------6-------8-------------------|
# ~ G|------------5---------------7---------------|
# ~ D|--------0-----------------------0-----------|
# ~ A|----0-------------------------------0-------|
# ~ E|6---------------------------------------8---| 
"""

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Joe'}  
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Bob'}, 
            'body': "That's what's the deal we're dealing in" 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'You should never smoke in pajamas' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)


@app.route('/api/contents/<uid>', methods=['GET'])
def contents(uid):
    
    json_data = request.get_json()
    
    print("uid: {}".format(uid))
    print("json_data: {}".format(json_data))

    answer = {
        'uid': uid,
        'pojama': 'people special'
    }
    return jsonify(answer)

