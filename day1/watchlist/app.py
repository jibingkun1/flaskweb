import os,sys

from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import click

WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///" # windows平台
else:
    prefix = "sqlite:////" #Mac，Linux平台
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# models 数据层
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

# views 视图函数
@app.route('/')
def index():

   user = User.query.first()  #查询出来用户记录
   movies = Movie.query.all() 
   return render_template('index.html',user=user,movies=movies)


# 自定义命令
# 建立空数据库
@app.cli.command()  # 注册为命令
@click.option('--drop',is_flag=True,help="先删除再创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化数据库完成")

# 向空数据库中插入数据
@app.cli.command()
def forge():
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
       {'title':"叶问2","year":"2016"}
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo("导入数据完成")


