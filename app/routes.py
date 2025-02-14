from flask import render_template
from app import app

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