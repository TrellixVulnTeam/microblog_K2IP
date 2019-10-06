from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Matt'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'This is a post'
        },
        {
            'author': {'username': 'Kelsey'},
            'body': 'Posting a thing'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)