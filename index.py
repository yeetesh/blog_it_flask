from flask import Flask,session
import pymongo
import user
import blog

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["blog_database"]

app = Flask(__name__)

@app.route('/')
def index():
    #get 10 published blogs and display
    blog_posts = blog.find_top(db)
    for i in blog_posts:
        print(i)
    return '10 published user blogs'

@app.route('/register')
def register():
    user.register(db,{'username' : 'test', 'password' : 'test'})
    session['username'] = 'test'
    return 'register'

@app.route('/login')
def login():
    user.login(db,{'username' : 'test', 'password' : 'test'})
    session['username'] = 'test'
    return 'login'

@app.route('/logout')
def logout():
    session.pop('test',None)
    return 'logout'

@app.route('/users')
def users():
    #display list of users in sorted order with hyperlink
    data = user.all_users(db)
    for i in data:
        print(i)
    return 'users'


@app.route('/user/<username>/<title>')
def user_blog(username,title):
    #check if published blog, display the blog
    data = blog.blog(db,username,title)
    print('title : ', title)
    for i in data:
        print(i)
    return 'single_blog'


@app.route('/user/<username>')
def user_blogs(username):
    #get published blogs by that user and display, give edit options if logged in with that username
    data = blog.user_blogs(db,username)
    for i in data:
        print(i)
    return 'user_blogs'

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug = True)

#give like and comment features as well

