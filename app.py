from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/content')
def content():
    return render_template('content.html')


@app.route('/tag')
def tag():
    return render_template('tag.html')


@app.route('/user_search')
def user_search():
    return render_template('user_search.html')


@app.route('/addtitle')
def addtitle():
    return render_template('addtitle.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5555)
