from flask import Flask,url_for

app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# @app.route('/home')
# def index():
#     return "<h1>Hello Flask llaall </h1>"

@app.route('/user/<name>')
def index(name):
    print(url_for('index',name="hahaha"))
    return "<h1>Hello %s </h1>"%name