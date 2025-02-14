from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm

@app.route('/hello/<audio_id>')
def hello(audio_id):
    return f"Hello, World! - {audio_id}"


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Erica'}
    posts = [
        {
            'author': {'username': 'Erica'},
            'body': 'Beautiful day in Ohio!'
        },
        {
            'author': {'username': 'Bit'},
            'body': 'The Castlevania show was so cool!'
        },
        {
            'author': {'username': 'Bit'},
            'body': 'The Castlevania show was so cool2!'
        },
        {
            'author': {'username': 'Bit'},
            'body': 'The Castlevania show was so cool3!'
        },
        {
            'author': {'username': 'Bit'},
            'body': 'The Castlevania show was so cool4!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/login', methods=['POST'])
def postLogin():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/postjson', methods=['POST'])
def postJson():
    # get json
    data = request.get_json()
    print(data)

    # do things with the data

    # return json data
    return data