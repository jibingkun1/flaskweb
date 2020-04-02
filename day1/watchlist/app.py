from flask import Flask,url_for,render_template

app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# @app.route('/home')
# def index():
#     return "<h1>Hello Flask llaall </h1>"

@app.route('/')
def index():
   name = "Bruce"
   movies = [
       {'title':"大赢家","year":"2020"},
       {'title':"囧妈","year":"2020"},
       {'title':"疯狂外星人","year":"2019"},
       {'title':"战狼","year":"2017"},
       {'title':"速度与激情8","year":"2018"},
       {'title':"极限特工","year":"2010"},
       {'title':"叶问","year":"2014"},
       {'title':"杀破狼","year":"2000"},
       {'title':"叶问2","year":"2016"},
   ]

   return render_template('index.html',name=name,movies=movies)